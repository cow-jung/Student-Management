students = [
    {'class':1,'number':1,'name':'강승균','kor': 90, 'eng': 85, 'math': 88},
    {'class':1,'number':2,'name':'고태균','kor': 81, 'eng': 85, 'math': 60},
    {'class':1,'number':3,'name':'김상철','kor': 91, 'eng': 48, 'math': 50},
    {'class':1,'number':4,'name':'김시창','kor': 40, 'eng': 74, 'math': 45},
    {'class':1,'number':5,'name':'백민욱','kor': 65, 'eng': 43, 'math': 76},
    {'class':2,'number':1,'name':'서다연','kor': 71, 'eng': 80, 'math': 70},
    {'class':2,'number':2,'name':'송주연','kor': 81, 'eng': 71, 'math': 85},
    {'class':2,'number':3,'name':'양소정','kor': 92, 'eng': 91, 'math': 72},
    {'class':2,'number':4,'name':'양해성','kor': 48, 'eng': 99, 'math': 46},
    {'class':2,'number':5,'name':'유민정','kor': 30, 'eng': 90, 'math': 70},
    {'class':3,'number':1,'name':'이재준','kor': 42, 'eng': 80, 'math': 77},
    {'class':3,'number':2,'name':'임주혁','kor': 50, 'eng': 43, 'math': 66},
    {'class':3,'number':3,'name':'정고은','kor': 60, 'eng': 75, 'math': 55},
    {'class':3,'number':4,'name':'정승빈','kor': 67, 'eng': 40, 'math': 88},
    {'class':3,'number':5,'name':'최유진','kor': 70, 'eng': 85, 'math': 99},
]

while True:
    print('=============== 학생 성적 관리 ===============')
    print('1. 학생 등록')
    print('2. 학생 수정')
    print('3. 학생 삭제')
    print('4. 성적 조회')
    print('5. 종료')
    students_menu = input('학생 성적 관리 메뉴를 선택하세요 : ')

    if students_menu == '1':
        print('=============== 학생 등록 ===============')
        print('1. 학생 정보 등록')
        print('2. 성적 정보 등록')


    elif students_menu == '2':
        print('=============== 학생 수정 ===============')
        print('1. 학생 정보 수정')
        print('2. 성적 정보 수정')


    elif students_menu == '3':
        print('=============== 학생 삭제 ===============')
        print()

        student_class = int(input('반을 입력하세요(숫자만): '))
        print(f'=============== {student_class}반 학생 목록 ===============')
        found_any = False # 해당 반에 학생이 한 명이라도 있는지 확인할 변수

        for student in students:
            if student['class'] == student_class:
                print(f'{student['number']}번 {student['name']}')
                found_any = True

        if found_any == False:
            print(f'{student_class}반에는 등록된 학생이 없습니다.')

        else:
            student_number = int(input('번호를 입력하세요(숫자만): '))
            student_name = input('이름을 입력하세요: ')

            delete_student = None

            for student in students:
                if (student['class'] == student_class) and (student['number'] == student_number) and (student['name'] == student_name):
                    delete_student = student
                break

            if delete_student == None:
                print('학생 정보를 찾을 수 없습니다.')
            else:
                students.remove(delete_student)
                print('학생 정보가 삭제되었습니다.')

    elif students_menu == '4':
        print('=============== 성적 조회 ===============')
        print('1. 반별 성적 조회')
        print('2. 전체 10등 조회')
        print('3. 학생 개인 조회')

    elif students_menu == '5':
        print('종료합니다.')
        break

    else:
        print('잘못 입력하셨습니다.')


