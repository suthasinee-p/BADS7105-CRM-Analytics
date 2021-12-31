<h1>Product Recommendation</h1>

<p align="left">
<img src="https://cdn.iconscout.com/icon/free/png-512/microsoft-excel-2-569282.png"
     width="100" height="100" ><br>
Data file : Customer Preference Survey (Responses) - Form Responses 1.csv <br>
Details   : 47 rows, 42 columns
</p>
<br>

<h2>Visualization</h2>
<img src="https://github.com/suthasinee-p/BADS7105-CRM-Analytics/blob/main/Homework%2003%20-%20Product%20Recommendation/images/Visualization.JPG">

<h2>Data Checking</h2>
<img src="https://github.com/suthasinee-p/BADS7105-CRM-Analytics/blob/main/Homework%2003%20-%20Product%20Recommendation/images/Data%20Checking.JPG">

<h2>Item - Item based</h2>

- Convert text 'เคย' to 1, 'ไม่เคย' to 0. So, we can start data manipulation .
- Perform <b>collaborative filtering</b> to see the score of relation between product.
- Display the result with network function, red score represent the relation between product.
- Note that label of product is Thai, need to install Thai font.

<img src="https://github.com/suthasinee-p/BADS7105-CRM-Analytics/blob/main/Homework%2003%20-%20Product%20Recommendation/images/ITEM-ITEM%20Heat%20Map.JPG">
<img src="https://github.com/suthasinee-p/BADS7105-CRM-Analytics/blob/main/Homework%2003%20-%20Product%20Recommendation/images/links_filtered.JPG">

<h2>User - User based</h2>

- Assign 'User' column, so we can do user-user similarity analysis
- Using <b>cosine similarity</b> and mean score to filter the items
- Now, we can recommend the product to the anoter users which likely to buy the same item.

<img src="https://github.com/suthasinee-p/BADS7105-CRM-Analytics/blob/main/Homework%2003%20-%20Product%20Recommendation/images/USER-USER%20Heat%20Map.JPG">


<h2>Product Recommendation</h2>
<img src="https://github.com/suthasinee-p/BADS7105-CRM-Analytics/blob/main/Homework%2003%20-%20Product%20Recommendation/images/Recom.JPG">

Reference<br/>
https://www.datacamp.com/community/tutorials/recommender-systems-python<br/>
https://github.com/mrolarik/basic-python/tree/master/python-thai-font-and-plot<br/>
https://seaborn.pydata.org/generated/seaborn.heatmap.html<br/> 
