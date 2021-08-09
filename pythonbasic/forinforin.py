#for문 한줄로 코딩

v = [list(range(111)),[10,11,12]]
print(v)

# for i in v:
#     for j in i:
#         print(j)


[j for i in v for j in i]


#if 문 한줄로 코딩

ran=3

if ran <5:
    print(0)
elif ran <10:
    print(1)
else:
    print(2)
  
print(0 if ran<5 else 1 if ran<10 else 2)  


#for if 한줄로 코딩

v = list(range(10,20))

for i in v:
    if i ==12:
        print(i)
    else:
        print("No")

[i if i ==12 else "No" for i in v]
