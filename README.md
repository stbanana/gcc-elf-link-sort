# gcc-elf-link-sort
一个用于对 arm elf 文件中包含的符号信息进行提取并且排序的小工具。

可以作为后处理任务方便地集成进编译流。

# 前提需要

使用 arm-none-eabi-objdump 工具，是 armgcc 工具链的一部分

可以使用 cmd 终端输入如下指令，检查是否具有这个工具

```sh
arm-none-eabi-objdump -v
```

如果使用其他 gcc 工具链，建议修改脚本中 "arm-none-eabi-objdump" 相关部分

# 如何使用

打包成 exe 文件并命名 例如 gccMapView.exe 。

在终端使用类似如下命令即可使用。

```sh
gccMapView.exe E:\PY32_PROJECT\gccMapView
```



需要传参一个目录地址给程序，程序会遍历这个个文件目录，为每个 .elf 文件自动生成。没有传参，那么以exe所在的目录作为地址。

name.symbols ：原版 objdump --syms 命令生成的符号表。

name.symbols.view ：经过地址排序和格式化后的符号表。



如果不使用命令行，将 .exe 与 .elf 文件放在同一文件夹下，双击 .exe 也可以使用。自动遍历 .exe 所在的目录，为每个 .elf 文件自动生成。

# 效果

原map文件如下
![原map](/README.DATA/原map.png)





![整理输出](/README.DATA/整理输出.png)
