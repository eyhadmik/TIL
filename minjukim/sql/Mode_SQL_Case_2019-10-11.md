# [Mode-SQL] Case 2019-10-11

**Problem)** **Write a query that includes a column that is `flagged "yes"` when a player is `from California`, and sort the results with those players first.**

    SELECT *
    		 , CASE WHEN state = 'CA' THEN 'yes'
    			 ELSE NULL
    			 END AS ca
    FROM benn.college_football_players
    ORDER BY ca;

**Problem) Write a query that includes `players' names` and a column that classifies them into `four categories based on height`. Keep in mind that the answer we provide is only one of many possible answers, since you could divide players' heights in many ways.**

    SELECT player_name
    		 , height
    		 , CASE WHEN height > 80 THEN 'class 1'
    						WHEN height > 75 THEN 'class 2'
    						WHEN height > 70 THEN 'class 3'
    						ELSE 'class 4'
    						END AS height_class
    FROM benn.college_football_players;

**Problem) Write a query that selects all columns from `benn.college_football_players` and adds an additional column that displays the `player's name` if that player is a `junior` or `senior`.**

    SELECT *
    		 , CASE WHEN year IN ('JR', 'SR') THEN player_name
    			 ELSE NULL
    			 END AS JR_OR_SR
    FROM benn.college_football_players;

**Problem) Write a query that `count`s the number of `300lb+ players` for each of the following regions: `West Coast` (CA, OR, WA), `Texas`, and `Other` (Everywhere else).**

    SELECT CASE WHEN state IN ('CA', 'OR', 'WA') THEN 'West Coast'
    						WHEN state = 'Texas' THEN 'Texas'
    						ELSE 'Other'
    						END AS following_region
    		 , COUNT(1) AS count
    FROM benn.college_football_players
    WHERE weight >= 300
    GROUP BY CASE WHEN state IN ('CA', 'OR', 'WA') THEN 'West Coast'
    							WHEN state = 'Texas' THEN 'Texas'
    							ELSE 'Other'
    							END;

**Problem) Write a query that calculates the combined weight of all `underclass players (FR/SO)` in California as well as the combined weight of all `upperclass players (JR/SR)` in California.**

    SELECT CASE WHEN year IN ('FR', 'SO') THEN 'under class'
    						ELSE 'upper class' END
    		 , SUM(weight) AS sum
    FROM benn.college_football_players
    WHERE state = 'CA'
    GROUP BY CASE WHEN year IN ('FR', 'SO') THEN 'under class'
    							ELSE 'upper class' END;

**Problem) Write a query that displays `the number of players` `in each state`, `with FR, SO, JR, and SR` players in separate columns and another column for the `total number` of players. Order results such that states with the most players come first.**

    SELECT state
    		 , COUNT(CASE WHEN year = 'FR' THEN 1 ELSE NULL END) FR_count
    		 , COUNT(CASE WHEN year = 'SO' THEN 1 ELSE NULL END) SO_count
    		 , COUNT(CASE WHEN year = 'JR' THEN 1 ELSE NULL END) JR_count
    		 , COUNT(CASE WHEN year = 'SR' THEN 1 ELSE NULL END) SR_count
    		 , COUNT(*) ALL_count
    FROM benn.college_football_players
    GROUP BY state
    ORDER BY ALL_count DESC;

**선미님 코드**

    SELECT CASE WHEN year = 'FR' THEN 1 ELSE NULL
    						WHEN year = 'SO' THEN 1 ELSE NULL
    						WHEN year = 'JR' THEN 1 ELSE NULL
    						WHEN year = 'SR' THEN 1 ELSE NULL 
    						END AS year_group
    FROM benn.college_football_players
    GROUP BY 1;

**Problem) Write a query that shows `the number of players` at schools with names that `start with A through M`, and the number at schools with names `starting with N - Z.`**

    SELECT full_school_name
    , LEFT(full_school_name, 1)
    , COUNT(*)
    FROM benn.college_football_players
    GROUP BY full_school_name
    ORDER BY full_school_name;

    # 안돌아감
    SELECT COUNT(CASE WHEN SUBSTRING(full_school_name, 1, 1) < 'n' THEN 1 ELSE NULL END) AS 'A-M'
    		 , COUNT(CASE WHEN SUBSTRING(full_school_name, 1, 1) >= 'n' THEN 1 ELSE NULL END) AS 'N-Z'
    FROM benn.college_football_players;

**제공 정답**

    SELECT CASE WHEN school_name < 'n' THEN 'A-M'
    						WHEN school_name >= 'n' THEN 'N-Z'
    						ELSE NULL 
    						END AS school_name_group
    		 , COUNT(1) AS players
    FROM benn.college_football_players
    GROUP BY 1;