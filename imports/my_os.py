import os
import time

# os.name 获取操作系统名字  windows系列 -> nt ,非windows系列 -> posix
print(os.name)

# os.sep 获取路径分隔符  windows系列 -> \ ,非windows系列 -> /
print(os.sep)

# os.path
# os.path.abspath 获取文件的绝对路径
print(os.path.abspath('../def.py'))

# os.path.isdir 判断是否为文件夹
print(os.path.isdir('../imports'))

# os.path.isfile 判断是否为文件
print(os.path.isfile('../imports'))

# os.path.exists 判断文件是否存在
print(os.path.exists('../imports'))

# os.path.splitext 拆分文件名与后缀
print(os.path.splitext('../def.py'))

# os 其他方法
# 改变当前文件工作目录
# os.chdir('../../PyProject')

# 获取当前脚本所在的工作目录
print(os.getcwd())

# 更改文件名
# os.rename('sys.py', 'my_sys.py')
# os.rename('time.py', 'my_time.py')

# 删除文件
# os.remove('delt.py')

# 创建文件夹
# os.mkdir('creatdir')

# 删除空文件夹
# os.rmdir('creatdir')
# os.removedirs('creatdir')

# 列出指定目录里的所有文件和文件夹
print(os.listdir('../../PyProject'))

#获取环境配置
print(os.environ)
print(os.environ.get('ALLUSERSPROFILE'))
