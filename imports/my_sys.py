import sys
sys.stdout = open('stdout.txt', 'w', encoding='utf8')
sys.stderr = open('stderr.txt', 'w', encoding='utf8')

print(sys.path)  # 得到一个列表,表示所有模块的查找路径

sys.stdin  # 接收用户输入
sys.stdout  # 修改输出位置
sys.stderr  # 修改错误输出位置

# st = sys.stdin
# centenr = st.readline()
# print(centenr)


print("正确输出")
print(1 / 0)
sys.exit(100)  # 结束程序
