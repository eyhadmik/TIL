# PYTHON3-14 

### 프로그래머스 문제풀이

- “완주하지 못한 선수” 문제

[https://programmers.co.kr/learn/courses/30/lessons/42576](https://programmers.co.kr/learn/courses/30/lessons/42576)

    테스트 코드 작성
    
    def test_solution():
        assert solution(
            ['leo', 'kiki', 'eden'],
            ['eden', 'kiki']
        ) == 'leo'
        assert solution(
            ['marina', 'josipa', 'nikola', 'vinko', 'filipa'],
            ['josipa', 'filipa', 'marina', 'nikola']
        ) == 'vinko'
        assert solution(
            ['mislav', 'stanko', 'mislav', 'ana'],
            ['stanko', 'ana', 'mislav']
        ) == 'mislav'
    
    기본 풀이
    
    def solution(participant, completion):
        # 사람 이름 Group By!
        runners = {}
        for runner in participant:
            runners[runner] = runners.get(runner, 0) + 1
        # 완주한 사람을 빼기
        for runner in completion:
            runners[runner] -= 1
        # 남아있는 사람 찾기
        for runner, count in runners.items():
            if count > 0:
                return runner
        # 혹시라도 못 찾으면 완주 못한 사람 없음
        return ''
    
    
    Counter
    
    https://docs.python.org/3/library/collections.html#collections.Counter
    
    Counter 사용 1단계
    
    from collections import Counter
    
    def solution(participant, completion):
        # 갯수를 모으는 부분을 최적화
        runners = Counter(participant)
        for runner in completion:
            runners[runner] -= 1
        for runner, count in runners.items():
            if count > 0:
                return runner
        return ''
    
    Counter 사용 2단계
    
    from collections import Counter
    
    def solution(participant, completion):
        # 갯수를 모으는 부분을 최적화
        runners = Counter(participant)
        # 갯수를 빼는 부분을 최적화
        runners -= Counter(completion)
        for runner, count in runners.items():
            if count > 0:
                return runner
        return ''
    
    Counter 사용 3단계
    
    from collections import Counter
    
    def solution(participant, completion):
        # 갯수를 모으는 부분을 최적화
        runners = Counter(participant)
        # 갯수를 빼는 부분을 최적화
        runners -= Counter(completion)
        # 남은 사람 얻는 부분을 최적화
        return next(runners.elements())
    
    최종 코드
    
    from collections import Counter
    
    def solution(participant, completion):
        return next((Counter(participant) - Counter(completion)).elements())
    
    # ⇒ 굳이 이렇게 안 해도 됩니다. 저도 처음부터 이렇게 한 건 아니에요.

### sql db 구축

- OperationalError: database is locked 오류? : 동시에 두 창을 열고 쓰면, db에 이미 하나가 접속 되어있으니까 오류 뜸. 그럴 땐 끄고 jupyter restart 하기