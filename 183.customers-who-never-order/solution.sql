# Write your MySQL query statement below
SELECT
    C.name as Customers
FROM
    Customers as C
    LEFT OUTER JOIN Orders
        ON C.id = Orders.customerId
WHERE
    Orders.id IS NULL
