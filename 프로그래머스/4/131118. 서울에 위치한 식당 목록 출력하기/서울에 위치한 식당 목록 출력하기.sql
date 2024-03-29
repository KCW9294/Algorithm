-- 코드를 입력하세요
SELECT RR.REST_ID,	RI.REST_NAME, RI.FOOD_TYPE, RI.FAVORITES, RI.ADDRESS, ROUND(AVG(RR.REVIEW_SCORE),2) as SCORE
FROM REST_INFO as RI
INNER JOIN REST_REVIEW as RR on RI.REST_ID = RR.REST_ID
WHERE ADDRESS LIKE '서울%'
GROUP BY RI.REST_ID
ORDER BY SCORE DESC, FAVORITES DESC;