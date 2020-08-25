
import copy
seasons = ['1', 2, 3, '4']

a = []
b = []
for i in seasons:
    a.append(i)
    b.append(copy.copy(i))
print(a, b)
print(list(enumerate(seasons, start=1)))

print('----------' * 10)
copy_test = {4: [1, 2, 3]}
copy_test1 = copy_test
copy_test2 = copy.copy(copy_test)
copy_test3 = copy.deepcopy(copy_test)
print(copy_test1, '\n', copy_test2, '\n', copy_test3, '\n')
copy_test[4].append(4)
print(copy_test1, '\n', copy_test2, '\n', copy_test3, '\n')


print(str([('--ifile', 'e:/wellhome'), ('-o', 'c:/wellhome')]))
import json
import re
a = 10

src_list = []
while a:
    dict_data = {1: a}
    src_list.append(dict_data)
    a -= 1

# with open('dict_write.json', 'w') as f:
#     f.write(json.dumps(src_list))
#
# for i in range(1, 10):
#     print(i)
#
# re_data = 'hu:1213'
#
# print(re.findall(r'\d+', re_data))

import sys
with open('dict_write.json', 'rb') as f:
    print(json.loads(f.read()))
print(sys.argv)