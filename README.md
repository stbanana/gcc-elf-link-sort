# gcc-elf-link-sort
一个用于对 arm elf 文件中包含的符号信息进行提取并且排序的小工具。

可以作为后处理任务方便地集成进编译流。

# 如何使用

打包成 exe 文件并命名 例如 gccMapView.exe 。

在终端使用类似如下命令即可使用。

```sh
gccMapView.exe E:\PY32_PROJECT\gccMapView
```



需要传参一个目录地址给程序，程序会遍历这个个文件目录，为每个 .elf 文件自动生成

name.symbols ：原版 objdump --syms 命令生成的符号表。

name.symbols.view ：经过地址排序和格式化后的符号表。
