Hacker Rank The Report

(SELECT s.name, g.grade, s.marks
FROM students AS s
LEFT JOIN grades AS g
ON s.marks >= g.min_mark 
AND s.marks <= g.max_mark
WHERE g.grade >= 8
ORDER BY s.marks DESC, s.name ASC)
UNION
(SELECT NULL, g.grade, s.marks
FROM students AS s
LEFT JOIN grades AS g
ON s.marks >= g.min_mark
AND s.marks <= g.max_mark
WHERE g.grade < 8
ORDER BY g.grade DESC, s.marks ASC)

SELECT s1.name, g1.grade, s1.marks 
FROM students AS s1
LEFT JOIN grades AS g1
ON s1.marks >= g1.min_mark 
AND s1.marks <= g1.max_mark
WHERE g1.grade >= 8
    
UNION
    
SELECT NULL, g2.grade, s2.marks
FROM students AS s2
LEFT JOIN grades AS g2
ON s2.marks >= g2.min_mark
AND s2.marks <= g2.max_mark
WHERE g2.grade < 8

ORDER BY s1.marks DESC, s1.name ASC, g2.grade DESC, s2.marks ASC

# Symmetric Pair

SELECT f1.x, f1.y
FROM functions AS f1
INNER JOIN functions AS f2
ON f1.y = f2.x
WHERE f1.x <= f1.y 
AND f1.x = f2.y
ORDER BY x ASC, y ASC

- x=y 인 점들은 리스트에 두개씩 있어야 함.

- x=y 인 점, x<>y 인 점 나눠서 union?

- group by 조건을 두개 줄 수 잇나?
x 값, y 값

-> Union 쓴다
1. x1 = y1 = x2 = y2 
2. x1 = y2, y1 = x2, x1 <> x2

# 풀이
SELECT f1.x, f1.y
FROM functions AS f1
WHERE f1.x = f1.y
GROUP BY f1.x, f1.y
HAVING COUNT(*) > 1

UNION

SELECT f1.x, f1.y
FROM functions AS f1 INNER JOIN functions AS f2 ON f1.x = f2.y AND f2.x = f1.y
WHERE f1.x < f1.y
ORDER BY x