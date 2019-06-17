f = open('123.txt','wb')
f.write(b'0123456789')
f.close()

# 여는거너 binary로 열었다
f = open('123.txt', 'rb')
print(f.tell())

f.seek(5,1)
data = f.read(2)
print(data)

f.seek(-5, 1)
data = f.read(3)
print(data)

f.seek(0,2) # 맨 끝으로 이동시킴

f.seek(-5, 1)
data = f.read(3)
print(data)

# 밑에 코드 with ~ as 으로 바꾸기

with open('fileio2.py','rt',encoding='utf-8') as f2:
    for linenum, line in enumerate(f2.readlines()):
        # if line == '':
        #     f2.close()
        #     break     with as 구문은 이 코드 필요없 close
        print('{0}:{1}'.format(linenum, line), end='')
f2.close()