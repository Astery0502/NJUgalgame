# -*- encoding: utf-8 -*-
# Ren'py 的 VSCode 编辑器支持

import os
import subprocess
import renpy

# VSCode 的文件位置，请根据你的配置自行修改
CODE_PATH = r'C:\Program Files\Microsoft VS Code\Code.exe'


def code(argv):
    subprocess.Popen([CODE_PATH] + argv)


class Editor(renpy.editor.Editor):
    has_projects = True

    def begin(self, new_window=False, **kwargs):
        self.args = ['-n' if new_window else '-r']

    def end(self, **kwargs):
        self.args.reverse()
        code(self.args)

    def open(self, filename, line=None, **kwargs):
        filename = os.path.realpath(renpy.exports.fsencode(filename))
        if line: # 若指定行号，则跳转            
            self.args.append('%s:%d' % (filename, line))
            self.args.append('-g') # 由于最后使用了 reverse 所以要放后面
            # 不过好像不加 -g 也可以？
        else:
            self.args.append(filename) # 打开文件
        self.args.append(os.path.split(filename)[0] + '/') # 打开文件所在的文件夹

    def open_project(self, directory):
        directory = os.path.realpath(renpy.exports.fsencode(directory))
        self.args.append('%s/' % directory)


def main():
    e = Editor()
    e.begin()

    for i in sys.argv[1:]:
        e.open(i)

    e.end()


if __name__ == "__main__":
    main()