# 将值转换为字符串并设置格式

print('\r\n---转换说明符 %s---')
## 转换说明符 %s
tpl = 'Hi, %s! %s is a beautiful day.'
values = ('man', 'Today')
print(tpl % values)

print('\r\n---Template()---')
## 模板字符串
from string import Template
tpl = Template('Hi, $name! $time is a beautiful day.')
print(tpl.substitute(name='man', time='Today')) # Hi, man! Today is a beautiful day.

print('\r\n---format()---')

## format
print('{} {} {}'.format(1, 2, 3)) # 1 2 3
print('{0} {1} {2} {1} {0}'.format(1, 2, 3)) # 1 2 3 2 1

from math import pi
print('{name} ≈ {value:.2f}'.format(value=pi, name='π')) # π ≈ 3.14

from math import e
print("Euler's constant is roughly {e}.".format(e=e)) # Euler's constant is roughly 2.718281828459045.
print(f"Euler's constant is roughly {e}.") # Euler's constant is roughly 2.718281828459045.
