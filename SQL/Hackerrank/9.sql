-- https://www.hackerrank.com/challenges/weather-observation-station-6/problem?isFullScreen=true
-- STUDY MORE | REGEXP

-- My previous submission:
-- SELECT city
-- FROM station
-- WHERE city LIKE 'a%' OR 
-- city LIKE 'e%' OR 
-- city LIKE 'i%' OR 
-- city LIKE 'o%' OR 
-- city LIKE 'u%';

SELECT city FROM station WHERE city REGEXP '^[aeiou]';