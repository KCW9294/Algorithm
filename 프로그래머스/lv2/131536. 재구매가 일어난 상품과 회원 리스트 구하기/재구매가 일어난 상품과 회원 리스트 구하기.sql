-- 코드를 입력하세요
SELECT user_id, product_id

FROM ONLINE_SALE 
GROUP BY 1,2
HAVING COUNT(product_id) >= 2
ORDER BY 1,2 DESC