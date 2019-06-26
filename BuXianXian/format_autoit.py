# coding:utf-8
import os

_AU3 = r'D:\张亚军\OrthoPlus自动化测试\脚本统计\new_case_mtx.au3'
_AU3_OUT = r'D:\张亚军\OrthoPlus自动化测试\脚本统计\new_case_mtx_format.au3'
_INDENT = ' '*4

def au3formater(line, indent):
    # line = line.strip().lower()
    line = line.strip()

    next_indent = indent
    if (line.startswith('End') or line.startswith('Until') or line in ('Next', 'Wend')):
        indent -= 1
        next_indent -= 1
    elif line.startswith('If') and line.endswith('Then'):
        next_indent += 1
    elif (line.startswith('Func') or line.startswith('For') or line.startswith('Select') or \
    line.startswith('Switch') or \
    line.startswith('While') or line == 'Do'):
        next_indent += 1
    elif line.startswith('Else') or line.startswith('Case'):
        indent -= 1
    new_line = _INDENT * indent + line

    return new_line, next_indent

def main():
    with open(_AU3, 'r',encoding='UTF-8') as fp:
        with open(_AU3_OUT, "w") as fpw:
            indent = 0
            line = fp.readline()
            while line:
                new_line, indent = au3formater(line, indent)
                fpw.write('%s\n' % new_line)
                line = fp.readline()


if __name__ == '__main__':
    main()