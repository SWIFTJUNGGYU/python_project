print("--------- Basic Practice ----------")

# 문자자료형
print('Hello World')
print("안녕하세요.")

# 숫자자료형
print(1)
print(3.15)

# Boolean자료형
print(True)
print(False)
'''꼭 앞글자는 대문자로 되어야한다'''

print("-----------------------------------")

# 변수
variableTxt = 'Text 변수'
variableNum = 3560

print(variableTxt)
print(variableNum)

# 변수의 규칙
var = '문자'
_var = '밑줄 문자'
var_1 = '문자 밑줄 숫자 혼합'
'''변수명에 공백 or 특수문자 사용불가'''

Var = '앞 대문자 변수'
VAR = '전체 대문자 변수'

print(var)
print(_var)
print(var_1)
print(Var)
print(VAR)

print("-----------------------------------")

# 형변환
# 문자형 → 정수형
numInt = int('2')

# 문자형 → 실수형
numFloat = float('1.5')

# 숫자 → 문자형
strNum = str(2)

# 실수형 → 정수형
numFloatInt = int(float('2.5'))
'''실수를 정수로 형변환시 소수점 이하의 값은 버림으로 처리'''


print(numInt)
print(numFloat)
print(strNum)
print(numFloatInt)

print("-----------------------------------")

# 문자열 인덱스
lang = 'PYTHON'

print(lang[0])  # 문자열 가장 첫번째
print(lang[-1]) # 문자열 가장 마지막

# 문자열 슬라이스
print(lang[3:6]) # 문자열 3번째부터 6번째 직전까지의 문자열 슬라이스
print(lang[2:])  # 문자열 2번째부터 끝까지의 문자열 슬라이스
print(lang[:4])  # 문자열 제일 첫번째부터 4번째 직전까지의 문자열 슬라이스
print(lang[:])   # 문자열의 제일 처음부터 끝까지 슬라이스

print("-----------------------------------")

# 여러줄의 문자열을 변수로 진행할 때
multiStr = '''파이썬은
영어로
Python'''

print(multiStr)
