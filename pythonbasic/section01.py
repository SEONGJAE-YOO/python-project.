import sys

print(sys.stdin.encoding)
print(sys.stdout.encoding)
   
for i in range(1,10):
    for j in range(1,10):
        print('%d * %d = ' % (i,j), i*j)

def 인사():
    print("안녕하세요")

인사()

def greet():
    print('jee')

greet()

class ckko:
    pass

#객체
ckko = ckko()

print(id(ckko))
print(dir(ckko))