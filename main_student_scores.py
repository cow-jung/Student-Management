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
    #print('===========================================')

    students_menu = input('학생 성적 관리 메뉴를 선택하세요 : ')
    print()
    if students_menu == '0':
        print('=============== 학생 조회 ===============')
        for student in students:
            print(f"{student['class']}반 {student['number']}번 {student['name']}")
        print()
    elif students_menu == '1':
        while True:
            print('=============== 학생 등록 ===============')
            print('1. 학생 & 성적 등록')
            print('2. 뒤로 가기')

            menu = input('학생 등록 메뉴 선택: ')

            if menu == '1':
                student_class = int(input('등록할 학생의 반을 입력하세요(숫자만) : '))
                number = int(input('등록할 학생의 번호를 입력하세요(숫자만) : '))
                name = input('등록할 학생의 이름을 입력하세요 : ')

                found = False   # 중복된 학생을 찾았는지 표시하는 변수. 아직 확인 전이니까 일단 False(없음)로 시작

                for student in students:
                    # 현재 확인 중인 학생의 반(class)과 번호(number)가
                    # 방금 입력받은 student_class, number와 둘 다 같은지 확인
                    # -> 반이 같아도 번호가 다르면 통과(중복 아님), 번호가 같아도 반이 다르면 통과(중복 아님)
                    # -> 반과 번호가 "둘 다" 같을 때만 진짜 중복으로 판단
                    if student['class'] == student_class and student['number'] == number:
                        found = True # 중복인 학생을 찾았으니 found를 True로 바꿈
                        break  # 더 이상 찾아볼 필요 없으니 반복문을 즉시 빠져나감

                # 반복문이 끝난 뒤, found 값을 보고 등록을 진행할지 말지 결정
                if found == True:
                    # 중복인 학생이 있었던 경우 -> 등록하지 않고 안내 메시지만 출력
                    print('이미 등록된 반/번호입니다.')
                    print()
                else:
                    # 중복이 없었던 경우 -> 이제서야 점수를 입력받고 학생을 새로 등록
                    kor = int(input('국어점수 : '))
                    eng = int(input('영어점수 : '))
                    math = int(input('수학점수 : '))

                    # 딕셔너리 형태로 학생 한 명의 정보를 만들어서 students 리스트 맨 뒤에 추가
                    students.append({'class': student_class, 'number': number, 'name': name, 'kor': kor, 'eng': eng, 'math': math})
                    # 새 학생을 추가한 뒤 리스트 순서가 뒤죽박죽일 수 있으니 다시 정렬
                    # key=lambda x: (x['class'], x['number'])
                    # -> 먼저 반(class) 기준으로 정렬하고, 반이 같으면 번호(number) 기준으로 정렬
                    students.sort(key=lambda x: (x['class'], x['number'])) # 학생 한 명(x)마다 (반, 번호) 두 개짜리 튜플을 기준값으로 써서 정렬해라는 뜻
                    print('학생 정보가 등록되었습니다.')
                    print()
            elif menu == '2':
                print('처음 메뉴로 돌아갑니다.')
                print()
                break

            else:
                print('잘못 입력하셨습니다.')
                print()


    elif students_menu == '2':
        while True:
            print('=============== 학생 수정 ===============')
            print('1. 학생 국어점수 수정')
            print('2. 학생 영어점수 수정')
            print('3. 학생 수학점수 수정')
            print('4. 뒤로 가기')
            menu = input('학생 수정 메뉴 선택: ')

            if menu == '1':  # 국어점수 수정
                student_class = int(input('국어점수를 수정할 학생의 반을 입력하세요: '))

                # 1단계: 입력한 반에 어떤 학생들이 있는지 먼저 보여줌
                print(f'=============== {student_class}반 학생 목록 ===============')
                found_any = False  # 그 반에 학생이 한 명이라도 있는지 확인

                for student in students:
                    if student['class'] == student_class:
                        print(f"{student['number']}번 {student['name']}")
                        found_any = True

                if found_any == False:
                    # 반에 학생이 아예 없으면 번호/이름 입력받을 필요도 없이 바로 종료
                    print(f'{student_class}반에는 등록된 학생이 없습니다.')
                    print()

                else:
                    # 2단계: 목록을 보고 번호와 이름을 입력받아 정확히 한 명을 특정
                    student_number = int(input('국어점수를 수정할 학생의 번호를 입력하세요: '))
                    student_name = input('국어점수를 수정할 학생의 이름을 입력하세요: ')
                    found = False  # 번호+이름까지 일치하는 학생을 찾았는지 확인

                    for student in students:
                        if (student['class'] == student_class and
                                student['number'] == student_number and
                                student['name'] == student_name):
                            # 3단계: 수정 전에 현재 정보(반/번호/이름/국어점수)를 보여줌
                            print(f"반 : {student['class']}")
                            print(f"번호 : {student['number']}")
                            print(f"이름 : {student['name']}")
                            print(f"현재 국어점수 : {student['kor']}점")

                            # 4단계: 새 점수를 입력받아서 수정
                            new_kor = int(input('수정할 국어점수를 입력하세요: '))
                            student['kor'] = new_kor
                            print(f'국어점수가 {new_kor}점으로 수정되었습니다.')
                            print()
                            found = True
                            break

                    if found == False:
                        print('해당하는 번호/이름의 학생이 없습니다.')
                        print()


            elif menu == '2':  # 영어점수 수정 (국어와 완전히 같은 구조)
                student_class = int(input('영어점수를 수정할 학생의 반을 입력하세요: '))

                print(f'=============== {student_class}반 학생 목록 ===============')
                found_any = False

                for student in students:
                    if student['class'] == student_class:
                        print(f"{student['number']}번 {student['name']}")
                        found_any = True

                if found_any == False:
                    print(f'{student_class}반에는 등록된 학생이 없습니다.')
                    print()

                else:
                    student_number = int(input('영어점수를 수정할 학생의 번호를 입력하세요: '))
                    student_name = input('영어점수를 수정할 학생의 이름을 입력하세요: ')
                    found = False

                    for student in students:
                        if (student['class'] == student_class and
                                student['number'] == student_number and
                                student['name'] == student_name):
                            print(f"반 : {student['class']}")
                            print(f"번호 : {student['number']}")
                            print(f"이름 : {student['name']}")
                            print(f"현재 영어점수 : {student['eng']}점")
                            new_eng = int(input('수정할 영어점수를 입력하세요: '))
                            student['eng'] = new_eng

                            print(f'영어점수가 {new_eng}점으로 수정되었습니다.')
                            print()
                            found = True
                            break

                    if found == False:
                        print('해당하는 번호/이름의 학생이 없습니다.')
                        print()


            elif menu == '3':  # 수학점수 수정 (동일한 구조)
                student_class = int(input('수학점수를 수정할 학생의 반을 입력하세요: '))

                print(f'=============== {student_class}반 학생 목록 ===============')
                found_any = False

                for student in students:

                    if student['class'] == student_class:
                        print(f"{student['number']}번 {student['name']}")
                        found_any = True

                if found_any == False:
                    print(f'{student_class}반에는 등록된 학생이 없습니다.')
                    print()

                else:
                    student_number = int(input('수학점수를 수정할 학생의 번호를 입력하세요: '))
                    student_name = input('수학점수를 수정할 학생의 이름을 입력하세요: ')
                    found = False

                    for student in students:
                        if (student['class'] == student_class and
                                student['number'] == student_number and
                                student['name'] == student_name):
                            print(f"반 : {student['class']}")
                            print(f"번호 : {student['number']}")
                            print(f"이름 : {student['name']}")
                            print(f"현재 수학점수 : {student['math']}점")

                            new_math = int(input('수정할 수학점수를 입력하세요: '))
                            student['math'] = new_math
                            print(f'수학점수가 {new_math}점으로 수정되었습니다.')
                            print()
                            found = True
                            break

                    if found == False:
                        print('해당하는 번호/이름의 학생이 없습니다.')
                        print()

            elif menu == '4':
                print('처음 메뉴로 돌아갑니다.')
                print()
                break

            else:
                print('잘못 입력하셨습니다.')
                print()

    elif students_menu == '3':
        while True:
            print('=============== 학생 삭제 ===============')
            print('1. 학생 삭제')
            print('2. 뒤로 가기')
            delete_menu = input('학생 삭제 메뉴 선택: ')

            if delete_menu == '1':
                student_class = int(input('삭제할 학생의 반을 입력하세요(숫자만): '))
                print(f'=============== {student_class}반 학생 목록 ===============')
                found_any = False  # 해당 반에 학생이 한 명이라도 있는지 확인할 변수

                # 입력한 반에 속한 학생들을 미리 보여줘서, 사용자가 번호/이름을 정확히 알고 입력하게 도와줌
                for student in students:
                    if student['class'] == student_class:
                        print(f"{student['number']}번 {student['name']}")
                        found_any = True # 한 명이라도 출력되면 True로 표시

                if found_any == False:
                    # 반복문을 다 돌았는데 한 번도 True가 안 됐다 = 그 반에 학생이 아예 없다
                    print(f'{student_class}반에는 등록된 학생이 없습니다.')
                    print()

                else:
                    # 해당 반에 학생이 있으니, 삭제할 학생을 특정하기 위해 번호와 이름을 추가로 입력받음
                    student_number = int(input('삭제할 학생의 번호를 입력하세요(숫자만): '))
                    student_name = input('삭제할 학생의 이름을 입력하세요: ')

                    # 아직 삭제할 학생을 못 찾은 상태로 시작 (찾으면 여기에 저장할 예정)
                    delete_student = None

                    for student in students:
                        # 반, 번호, 이름이 전부 일치하는 학생인지 확인
                        if (student['class'] == student_class) and (student['number'] == student_number) and (
                                student['name'] == student_name):
                            delete_student = student # 조건에 맞는 학생을 찾았으니 변수에 저장
                            break # 찾았으니 더 돌 필요 없이 바로 반복문 종료

                    if delete_student == None:
                        # 반복문을 끝까지 돌았는데도 delete_student가 None이면 = 조건에 맞는 학생이 없었다
                        print('학생 정보를 찾을 수 없습니다.')
                        print()
                    else:
                        # 조건에 맞는 학생을 찾았으니 리스트에서 실제로 제거
                        students.remove(delete_student)
                        print('학생 정보가 삭제되었습니다.')
                        print()

            elif delete_menu == '2':
                print('처음 메뉴로 돌아갑니다.')
                print()
                break

            else:
                print('잘못 입력하셨습니다.')
                print()


    elif students_menu == '4':
        while True:
            print('=============== 성적 조회 ===============')
            print('1. 전체 학생 조회')
            print('2. 반별 성적 조회')
            print('3. 과목별 조회')
            print('4. 학생 개인 조회')
            print('5. 뒤로 가기')
            info_menu = input('성적 조회 메뉴 선택 : ')

            if info_menu == '1':
                print('=============== 전체 학생 조회 ===============')
                for student in students:
                    print(f"{student['class']}반 {student['number']}번 {student['name']} 국어점수: {student['kor']}점 영어점수: {student['eng']}점 수학점수: {student['math']}점")
                print()

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
                        print(f"국어점수 : {item['kor']}점")
                        print(f"영어점수 : {item['eng']}점")
                        print(f"수학점수 : {item['math']}점")

                        total = item['kor'] + item['eng'] + item['math']
                        avg = total / 3

                        print(f'개인 총점 : {total}점')  # 학생 개인 총점도 같이 보여주면 좋음
                        print(f'개인 평균 : {avg:.2f}점')
                        print('-' * 30)

                        # 반 전체 합계에 이 학생의 점수를 더해줌
                        class_kor_total += item['kor']
                        class_eng_total += item['eng']
                        class_math_total += item['math']
                        student_count += 1  # 학생 한 명 셌으니 카운트 +1
                        print()
                # 반복문이 다 끝난 뒤, 그 반에 학생이 있었는지 확인
                if student_count == 0:
                    print(f'{class_info}반에는 등록된 학생이 없습니다.')
                    print()

                else:
                    # 반 전체 총점 = 국어+영어+수학 합계를 다 더한 값
                    class_total = class_kor_total + class_eng_total + class_math_total

                    # 반 평균 = 반 전체 총점 / (학생 수 * 과목 수 3개)
                    class_avg = class_total / (student_count * 3)

                    print(f'=============== {class_info}반 전체 성적 ===============')
                    print(f'국어 총점 : {class_kor_total}점 / 평균 : {class_kor_total / student_count:.2f}점')
                    print(f'영어 총점 : {class_eng_total}점 / 평균 : {class_eng_total / student_count:.2f}점')
                    print(f'수학 총점 : {class_math_total}점 / 평균 : {class_math_total / student_count:.2f}점')
                    print(f'반 전체 총점 : {class_total}점')
                    print(f'반 전체 평균 : {class_avg:.2f}점')
                    print()
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
                    print()

                else:
                    print(f"국어 평균 : {kor_total / count:.2f}점")
                    print(f"영어 평균 : {eng_total / count:.2f}점")
                    print(f"수학 평균 : {math_total / count:.2f}점")
                    print()


            elif info_menu == '4':
                print('=============== 학생 개인 성적 조회 ===============')
                student_class = int(input('조회할 학생의 반을 입력하세요(숫자만) : '))

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
                    print()

                else:
                    # 해당 반에 학생이 있으니, 조회할 학생을 특정하기 위해 번호와 이름을 추가로 입력받음
                    student_number = int(input('조회할 학생의 번호를 입력하세요(숫자만) : '))
                    student_name = input('조회할 학생의 이름을 입력하세요 : ')
                    found = False  # 정확히 일치하는 학생을 찾았는지 확인 (기존 로직 그대로 유지)

                    for item in students:
                        if (item['class'] == student_class and
                                item['number'] == student_number and
                                item['name'] == student_name):

                            print(f"\n{item['class']}반 {item['number']}번 {item['name']}")

                            if 'kor' in item:
                                print(f"국어점수 : {item['kor']}점")
                                print(f"영어점수 : {item['eng']}점")
                                print(f"수학점수 : {item['math']}점")

                                total = item['kor'] + item['eng'] + item['math']
                                avg = total / 3

                                print(f"평균 : {avg:.2f}점")
                                print()
                                found = True

                            else:
                                print("성적이 등록되지 않았습니다.")
                                print()

                    if found == False:
                        print("학생의 정보를 찾을 수 없습니다.")
                        print()

            elif info_menu == '5':
                print('처음 메뉴로 돌아갑니다.')
                print()
                break

            else:
                print('잘못 입력하셨습니다.')
                print()

    elif students_menu == '5':
        print('종료합니다.')
        break

    else:
        print('잘못 입력하셨습니다.')
        print()

