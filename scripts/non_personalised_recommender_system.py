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

'''
This dataset contains attributes of 1682 movies. 
There are 24 columns out of which last 19 columns specify 
the genre of a particular movie. These are binary columns, 
i.e., a value of 1 denotes that the movie belongs to that genre, 
and 0 otherwise.

We have release date missing for only 1 movie in the
 dataset and rest of the variables do not 
 have any missing value
'''

## 3.  Merging Movie information to ratings dataframe 
'''
The movie names are contained in a separate file. 
Let's merge that data with ratings and store it in ratings dataframe.
The idea is to bring movie title information in ratings dataframe as 
it would be useful later on
'''
ratings = ratings.merge(movie_info[['movie id','movie title']], how='left', left_on = 'movie_id', right_on = 'movie id')

print(ratings.head())
'''
Lets also combine movie id and movie title separated by ': ' and store it in a new column named movie
'''

ratings['movie'] = ratings['movie_id'].map(str) + str(': ') + ratings['movie title'].map(str)


print(ratings.columns)

ratings = ratings.drop(['movie id', 'movie title', 'movie_id','unix_timestamp'], axis = 1)

ratings = ratings[['user_id','movie','rating']]

'''
For using non personalised recommender systems we are only interested in popular movies so we keep movies with atleast 100 ratings in the dataframe and drop the rest

'''
movie_counts = ratings['movie'].value_counts()
ratings = ratings[(ratings['movie'].isin(movie_counts[movie_counts >= 100].index))]

'''
Next, we create a user item matrix using Pandas Pivot Function such that users are in the index and each movie is represented by a separate column**
- Merge user data with ratings data
- Create user movie matrix using user ids as rows and movies as columns & name it 'user_movie_matrix'
'''

n_users = ratings.user_id.unique().shape[0]
n_items = ratings.movie.unique().shape[0]

print(n_users,n_items)

user_movie_matrix = ratings.pivot(index = 'user_id', columns = 'movie', values = 'rating')

print(user_movie_matrix)

ratings = ratings.merge(users[['user_id','sex']], how = 'left', on = 'user_id')
ratings = ratings[['user_id','sex','movie','rating']]


