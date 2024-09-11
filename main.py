import os
import glob
import re
import sys
import csv
from collections import namedtuple

# 定义一个命名元组来存储符号信息
Symbol = namedtuple('Symbol', 'address attribute type section size name')


def process_elf_file(elf_file, output_directory):
    # 生成符号表文件名
    symbol_file = os.path.join(output_directory, os.path.basename(elf_file).replace('.elf', '.symbols'))
    sorted_symbol_file = os.path.join(output_directory, os.path.basename(elf_file).replace('.elf', '.symbols.view'))

    # 使用 shell 命令将符号表输出到文件
    os.system(f"arm-none-eabi-objdump --syms {elf_file} > {symbol_file}")

    # 读取符号表文件内容
    with open(symbol_file, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # 定义正则表达式模式
    pattern = re.compile(
        r'^\s*([0-9a-fA-F]+)\s+([lgw])\s+(F|O|df|d)?\s+([\.\w*]+)\s+([0-9a-fA-F]+)\s+(.*?)$'
    )

    symbols = []

    # 使用正则表达式逐行匹配数据
    for line in lines:
        match = pattern.match(line)
        if match:
            address, attribute, type_, section, size, name = match.groups()
            type_ = type_ if type_ else ""
            symbols.append(Symbol(address, attribute, type_, section, size, name))

    # 将符号按地址排序
    symbols.sort(key=lambda sym: int(sym.address, 16))

    # 表头注释
    header_comment = (
        "# 属性: l (本地), g (全局), w (弱符号)\n"
        "# 类型: F (函数), O (对象), df (调试文件), d (调试符号)\n"
    )

    # 表头
    header = ['地址(0x)', '属性', '类型', '节段', '大小(0x)', '名称']

    # 列宽度
    column_widths = [14, 4, 4, 14, 10, 40]

    # 打印表头和排序后的符号表到文件
    with open(sorted_symbol_file, 'w', encoding='utf-8') as f:
        f.write(header_comment)
        f.write(''.join([f"{header[i]:<{column_widths[i]}}" for i in range(len(header))]) + "\n")

        for sym in symbols:
            f.write(
                f"{sym.address:<{column_widths[0]}}"
                f"{sym.attribute:<{column_widths[1]}}"
                f"{sym.type:<{column_widths[2]}}"
                f"{sym.section:<{column_widths[3]}}"
                f"{sym.size:<{column_widths[4]}}"
                f"{sym.name:<{column_widths[5]}}\n"
            )

    print(f"Processed {elf_file}, sorted symbols written to {sorted_symbol_file}")


def main():
    # 获取工作目录
    if len(sys.argv) < 2:
        print("No directory specified, processing current directory.")
        directory = os.getcwd()
    else:
        directory = sys.argv[1]
        if not os.path.isdir(directory):
            print(f"Error: {directory} is not a valid directory.")
            sys.exit(1)

    # 遍历指定目录下的所有 .elf 文件
    elf_files = glob.glob(os.path.join(directory, "*.elf"))

    # 处理每个 .elf 文件
    for elf_file in elf_files:
        process_elf_file(elf_file, directory)


if __name__ == "__main__":
    main()
