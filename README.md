# learn-python-the-hard-way
code of book - "learn python the hard way".

| Learner | content |
|-----------|----------|
| cyt | Python-Basic |

first update ex1-37
```python
# comment
# ex1 ex2 ex5 ex7-9 print 
print "hello"
print 'hello'
print "I update %d files" % 37    # %d,%r,%s 格式化字符输出 ex5
print """
print section1
section2
"""

# ex3 count(+,-,*,/,%,<,>,<=,>=)
print 12+5

# ex4 ex5 variable
cars = 100
weight = 120.56
name = 'Shaw'

# ex6 string 
w = 'hellow'
e = 'world'
print w+e #连续打印

# ex10 转义字符

# ex11 ex12 input
age = raw_input()
age = int(raw_input())  # 转换成数字
age = raw_input("Your age? \n")  # 提示符

# ex13 ex14 argument
from sys import argv
script, first, second, third = argv #运行程序时 需要输入三个参数

#

```
[ex15]
[ex15]:https://github.com/sillyer/learn-python-the-hard-way/blob/master/ex15.py 
```
# pydoc open 查看open函数相关文档
txt = open(filename) # filename 要读入的文件名称 
print txt.read()  # .read() 读入文件内容
```
[ex16]
[ex17]
[ex16]:https://github.com/sillyer/learn-python-the-hard-way/blob/master/ex16.py
[ex17]:https://github.com/sillyer/learn-python-the-hard-way/blob/master/ex17.py
```
input = open(filename_in, 'r')  # 'w'表示写入模式，会清空文档，'r'读模式， 'a'=append 追加模式 默认为r
target = input.read()
oneline = input.readline()
output = open(filename_out, 'w')
output.wirte(target)

len(target) # 文件长度

from os.path import exists
exists(filename_out)  # 验证filename_out这个文件是否存在？ 存在true，不存在false

```
[ex18 函数]
[ex18 函数]:https://github.com/sillyer/learn-python-the-hard-way/blob/master/ex18.py
