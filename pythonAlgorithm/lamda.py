#coding test 1

def add(a,b):
    return a + b

def subtract(a,b):
    return a - b

result = add(3,7)
print(result)

result = subtract(3,7)
print(result)

#coding test 2
a = 0

def func():
    global a #함수 바깥에 선언된 변수를 바로 참조 
    a += 1

for i in range(10):
    func()

print(a) 

#코딩 테스트 3 (람다식)

def add(a,b):
    return a + b

print(add(3,7))

#lamda
print((lambda a,b: a+b)(3,7))


#lamda 
array = [('asdd',50),('dww',33),('qwd',11)]

#1
def my_key(x):
    return x[1]

print(sorted(array, key=my_key))

#2
print(sorted(array, key=lambda x:x[1]))
