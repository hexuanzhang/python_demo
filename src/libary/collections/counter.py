from collections import Counter

# Counter()
print(Counter())
print(Counter('abcbabcba'))
print(Counter(['a', 'b', 'a', 'c', 'b', 'b']))
print(Counter({'a': 4, 'b': 2}))
print(Counter(a=3, b=6))

print('---修改计数---')
# 修改计数
c = Counter(['a', 'b', 'a', 'c', 'b', 'b'])
print(c['a'])
print(c['d'])
c['a'] = 5
print(c['a'])
c['c'] = 0
print(c);
del c['c']
print(c)
c.clear()
print(c)
c = Counter(a=-1, b=3, c=0, d=2, e=1)
print(+c)

print('---elements()---')
# elements()
c = Counter(a=3, b=0, c=5, d=6)
print(c.elements())

print('---most_common(n)---')
# most_common(n)
c = Counter(a=3, b=0, c=5, d=6)
print(c.most_common())
print(c.most_common(2))
print(c.items())

print('---subtract(counter)---')
# subtract(counter)
c = Counter(a=3, b=0, c=5, d=6)
c.subtract(Counter(a=1, b=1, c=2))
print(c)

print('---update(counter)---')
# update(counter)
c = Counter(a=3, b=0, c=5, d=6)
c.update('abdeacd')
# c.update(Counter(a=1, b=1, c=2, e=3))
print(c)

print('---数学运算---')
# 数学运算
c = Counter(a=3, b=1, c=1)
d = Counter(a=1, b=2, c=1)
## c+d 的效果与 c.update(d) 类似
print(c+d)

## c-d 的效果与 c.subtract(d) 类似，两者的区别在于 c-d 只会保留计数大于 0 的元素
print(c-d)
## c&d 相当于 min(c[x], d[x])
print(c&d)
## c|d 相当于 max(c[x], d[x])
print(c|d)

print('---一元操作---')
c = Counter(a=3, b=0, c=-5)
## +c = c-Counter()
print(+c)
print(c-Counter())
## -c = Counter-c
print(-c)
print(Counter()-c)


print('---Counter 转换---')
c = Counter(a=3, b=0, c=5, d=6)
print(list(c))
print(set(c))
print(dict(c))
print(c.items())
