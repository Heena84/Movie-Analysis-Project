import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv("IMDB-Movie-Data.csv")

print(df.shape)
print(df.columns)
print(df.head)

# Check for missing values
print(df.isnull().sum())

# Drop rows with missing gross or rating
df = df.dropna(subset=['Rating', 'Gross'])

# Convert 'Gross' column (which has $ and commas) to numeric
df['Gross'] = df['Gross'].replace(r'[\$,]', '', regex=True).astype(float)

df.groupby('Genre')['Gross'].mean().sort_values(ascending=False)

#Which genre earns the most?
df.groupby('Genre')['Gross'].mean().sort_values(ascending=False)

#Do higher-rated movies earn more?
sns.scatterplot(x='Rating', y='Gross', data=df)
plt.title('Rating vs Gross Income')
plt.show()

#Which year had the highest average earnings?
df['Year'] = df['Year'].astype(str).str.extract(r'(\d{4})').astype(int)
df.groupby('Year')['Gross'].mean().sort_values(ascending=False).head(10)

# Top 10 earning genres
top_genres = df.groupby('Genre')['Gross'].mean().sort_values(ascending=False).head(15)
top_genres.plot(kind='bar', title='Top 10 Genres by Avg Gross', ylabel='Gross ($)', figsize=(15,5))
plt.show()

# Rating distribution
sns.histplot(df['Rating'], bins=20, kde=True)
plt.title('Distribution of IMDB Ratings')
plt.show()


# Split the Genre column into lists
df['Genre'] = df['Genre'].astype(str)  # Ensure it's string
df['Genre'] = df['Genre'].str.split(',')

# Explode the lists into separate rows
df_exploded = df.explode('Genre')

# Now group by individual genre
top_genres = df_exploded.groupby('Genre')['Gross'].mean().sort_values(ascending=False).head(20)

# Plot again
top_genres.plot(kind='bar', title='Top 20 Genres by Avg Gross (Separated)', ylabel='Gross ($)', figsize=(20,5))
plt.show()

