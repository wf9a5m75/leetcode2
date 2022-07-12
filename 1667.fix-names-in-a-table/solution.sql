# Write your MySQL query statement below
Select
    user_id,
    CONCAT(UPPER(LEFT(name, 1)), LOWER(SUBSTRING(name, 2))) as name
FROM
    users
ORDER BY
    user_id
