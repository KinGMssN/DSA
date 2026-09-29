SELECT product_name,year,price
FROM Sales as s
LEFT JOIN Product as p ON p.product_id=s.product_id  