import pandas as pd
import numpy as np


#1.Reading dataset
users = pd.read_csv('/Users/paramanandbhat/Downloads/Non_personalisedrecommendersystemsinpython-201024-234034 (1)/user_demographics.csv')

#Reading ratings file:
ratings= pd.read_csv('/Users/paramanandbhat/Downloads/Non_personalisedrecommendersystemsinpython-201024-234034 (1)/ratings.csv')

#Reading items file:
movie_info = pd.read_csv('/Users/paramanandbhat/Downloads/Non_personalisedrecommendersystemsinpython-201024-234034 (1)/movie_info.csv')

## 2. Basic Exploration 
### Exploring user data
# shape of the users data
print(users.shape)
# view the users data
users.head()
print(users.head())

pd.isnull(users).sum()

print(pd.isnull(users).sum())

'''
So, we have 943 users in the dataset and each user has 5 features, i.e. user_ID, age, sex, occupation and zip_code. We have no missing values in the user data. Now let’s look at the ratings file.

'''

### Exploring ratings data
# shape of the data
print(ratings.shape)
# view the ratings data
print(ratings.head())


ratings[(ratings['user_id'] == 1)&(ratings['movie_id'] == 100)]

print(ratings[(ratings['user_id'] == 1)&(ratings['movie_id'] == 100)])

pd.isnull(ratings).sum()

print(pd.isnull(ratings).sum())

'''
We have 100k ratings for different user and
 movie combinations. Again there are no 
 missing values here.
 Now lets examine the items file.
'''
### Exploring Movie Information data
# shape of the data
print(movie_info.shape)
# view the items file
print(movie_info.head())

# Check missing values in movie information
pd.isnull(movie_info).sum()

print(pd.isnull(movie_info).sum())

