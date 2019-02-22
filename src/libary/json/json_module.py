import json

data = {
    'status': True,
    'extra': None,
    'name': 'a',
    'id': 1
}

print(json.dumps(data))

print('\r\n---ensure_ascii---')
## ensure_ascii 参数
data = { '姓名': 'a', '年龄': 'b' }
print(json.dumps(data))
print(json.dumps(data, ensure_ascii=False))

print('\r\n---allow_nan---')
## allow_nan 参数
data = { 'nan': float('nan'), 'infinity': float('inf'), '-infinity': float('-inf') }
print(json.dumps(data))
# print(json.dumps(data, allow_nan=False))

print('\r\n---check_circular---')
## check_circular 参数
data = {}
data['self'] = data
# print(json.dumps(data))
# print(json.dumps(data, check_circular=False))

print('\r\n---indent---')
## indent 参数
data = { 'name': 'a', 'age': 18, 'score': { 'english': 80, 'math': 90 }}
print(json.dumps(data))
print(json.dumps(data, indent=0))
print(json.dumps(data, indent=4))

print('\r\n---separators---')
## separators 参数
data = { 'name': 'a', 'age': 18, 'score': { 'english': 80, 'math': 90 }}
print(json.dumps(data, separators=(',', ':')))

print('\r\n---skipkeys---')
## skipkeys 参数
data = { (1, 2): 123}
print(json.dumps(data, skipkeys=True))
# print(json.dumps(data))

print('\r\n---sort_keys---')
## sort_keys 参数
data = { 'name': 'a', 'age': 18, 'score': { 'english': 80, 'math': 90 }}
print(json.dumps(data, sort_keys=True))
print(json.dumps(data))

print('\r\n---json.dump()---')
## json.dump()
data = { 'name': 'a', 'age': 18, 'score': { 'english': 80, 'math': 90 }}
with open('output.json', 'w') as fp:
    json.dump(data, fp)

print('\r\n---json.loads()---')
## json.loads()
data = { 'name': 'a', 'age': 18, 'score': { 'english': 80, 'math': 90 }}
print(json.loads(json.dumps(data)))

print('\r\n---json.load()---')
## json.load()
with open('output.json', 'r') as f:
    print(json.load(f))