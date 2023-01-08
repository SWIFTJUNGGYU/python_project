print("--------- Basic Practice ----------\n")

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

print("-----------------------------------\n")

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

print("-----------------------------------\n")

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

print("-----------------------------------\n")

# 문자열 인덱스
lang = 'PYTHON'

print(lang[0])  # 문자열 가장 첫번째
print(lang[-1]) # 문자열 가장 마지막

# 문자열 슬라이스
print(lang[3:6]) # 문자열 3번째부터 6번째 직전까지의 문자열 슬라이스
print(lang[2:])  # 문자열 2번째부터 끝까지의 문자열 슬라이스
print(lang[:4])  # 문자열 제일 첫번째부터 4번째 직전까지의 문자열 슬라이스
print(lang[:])   # 문자열의 제일 처음부터 끝까지 슬라이스

print("-----------------------------------\n")

# 여러줄의 문자열의 변수선언 방법
multiStr = '''파이썬은
영어로
Python'''

print(multiStr)

print("-----------------------------------\n")

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

print("-----------------------------------\n")

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

print("-----------------------------------\n")

# 튜플
'''리스트와 달리 한번 지정 후 수정할 수 없다'''
'''읽기전용 리스트'''
dev_tuple = ('파이썬', '플러터', '자바')
print(dev_tuple)        # ('파이썬', '플러터', '자바')

# 튜플 언패킹
'''지정된 튜플을 다른 변수로 풀어놓는 것'''
number_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
(one, two, *others, nine, ten) = number_tuple

print(one)              # 1
print(two)              # 2
print(others)           # [3, 4, 5, 6, 7, 8] *표시된 변수는 나머지 값들의 리스트로 지정된다.
print(nine)             # 9
print(ten)              # 10

print("-----------------------------------\n")

# 세트
'''데이터의 중복허용X, 순서X'''

num_set = {8,1,6,2,3,4,4,0,5,2,6,1,8}
print(num_set)          # {0, 1, 2, 3, 4, 5, 6, 8}

num_set.add(9)
print(num_set)          # {0, 1, 2, 3, 4, 5, 6, 8, 9}

num_set.remove(5)
print(num_set)          # {0, 1, 2, 3, 4, 6, 8, 9}

num_set.clear()
print(num_set)          # set()

del num_set
#print(num_set)          # 완전삭제 Error: 'num_set' is not defined

print("-----------------------------------\n")

# 딕셔너리
'''key와value의 조합'''
'''{key1:value1, key2:value2...}'''

son_7 = {
    'name':'Son heung min',
    'age': 31,
    'height': 180,
    'kick': 'Right&Left',
    'club': 'TOT',
    'color': 'White'
}

# 딕셔너리 값 확인
print(son_7['name'])      # Son heung min
print(son_7['age'])       # 31
print(son_7.get('height'))# 180

# 딕셔너리 값 추가
son_7['grade'] = 'high school'
print(son_7.get('grade'))# High school

print("-----------------------------------\n")

# 튜플 ↔ 리스트 형변환
'''추가, 수정, 제거가 되지않는 튜플에 
   이와 같은 기능을 가능하게 만드는 방법'''

var_tuple = ('A', 'B', 'C')
var_list = list(var_tuple)              # 튜플을 추가, 수정, 제거가 가능한 리스트로 형변환
var_list.append('D')
var_tuple = tuple(var_list)

print(var_tuple)                        # ('A', 'B', 'C', 'D')

print("-----------------------------------\n")

# 리스트 ↔ 세트 형변환
'''중복값이 포함된 리스트의 중복값을 제거하는 방법1'''

var_list = ['A', 'B', 'C', 'B', 'A']
var_set = set(var_list)                 # 세트는 중복값을 허용하지 않기 때문에 리스트에 포함된 중복값 제거
var_list = list(var_set)
print(var_list)                         # ['B', 'A', 'C']

'''세트 개념은 순서도 값의 순서도 보장하지 않기 때문에
리스트 데이터의 순서가 섞일 수 있다.'''

print("-----------------------------------\n")

# 리스트 ↔ 딕셔너리 형변환
'''중복값이 포함된 리스트의 중복값을 제거하는 방법2 (순서 보장)'''

var_list = ['A', 'B', 'C', 'C', 'B']
var_dic = dict.fromkeys(var_list)       # 딕셔너리는 중복값을 허용하지 않고 순서를 보장함

print(var_dic)                          # {'A':None, 'B':None, 'C':None}

var_list = list(var_dic)
print(var_list)                         #['A', 'B', 'C']
