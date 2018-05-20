from collections import defaultdict, namedtuple

websites = [
    ('Sohu', 'http://www.google.com/', '张朝阳'),
    ('Sina', 'http://www.sina.com.cn/', '王志东'),
    ('163', 'http://www.163.com/', '丁磊')
]
WebSite = namedtuple('Website', ['name', 'url', 'founder'])
for website in websites:
    website = WebSite._make(website)
    print(website)

members = [
    # Age, name
    ['male', 'John'],
    ['male', 'Jack'],
    ['female', 'Lily'],
    ['male', 'Pony'],
    ['female', 'Lucy'],
]
result = defaultdict(list)
for sex, name in members:
    result[sex].append(name)
print(result)
s = result['s']
print(s)