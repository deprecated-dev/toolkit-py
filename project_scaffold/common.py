'''
Date: 2022.02.02 19:08
Description: Automatically create basic common files.
LastEditors: Rustle Karl
LastEditTime: 2022.02.02 19:08
'''
import os
from datetime import datetime

__all__ = [
    'Entity',
    'TEMPLATE_LICENSE',
    'TEMPLATE_README',
    'TEMPLATE_GITIGNORE',
    'TEMPLATE_MAKEFILE',
]


class Entity(object):

    def __init__(self, file, content):
        self.file = file
        self.content = content

    def create(self):
        if os.path.exists(self.file):
            return

        with open(self.file, 'w', encoding='utf-8') as fp:
            fp.write(self.content)


# LICENSE
TEMPLATE_LICENSE = Entity('LICENSE', '''\
The MIT License (MIT)

Copyright (c) %d Rustle Karl

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
''' % datetime.now().year)

# README.md
TEMPLATE_README = Entity('README.md', '''\
# README
''')

# .gitignore
TEMPLATE_GITIGNORE = Entity('.gitignore', '''\
# Others
.sync_folder.json
bin/
scratch/
.dockerignore
.gitignore

# IDE
.idea/
.vscode/
.vscode-test/
.vscodeignore

# Dart
.dart_tool/
.packages/
build/

# Go
vendor/
go.sum

# Python
venv/
__pycache__/
dist/
*egg-info/

# JavaScript / TypeScript
node_modules/
*.vsix
*.lock
.yarnrc

# Log
*.log
logs/

# Dropbox
*.paper
''')

# Makefile
TEMPLATE_MAKEFILE = Entity('Makefile', '''\
.PHONY: ;
.SILENT: ;               # no need for @
.ONESHELL: ;             # recipes execute in same shell
.NOTPARALLEL: ;          # wait for target to finish
.EXPORT_ALL_VARIABLES: ; # send all vars to shell

.IGNORE: dep clean;            # ignore all errors, keep going

ifeq ($(OS), Windows_NT)
SHELL := pwsh.exe
.SHELLFLAGS := -NoProfile -Command
endif
''')


def create_common_files():
    TEMPLATE_LICENSE.create()
    TEMPLATE_README.create()
    TEMPLATE_GITIGNORE.create()

    scratch = 'scratch'

    if not os.path.exists(scratch):
        os.mkdir(scratch)