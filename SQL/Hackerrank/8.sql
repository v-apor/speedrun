-- https://www.hackerrank.com/challenges/weather-observation-station-4/problem?isFullScreen=true


-- My Stupid Solution
-- WITH total_table AS
-- (SELECT count(*) AS total_count FROM station),
-- distinct_table AS
-- (SELECT count(DISTINCT city) AS distinct_count FROM station)
-- SELECT total_count - distinct_count as difference FROM total_table, distinct_table;

-- Easier Solution
SELECT count(*) - count(DISTINCT city) FROM station;