import sys

print(1)
print('hello','','hello')

# sep 파라미터 쓰는 법
x = 0.2
s = 'hello'
print(str(x) + ' ' + s)
print(x,s, sep=' ')

# 기본적인 print() 함수 호출
print(sep=' ', end='\n')

# file 파라미터를 지정
print('hello World', file=sys.stdout)
print('error : hello World', file=sys.stderr)

# file 출력
f = open('hello.txt', 'w')
print(type(f))
print('hello world12345', type(f), file=f)
f.close()

# 참고
sys.stdout.write('Hello World!!')