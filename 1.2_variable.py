#变量的作用及使用
#2020.10.7

# 1.1个人理解：定义变量实际就是给数据所在内存地址命名（贴标签）
# 1.2Python定义变量较简单，可直接赋值，只需要注意定义命名规则。
# 1.3命名规则
#     1.3.1数字，字母，下划线组成
#         如apple_number, student_height
#     1.3.2不能数字开头
#         如不能6person
#     1.3.3不能使用内置关键字
#         如不能False, if, try, with， import
#     1.3.4区分大小写
#         num和Num不为同一个变量
#     1.3.5命名习惯
#         大驼峰/小驼峰/下划线，如MyName，myName，my_name

#将1赋值给a变量（给数据1贴了一个名字为a的标签）
a = 1

num1 = 'happy'
NUM1 = 'happy'
num2 = 1
NUM2 = 2
print ("变量num1的地址为：",id(num1))
print ("变量NUM1的地址为：",id(NUM1))  #地址相同
print ("变量num2的地址为：",id(num2))
print ("变量NUM2的地址为：",id(NUM2))  #地址不同