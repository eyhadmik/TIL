gp# SQL/PANDAS_09

- 9월 24일 수업 피드백
- 9월 회고 / 10월 스케쥴
- 모델링을 할 수 있는 사람? : 예측, 함수 모델을 쓸 수 있는 사람 (머신러닝 문제)
- 의사결정 나무 - random forest
- 딥러닝/머신러닝 자료 추천 - 선미님께 문의

# SQL

- [프로그래머스 코딩테스트 고득점 Kit](https://programmers.co.kr/learn/challenges?tab=practice_kit)

# Programmers sql 풀이

- [select](https://programmers.co.kr/learn/courses/30/parts/17042)

        ```sql
        # 동물의 아이디와 이름 
        SELECT ANIMAL_ID, NAME
        FROM ANIMAL_INS
        ORDER BY ANIMAL_ID;
        
        
        # 여러 기준으로 정렬하기
        SELECT ANIMAL_ID, NAME, DATETIME
        FROM ANIMAL_INS
        ORDER BY NAME, DATETIME DESC;
        
        
        # 상위 n개 레코드 
        SELECT NAME
        FROM ANIMAL_INS
        ORDER BY DATETIME
        LIMIT 1;
        -- sub 쿼리 사용 
        SELECT NAME
        FROM ANIMAL_INS
        WHERE DATETIME = (SELECT MIN(DATETIME)
                          FROM ANIMAL_INS)
        ```
        
        
        
        

- [sum/min/max](https://programmers.co.kr/learn/courses/30/parts/17043)

        ```sql
        # 최댓값 구하기 (`ORDER BY`, `LIMIT` 풀이 이외에, `WHERE` 절 서브쿼리를 사용해서 풀어보세요)
        SELECT DATETIME AS 시간 
        FROM ANIMAL_INS
        ORDER BY DATETIME DESC
        LIMIT 1;
        -- 서브쿼리
        SELECT DATETIME AS 시간
        FROM ANIMAL_INS
        WHERE DATETIME = (SELECT MAX(DATETIME)
                          FROM ANIMAL_INS)
        -- MAX로만 풀기
        SELECT MAX(DATETIME)
        FROM ANIMAL_INS)
        
        
        # 최소값 구하기 
        SELECT DATETIME AS 시간 
        FROM ANIMAL_INS
        order by datetime
        limit 1
        ;
        
        # 동물 수 구하기 
        SELECT COUNT(ANIMAL_ID) AS count
        FROM ANIMAL_INS
        ;
        
        # 중복 제거하기
        SELECT COUNT(NAME)
        FROM (
            SELECT NAME 
            FROM ANIMAL_INS
            WHERE NAME IS NOT NULL
            GROUP BY NAME
            ) AS A
        ```

# Basic statistics with Python

- Pandas `apply()`, Python `lambda` 과제 풀이
- 8월 수업 중 [[Basic Statistics for Data Analysis](https://github.com/dataitgirls3/Teaching-Materials/blob/master/Basic%20Statistics%20for%20Data%20Analysis.ipynb)] 문제 풀이 (간단한 통계 계산하는 함수 직접 구현하기)
- [Python Comprehension](https://github.com/dataitgirls3/Teaching-Materials/blob/master/Comprehension.ipynb)