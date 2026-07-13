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
    print('1. 학생 조회')
    print('2. 학생 수정')
    print('3. 학생 삭제')
    print('4. 성적 조회')
    print('5. 종료')
    students_menu = input('학생 성적 관리 메뉴를 선택하세요 : ')

    if students_menu == '1':
        print('=============== 학생 조회 ===============')
        for student in students:
            print(f"{student['class']}반 {student['number']}번 {student['name']} {student['kor']} {student['eng']} {student['math']}")


    elif students_menu == '2':
        print('=============== 학생 수정 ===============')
        while True:
            print('1. 학생 국어점수 수정')
            print('2. 학생 영어점수 수정')
            print('3. 학생 수학점수 수정')
            print('4. 뒤로 가기')
            menu = input('메뉴 선택: ')
            if menu == '1': # 메뉴 1번을 입력하여 국어점수 수정
                student_class = int(input('국어 점수를 수정할 학생의 반을 입력하세요: ')) # 정수이므로 int
                student_number = int(input('국어 점수를 수정할 학생의 번호를 입력하세요: '))
                for student in students:
                    if student['class'] == student_class and student['number'] == student_number:
                        # 학생의 반과 번호가 일치하는지 and를 써서 확인
                        print(f'수정할 학생의 이름은 {student['name']}입니다.') # 점수를 수정할 학생의 이름 출력
                        new_kor = input('수정할 국어점수를 입력하세요: ') # 새로운 점수를 new_kor 변수에 저장
                        student['kor'] = new_kor # 기존 국어 점수를 변경
                        print(f'국어점수가 {new_kor}점으로 수정되었습니다.')
                        break
                else:
                    print('해당하는 반과 번호의 학생이 없습니다.')

            elif menu == '2':
                student_class = int(input('영어 점수를 수정할 학생의 반을 입력하세요: '))
                student_number = int(input('영어 점수를 수정할 학생의 번호를 입력하세요: '))
                for student in students:
                    if student['class'] == student_class and student['number'] == student_number:
                        print(f'수정할 학생의 이름은 {student['name']}입니다.')
                        new_eng = input('수정할 영어점수를 입력하세요: ')
                        student['eng'] = new_eng  # 새로운 점수를 new_eng 변수에 저장
                        print(f'영어점수가 {new_eng}점으로 수정되었습니다.')
                        break
                else:
                    print('해당하는 반과 번호의 학생이 없습니다.')

            elif menu == '3':
                student_class = int(input('수학 점수를 수정할 학생의 반을 입력하세요: '))
                student_number = int(input('수학 점수를 수정할 학생의 번호를 입력하세요: '))
                for student in students:
                    if student['class'] == student_class and student['number'] == student_number:
                        print(f'수정할 학생의 이름은 {student['name']}입니다.')
                        new_math = input('수정할 수학점수를 입력하세요: ')
                        student['math'] = new_math # 새로운 점수를 new_math 변수에 저장
                        print(f'수학점수가 {new_math}점으로 수정되었습니다.')
                        break
                else:
                    print('해당하는 반과 번호의 학생이 없습니다.')

            elif menu == '4':
                print('처음 메뉴로 돌아갑니다.')
                break

    elif students_menu == '3':
        print('=============== 학생 삭제 ===============')


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