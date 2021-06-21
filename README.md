# pet-album  

멋쟁이사자처럼 9기 미니 아이디어톤 : 반려동물 앨범 서비스

## 조원

```
김소연: 
박수현:
이현지:
정세진:
```

### 처음 작업 시

혹은 작업 도중 도저히 살릴 수 없어서(...) 다시 받아오는 경우

1. git 원격 레포지토리 clone 받기
   - `git clone https://github.com/likelion-kookmin/pet-album.git`
2. 가상환경 생성 및 실행
   - 생성
     - Windows: `python -m venv venv`
     - Mac: `python3 -m venv venv`
   - 실행
     - Windows: `source venv/Scripts/activate`
     - Mac: `source venv/bin/activate`
3. `pip install -r requirements.txt`


### 작업 전 체크사항

1. 가상환경 실행 했나요?
2. 개인 브랜치로 전환 했나요?

각자 개인 브랜치에서 작업해봅시다!

1. 작업할 브랜치 생성하기
   - 개인 브랜치가 없어서 최초로 생성하거나 새 기능을 구현할 때
   - (특별한 이유가 없다면) main 브랜치 가장 최근 상태에서 브랜치를 따보아요.
   - `git branch [브랜치명]`
      - 브랜치명은 다음과 같이: `자신의이름-구현할기능`
        - ex) spongebob-user
2. 작업할 브랜치로 전환하기
   - `git checkout [브랜치명]`
     - ex) `git checkout spongebob-user`



### git 기본 명령어

1. git 원격 레포지토리의 변경 사항을 로컬 레포지토리에 받아오기
   - `git pull origin main` 혹은 `git pull`
2. git 로컬 레포지토리에 변경 사항을 **staging** 상태로 만들기
   - `git add [스테이징할 파일, 혹은 디렉토리]`
   - 작업하는 최상위 디렉토리에서 `git add .`로 자주 사용합니다.
3. git 로컬 레포지토리에 **commit** 하기
   - `git commit -m "커밋 메시지"`
4. git 원격 레포지토리에 **push** 하기
   - `git push origin [자신이 작업하는 브랜치]`
   - main 브랜치에 바로 푸시하지 않도록 주의!!
