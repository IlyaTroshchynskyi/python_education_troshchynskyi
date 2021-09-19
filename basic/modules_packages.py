import re

find_members = []
for obj in dir(re):
    if 'find' in obj:
        find_members.append(obj)

find_members.sort()
print(find_members)