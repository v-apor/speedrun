-- https://www.hackerrank.com/challenges/weather-observation-station-12/problem?isFullScreen=true

SELECT DISTINCT city FROM station WHERE city NOT REGEXP '^[aeiou]' AND city NOT REGEXP '[aeuio]$'