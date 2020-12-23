# Census_Income_Analysis

Most interesting analyses are done on recent data. We found it rather intriguing to work on a relatively old data that contained information of US census data. We started our analysis by understanding what census is and how it is such an important part in understanding the progress of any country.Our data from from 1994 which included features like age, education, marital status, hours of work and salary below or above 50K annually and the number of people satisfying these categories.
We transformed some columns to avoid confusion between column names and function call.


We also created our custom function, since the code gor repeated twice. We import this module before we can use it.
We found out that marital status goes not affect the womans salary status, which was rather interesting. Also, the most whites had a high salary compared to the other races. Unfortunately, farmers who, despite having high education and long hours of work, small proportion of them had. hgh salary.
In our data, age had the high feature importance, along with number of people falling in that category(fnlwgt), education and weekly hours worked. This was pretty practical and understandable when we tried to think of real life scenerios.
We also carried out predictive analysis, though not of any practical significance helped us brainstorm a good model. Our business scenerio was an interpretable model and has no latency requiremement. All our features are independent of each other, and the ones which practically had direct significance - education name and education number, education _name was dropped.
For the above description, naive bayes algorithm was most suited. The metric to jugde the model was - AUC (Area Under the Curve). This is because, our dataset is unbalanced (3:1, < 50k: >50K ), categorical and both the categories have equal importance. Precision and recall are preferred when one category has a higher importance.
We considered laplace smoothing, however, on reading we realised it is most recommended for text data, to avoid overfitting/ underfitting. We carried out 'One hot encoding' to convert categorical values to numberical values.
The Naive Bayes model had AUC - 0.83 . To improve performance, we normalised our only continous column, which also had the highest feature importance - fnlwgt. This ncreased the AUC value to AUC: 0.89.
