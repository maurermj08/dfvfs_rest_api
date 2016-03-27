#!/usr/bin/env python
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""This is the setup file for the project. The standard setup rules apply:

   python setup.py build
   sudo python setup.py install
"""

from setuptools import find_packages
from setuptools import setup

dfvfs_rest_api_description = (
    u'dfVFS REST API is a proof of concept api for'
    u'accessing a filesystem using dfVFS on a remote'
    u'system using the Path Specification')

setup(
    name=u'dfvfs_rest_api',
    version=u'2016.03',
    description=u'dfVFS REST API',
    long_description=dfvfs_rest_api_description,
    license=u'Apache License, Version 2.0',
    url=u'http://diftdisk.blogspot.com//',
    maintainer=u'Michael Maurer',
    maintainer_email=u'maurermj08@gmail.com',
    classifiers=[
        u'Development Status :: 1 - Beta',
        u'Environment :: Web Environment',
        u'Operating System :: OS Independent',
        u'Programming Language :: Python',
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    scripts=[u'dfvfs_rest_api.py'],
    install_requires=frozenset([
        u'bottle'
    ])
)
