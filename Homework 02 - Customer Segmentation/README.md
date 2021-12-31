# Dataset 
SupermarketData.csv

# Calculate features 
1. BASKET_ID
2. PROD_CODE
3. PROD_CODE_10
4. PROD_CODE_20
5. PROD_CODE_30
6. PROD_CODE_40
7. FirstDate get min from SHOP_DATE
8. LastDate get max from SHOP_DATE

# Prepare customer single view

1. Create df_csv2
select CUST_CODE ,SHOP_WEEK, sum(attend) as TotalAtt
from dataframe
group by CUST_CODE, SHOP_WEEK ;

2. Create df_csv3
select CUST_CODE ,SHOP_WEEK,  min(TotalAtt) as TotalAttMin , max(TotalAtt) as TotalAttMax
from df_csv2
group by CUST_CODE, SHOP_WEEK ;