import re
import os.path
import googletrans
translator = googletrans.Translator()

def menu_selector():
    while True:
        print("모드를 선택해주세요.", end = '\n\n')
        print("1 : 단어, 문장 번역 모드.")
        print("2 : 글 번역 및 분석 모드.")
        print("3 : 글 파일 번역 및 분석 모드.")
        print("-1 : 프로그램 종료.")
        print(">> ", end = '')
        
        mode = input()

        if mode == '1':
            mode = int(mode)
            break
        elif mode == '2':
            mode = int(mode)
            break
        elif mode == '3':
            mode = int(mode)
            break
        elif mode == '-1':
            mode = int(mode)
            break
        else:
            print('')
            print("잘못된 입력입니다.")
            print('==================================')
        
    return mode

def split_string(string):
    marks = []
    for idx in range(0, len(string)):
        if string[idx] == '.':
            marks.append('.')
        if string[idx] == '!':
            marks.append('!')
        if string[idx] == '?':
            marks.append('?')

    string = string.replace('!', '.')
    string = string.replace('?', '.')

    string = string.split('. ')
    for idx in range(0, len(string) - 1):
        string[idx] = string[idx] + marks[idx]
    if string[len(string) - 1][-1] == '.':
        string[len(string) - 1] = string[len(string) - 1][:-1] + marks[len(string) - 1]
    return string

def mode_1():
    while True:
        print("문장을 입력하세요. (모드 종료 : -1 입력.)")
        print(">> ", end = '')
        string = input()
        if string == '-1':
            print('==================================')
            return -1
        print('')
        print("변역 결과 : " + translator.translate(string, dest = 'ko').text)
        print('==================================')
        print("다른 문장을 번역 할까요? (Y / N)")

        def ask_repeat():
            while True:
                print(">> ", end = '')
                repeat = input()
                if repeat == 'Y' or repeat == 'y':
                    print('==================================')
                    return 1
                elif repeat == 'N' or repeat == 'n':
                    print("단어, 문장 번역 모드를 종료합니다.")
                    print('==================================')
                    return -1
                else:
                    print("잘못된 입력입니다.")
                    print("다른 문장을 번역 할까요? (Y / N)")
        repeat = ask_repeat()
        if repeat == 1:
            continue
        elif repeat == -1:
            break

def mode_2():
    while True:
        print("글을 입력하세요. (모드 종료 : -1 입력.)")
        print(">> ", end = '')
        string = input()
        if string == '-1':
            print('==================================')
            return -1
        splitstring = split_string(string)
        print('==================================')
        for idx in range(0, len(splitstring)):
            print(idx + 1, end = '')
            print(' : ', end = '')
            print(splitstring[idx])
            print(translator.translate(splitstring[idx], dest = 'ko').text, end = '\n\n')

        print('==================================')
        print("문장 세부 번역을 실행할까요? (Y / N)")
        def ask_analyze():
            while True:
                print(">> ", end = '')
                repeat = input()
                if repeat == 'Y' or repeat == 'y':
                    print('==================================')
                    return 1
                elif repeat == 'N' or repeat == 'n':
                    print('==================================')
                    return -1
                else:
                    print("잘못된 입력입니다.")
                    print("문장 세부 번역을 실행할까요? (Y / N)")
        analyze = ask_analyze()
        if analyze == 1:
            def analyze_string(string):
                while True:
                    
                    print("번역할 문장번호를 입력하세요.")
                    print(">> ", end = '')
                    str_num = input()
                    if str_num.isdigit() == False:
                        print("잘못된 입력입니다.")
                        continue
                    str_num = int(str_num)
                    if str_num > len(string):
                        print("잘못된 입력입니다.")
                        continue
                    print('==================================')
                    print(str(str_num) + " : " + string[str_num - 1])
                    print(translator.translate(string[str_num - 1], dest = 'ko').text)
                    print('')
                    splitsentence = []
                    splitsentence = string[str_num - 1]
                    if splitsentence[-1] == '.' or '!' or '\\?':
                        splitsentence = splitsentence[:-1]
                    splitsentence = splitsentence.split()
                    
                    for idx in range(0, len(splitsentence)):
                        print(splitsentence[idx] + " : " + translator.translate(splitsentence[idx], dest = 'ko').text)
                    print('==================================')

                    print("다른 문장을 분석할까요? (Y / N)")

                    def ask_repeat():
                        while True:
                            print(">> ", end = '')
                            repeat = input()
                            if repeat == 'Y' or repeat == 'y':
                                return 1
                            elif repeat == 'N' or repeat == 'n':
                                print("문장 분석모드를 종료합니다.")
                                print('==================================')
                                return -1
                            else:
                                print("잘못된 입력입니다.")
                                print("다른 문장을 분석할까요? (Y / N)")
                    repeat = ask_repeat()
                    if repeat == 1:
                        print('==================================')
                        continue
                    elif repeat == -1:
                        break
            analyze_string(splitstring)
            
        print("다른 글을 번역 할까요? (Y / N)")

        def ask_repeat():
            while True:
                print(">> ", end = '')
                repeat = input()
                print('==================================')
                if repeat == 'Y' or repeat == 'y':
                    return 1
                elif repeat == 'N' or repeat == 'n':
                    print("글 번역 및 분석모드를 종료합니다.")
                    print('==================================')
                    return -1
                else:
                    print("잘못된 입력입니다.")
                    print("다른 글을 번역 할까요? (Y / N)")
        repeat = ask_repeat()
        if repeat == 1:
            continue
        elif repeat == -1:
            break

def mode_3():
    print("main.py 파일과 같은 디렉토리에 번역할 txt 파일을 위치해주세요.")
    while True:
        print("txt파일의 이름을 확장자까지 적어주세요. (모드 종료 : -1 입력.)")
        print(">> ", end = '')
        filename = input()
        if filename == '-1':
            print('==================================')
            return -1
        if os.path.isfile(filename) == False:
            print("파일을 찾을 수 없습니다.")
            print("파일명을 다시 입력해주세요.")
        else:
            break

    print('==================================')
    readfile = open(filename, 'r')
        
    string = []
    string = readfile.read()
    splitstring = split_string(string)
    for idx in range(0, len(splitstring)):
        print(idx + 1, end = '')
        print(' : ', end = '')
        print(splitstring[idx])
        print(translator.translate(splitstring[idx], dest = 'ko').text, end = '\n\n')
    readfile.close()
    print('==================================')
    filename = filename.replace('.txt', '')
    writefile = open(filename+ '_translated' +'.txt', 'w')
    for idx in range(0, len(splitstring)):
        writefile.write(splitstring[idx] + '\n')
        writefile.write(translator.translate(splitstring[idx], dest = 'ko').text +'\n\n')
    
    print("문장 세부 번역을 실행할까요? (Y / N)")
    def ask_analyze():
        while True:
            print(">> ", end = '')
            repeat = input()
            if repeat == 'Y' or repeat == 'y':
                print('==================================')
                return 1
            elif repeat == 'N' or repeat == 'n':
                print('==================================')
                return -1
            else:
                print("잘못된 입력입니다.")
                print("문장 세부 번역을 실행할까요? (Y / N)")  
    analyze = ask_analyze()
    if analyze == 1:
        def analyze_string(string):
            while True:
                print("번역할 문장번호를 입력하세요.")
                print(">> ", end = '')
                str_num = input()
                if str_num.isdigit() == False:
                    print("잘못된 입력입니다.")
                    continue
                str_num = int(str_num)
                if str_num > len(string):
                    print("잘못된 입력입니다.")
                    continue
                print('==================================')
                print(str(str_num) + " : " + string[str_num - 1])
                print(translator.translate(string[str_num - 1], dest = 'ko').text)
                print('')
                splitsentence = []
                splitsentence = string[str_num - 1]
                if splitsentence[-1] == '.' or '!' or '\\?':
                    splitsentence = splitsentence[:-1]
                splitsentence = splitsentence.split()
                    
                for idx in range(0, len(splitsentence)):
                    print(splitsentence[idx] + " : " + translator.translate(splitsentence[idx], dest = 'ko').text)
                print('==================================')

                print("이 내용을 저장할까요? (Y / N)")

                while True:
                    print(">> ", end = '')
                    save = input()
                    if save == 'Y' or save == 'y':
                        writefile.write('==================================\n\n')
                        writefile.write(str(str_num) + " : " + string[str_num - 1] + '\n')
                        writefile.write(translator.translate(string[str_num - 1], dest = 'ko').text + '\n\n')
                        for idx in range(0, len(splitsentence)):
                            writefile.write(splitsentence[idx] + " : " + translator.translate(splitsentence[idx], dest = 'ko').text + '\n')
                        writefile.write('\n==================================\n\n')
                        break
                    elif save == 'N' or save == 'n':
                        break
                    else:
                        print("잘못된 입력입니다.")
                        print("이 내용을 저장할까요? (Y / N)")

                print('')    
                print("다른 문장을 분석할까요? (Y / N)")

                def ask_repeat():
                    while True:
                        print(">> ", end = '')
                        repeat = input()
                        if repeat == 'Y' or repeat == 'y':
                            return 1
                        elif repeat == 'N' or repeat == 'n':
                            print('')
                            print("문장 분석모드를 종료합니다.")
                            return -1
                        else:
                            print("잘못된 입력입니다.")
                            print("다른 문장을 분석할까요? (Y / N)")
                repeat = ask_repeat()
                if repeat == 1:
                    continue
                elif repeat == -1:
                    break
        analyze_string(splitstring)
    writefile.close()
    print('')
    print("글 파일 번역 및 분석 모드를 종료합니다.")
    print('==================================')
    
while True:      
    menu_select = menu_selector()
    if menu_select == 1:
        print("단어, 문장 번역 모드를 실행합니다.", end = '\n\n')
        mode_1()
        
    elif menu_select == 2:
        print("글 번역 및 분석모드를 실행합니다.", end = '\n\n')
        mode_2()

    elif menu_select == 3:
        print("글 파일 번역 및 분석 모드를 실행합니다.", end = '\n\n')
        mode_3()

    elif menu_select == -1:
        print('==================================')
        print("프로그램을 종료합니다.")
        break

    print('')
