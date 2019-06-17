f = open('text.txt', 'rt', encoding='utf-8')

text = f.read()

print(text)

text = f.read() # 포인터가 끝까지 온거다

print('---', text, '----')

#
pos = f.tell()
print(pos)

# (offeset, form_what)
# 1st param: offset
# 2nd param: from_what(0:시작, 1: 현재위치 . 2: 끝)
# text mode에서는 from_what은 0(파일 시작)만 허용
f.seek(16, 0) # 이동시킬때
text = f.read()
print(text)

# 예외는 seek(0,2) 끝으로 이동하는 경우
f.seek(0, 2) # append 할라고

# line 단위로 읽기
linenum = 0
f2 = open('fileio2.py','r',encoding='utf-8')
# for line in f2.readlines():
#     print(line, end='')
while True:
    line = f2.readline()
    if line == '':
        f2.close()
        break
    linenum += 1
    print('{0}:{1}'.format(linenum, line), end='')

f2.close()


# linenum 더 간단하게 얻기
f3 = open('fileio2.py','r',encoding='utf-8')
lines = f3.readlines()
for linenum, line in enumerate(lines):
    print('{0}:{1}'.format(linenum, line), end='')
f3.close()




