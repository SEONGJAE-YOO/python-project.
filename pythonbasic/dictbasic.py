D = {'join':'0011','Maria':'1234'}
print(D['join'])

# 사전 D에 key가 'a'이고 value가 3인 원소를 추가
D['A'] = 3
print(D)

#{'join': '0011', 'Maria': '1234', 'A': 3}


#VALUE 값 수정
D['A'] = 4
print(D)

#{'join': '0011', 'Maria': '1234', 'A': 4}


#######
D = {'name' : 'Kim', 'phone':'01010023', 'birth':'1234'}

print(D.keys())

#dict_keys(['name', 'phone', 'birth'])

print(D.values())

#dict_values(['Kim', '01010023', '1234'])

print(D.items())

#dict_items([('name', 'Kim'), ('phone', '01010023'), ('birth', '1234')])

print(D.get('name')) #name 키값 꺼낸다

#Kim