import pandas as pd
import numpy as np


#1.# Load datasets
users = pd.read_csv('/Users/paramanandbhat/Downloads/Non_personalisedrecommendersystemsinpython-201024-234034 (1)/user_demographics.csv')

#Reading ratings file:
ratings= pd.read_csv('/Users/paramanandbhat/Downloads/Non_personalisedrecommendersystemsinpython-201024-234034 (1)/ratings.csv')

#Reading items file:
movie_info = pd.read_csv('/Users/paramanandbhat/Downloads/Non_personalisedrecommendersystemsinpython-201024-234034 (1)/movie_info.csv')

#2.Basic exploration of user data
print("Users Data Shape:", users.shape)
print("First 5 rows of Users Data:\n", users.head())
print("Missing Values in Users Data:\n", pd.isnull(users).sum())

# 3.Basic exploration of ratings data
print("Ratings Data Shape:", ratings.shape)
print("First 5 rows of Ratings Data:\n", ratings.head())
print("Missing Values in Ratings Data:\n", pd.isnull(ratings).sum())

#4 Basic exploration of movie information data
print("Movie Information Data Shape:", movie_info.shape)
print("First 5 rows of Movie Information Data:\n", movie_info.head())
print("Missing Values in Movie Information Data:\n", pd.isnull(movie_info).sum())

# 5.Merge movie information with ratings data
ratings = ratings.merge(movie_info[['movie id','movie title']], left_on='movie_id', right_on='movie id')
ratings['movie'] = ratings['movie_id'].astype(str) + ": " + ratings['movie title']

print(ratings['movie'])

# Drop unnecessary columns
ratings.drop(['movie id', 'movie title', 'movie_id', 'unix_timestamp'], axis=1, inplace=True)
ratings = ratings[['user_id', 'movie', 'rating']]

print(ratings.describe())

print(ratings.head())

# Filter movies with at least 100 ratings
movie_counts = ratings['movie'].value_counts()
ratings = ratings[ratings['movie'].isin(movie_counts.index[movie_counts >= 100])]

# Create user-movie matrix
# Add the gender information from the users DataFrame to the user_movie_matrix
users['sex'] = users.set_index('user_id')['sex']
print(users.head())


# Merge user demographics with ratings
ratings = ratings.merge(users[['user_id', 'sex']], on='user_id')
ratings = ratings[['user_id', 'sex', 'movie', 'rating']]

# Non-personalized recommender systems using average ratings
top_avg_ratings = users.mean().sort_values(ascending=False).head(5)
print("Top 5 Movies by Average Rating:\n", top_avg_ratings)

# Non-personalized recommender systems using rating count
top_rating_counts = users.count().sort_values(ascending=False).head(5)
print("Top 5 Movies by Rating Count:\n", top_rating_counts)

# Non-personalized recommender systems using count of ratings 4 and above
ratings_4_above = users[users >= 4].count() / users.count()
top_ratings_4_above = ratings_4_above.sort_values(ascending=False).head(5)
print("Top 5 Movies by Count of Ratings 4 and Above:\n", top_ratings_4_above)

# Weak personalization using gender information
# Calculate the difference in average ratings between male and female users for each movie
users['sex'] = users['sex']
# Ensure the matrix only contains numeric values (ratings) and 'sex' column
user_movie_matrix = users.apply(pd.to_numeric, errors='coerce')

# Create separate DataFrames for male and female users
df_m = user_movie_matrix[user_movie_matrix['sex'] == 'M'].drop('sex', axis=1)
df_f = user_movie_matrix[user_movie_matrix['sex'] == 'F'].drop('sex', axis=1)

# Calculate the mean ratings for each movie by male and female users, handling NaN values appropriately
mean_ratings_m = df_m.mean(axis=0, skipna=True)
mean_ratings_f = df_f.mean(axis=0, skipna=True)

# Calculate the difference in mean ratings between genders
gender_diff = mean_ratings_f.subtract(mean_ratings_m)

# Sort the differences and print the top 5 movies with the largest difference
top_gender_diff = gender_diff.sort_values(ascending=False).head(5)
print("Top 5 Movies with the Largest Difference in Average Ratings Between Genders:\n", top_gender_diff)