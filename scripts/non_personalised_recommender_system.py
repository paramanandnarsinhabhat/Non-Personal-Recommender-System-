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

 ## 3.  Merging Movie information to ratings dataframe 
'''
Currently movie and ratings are different dartaframes.
As we need info on movie and rating, we will bw merging these 2 dataframes
'''

ratings = ratings.merge(movie_info[['movie id','movie title']], how='left', left_on = 'movie_id', right_on = 'movie id')

print(ratings.head())

ratings['movie'] = ratings['movie_id'].map(str) + str(': ') + ratings['movie title'].map(str)

df_movie = ratings['movie']

print(df_movie)

print(ratings.columns)

#We are only interested in user , movie , and rating
ratings = ratings.drop(['movie id', 'movie title', 'movie_id','unix_timestamp'], axis = 1)

ratings = ratings[['user_id','movie','rating']]

print(ratings)

movie_counts = ratings['movie'].value_counts()

print(movie_counts)

ratings = ratings[(ratings['movie'].isin(movie_counts[movie_counts >= 100].index))]

#We now have dataframe that has more than 100 reviews
n_users = ratings.user_id.unique().shape[0]
n_items = ratings.movie.unique().shape[0]

print(n_users,n_items)

user_movie_matrix = ratings.pivot(index = 'user_id', columns = 'movie', values = 'rating')

print(user_movie_matrix)


ratings = ratings.merge(users[['user_id','sex']], how = 'left', on = 'user_id')
ratings = ratings[['user_id','sex','movie','rating']]

print(ratings)


## 4. Non Personalised Recommender Systems using average ratings

df_nonreccomender_average = user_movie_matrix.mean(axis=0).sort_values(ascending=False).head(5)
print(df_nonreccomender_average)

## 5. Non Personalised Recommender Systems using number of ratings or rating count 

df_nonreccomender_count = user_movie_matrix.count(axis=0).sort_values(ascending=False).head(5)

print(df_nonreccomender_count)

## 6. Non Personalised Recommender Systems using count of ratings 4 and above 

df_apply = user_movie_matrix.apply(pd.value_counts)

print(df_apply)

df_four = user_movie_matrix.apply(lambda x: x[x>=4]).count(axis=0) / user_movie_matrix.apply(lambda x: x).count(axis=0)
df_four.sort_values(ascending = False).head(5)

print(df_four.sort_values(ascending = False).head(5))


## 7. Weak Personalisation using Gender Information
# Ensure all columns except 'sex' are numeric
# Assuming all other columns are movie ratings which should be numeric
for col in user_movie_matrix.columns:
    if col != 'sex':
        user_movie_matrix[col] = pd.to_numeric(user_movie_matrix[col], errors='coerce')

# Filter for male and female users
df_m = user_movie_matrix[user_movie_matrix['sex'] == 'M']
df_f = user_movie_matrix[user_movie_matrix['sex'] == 'F']







