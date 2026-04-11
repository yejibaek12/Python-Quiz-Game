# **프로젝트 개요**
Python과 Git을 활용하여 터미널 환경에서 동작하는 **나만의 퀴즈 게임**을 직접 설계하고 구현한다. 프로그램의 전체 실행 흐름을 만들고 데이터 영속성과 버전 관리를 경험하는데 목적을 둔다. 
- **Python 객체 지향 프로그래밍**: 최소 2개 이상의 클래스를 정의하여 역할을 분리하고,  코드를 역할별로 구조화
- **데이터 영속성 확보**: `state.json` 파일을 활용하여 프로그램 종료 후에도 퀴즈 데이터와 최고 점수를 유지
- **Git을 이용한 이력 관리**: 기능단위 커밋을 통해 개발 과정을 체계적으로 기록하며, 브랜치를 나누어 작업한 뒤 병합하는 워크플로우를 통해 실제 협업의 기초가 되는 버전 관리 프로세스를 경험

<br>

# 1. 실행 환경
- ![VS Code 실행 환경](./screenshot/version.png)

<br>

# 2. 수행 체크리스트
**1단계: 저장소 초기 설정**
- [X] GitHub에 새 저장소 만들기
- [X] 로컬 설정
- [X] 기본 파일 생성: .gitignore, README.md
- [X] 새 레파지토리와 연결

**2단계: 핵심 로직 구현 (클래스 및 기능 개발)**
- [X] Quiz 클래스 정의: 문제, 선택지, 정답 속성을 포함한 개별 퀴즈 객체 설계
- [X] 기본 데이터 생성: 직접 정한 주제로 5개 이상의 퀴즈 인스턴스 생성
- [X] QuizGame 클래스 정의: 게임의 핵심 기능(풀기, 추가, 목록, 점수, 종료)을 메서드로 분리

**3단계: 예외 처리 및 프로그램 안정성 확보**
- [X] 입력 예외 처리: 숫자 변환 실패(ValueError), 범위 밖 숫자 입력 등에 대한 방어 코드
- [X] 비정상 종료 대응: 빈 입력 처리 및 Ctrl+C(KeyboardInterrupt) 발생 시 안전한 종료 로직
- [X] 파일 손상 대비: state.json 파일이 없거나 손상되었을 때 기본 데이터로 복구하는 기능

**4단계: 데이터 영속성**
- [X] JSON 입출력: state.json 파일 저장 및 불러오기 구현
- [X] 인코딩 설정: UTF-8 권장

**5단계: 브랜치 생성 및 병합**
- [X] 브랜치 생성 및 전환 (checkout -b dev-yeji)
- [X] 기능별 커밋 최소 10개 이상
- [X] main 브랜치로 합치기 (merge)

**6단계: Git 저장소 복제**
- [X] Git 복제: 다른 폴더에 clone 받고 수정 후 push 실습
- [X] Git pull: 기존 폴더에서 변경사항 가져오기

<br>

# 3. 저장소 초기 설정
## (1) 폴더 및 파일 생성
```bash
$ mkdir Python-Quiz-Game
$ cd Python-Quiz-Game
$ touch .gitignore README.md
```
## (2) 로컬 설정
```bash 
$ git init
```

## (3) 새 저장소 연결 및 확인 
```bash
$ git remote add origin https://github.com/yejibaek12/Python-Quiz-Game.git

$ git remote -v
origin  https://github.com/yejibaek12/Python-Quiz-Game.git (fetch)
origin  https://github.com/yejibaek12/Python-Quiz-Game.git (push)
```
## (4) 커밋 생성
```bash
$ git add .
$ git commit -m "Init: 저장소 초기화 및 기본 파일 생성"
$ git push origin master
```

