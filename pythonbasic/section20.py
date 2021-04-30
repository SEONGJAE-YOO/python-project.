# Section12-3
# 파이썬 데이터베이스 연동(SQLite)
# 테이블 수정 및 삭제

import sqlite3

# DB생성(파일)
conn = sqlite3.connect('C:/GIT/pythonbasic/resource/database_section20.db')

# Cursor연결
c = conn.cursor()

# 데이터 수정1
c.execute("UPDATE users SET username = ? WHERE id = ?", ('niceman2', 1))

# 데이터 수정2
c.execute("UPDATE users SET username = :name WHERE id = :id", {"name": 'niceman', 'id': 3})

# 데이터 수정3
c.execute("UPDATE users SET username = '%s' WHERE id = '%s'" % ('badboy', 5))

# 중간 데이터 확인1
for user in c.execute('SELECT * FROM users'):
    print(user)

# # Row Delete1
c.execute("DELETE FROM users WHERE id = ?", (2,))

# Row Delete2
c.execute("DELETE FROM users WHERE id = :id", {'id': 5})

# Row Delete3
c.execute("DELETE FROM users WHERE id = '%s'" % 4)

# 중간 데이터 확인2
for user in c.execute('SELECT * FROM users'):
    print(user)

# -실행 결과
#(1, 'niceman2', 'Kim@naver.com', '010-0000-0000', 'Kim.com', '2021-04-30 15:14:55')
#(3, 'niceman', 'Lee@naver.com', '010-2222-2222', 'Lee.com', '2021-04-30 15:14:55')



# 테이블 전체 데이터 삭제
print("users db deleted : ", conn.execute("delete from users").rowcount, "rows")

#-실행결과
#users db deleted :  2 rows

# # 관계형 데이터 베이스

# 커밋
conn.commit()

# 접속 해제
conn.close()
#-실행결과
#users db deleted :  0 rows