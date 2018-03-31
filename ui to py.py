import os

name = input("将要转换为py文件的ui文件拖入这里并按回车开始转换  \n")
path, filename = os.path.split(name)
pyname = filename.replace("ui", "py")
os.system("pyuic5 " + name + " -o " + path + "\\" + pyname)
