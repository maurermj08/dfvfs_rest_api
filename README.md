# dfvfs_rest_api
REST API for accessing remote file-system objects using dfVFS

Evidence can be accessed by going to /evidence/<Path Spec>

If the path specification is for a file it returns the entire file.
If the path specification is for a directory it returns all of the subpath specifications in that directory.

Example:
    wget http://localhost:8181/evidence/%7B%22inode%22:%2029057,%20%22type_indicator%22:%20%22TSK%22,%20%22__type__%22:%20%22PathSpec%22,%20%22location%22:%20%22/Documents%20and%20Settings/tdungan/My%20Documents/Alloy%20Research/Additional%20Information/historyofpeters.ppt%22,%20%22parent%22:%20%7B%22type_indicator%22:%20%22EWF%22,%20%22__type__%22:%20%22PathSpec%22,%20%22parent%22:%20%7B%22type_indicator%22:%20%22OS%22,%20%22__type__%22:%20%22PathSpec%22,%20%22location%22:%20%22/Training/SANS508/xp-tdungan-10.3.58.7/xp-tdungan-c-drive/xp-tdungan-c-drive.E01%22%7D%7D%7D -O historyofpeters.ppt

