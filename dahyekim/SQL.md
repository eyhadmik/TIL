# SELECT

* SELECT ALL

```SQL
SELECT*
FROM employeeS
```
* SELECT Column and AS

```SQL
SELECT e.emp_name
FROM employeeS as e
```

* Multiple
```SQL
SELECT city,state
FROM station
```


# WHERE 

* Condition

```SQL
SELECT *
FROM city
WHERE population > 100000
AND countrycode = 'USA'
```

* Distinct & even number

```SQL
SELECT DISCTINCT city
FROM station
WHERE mod(city,2)=0
```
# NOT
```sql
SELECT city
FROM station
WHERE NOT (a<>0 or b<>0)
```

# COUNT

```SQL
SELECT count (city) - SELECT count (distinct city)
FROM station
```


# LIKE & NOT LIKE

```sql
SELECT distinct s.city
FROM station as
WHERE city like 'a%'
or city like 'e%'
or city like 'i%'
or city like 'o%'
or city like 'u%'
```

```sql
SELECT city
FROM station
WHERE city like '%\%%'
```

```sql
SELECT city
FROM station
WHERE city like 'It''s'
```

> % : %\%%
<br> ' : ''''

* REGEXP

* aeiou로 시작

```sql
SELECT DISTINCT city 
FROM station
WHERE city REGEXP '^a|^e|^i|^o|^u'
```

```sql
SELECT DISTINCT city 
FROM station
WHERE city REGEXP '^[aeiou]'
```

* aeiou로 끝

```sql
SELECT distinct city
FROM station
WHERE city REGEXP 'a$|e$|i$|o$|u$'
```

```sql
SELECT distinct city
FROM station
WHERE city REGEXP '[aeiou]$'
```
* a,e,i,o,u 로 시작 &  a,e,i,o,u 끝
```sql
SELECT distinct city
FROM station 
WHERE city REGEXP '^[aeiou]'
and city REGEXP '[aeiou]$'
```

```sql
SELECT distinct city
FROM station 
WHERE city REGEXP '^[aeiou].*[aeiou]$'
```
>. : 모든 char
<br> * : 0 or more 

# ORDER

* 오름차순

```sql
SELECT city
FROM station
ORDER BY city asc
```

* 내림차순
```sql
SELECT city
FROM station
ORDER BY city desc
```
* 복수의 열
```sql
SELECT city
FROM station
ORDER BY a,b

a>b순서대로 정렬
```

* NULL 값은 가장 작은 값

# LIMIT

* no를 내림차순 하면서 3행까지 출력
```sql
SELECT city
FROM station
ORDER BY no DESC
LIMIT 3 
```

# OFFSET
* 3건씩 총 3페이지 > 3페이지 표시

```sql
SELECT city
FROM station
LIMIT 3
OFFSET 3
```
# CALCUTATION
```sql
SELECT city , PRICE * QUANTITY (AS) AMOUNT
FROM station
```
```sql
SELECT *
, PRICE * QUANTITY "매출"
FROM A
```

```SQL
SELECT * 
, PRICE * QUANTITY AS "금액"
WHERE "금액" >= 2000
FROM A
[ERROR]

WHERE > SELECT 순으로 처리
WHERE 에서 사용한 "금액"은 처리 불가
```

* Calculation & Order
```sql
SELECT * 
, price * quantity as amount
FROM station
ORDER BY amount DESC
```

# FUCTION
## ROUND
```sql
SELECT *
, ROUND (amout,1)
FROM station
```
## CONCAT
```SQL
SELECT CONCAT (amoun,unit)
FROM sample1
```

## SUBSTRING
```SQL
SUBSTRING('19900708',5,2)
```
## TRIM
```SQL
TRIM('ABC   ')
```
# DATE

```SQL
SELECT current_timestamp
```
```sql
SELECT current_timestamp + 1day
```

```SQL
DATEDIFF('2019-07-24','2019-01-01')
```

# CASE WEHN
```SQL
CASE
WHEN 1 THEN '남자'
WHEN 2 THEN '여자'
END
```

```SQL
SELECT a
, CASE WEHN a IS NULL THEN 0
ELSE a END
"a(null=0)"
FROM sample
```
* Result

a|a(null=0)
-|-
1|2
NULL|0

* COALESCE
```SQL
SELECT a
, COALESCE (a,0)
FROM sample1
```

## Multple Case
```sql
update-ing

SELECT a AS "코드"
CASE
    WHEN 1 = a THEN '남자'
    WHEN 2 = a THEN '여자'
    ELSE '미지정'
END AS "성별" FROM sample1

SELECT a AS "코드"
CASE 
    WHEN 1 THEN '남자'
    WHEN 2 THEN '여자'
    ELSE '미지정'
END AS "성별" FROM sample1
```

# INSERT
INSERT INTO city
VALUES (1,'ABC','2019-07-24')

INSERT INTO city (no, a)
VALUES (2,'DEF')

# REGULAR EXPRESSON
```
.       - Any Character Except New Line
\d      - Digit (0-9)
\D      - Not a Digit (0-9)
\w      - Word Character (a-z, A-Z, 0-9, _)
\W      - Not a Word Character
\s      - Whitespace (space, tab, newline)
\S      - Not Whitespace (space, tab, newline)

\b      - Word Boundary
\B      - Not a Word Boundary
^       - Beginning of a String
$       - End of a String

[]      - Matches Characters in brackets
[^ ]    - Matches Characters NOT in brackets
|       - Either Or
( )     - Group

Quantifiers:
*       - 0 or More
+       - 1 or More
?       - 0 or One
{3}     - Exact Number
{3,4}   - Range of Numbers (Minimum, Maximum)
```
