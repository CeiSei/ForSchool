수능 영어 학습기
===========

본 프로그램은 수능 위주의 영어 학습을 돕기 위해 만들어진 프로그램입니다.
총 세 가지 모드를 통해 문장 혹은 문단의 어휘적 분석에 도움을 받을 수 있습니다.

## 모드 1.

모드 1은 하나의 단어 혹은 문장을 해석하는 모드입니다.

### 사용방법

1. 모드 선택 메뉴에서 1을 입력합니다.
2. 해석하고자 하는 단어 혹은 문장을 입력하고 엔터키를 입력합니다. 이 단계에서 모드를 종료하려면 -1을 입력합니다.
3. 해석결과를 확인하고, 다른 단어 혹은 문장을 해석하려면 Y를 입력합니다.
4. 단어 혹은 문장 해석을 마치고 메뉴로 돌아가려면 N을 입력합니다.


## 모드 2.

모드 2는 하나의 문단을 해석하는 모드입니다. 문단을 문장으로 분해하여 각 문장의 해석을 제공합니다. 또한, 각 문장을 다시 분해하여
단어의 의미를 해석할 수도 있습니다.

### 사용방법

1. 모드 선택 메뉴에서 2를 입력합니다.
2. 해석하고자 하는 문단을 입력하고 엔터키를 입력합니다. 이 단계에서 모드를 종료하려면 -1을 입력합니다.
3. 해석결과를 확인하고, 문장을 분해하여 단어를 해석하려면 Y를 입력합니다.
  3-1. 해석할 문장의 번호를 입력합니다.
  3-2. 다른 문장을 분해하여 해석하려면 Y를 입력하고 3-1로 돌아갑니다.
4. 다른 문단을 해석하려면 Y를 입력합니다.
5. 문단 해석을 마치고 메뉴로 돌아가려면 N을 입력합니다.


## 모드 3.

모드 3은 하나의 문단이 담긴 텍스트 파일을 해석하는 모드입니다. main.py와 같은 디렉토리에 해석할 텍스트 파일을 위치시키고
파일명을 입력하면 파일 내용에 대한 해석을 제공합니다. 모드 2에서와 같이 문단을 이루고 있는 각 문장마다의 해석을 제공하고,
문장을 이루고 있는 각 단어마다의 해석을 제공합니다.

### 사용방법

1. 모드 선택 메뉴에서 3을 입력합니다.
2. 해석하고자 하는 텍스트 파일을 main.py와 같은 디렉토리에 위치시킵니다.
3. 텍스트 파일의 이름을 확장자까지 정확하게 입력합니다. 이 단계에서 모드를 종료하려면 -1을 입력합니다.
4. 해석결과를 확인하고, 문장을 분해하여 단어를 해석하려면 Y를 입력합니다.
  4-1. 해석할 문장의 번호를 입력합니다.
  4-2. 해석한 내용을 해석파일에 저장할지 선택합니다.
  4-3. 다른 문장을 분해하여 해석하려면 Y를 입력하고 4-1로 돌아갑니다.
5. 문단 해석을 마치면 '파일명_translated.txt' 파일이 main.py가 위치한 디렉토리에 저장되고 프로그램은 자동으로 메뉴로 돌아갑니다.


## 참고자료.

1. Google Translation API (googletrans downloaded by pip. -> python -m pip install -U googletrans==4.0.0-rc1)

## 라이센스.

Apache 라이센스 버전 2.0(이하 "라이센스")에 따라 라이센스가 부여되며 라이센스를 준수하지 않는 한 이 파일을 사용할 수 없습니다.

http://www.apache.org/licenses/LICENSE-2.0