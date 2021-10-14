from collections import namedtuple

student = namedtuple('name', ['name', 'age', 'sex'])
tu = student("pdd", 20, '男')
print(tu)

