# 这是单行注释

'''
 使用多个界定符分割字符串

 你需要将一个字符串分割为多个字段，但是分隔符(还有周围的空格)并不是固定的。
'''

import re

line = 'asdf fjdk; afed, fjek,asdf,      foo'

# （1）使用str.split()进行字符串分隔
# 对于多个空格，也会进行分隔
print(line.split(' '))

# （2）使用正则表达式进行分隔
# 使用r''表示是raw string，不会对字符串进行转义
parts = re.split(r'[;,\s]\s*', line)
print(parts)

# （3）捕获分组
fields = re.split(r'(;|,|\s)\s*', line)
print(fields)

# (4)重建数组
values = fields[::2]
delimiters = fields[1::2]
# 往后面添加了一个空格
delimiters.append('')
print('values=', values)
print('delimiters=', delimiters)

# zip的作用是合并两个列表
newline = ''.join(v + d for v, d in zip(values, delimiters))
print(newline)

#（5）需要使用（），但是不想捕获
parts = re.split(r'(?:,|;|,|\s)\s*', line)
print(parts)
