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
    print('0. 학생 조회')
    print('1. 학생 등록')
    print('2. 학생 수정')
    print('3. 학생 삭제')
    print('4. 성적 조회')
    print('5. 종료')
    students_menu = input('학생 성적 관리 메뉴를 선택하세요 : ')

    if students_menu == '0':
        print('=============== 학생 조회 ===============')

    elif students_menu == '1':
        print('=============== 학생 등록 ===============')

    elif students_menu == '2':
        print('=============== 학생 수정 ===============')

    elif students_menu == '3':
        print('=============== 학생 삭제 ===============')


    elif students_menu == '4':
        print('=============== 성적 조회 ===============')
        print('1. 전체 학생 조회')
        print('2. 반별 성적 조회')
        print('3. 과목별 조회')
        print('4. 학생 개인 조회')
        info_menu = input('성적 조회 메뉴를 선택하세요 : ')

        if info_menu == '1':
            print('=============== 전체 학생 조회 ===============')
            for student in students:
                print(f"{student['class']}반 {student['number']}번 {student['name']} 국어: {student['kor']} 영어: {student['eng']}, 수학: {student['math']}")


        elif info_menu == '2':

            print('=============== 반별 성적 조회 ===============')
            class_info = int(input('조회할 반을 입력하세요 : '))

            # 반 전체 합계를 누적할 변수들 (반복문 시작 전에 0으로 초기화)
            class_kor_total = 0
            class_eng_total = 0
            class_math_total = 0
            student_count = 0  # 해당 반 학생이 몇 명인지 세는 변수

            for item in students:
                if item['class'] == class_info:
                    print(f'번호 : {item["number"]}')
                    print(f"이름 : {item['name']}")
                    print(f"국어 성적 : {item['kor']}")
                    print(f"영어 성적 : {item['eng']}")
                    print(f"수학 성적 : {item['math']}")

                    total = item['kor'] + item['eng'] + item['math']
                    avg = total / 3

                    print(f'개인 총점 : {total}')  # 학생 개인 총점도 같이 보여주면 좋음
                    print(f'개인 평균 : {avg:.2f}')
                    print('-' * 30)

                    # 반 전체 합계에 이 학생의 점수를 더해줌
                    class_kor_total += item['kor']
                    class_eng_total += item['eng']
                    class_math_total += item['math']
                    student_count += 1  # 학생 한 명 셌으니 카운트 +1

            # 반복문이 다 끝난 뒤, 그 반에 학생이 있었는지 확인
            if student_count == 0:
                print(f'{class_info}반에는 등록된 학생이 없습니다.')

            else:
                # 반 전체 총점 = 국어+영어+수학 합계를 다 더한 값
                class_total = class_kor_total + class_eng_total + class_math_total

                # 반 평균 = 반 전체 총점 / (학생 수 * 과목 수 3개)
                class_avg = class_total / (student_count * 3)

                print(f'=============== {class_info}반 전체 성적 ===============')
                print(f'국어 총점 : {class_kor_total} / 평균 : {class_kor_total / student_count:.2f}')
                print(f'영어 총점 : {class_eng_total} / 평균 : {class_eng_total / student_count:.2f}')
                print(f'수학 총점 : {class_math_total} / 평균 : {class_math_total / student_count:.2f}')
                print(f'반 전체 총점 : {class_total}')
                print(f'반 전체 평균 : {class_avg:.2f}')

        elif info_menu == '3':
            print("=============== 과목별 평균 조회 ===============")

            kor_total = 0
            eng_total = 0
            math_total = 0
            count = 0

            for item in students:

                if 'kor' in item:
                    kor_total += item['kor']
                    eng_total += item['eng']
                    math_total += item['math']
                    count += 1

            if count == 0:
                print("등록된 성적이 없습니다.")

            else:
                print(f"국어 평균 : {kor_total / count:.2f}")
                print(f"영어 평균 : {eng_total / count:.2f}")
                print(f"수학 평균 : {math_total / count:.2f}")



        elif info_menu == '4':
            print('=============== 학생 개인 성적 조회 ===============')
            student_class = int(input('조회할 반을 입력하세요(숫자만) : '))

            # 입력한 반에 어떤 학생들이 있는지 미리 보여줘서, 번호/이름을 정확히 알고 입력하게 도와줌
            print(f'=============== {student_class}반 학생 목록 ===============')
            found_any = False  # 해당 반에 학생이 한 명이라도 있는지 확인할 변수
            for student in students:
                if student['class'] == student_class:
                    print(f"{student['number']}번 {student['name']}")
                    found_any = True  # 한 명이라도 출력되면 True로 표시

            if found_any == False:
                # 반복문을 다 돌았는데 한 번도 True가 안 됐다 = 그 반에 학생이 아예 없다
                print(f'{student_class}반에는 등록된 학생이 없습니다.')

            else:
                # 해당 반에 학생이 있으니, 조회할 학생을 특정하기 위해 번호와 이름을 추가로 입력받음
                student_number = int(input('조회할 번호를 입력하세요(숫자만) : '))
                student_name = input('조회할 이름을 입력하세요 : ')
                found = False  # 정확히 일치하는 학생을 찾았는지 확인 (기존 로직 그대로 유지)

                for item in students:

                    if (item['class'] == student_class and
                            item['number'] == student_number and
                            item['name'] == student_name):

                        print(f"\n{item['class']}반 {item['number']}번 {item['name']}")

                        if 'kor' in item:

                            print(f"국어 : {item['kor']}")
                            print(f"영어 : {item['eng']}")
                            print(f"수학 : {item['math']}")

                            total = item['kor'] + item['eng'] + item['math']
                            avg = total / 3

                            print(f"평균 : {avg:.2f}")

                            found = True

                        else:

                            print("성적이 등록되지 않았습니다.")

                if found == False:
                    print("학생 정보를 찾을 수 없습니다.")

        else:
            print('잘못 입력하셨습니다.')

    elif students_menu == '5':
        print('종료합니다.')
        break

    else:
        print('잘못 입력하셨습니다.')


