<h1>Product Recommendation</h1>

<p align="left">
<img src="https://cdn.iconscout.com/icon/free/png-512/microsoft-excel-2-569282.png"
     width="100" height="100" ><br>
Data file : Customer Preference Survey_Edit.xlsx <br>
Details   : 48 rows, 63 columns
</p>
<br>

<h2>Data Checking</h2>
<img src="https://github.com/PaoLastHope/BADS7105/blob/7053e994fd8fe3f64a15e2f97885e77c0f9e6c17/HOMEWORK%2007/images/it1.PNG">

<h2>Item - Item based</h2>

- Convert text 'เคย' to 1, 'ไม่เคย' to 0. So, we can start data manipulation .
- Perform <b>collaborative filtering</b> to see the score of relation between product.
- Display the result with network function, red score represent the relation between product.
- Note that label of product is Thai, need to install Thai font.

<img width="600" src="https://github.com/PaoLastHope/BADS7105/blob/62f444278886d09e96e66ef36ee5717ccefc69b9/HOMEWORK%2007/images/it2.PNG">
<img width="600" src="https://github.com/PaoLastHope/BADS7105/blob/7053e994fd8fe3f64a15e2f97885e77c0f9e6c17/HOMEWORK%2007/images/it3.png">
<img width="600" src="https://github.com/PaoLastHope/BADS7105/blob/62f444278886d09e96e66ef36ee5717ccefc69b9/HOMEWORK%2007/images/t35.PNG">
<img width="600" src="https://github.com/PaoLastHope/BADS7105/blob/62f444278886d09e96e66ef36ee5717ccefc69b9/HOMEWORK%2007/images/t36.PNG">
<img src="https://github.com/PaoLastHope/BADS7105/blob/4bb1ba4a2d980deffbe0141623ffd03feda6cc29/HOMEWORK%2007/images/it4n.png">
<img src="https://github.com/PaoLastHope/BADS7105/blob/7053e994fd8fe3f64a15e2f97885e77c0f9e6c17/HOMEWORK%2007/images/it5.png">

<h2>User - User based</h2>

- Assign 'User' column, so we can do user-user similarity analysis
- Using <b>cosine similarity</b> and mean score to filter the items
- Now, we can recommend the product to the anoter users which likely to buy the same item.

<img width="500" src="https://github.com/PaoLastHope/BADS7105/blob/db4dd95ec640681cdd3850cac060fc86cca25038/HOMEWORK%2007/images/uu1.PNG"> 
<img src="https://github.com/PaoLastHope/BADS7105/blob/4bb1ba4a2d980deffbe0141623ffd03feda6cc29/HOMEWORK%2007/images/uu3n.png">
<img src="https://github.com/PaoLastHope/BADS7105/blob/db4dd95ec640681cdd3850cac060fc86cca25038/HOMEWORK%2007/images/uu2.PNG">

Reference<br/>
https://www.datacamp.com/community/tutorials/recommender-systems-python<br/>
https://github.com/mrolarik/basic-python/tree/master/python-thai-font-and-plot<br/>
https://seaborn.pydata.org/generated/seaborn.heatmap.html<br/> 
