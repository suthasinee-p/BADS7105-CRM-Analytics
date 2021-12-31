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


<h2>Compare Model Performance</h2>
<img src="https://github.com/suthasinee-p/BADS7105-CRM-Analytics/blob/main/Homework%2002%20-%20Customer%20Segmentation/images/Compare_model_performance.JPG">


<h2>PCA Plot</h2>
<img src="https://github.com/suthasinee-p/BADS7105-CRM-Analytics/blob/main/Homework%2002%20-%20Customer%20Segmentation/images/PCA_plot.JPG">

<h2>k-mean</h2>
<img src="https://github.com/suthasinee-p/BADS7105-CRM-Analytics/blob/main/Homework%2002%20-%20Customer%20Segmentation/images/k-mean.JPG">

<h2>Spectral Clustering Clustering</h2>
<img src="https://github.com/suthasinee-p/BADS7105-CRM-Analytics/blob/main/Homework%2002%20-%20Customer%20Segmentation/images/Spectral%20Clustering%20Clustering.JPG">

<h2>Interpret results and plan for actions</h2>
<img src="https://github.com/suthasinee-p/BADS7105-CRM-Analytics/blob/main/Homework%2002%20-%20Customer%20Segmentation/images/Interpret%20results%20and%20plan%20for%20actions.JPG">
