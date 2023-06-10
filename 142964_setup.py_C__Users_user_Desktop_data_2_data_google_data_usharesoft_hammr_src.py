# Copyright 2007-2015 UShareSoft SAS, All rights reserved
#
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from setuptools import setup,find_packages
from hammr.utils.constants import *


# Declare your packages' dependencies here, for eg:
requires=['uforge_python_sdk>=3.6',
                    'httplib2==0.9',
                    'texttable>=0.8.1',
                    'progressbar==2.3',
                    'argparse',
                    'paramiko==1.12',
                    'pyparsing==2.0.2',
                    'hurry.filesize==0.9',
                    'termcolor==1.1.0',
                    'junit-xml==1.3',
                    'xmlrunner==1.7.7',
                    'ussclicore']

setup (  

  install_requires=requires,
  
  # Fill in these to make your Egg ready for upload to
  # PyPI
  name = 'hammr',
  version = VERSION,
  description='Command-line tool for building conistent and repeatable machine images for multiple cloud platforms',
  long_description='command-line tool for building/publishing/migrating consistent machine images for virtual datacenters and cloud platforms',
  packages = find_packages(),
  author = 'Joris Bremond',
  author_email = 'joris.bremond@usharesoft.com',
  license="Apache License 2.0",
  url = 'http://hammr.io',
  classifiers=(
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
        'Operating System :: POSIX',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ),
       
  
  #long_description= 'Long description of the package',
  scripts = ['bin/hammr', 'bin/hammr.bat'],
  
)
