"Trailblazer"의 어원은 "trail"과 "blaze" 두 단어로 이루어져 있습니다. "Trail"은 우리가 알다시피 '길, 탐험로'를 의미하며, "blaze"는 원래 '불, 불길'을 의미하지만, 관련어로는 나무에 표시를 남기는 행위도 의미합니다. 예전에는 탐험가나 숲속의 길을 찾는 사람들이 나무에 흰 도장을 찍어 길을 표시했는데, 이러한 표시 자체를 "blaze"라고 불렀습니다. 따라서 "trailblazer"는 새로운 길을 열며, 그 길에 표시를 남겨 다른 사람들이 쉽게 따라올 수 있도록 하는 사람을 의미합니다.

"Trailblazer"는 긍정적인 의미로 널리 사용되며, 혁신가, 선구자, 또는 새로운 길을 밝혀주는 지도자를 가리키는 말입니다. 차별적이거나 모욕적인 의미는 없으며, 주로 존경과 동경의 대상으로 여겨지는 인물이나 그룹을 설명할 때 쓰입니다. 따라서 프로젝트 이름으로 사용하기에도 적합하며, 새로운 것을 창출하고, 혁신을 추구하는 프로젝트라는 이미지를 전달할 수 있습니다.

요약하자면, "trailblazer"는 긍정적인 의미를 가지고 있으며, 프로젝트 이름으로 사용하기에 부적절한 점은 없습니다.

알고리즘 기말 과제 프로젝트 (일명 "길"잡이 : Trailblazer)

<Github 사용법> - Curated and Refined ChatGPT 4.5 

0. 디렉토리 탐색

0-1. 윈도우 cd <경로> : 원하는 디렉토리로 이동합니다. dir : 현재 디렉토리의 파일 및 폴더 목록을 확인합니다.

0-2. 리눅스/맥 cd <경로> : 원하는 디렉토리로 이동합니다. pwd : 현재 디렉토리의 경로를 확인합니다. ls -al : 현재 디렉토리의 파일 및 폴더 목록을 자세히 확인합니다. tree : 디렉토리 구조를 트리 형태로 확인합니다. (별도 설치 필요)

1. Git 사용자 정보 설정

1-1. 사용자 정보 추가 git config --global user.name "<사용자 이름>" git config --global user.email "<사용자 이메일>"

1-2. 사용자 정보 삭제 git config --global --unset user.name "<사용자 이름>"
1-2. 사용자 정보 삭제 git config --global --unset-all user.name 
1-2. 사용자 정보 삭제 git config --global --unset user.email "<사용자 이메일>"
1-2. 사용자 정보 삭제 git config --global --unset-all user.email

1-3. 사용자 정보 확인 git config --global --list

2. 원격 저장소(remote) 설정

2-1. 원격 저장소 추가 git remote add origin <원격 저장소 주소>

2-2. 원격 저장소 확인 git remote -v

3. Git Bash 실행

3-1. 윈도우 탐색기에서 원하는 폴더를 우클릭 후 "Git Bash Here" 선택

3-2. 리눅스/맥 터미널을 실행한 후 원하는 디렉토리로 이동

4. Git 저장소 초기화

4-1. 새 저장소 초기화 git init

4-2. 기존 저장소 복제 git clone <원격 저장소 주소>

5. 파일 스테이징(Staging)

5-1. git add . : 현재 디렉토리의 모든 변경 사항을 스테이징합니다. 
5-2. git add -A : 현재 및 하위 디렉토리의 모든 변경 사항을 스테이징합니다. 
5-3. git add <파일명> : 특정 파일의 변경 사항만 스테이징합니다.

※ 이 단계에서는 변경 사항이 아직 커밋되지 않습니다.

6. 브랜치(Branch) 이해하기

브랜치는 작업 흐름을 분리하여 협업과 변경사항 관리를 돕는 기능입니다.

6-1. 브랜치 목록 보기 git branch : 로컬 브랜치 목록 확인 
6-2. git branch -a : 모든 로컬 및 원격 브랜치 목록 확인

6-3. 브랜치 이동 및 생성 git checkout <브랜치명> : 특정 브랜치로 이동 git checkout -b <새 브랜치명> : 새 브랜치를 생성하고 이동

6-4. 원격 브랜치 최신 상태 동기화 git fetch --all

6-5. 브랜치 삭제 git branch -d <브랜치명> : 로컬 브랜치를 삭제 
6-6. git push origin --delete <브랜치명> : 원격 브랜치를 삭제

* commit과 push의 차이

commit : 로컬 컴퓨터에만 변경 사항을 저장합니다. push : 로컬 컴퓨터에 commit된 내용을 원격 저장소(GitHub)에 올려 협업자들과 공유합니다.

※ commit 후 반드시 push를 해야 협업자에게 공유됩니다.

7. 변경 사항 커밋(commit)
커밋은 변경 사항을 버전 단위로 저장하는 작업입니다.

7-1. git commit -m "<커밋 메시지>" : 스테이징된 변경 사항을 커밋합니다. 
7-2. git commit --amend : 직전의 커밋 메시지나 내용을 수정합니다.

※ push 전까지는 로컬에만 저장됩니다.

8. 커밋 해시 확인 및 되돌리기

8-1. 커밋 해시 확인 git log : 최근 커밋 내역과 해시값을 확인합니다.

8-2. 커밋 되돌리기 git reset --hard <커밋 해시> : 특정 커밋으로 완전히 돌아갑니다. (변경 사항 삭제됨) git reset --soft <커밋 해시> : 특정 커밋으로 돌아가지만 이후 변경 사항을 유지합니다.

8-3. 변경 사항 임시 저장(stash) git stash : 변경 사항을 임시로 저장합니다. git stash pop : 임시 저장된 내용을 다시 불러옵니다.

9. 변경 사항 원격 저장소와 동기화(push/pull)

9-1. pull (가져오기) git pull origin <브랜치명> : 원격 저장소의 최신 내용을 로컬로 받아옵니다.

9-2. push (올리기) git push origin <브랜치명> : 로컬의 변경 사항을 원격 저장소로 올립니다.

※ push하기 전에 반드시 pull을 실행하여 충돌을 예방합니다.

10. Pull Request(PR) 생성 및 관리

Pull Request(PR)는 변경 사항을 팀원들과 리뷰하고 최종적으로 원격 저장소에 병합(merge) 요청을 하는 기능입니다.

10-1. GitHub 웹에서 PR 생성 ① GitHub에서 "Pull requests" 탭 선택 ② "New pull request" 버튼 클릭 ③ base 브랜치(일반적으로 main)와 내 브랜치 선택 ④ 변경 사항 확인 후 "Create pull request" 클릭 ⑤ 제목과 설명 입력 후 최종 제출

10-2. CLI에서 PR 생성 (GitHub CLI 설치 필요) gh pr create --base <기준 브랜치> --head <내 브랜치> --title "<제목>" --body "<설명>"

※ PR 제출 후 팀원들이 코드 리뷰를 통해 승인 또는 수정을 요청할 수 있습니다.
