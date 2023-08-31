#Première requête

SELECT
    date AS order_date,
    SUM(prod_price * prod_qty) AS ventes
FROM
    TRANSACTIONS
WHERE
    date BETWEEN '2019-01-01' AND '2019-12-31'
GROUP BY
    date
ORDER BY
    date;

#Deuxième requête
	
SELECT
    t.client_id,
    SUM(CASE WHEN pn.product_type = 'MEUBLE' THEN t.prod_price * t.prod_qty ELSE 0 END) AS ventes_meuble,
    SUM(CASE WHEN pn.product_type = 'DECO' THEN t.prod_price * t.prod_qty ELSE 0 END) AS ventes_deco
FROM
    TRANSACTIONS t
JOIN
    PRODUCT_NOMENCLATURE pn ON t.prod_id = pn.product_id
WHERE
    t.date BETWEEN '2020-01-01' AND '2020-12-31'
GROUP BY
    t.client_id;


