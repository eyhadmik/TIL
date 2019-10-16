# MODE JOIN 2019-10-14

### JOIN

**Problem) Write a query that selects `the school name`, `player name`, `position`, and `weight`
for every player `in Georgia`, `ordered by weight` (heaviest to lightest). Be sure to make an alias for the table, and to reference all column names in relation to the alias.**

    	SELECT p.school_name
    			 , p.player_name
    			 , p.position
    			 , p.weight
    		FROM benn.college_football_players AS p
    	 WHERE p.state = 'GA'
    ORDER BY p.weight DESC;

### INNER JOIN

**Problem) Write a query that displays `player names`, `school names` and `conferences` for schools in the `"FBS (Division I-A Teams)"` division.** 

    SELECT p.player_name, p.school_name, t.conference
      FROM benn.college_football_players AS p
      JOIN benn.college_football_teams AS t
     	  ON p.school_name = t.school_name
     WHERE t.division = 'FBS (Division I-A Teams)';

### LEFT JOIN

**Problem) Write a query that performs an `inner join` between the `tutorial.crunchbase_acquisitions` table and the `tutorial.crunchbase_companies` table, but instead of listing individual rows, `count the number` of non-null rows in each table.** 

    		SELECT COUNT(*)
    			FROM tutorial.crunchbase_acquisitions AS a
    INNER JOIN tutorial.crunchbase_companies AS c
    				ON a.company_name = [c.name](http://c.name/);

**Problem) Modify the query above to be a `LEFT JOIN`.
Note the difference in results.** 

    	 SELECT COUNT(*)
    		 FROM tutorial.crunchbase_acquisitions AS a
    LEFT JOIN tutorial.crunchbase_companies AS c
    			 ON a.company_name = [c.name](http://c.name/);

**Problem) `Count` the number of `unique companies`(don't double-count companies) and `unique acquired companies` `by state`. Do not include results for which there is no state data, and `order by` `the number of acquired companies` from highest to lowest.** 

       SELECT c.state_code
    			  , COUNT(DISTINCT [c.name](http://c.name/)) AS company
    			  , COUNT(DISTINCT a.acquirer_name) AS aquired_company
    		 FROM tutorial.crunchbase_companies as c
    LEFT JOIN tutorial.crunchbase_acquisitions as a
    			 ON [c.name](http://c.name/) = a.company_name
        WHERE c.state_code IS NOT NULL
     GROUP BY c.state_code
     ORDER BY 2 DESC
    ;

### RIGHT JOIN

**Problem) Rewrite the previous practice query in which you counted total and acquired companies by state, but with a `RIGHT JOIN` instead of a LEFT JOIN. The goal is to produce the exact same results**.

    		SELECT c.state_code
    				 , COUNT(DISTINCT c.name) AS company
    				 , COUNT(DISTINCT a.acquirer_name) AS aquired_company
    		  FROM tutorial.crunchbase_acquisitions as a
    RIGHT JOIN tutorial.crunchbase_companies as c
    				ON c.name = a.company_name
    		 WHERE c.state_code IS NOT NULL
    	GROUP BY c.state_code
    	ORDER BY 2 DESC
    ;

### JOIN Using WHERE or ON

**Problem) Write a query that shows a c`ompany's name`
, `"status"` (found in the Companies table)
, and `the number of unique investors` in that company.
`Order by` `the number of investors` from most to fewest.
Limit to only companies in the state of `New York`.**

    	 SELECT [c.name](http://c.name/)
    	   	  , c.status
    		    , COUNT(DISTINCT i.investor_name) AS count_investor
    		 FROM tutorial.crunchbase_companies AS c
    LEFT JOIN tutorial.crunchbase_investments AS i
    			 ON [c.name](http://c.name/) = i.company_name
    	  WHERE c.state_code = 'NY'
     GROUP BY [c.name](http://c.name/), c.status
     ORDER BY count_investor DESC;

**Problem) Write a query that lists investors based on `the number of companies` in which they are invested. Include a row for companies with no investor, and order from most companies to least.** 

-- 투자자 없는 회사 전체 수 카운트해서 마지막 줄에 끼워넣기

    (
    	SELECT investor_name AS investor
    	     , COUNT(company_name) AS number_of_company
    		FROM tutorial.crunchbase_investments
    GROUP BY investor_name
    )
    
    	 UNION
    
    (
    	SELECT 'None' AS investor
    	     , COUNT(name) AS number_of_company
    	  FROM tutorial.crunchbase_companies
    	 WHERE funding_total_usd IS NULL
    )
    
    ORDER BY number_of_company DESC;

### FULL JOIN

**Problem) Write a query that joins `tutorial.crunchbase_companies` and `tutorial.crunchbase_investments_part1` using a `FULL JOIN`. `Count up` the number of rows that are `matched`/`unmatched`as in the example above.** 

    	 SELECT COUNT(CASE WHEN [c.name](http://c.name/) IS NOT NULL AND i.company_name IS NULL
    										 THEN 1 ELSE NULL END) AS companies_only
    		  	, COUNT(CASE WHEN [c.name](http://c.name/) IS NOT NULL AND i.company_name IS NOT NULL
    										 THEN 1 ELSE NULL END) AS both_table
    			  , COUNT(CASE WHEN [c.name](http://c.name/) IS NULL AND i.company_name IS NOT NULL
    									 	 THEN 1 ELSE NULL END) AS investment_only
    		 FROM tutorial.crunchbase_companies AS c
    FULL JOIN tutorial.crunchbase_investments_part1 AS i
    			 ON [c.name](http://c.name/) = i.company_name
    ;

### UNION

**Problem) Write a query that appends the two `crunchbase_investments` datasets above (including duplicate values). Filter the first dataset to only `companies with names that start with the letter "T"`, and filter the second to `companies with names starting with "M"` (both not case-sensitive). Only include the `company_permalink`, `company_name`, and `investor_name` columns.**

    SELECT company_permalink
    		 , company_name
    		 , investor_name
      FROM tutorial.crunchbase_investments
     WHERE company_name LIKE 'T%'
    
     UNION
    
    SELECT company_permalink
    		 , company_name
    		 , investor_name
      FROM tutorial.crunchbase_investments
     WHERE company_name LIKE 'M%'
    ;

**Problem) Write a query that shows 3 columns. The first indicates which dataset (`part 1` or `2`) the data comes from, the second shows `company status`, and the third is a count of `the number of investors`.**

**Hint: you will have to use the tutorial.crunchbase_companies table
as well as the investments tables. And you'll want to group by status and dataset.**

    -- 너무 느려. 5분
    
    		SELECT 'part1' AS part
    					, c.status
    					, COUNT(i1.investor_name) AS count
    			FROM tutorial.crunchbase_companies c
    INNER JOIN tutorial.crunchbase_investments_part1 i1
    				ON c.name = i1.company_name
    	GROUP BY c.status
    
    		UNION
    
    		SELECT 'part2' AS part
    					, c.status
    					, COUNT(i2.investor_name) AS count
    			FROM tutorial.crunchbase_companies c
    INNER JOIN tutorial.crunchbase_investments_part2 i2
    				ON c.name = i2.company_name
    	GROUP BY c.status
    ;

    --순서 바꾼다, 그래도 오래 걸림 3분
    SELECT df.part
    		 , c.status
    		 , COUNT(df.investor_name) AS count
    FROM (
    			SELECT 'part1' AS part
    						, i1.investor_name
    						, i1.company_name
    			   FROM tutorial.crunchbase_investments_part1 i1
    
    				UNION
    
    			SELECT 'part2' AS part
    		       , i2.investor_name
    		       , i2.company_name
    			  FROM tutorial.crunchbase_investments_part2 i2
    		) df
    
    		JOIN tutorial.crunchbase_companies c
    			ON c.name = df.company_name
    GROUP BY df.part, c.status
    ;