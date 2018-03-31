# -*- coding: utf-8 -*-
import os

name = input("将要转换的py文件的拖入这里并按回车  \n")
judgment = input("gui程序且不想显示命令行请输入y  \n")
single_file = input("静态编译请键入y \n")
w = ""
f = ""
if judgment == "y":
    w = "-w "
if single_file == "y":
    f = "-F "
path, filename = os.path.split(name)
pyname = filename.replace("ui", "py")
os.system("pyinstaller " + f + w + name)
input()
