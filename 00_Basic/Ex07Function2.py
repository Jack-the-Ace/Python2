# 파이썬에 내장된 함수... 중 .. 가장 많이 사용하는 파일입출력기능

# 1) 파일에 데이터를 저장하기 (특별한 경로가 없으면 터미널의 현재경로)
file=open('aaa.txt',"w") #mode: w(write), a(append), r(read)
file.write('this is python programming.. 안녕하세요')
file.close()

# 2) 파일의 데이터를 읽어오기
file=open('aaa.txt','r')
contents=file.read()
print('파일에서 읽어온 글씨:', contents)
file.close()
print('='*100)

# 3) len() : 배열이나, 문자열의 길이를 리턴해주는 함수
message='nice to meet you'
print(len(message))

data= [10,20,30,40,50]
print(len(data))

# 4) max(), min()
a= max(data)
print(a)
b= min(data)
print(b)

# 5) round() - 반올림
score= 87.4
#score= 87.5
print(round(score))




