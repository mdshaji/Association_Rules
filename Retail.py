import numpy as np
import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules

df =pd.read_csv("D:/Module 23 -Association Rules/transactions_retail1.csv",sep=",")
df.head()
df.shape

df.isna().sum()
df1 = df.dropna()


encoded_vals = []
for index, row in df.iterrows(): 
    labels = {}
    uncommons = list(set(df1) - set(row))
    commons = list(set(df1).intersection(row))
    for uc in uncommons:
        labels[uc] = 0
    for com in commons:
        labels[com] = 1
    encoded_vals.append(labels)
    
Retail = pd.DataFrame(encoded_vals)

### Running Apriori algorithm
##With support=0,005 and max_len=2
frequent_items = apriori(Retail,min_support = 0.005, max_len =2 , use_colnames = True )
frequent_items.sort_values('support', ascending = False, inplace = True)

## Building rules
## with min_threshold =1
rules_dummies = association_rules(frequent_items, metric = 'lift', min_threshold = 1)
rules_dummies.sort_values('lift',ascending =False,inplace =True)

############# To eliminate redudancy in rules########

def to_list(i):
    return(sorted(i))
    
rules_add = rules_dummies.antecedents.apply(to_list) + rules_dummies.consequents.apply(to_list)

rules_add = rules_add.apply(sorted)

rules_set = list(rules_add)

unique_rules = [list(m) for m in set(tuple(i) for i in rules_set)]
index_rules = []
for i in unique_rules:
    index_rules.append(rules_set.index(i))
    
### rules without redudancy##
rules_without_redud = rules_dummies.iloc[index_rules,:]

### sorting
rules_without_redud.sort_values('lift', ascending = False, inplace =True)

### Support and confidence
Support = rules_without_redud['support']
confidence = rules_without_redud['confidence']

import matplotlib.pyplot as plt

plt.scatter(Support,confidence);plt.xlabel("Support");plt.ylabel("Confidence")


############################# Model with other than Zero values#####
x_without_dum = Retail.iloc[:,[1,2,3,4,5]]

#### Applying Apriori with support = 0.005 and max length =2
frequents_item1 = apriori(x_without_dum, min_support=0.005, max_len = 2, use_colnames=True)
frequents_item1.sort_values('support',ascending = False, inplace = True)

###Building rules with minimum threshold = 1
rules_without = association_rules(frequents_item1, metric='lift', min_threshold =1)
rules_without.sort_values('lift',ascending = False, inplace =True)

###Eliminate the reducdancy####
def to_list_out(i):
    return(sorted(i))
    
rules_out_add = rules_without.antecedents.apply(to_list_out)+rules_without.consequents.apply(to_list_out)

rules_out_add = rules_out_add.apply(sorted)
rules_set_out = list(rules_out_add)

##unique values
unique_values_out = [list(n) for n in set(tuple(i) for i in rules_set_out)]
index_rules_out=[]
for i in unique_values_out:
    index_rules_out.append(rules_set_out.index(i))

## rules without redundancy
rules_without_out = rules_without.iloc[index_rules_out,:]

## Sorting
rules_without_out.sort_values('lift', ascending= False, inplace =True)

Support_out = rules_without_out["support"]
Confidence_out = rules_without_out["confidence"]
lift = rules_without_out["lift"]

#### Plotting 3D plot for support, confidence and lift
from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection = "3d")
ax.scatter(Support_out, Confidence_out, lift)
ax.set_xlabel("Support_out")
ax.set_ylabel("Confidence_out")
ax.set_zlabel("lift")


#### scatter plot for rules for support, confidence and lift
import matplotlib.pyplot as plt
import scipy as sp

plt.scatter(Support_out, Confidence_out,c= lift,cmap='gray')
plt.colorbar()
plt.xlabel("Support")
plt.ylabel("Confidence")


### Model with other than Zero values and  model with the dummy variables given in the data set itself are giving two different values
##Considering the model with the dummy variables given in the data set itself are giving two different values
