<h1>Campaign Response Model</h1>

<p align="left">
<img src="https://cdn.iconscout.com/icon/free/png-512/microsoft-excel-2-569282.png"
     width="100" height="100" ><br/>
Data file : Retail_Data_Response.csv <br/>
Details   : 6885 rows, 2 columns

Data file : Retail_Data_Transactions.csv <br/>
Details   : 125001 rows, 3 columns
</p>

<b>Data Checking</b>

<p>
<img width="200" src="https://github.com/suthasinee-p/BADS7105-CRM-Analytics/blob/main/Homework%2004%20-%20Campaign%20Response%20Model/images/Data_Checking1.PNG">
<img width="300" src="https://github.com/suthasinee-p/BADS7105-CRM-Analytics/blob/main/Homework%2004%20-%20Campaign%20Response%20Model/images/Data_Checking2.PNG">
</p>

<b>Data Preparetion</b>

- Calculate value of recency, frequency, monetary_value, AOU andticket_size
- Perform data imbalance with SMOTE 

<img width="450" src="https://github.com/suthasinee-p/BADS7105-CRM-Analytics/blob/main/Homework%2004%20-%20Campaign%20Response%20Model/images/Data_Preparetion.PNG">

<b>Visualization</b>

<img width="450" src="https://github.com/suthasinee-p/BADS7105-CRM-Analytics/blob/main/Homework%2004%20-%20Campaign%20Response%20Model/images/dv1.png">
<img width="500" src="https://github.com/suthasinee-p/BADS7105-CRM-Analytics/blob/main/Homework%2004%20-%20Campaign%20Response%20Model/images/dv2.png">
<img width="500" src="https://github.com/suthasinee-p/BADS7105-CRM-Analytics/blob/main/Homework%2004%20-%20Campaign%20Response%20Model/images/dv3.png"> 

<b>Process ML - SVM </b>

- Running with SVM RFM
<img width="400" src="https://github.com/suthasinee-p/BADS7105-CRM-Analytics/blob/main/Homework%2004%20-%20Campaign%20Response%20Model/images/svm1.PNG">
- Running with SVM CLV
<img width="400"src="https://github.com/suthasinee-p/BADS7105-CRM-Analytics/blob/main/Homework%2004%20-%20Campaign%20Response%20Model/images/svm2.PNG">

<b>Process ML - Logistic Regression with RMF and CLV</b>

- Running with LR RFM
<img width="400" src="https://github.com/suthasinee-p/BADS7105-CRM-Analytics/blob/main/Homework%2004%20-%20Campaign%20Response%20Model/images/log1.PNG">
- Running with LR CLV
<img width="400" src="https://github.com/suthasinee-p/BADS7105-CRM-Analytics/blob/main/Homework%2004%20-%20Campaign%20Response%20Model/images/log2.PNG">

<b>Process ML - XGBoost with RMF and CLV</b>

- Running with XGBoost RFM
<img width="400" src="https://github.com/suthasinee-p/BADS7105-CRM-Analytics/blob/main/Homework%2004%20-%20Campaign%20Response%20Model/images/xg1.PNG">
- Running with XGBoost CLV
<img width="400" src="https://github.com/suthasinee-p/BADS7105-CRM-Analytics/blob/main/Homework%2004%20-%20Campaign%20Response%20Model/images/xg2.PNG">
- Running with XGBoost Tuning
<img width="400" src="https://github.com/suthasinee-p/BADS7105-CRM-Analytics/blob/main/Homework%2004%20-%20Campaign%20Response%20Model/images/xg3.PNG">

<b>Best Model</b>

<img width="400" src="https://github.com/suthasinee-p/BADS7105-CRM-Analytics/blob/main/Homework%2004%20-%20Campaign%20Response%20Model/images/Best_Model.PNG">
