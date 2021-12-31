<h1>Churn Prediction Model</h1>

<img src="https://github.com/suthasinee-p/BADS7105-CRM-Analytics/blob/main/Homework%2006%20-%20Churn%20Prediction%20Model/Ch1.JPG">

<code>
SELECT   CW AS WEEK,   NEW_CUST,   REPEAT_CUST,   RETURN_CUST,   REPEAT_CUST - LAG(TOT, 1) OVER(ORDER BY CW) AS CHURN_CUST
FROM (
  SELECT  CW,
    COUNT(CASE WHEN STATUS = 'NEW' THEN CC ELSE NULL END) AS NEW_CUST,
    COUNT(CASE WHEN STATUS = 'REP' THEN CC ELSE NULL END) AS REPEAT_CUST,
    COUNT(CASE WHEN STATUS = 'RET' THEN CC ELSE NULL END) AS RETURN_CUST,
    COUNT(CC) AS TOT
  FROM (
    SELECT 
      PRE_W,
      CW,
      CC,
      CASE
        WHEN DATE_DIFF(CW, PRE_W, DAY) IS NULL THEN 'NEW'
        WHEN DATE_DIFF(CW, PRE_W, DAY) <= 7 THEN 'REP'
        WHEN DATE_DIFF(CW, PRE_W, DAY) > 7 THEN 'RET'
      ELSE
      NULL
    END
      AS STATUS
    FROM (
      SELECT
        LAG(CW, 1)OVER(PARTITION BY CC ORDER BY CW) AS PRE_W,
        CW,
        CC
      FROM (
        SELECT
          DISTINCT DATE_TRUNC(PARSE_DATE('%Y%m%d',
              SHOP_DATE), WEEK) AS CW,
          CUST_CODE AS CC
        FROM
          `suthasinee-project.my_dataset.my_market`
        WHERE
          CUST_CODE IS NOT NULL)))
  GROUP BY
    CW)
ORDER BY
  WEEK ASC;
</code>