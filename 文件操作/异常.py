try:
    x = 5 / 2
except Exception as e:  # 如果程序出错立刻跳转except语句,不会指向异常下面的语句
                        # Exception 错误类型的父类，若缓存指定错误类型，就只能捕获这种异常的错误
    print('发现异常...')
else: # 如果程序没有出错
    print('计算结果是',x)
