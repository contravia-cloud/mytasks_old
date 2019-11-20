myproject
    - mytasks
        - mytask1
        - ...
    - env

1. 설정 초기화
    전역 사용자명/이메일 구성하기
    git config --global user.name "이름"
    git config --global user.email "깃허브 메일주소" // 매번 물어보는 귀찮음을 피하기 위해 설정.
    저장소별 사용자명/이메일 구성하기 (해당 저장소 디렉터리로 이동후)
    git config user.name “Your name”
    git config user.email “Your email address”

    전역 설정 정보 조회
    git config - -global - -list

2. 현재 폴더 깃 관리 폴더로 설정
    git init            // 현재 폴더를 깃 명령어를 사용할 수 있는 디렉토리로 만든다.

3. 원격 저장소 위치 확인
    git remote -v : 원격 저장소가 있는 곳 확인 (fetch 와 push 장소 표시해줌)
    git remote add origin https://github.com/contravia-cloud/mytasks.git // 로컬과 원격 저장소를 연결한다.

4. 변경사항 검토
    git status          // 현재 상태를 훑어보고

5. upload
    git add 화일명.확장자  // 깃 주목 리스트에 화일을 추가하고 or
    git add .           // 이 명령은 현재 디렉토리의 모든 화일을 추가할 수 있다.

    git commit -m “현재형으로 설명” // 커밋해서 스냅샷을 찍는다.

    git push -u origin master  // 깃허브로 푸시한다.

참조 : https://nolboo.kim/blog/2013/10/06/github-for-beginner/
==============================================================
git clone https://github.com/contravia-cloud/Academy.ALZZA.git
git clone https://github.com/contravia-cloud/mytasks.git

이미 다운 받았고, 최신 내용을 git 서버에서 받아와야 한다면,
git pull과 git fetch로 받을수 있습니다.
git pull // 코드를 받아와 변경점을 merge한다.
git fetch // 코드를 받아온다.
