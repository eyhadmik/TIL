# SQL/PANDAS_10

# sql 프로그래머스 풀이

- 입양시각 구하기(2)

    SELECT B.HR, COUNT(A.ANIMAL_ID)
    FROM(
        # ANIMAL_ID와 해당 아이디의 HR(HOUR)만 선택
        SELECT HOUR(DATETIME) AS HR, ANIMAL_ID
        FROM ANIMAL_OUTS
        ) AS A 
        
        # 어떤 수에 대해서 24로 나눈 나머지는 0부터 23까지 나옴
        # DISTINCT를 주어 0부터 23 숫자를 하나씩 선택
        RIGHT JOIN (
            SELECT DISTINCT (CAST(SUBSTRING(ANIMAL_ID FROM 2) AS SIGNED) % 24) AS HR
            FROM ANIMAL_OUTS
        ) AS B  
        # A에서 해당 아이디의 HR 과 연결
        # 예) A의 ANIMAL_ID = 319408 이고 HR = 11 이면 B에서 나온 0부터 23 중 11과 연결
        ON A.HR = B.HR
        GROUP BY B.HR
        ORDER BY B.HR
    
    -- 
    SUBSTR(str FROM pos)
    
    SELECT SUBSTRING('동해물과백두산이' FROM 5);
    결과) 백두산이
    해석) 5번째 문자열부터 읽으시오.

- 오랜기간 보호한 동물(2)

    /* 날짜형 데이터 타입 다루기 */
        SELECT I.ANIMAL_ID, I.NAME
        FROM ANIMAL_INS AS I
            INNER JOIN ANIMAL_OUTS AS O ON O.ANIMAL_ID = I.ANIMAL_ID
        ORDER BY O.DATETIME - I.DATETIME DESC
        LIMIT 2;
        
        # date diff 함수 사용 
        SELECT ao.ANIMAL_ID, ao.NAME
        FROM ANIMAL_INS as ai
            join ANIMAL_OUTS as ao ON ai.ANIMAL_ID = ao.ANIMAL_ID
        ORDER BY DATEDIFF(ai.DATETIME, ao.DATETIME)
        LIMIT 2
        
        # 선미님 풀이 
        SELECT i.ANIMAL_ID, i.NAME
        FROM ANIMAL_INS i
             INNER JOIN ANIMAL_OUTS o ON i.ANIMAL_ID = o.ANIMAL_ID
        ORDER BY TIMESTAMPDIFF(second, i.DATETIME, o.DATETIME) DESC
        LIMIT 2

# COMPREHENSION 연습