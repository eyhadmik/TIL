# Git by Ashal
# 2019-08-07

#### Git 을 설명하는 두 가지 방법
1. 버전관리
2. 형상관리

버전관리 | 형상관리
----|----
시간여행 | 평행우주 multi-verse
일렬로 된 선의 한 점 | 서로 다른 세계에서 각기 다른 지점

#### 형상관리의 입장에서 설명 
- 여러 가지 브랜치의 각기 다른 작업이 가능

- 각각의 브랜치Branch 를 병합 Merge
    ##### : 브랜치Branch 를 만드는 목적

- Pull Request = Fetch + Merge

> "계속 최신으로 유지하기" 가 중요하다

# fetch 는 upstream 에서
# push 는 origin 으로

## upstream 만들기
> git add upstream git@github.com:dataitgirls3/TIL.git


>### [다 같이 쓰는 원격 저장소: upstream]
>### |               ↓ forked        ↑ Pull request 
>### | [나 혼자 쓰는 원격 저장소: origin]
>### | (clone 하면서 자동으로 origin 이라고 이름 생성된다)
>### ↓ fetch         ↓ clone         ↑ Push
>### [로컬 저장소:]

- 가져올 때는 upstream 에서 한 번에 가져온다 (fetch: data 가져온다)
- 올릴 때는 Push, Pull Request 두 단계를 거쳐서 올린다

각각의 저장소에 branch 가 따로 존재한다

## Routine
1. Branch 만든다
2. Commit
3. Upstream 에서 Fetch 받아오고 
    - 최신파일은 upstream 에 있다
4. 내 Branch 를 최신으로 맞춰준다 Rebase 
    - Rebase 는 가장 최신으로 하는 게 좋아서 마지막 작업으로 한다
5. Pull

- 이 모든 작업을 한 번에 해주는 코드
## fetch / rebase
>### git pull --rebase origin master 
### : 불필요한 것들은 Pull 안된다
### : Fetch - rebase - pull 까지 한번에 완료
### : git status 가 clean 한 상태에서 해야 함

## rebase 하는 이유
### : 깔끔하게 정리된다
### : 예전 log 찾기 쉬워짐

origin/master 는 별로 안 중요함. 내가 올리는 데이터가 잠시 거쳐가는 쓸개같은 곳..

Source Tree 에서 그래프 보면 좋음

- Branch 하나에서 여러 작업을 이어서 하면 리뷰하기 어려워진다
- 명확한 작업 하나를 Branch 하나에서 하는 것이 좋다

#### 하나의 브랜치에서 작업하다가 새로운 브랜치를 만들 때
> git checkout -b test upstream/master
Source Tree 에서는 그냥 Base 를 더블클릭 하면 됨
> git checkout -b test
: test 라는 브랜치를 새로 만들고, checkout 까지 한다
upstream/master 를 뒤에 추가하면
: upstream/master 를 Base 로 해서 새로운 Branch 만들어준다

나눠서 하려면 
git fetch (최신 버전 가져오기)
git chekckout -b (Branch 새로 만들고 Checkout)
git rebase (최신으로 Base 옮기기)
add/commit/push
pull request

> git remote -v 
#### : 원격 저장소 자세한 정보

> git branch 
#### : 로컬에 있는 Branch 만 보여준다

> git branch -a 
#### : Remote 에 있는 Branch 까지 보여준다

> git fetch upstream
> git fetch upstream master
#### : 최초에는 fetch 따로 해줘야 한다
##### : Branch 이름까지 추가해야 실행되던데...

file 지운 후 commit 하면 된다

- idea 폴더
: git 이 작업하는 내용 넣어서 만듦
: 지우는 게 좋다