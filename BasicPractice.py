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

# 여러줄의 문자열의 변수선언 방법
multiStr = '''파이썬은
영어로
Python'''

print(multiStr)

print("-----------------------------------")

# 출력방법 5가지
python = '파이썬'
java = '자바'
C = 'C언어'
C_sharp = 'c#'

print(python + ' ' + java)  #파이썬 자바

print(python, java)         #파이썬 자바

print('요즘 대세 개발언어 2종류는 {}과 {}입니다.'.format(python,java))

print('{2}와{3} 같은 언어는 불편하고 어려워요. {0}이 최고입니다.'.format(python,java,C,C_sharp))

print(f'개발언어 중 {python}부터 공부하고 {java}를 공부하세요.')

print("-----------------------------------")

# 리스트
dev_list = ['파이썬','자바','플러터','C','C','C']    # 리스트는 중복데이터 허용

multi_list = [10,3.14,'Number',True,False]         # 여러 종류의 데이터 한꺼번에 허용

empty_list = []                                     # 빈 리스트 허용

# 리스트 출력
print(dev_list[1])  # 자바
'''리스트 안에 있는 값들은 순서가 보장되어 있음.'''

# 리스트 슬라이스
print(multi_list[0:4])  # [10,3.14,'Number',True]

# 리스트에 포함된 데이터 확인 = Boolean 값
print('C' in dev_list)  # True

# 리스트 안의 데이터 갯수 확인
print(len(dev_list))    # 6

# 리스트 데이터 추가
dev_list.append('javaScript')
print(dev_list)         # ['파이썬','자바','플러터','C','C','C','javascript']

# 리스트 데이터 삭제
dev_list.remove('플러터')
print(dev_list)         # ['파이썬','자바','C','C','C','javascript']

print("-----------------------------------")

#튜플
