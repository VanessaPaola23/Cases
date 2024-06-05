#Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#Data analysis exploration
SampleData='sampleData.csv'
df = pd.read_csv(SampleData,index_col=0)

df.head(15)
df.dtypes
df['productAgrupationID'].max()
(df['productID'].unique()).size #592

#df.value_counts
#70393 rows x 5 columns

#Customers = 70393
df['customer'].value_counts

#1. Top 5 main customers of 100
(df['customer'].unique()).size
SampleData_ByCustomer=df.groupby('customer')['product_cases_ordered'].sum()
SampleData_ByCustomer
Top_Customers=SampleData_ByCustomer.sort_values(ascending=0)
Top_Customers.head(5)
#Top 5 customers
#247474    37792.208
#488882    35826.100
#215932    30155.046
#214634    28881.493
#235365    28729.988
#
#

#2. Determine the most popular productAgrupationID based on the total number of cases ordered.
#The most popular productAgrupationID is 1121.0 purchasing an amount of 85874.702
SampleData_ByproductAgrupationID=df.groupby('productAgrupationID')['product_cases_ordered'].sum()
Top_Agrupation_ByproductAgrupationID=SampleData_ByproductAgrupationID.sort_values(ascending=0)
Top_Agrupation_ByproductAgrupationID.head(1)
#
#

#3. Identify the most ordered product ID of each productAgrupationID 
#there are 223 productAgrupationID uniques
(df['productAgrupationID'].unique()).size 
B = df.groupby(['productAgrupationID', 'productID']).agg({'product_cases_ordered': 'sum'})

#3.1 ans
#Obtain the maximum index of product_cases_ordered for each productAgrupationID
max_indices = B.groupby('productAgrupationID')['product_cases_ordered'].idxmax()

# Obtain the productID related to maximum indexes (sales indexes)
max_product_ids = B.loc[max_indices, :]
print(max_product_ids)

#3.2 ans
T=df.groupby(['productAgrupationID','productID']).agg({'productID': 'count'})
T
#Obtain the maximum index of productID count for each productAgrupationID
max_index = T.groupby('productAgrupationID')['productID'].idxmax()
max_index
# Obtain the productID related to maximum indexes (count productID indexes)
max_product = T.loc[max_index, :]
print(max_product)

#Export max_product_ids to Excel
# max_product_ids.to_excel('tabla_arcacont.xlsx',index=1)
# max_product.to_excel('tabla_arcacont_2.xlsx',index=1)

#productID --> product_cases_ordered --->productAgrupationID


#4. How does the sales volume vary across different territories?

SampleData_ByTerritory=df.groupby('territory')['product_cases_ordered'].sum()
Sample=SampleData_ByTerritory.sort_values(ascending=False)
Sample.plot(kind='bar', color='green', grid=1)
plt.show()


#5.  Are there any notable patterns or trends in the productAgrupationID with high sales volume?

A = df.groupby('productAgrupationID').agg({
    'customer': 'first',
    'productID': 'first',
    'territory': 'first',
    'product_cases_ordered': 'sum'
})
A
# Sort by product_cases_ordered in descending order
Top_Agrupation = A.sort_values(by='product_cases_ordered', ascending=False)
Top_Agrupation
#

Top_Agrupation['territory'].mode() #263 code is the most repeated data
Top_Agrupation['customer'].mode() #  193136 and 380726
Top_Agrupation['productID'].mode()


Cases_Where_Territory263 = Top_Agrupation.loc[Top_Agrupation['territory'] == 263]
TopFive=Cases_Where_Territory263.head(5)
TopFive
TopFive.to_excel('tabla_arcacont3.xlsx',index=1)

#in the territory 263 the most purchased item is 877 by customer 221231, followed by: 1178 by 232694,
#3318 by 218167 ,2889 by 231089, 3451 by 231089
