#여러 줄인 문자열을 변수에 대입하고 싶을 때
#1. \n
multiline = "Life is too short\nYou need python"
multiline

#2. ''' 또는 """ 사용하기
multiline1 = '''
Life is too short
You need Python
'''
print(multiline1)

multiline2 = """
Life is too short
You need Python
"""
print(multiline2)

#이스케이프 코드
# \n : 문자열 안에서 줄을 바꿀 때 사용
# \f : 문자열 사이에 탭 간격을 줄 때 사용
# \\ : 문자 \를 그대로 표현할 때 사용
# \' : 작은 따옴표(')를 그대로 표현할 때 사용
# \" : 큰 따옴표(")를 그대로 표현할 때 사용
# \r : 캐리지 리턴(줄 바꿈 문자, 현재 커서를 가장 앞으로 이동)
# \f : 폼 피드(줄 바꿈 문자, 현재 커서를 다음 줄로 이동)
# \a : 벨소리 (출력할 PC 스피커에서 삑 소리가 난다)
# \b : 벡스페이스
# \000 : 널문자

