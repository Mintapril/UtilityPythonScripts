import os
import shutil

xmlfilepath = input("将需要转换的Etterna.xml文件拖到这里并回车确认 \n")
path, xmlfile = os.path.split(xmlfilepath)
shutil.copyfile(xmlfilepath, os.path.join(path, "EtternaBackup.xml"))
backupfilepath = os.path.join(path, "EtternaBackup.xml")
xmlfile = open(backupfilepath, "r", errors = 'ignore')
newfile = open(os.path.join(path,"Etterna.xml"), "w+")
for line in xmlfile:
    if " NoMines," in line:
        line = line.replace(" NoMines,", "")
    if " Shuffle," in line:
        line = line.replace(" Shuffle,", "")
    if " SoftShuffle," in line:
        line = line.replace(" SoftShuffle,", "")
    if " Right," in line:
        line = line.replace(" Right,", "")
    if " Left," in line:
        line = line.replace(" Left,", "")
    if " Reverse," in line:
        line = line.replace(" Reverse,", "")
    newfile.write(line)
xmlfile.close()
newfile.close()
input("转换成功,原文件已备份为EtternaBackup.xml \n回车键退出")

