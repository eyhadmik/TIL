# 10월 4일 SQL 과제 풀이

## Programmers SQL `GROUP BY` [입양시각 구하기(1)](https://programmers.co.kr/learn/courses/30/lessons/59412)

### 내 풀이 → 범위는 Between 을 이용하기

    SELECT HOUR(DATETIME), COUNT(ANIMAL_ID)
    FROM ANIMAL_OUTS
    WHERE HOUR(DATETIME) > 8 AND HOUR(DATETIME) < 20
    GROUP BY HOUR(DATETIME)

### 범위 설정 Between (혜정님 풀이)

`Between`: Professional, 연산속도도 가장 빠르다

    HAVING HOUR BETWEEN 9 AND 19

### Substring (예슬님 풀이 수정)

`SUBSTRING(DATETIME, 12, 2)`

`2019-10-04 10:34:00`, 12번째 값부터 2개 → `10`

    SELECT SUBSTRING(DATETIME, 12, 2) AS TIME
    , COUNT(*)
    FROM ANIMAL_OUTS
    GROUP BY TIME
    HAVING TIME BETWEEN 9 AND 19
    ORDER BY TIME

### Substring_index (재민님 풀이)

    SELECT SUBSTRING_INDEX(SUBSTRING_INDEX(DATETIME, ' ', -1), ':', 1) AS HOUR, COUNT(*) AS COUNT
    FROM ANIMAL_OUTS
    GROUP BY HOUR
    HAVING HOUR >= 9 AND HOUR <= 19
    ORDER BY HOUR

---

## Programmers SQL `GROUP BY` [입양시각 구하기(2)](https://programmers.co.kr/learn/courses/30/lessons/59413)

### 단비님 풀이

    SELECT ALL_HOURS.HOUR, COUNT(O.DATETIME)
    FROM (
            SELECT 0 AS HOUR
            UNION ALL
                SELECT 1
            UNION ALL
                SELECT 2
            UNION ALL
                SELECT 3
            UNION ALL
                SELECT 4
            UNION ALL
                SELECT 5
            UNION ALL
                SELECT 6
            UNION ALL
                SELECT 7
            UNION ALL
                SELECT 8
            UNION ALL
                SELECT 9
            UNION ALL
                SELECT 10
            UNION ALL
                SELECT 11
            UNION ALL
                SELECT 12
            UNION ALL
                SELECT 13
            UNION ALL
                SELECT 14
            UNION ALL
                SELECT 15
            UNION ALL
                SELECT 16
            UNION ALL
                SELECT 17
            UNION ALL
                SELECT 18
            UNION ALL
                SELECT 19
            UNION ALL
                SELECT 20
            UNION ALL
                SELECT 21
            UNION ALL
                SELECT 22
            UNION ALL
                SELECT 23
            ) AS ALL_HOURS 
            LEFT JOIN ANIMAL_OUTS AS O ON ALL_HOURS.HOUR = HOUR(O.DATETIME)
    GROUP BY ALL_HOURS.HOUR

### 좀 더 간단하게 머리 쓴 코드

    SELECT A.HR, COUNT(B.ANIMAL_ID)
    FROM (
        SELECT DISTINCT(CAST(SUBSTRING(ANIMAL_ID FROM 2) AS SIGNED) % 24) AS HR
        # 0 ~ 23 까지 들어있는 칼럼을 만든다
        # DISTINCT: 하나씩만 가져온다
        # CAST() AS : Type 설정해준다
        # SIGNED: 부호 달아준다
        # SUBSTRING(@@ FROM 2): 2번째 글자부터 가져온다
        FROM ANIMAL_OUTS
    ) AS A
    LEFT JOIN ( 
        SELECT HOUR(DATETIME) HR, ANIMAL_ID
        FROM ANIMAL_OUTS
    ) AS B
    ON A.HR = B.HR
    GROUP BY A.HR
    ORDER BY A.HR

---

## Programmers SQL `DATE, STRING` [오랜 기간 보호한 동물(2)](https://programmers.co.kr/learn/courses/30/lessons/59411)

### 내 풀이

    SELECT i.ANIMAL_ID, i.NAME
    FROM ANIMAL_INS i INNER JOIN ANIMAL_OUTS o ON i.ANIMAL_ID = o.ANIMAL_ID
    ORDER BY (o.DATETIME - i.DATETIME) DESC
    LIMIT 2

### DATEDIFF() 함수 쓰기

    ORDER BY DATEDIFF(i.DATETIME, o.DATETIME) DESC

### TIMESTAMPDIFF() 함수 쓰기

지정해주는 단위(아래 예시에서는 초 단위)까지 계산

    ORDER BY TIMESTAMPDIFF(second, i.DATETIME, o.DATETIME) DESC