f = open('test.txt')
print(f.read(1))
print(f.read())
f.close()


f = open('test.txt')
for line in f:
    print(line)
f.close()


l = [str(i)+str(i-1) for i in range(20)]
f = open('text.txt', 'w')
for index in l:
    f.write(index + '\n')
f.close()