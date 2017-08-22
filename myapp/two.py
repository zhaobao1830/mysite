from importlib import reload
from myapp import one
print(one.name)
if __name__ == '__main__':
    print('two模块是执行模块')
else:
    print('two模块是被其他模块导入运行')

reload(one)