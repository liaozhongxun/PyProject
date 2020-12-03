# 读取旧文件数据,再添加到新文件中
import os

oldfilename = input('请输入一个文件路径:')

if os.path.isfile(oldfilename):
    splitname = oldfilename.rpartition('.')
    oldfile = open(oldfilename, 'rb')
    newfile = open(splitname[0] + '.copy.' + splitname[2], 'wb')

    while True:  # 为了处理很多的文件，一点一点的读写
        conten = oldfile.read(1024)  # 读完一段之后光标会停留在最后读取的地方,所已下一次读取会接的上
        newfile.write(conten)
        if not conten:
            break

    newfile.close()
    oldfile.close()
else:
    print('文件不存在')

# 二进制才能读取视频和图片这类文件
