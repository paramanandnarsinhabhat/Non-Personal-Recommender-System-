import pandas as pd
import numpy as np


#1.# Load datasets
users = pd.read_csv('/Users/paramanandbhat/Downloads/Non_personalisedrecommendersystemsinpython-201024-234034 (1)/user_demographics.csv')

#Reading ratings file:
ratings= pd.read_csv('/Users/paramanandbhat/Downloads/Non_personalisedrecommendersystemsinpython-201024-234034 (1)/ratings.csv')

#Reading items file:
movie_info = pd.read_csv('/Users/paramanandbhat/Downloads/Non_personalisedrecommendersystemsinpython-201024-234034 (1)/movie_info.csv')

#Users, Ratings and movie_info are now loaded

### Exploring user data
# shape of the users data
print(users.shape)
# view the users data
print(users.head())

print(pd.isnull(users).sum())

### Exploring ratings data
# shape of the data
print(ratings.shape)
# view the ratings data
print(ratings.head())

df_ratings = ratings[(ratings['user_id'] == 1)&(ratings['movie_id'] == 100)]

print(df_ratings)

print(pd.isnull(ratings).sum())

### Exploring Movie Information data
# shape of the data
print(movie_info.shape)
# view the items file
print(movie_info.head())

# Check missing values in movie information
pd.isnull(movie_info).sum()

df_null_movie_info = pd.isnull(movie_info).sum()


print(df_null_movie_info)

