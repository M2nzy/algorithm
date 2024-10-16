SELECT C.AUTHOR_ID, C.AUTHOR_NAME,
CATEGORY, SUM(sales*PRICE) AS SALES FROM BOOK_SALES A
LEFT JOIN BOOK B ON A.BOOK_ID = B.BOOK_ID LEFT JOIN AUTHOR C ON B.AUTHOR_ID = C.AUTHOR_ID WHERE SALES_DATE LIKE '2022-01%'
GROUP BY B.author_id, CATEGORY
ORDER BY AUTHOR_ID ASC, CATEGORY DESC