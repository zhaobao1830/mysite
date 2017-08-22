name = 'tom'
def func():
    return name
if __name__ == '__main__':
    print('one模块是执行模块')
else:
    print('one模块是被其他模块导入运行')