#注释+转义字符
#2020.10.7

#this is an annotation for single line
"""
this is an annotation for multiple line
second line
third line
这几行将会被解释器忽略
"""

'''
this is another way to annotate
second line
third line
'''

#单行注释
#print("解释器将会忽略此行")
print("此行不会被忽略")  #简单的内容可以放在语句后面

# 快捷键为Ctrl+/

#转义字符 Escape character 
# \n 换行
# \t 制表符，（4个空格）
print("-----------------")
print("输出的内容",end="\n")  # end="\n"换行结束符，print()默认换行
print("输出的内容",end=" >>>这个是结束符号\n")
print("hello\nPython")      # \n转义
print("\tabcd")             # \t制表符

