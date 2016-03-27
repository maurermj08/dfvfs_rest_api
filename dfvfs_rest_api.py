import cherrypy
import argparse
import json
from bottle import Bottle, request, static_file, abort
from dfvfs.resolver import resolver
from dfvfs.serializer.json_serializer import JsonPathSpecSerializer


class DfVFSRestApi(object):

    def __init__(self, address, port):
        """Initializes Efetch variables and utils.

        Args:
            argv ([str]): A list of system arguments
        """
        self._address = address
        self._port = port
        self._app = Bottle()

        self._route()

    def start(self):
        """Starts the Bottle server."""
        self._app.run(host=self._address, port=self._port, server='cherrypy')

    def _route(self):
        """Applies the routes to Efetch methods."""
        self._app.route('/evidence/<path_spec:path>', method='GET', callback=self._evidence)

    def _evidence(self, path_spec):
        """Returns the evidence file at the specified PathSpec"""
        #try:
        return DfVFSApi.get_evidence(path_spec)
        #except TypeError:
        #    abort(400, 'TypeError: The id must be a valid dfVFS path specification')


class DfVFSApi(object):

    @staticmethod
    def get_evidence(path_spec):
        """Returns the evidence file at the specified PathSpec string"""
        decoded_path_spec = JsonPathSpecSerializer.ReadSerialized(unicode(path_spec))
        file_entry = resolver.Resolver.OpenFileEntry(decoded_path_spec)

        if file_entry.IsFile():
            return file_entry.GetFileObject()
        else:
            sub_entries = []
            for sub_file_entry in file_entry.sub_file_entries:
                sub_entries.append(JsonPathSpecSerializer.WriteSerialized(sub_file_entry.path_spec))
            return json.dumps(sub_entries)

def icat(file_entry, output_path):
    """Gets the file at full_path and outputs it to the output path"""
    in_file = file_entry.GetFileObject()
    out_file = open(output_path, "wb")
    data = in_file.read(32768)
    while data:
        out_file.write(data)
        data = in_file.read(32768)
    in_file.close()
    out_file.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(u'-a', u'--address',
                        help=u'the IP address or hostname this server runs on',
                        action=u'store',
                        default=u'localhost')
    parser.add_argument(u'-p', u'--port', type=int,
                        help=u'the port this servers runs on',
                        action=u'store',
                        default=8181)
    args = parser.parse_args()
    dfvfs_rest_api = DfVFSRestApi(args.address, args.port)
    dfvfs_rest_api.start()
