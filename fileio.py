# textmode 가 default:t
f = open('text.txt', 'wt', encoding='utf-8') # write text
# 1. 호출해서
write_size = f.write('안녕하세요\n파이썬입니다.')
# 2. 파라미터로
print('hello world12345', type(f), file=f)

print(write_size)

# binary mode : b
f = open('text2.txt', 'wb')
write_size = f.write(bytes('안녕하세요\n파이썬입니다.', encoding='utf-8'))  # text를 바이트로 바꿔야 함
f.close()
print(write_size)

# read test
f = open('text.txt', 'rt', encoding='utf-8')
text = f.read()
f.close()
print(text)

# binary read : copy file
fsrc = open('python.png', 'rb')
data = fsrc.read()
fsrc.close()

print(type(data))

fdest = open('python2.png', 'wb') # 열고
fdest.write(data) # data 넣기
fdest.close()











