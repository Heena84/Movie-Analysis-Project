# 🎬 Movie Revenue & Rating Analysis

## 📌 Project Overview

This project analyzes IMDb movie data to uncover insights about movie ratings, genres, and revenue performance using Python.

The objective is to understand:

- Which genres generate the highest revenue
- Whether highly-rated movies earn more revenue
- Revenue trends across different movie categories
- Distribution of movie ratings

This project demonstrates data cleaning, exploratory data analysis (EDA), data visualization, and business insight generation using Python.

---

## 🎯 Business Problem

Movie production companies invest millions of dollars into films.

This analysis helps answer:

- Which genres are most profitable?
- Do higher IMDb ratings lead to higher revenue?
- Which movie categories should studios focus on?

---

## 📂 Dataset

Dataset Source:

https://www.kaggle.com/datasets/PromptCloudHQ/imdb-data

File Used:

`movie_metadata.csv`

Dataset contains information such as:

- Movie Title
- Genre
- Year
- Director
- IMDb Rating
- Revenue (Millions)
- Runtime
- Votes

---

## 🛠️ Tools & Technologies Used

### Programming Language
- Python

### Libraries
- Pandas
- NumPy
- Matplotlib
- Seaborn

### IDE
- Visual Studio Code

### Version Control
- Git
- GitHub

---

## 📚 Skills Demonstrated

### Data Cleaning
- Handling missing values
- Removing null records
- Converting data types

### Data Analysis
- GroupBy Operations
- Aggregations
- Sorting
- Filtering

### Data Visualization
- Bar Charts
- Histograms
- Scatter Plots

### Business Insights
- Revenue Analysis
- Genre Performance Analysis
- Rating Trends

---

# 📋 Project Workflow

## Step 1: Import Libraries

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
```

---

## Step 2: Load Dataset

```python
df = pd.read_csv("movie_metadata.csv")
```

---

## Step 3: Explore Data

```python
print(df.head())
print(df.info())
print(df.describe())
```

---

## Step 4: Handle Missing Values

```python
df = df.dropna(subset=['Revenue (Millions)'])
```

---

## Step 5: Revenue Analysis by Genre

```python
avg_revenue = df.groupby('Genre')['Revenue (Millions)'].mean()
```

---

## Step 6: Create Visualizations

### Top Genres by Average Revenue

```python
top_genres = df.groupby('Genre')['Revenue (Millions)'].mean().sort_values(ascending=False).head(10)

top_genres.plot(
    kind='bar',
    figsize=(10,5),
    title='Top 10 Genres by Average Revenue'
)

plt.show()
```

---

### IMDb Rating Distribution

```python
sns.histplot(df['Rating'], bins=20)
plt.title('IMDb Rating Distribution')
plt.show()
```

---

### Rating vs Revenue

```python
sns.scatterplot(
    x='Rating',
    y='Revenue (Millions)',
    data=df
)

plt.title('Rating vs Revenue')
plt.show()
```

---

# 📊 Key Findings

### 1. Revenue Differs Significantly Across Genres

Some genres consistently generate higher average revenue than others.

---

### 2. High Ratings Do Not Always Mean High Revenue

Several highly-rated movies generated moderate revenue while some lower-rated movies generated substantial revenue.

---

### 3. Revenue Distribution Is Highly Skewed

A small number of blockbuster movies contribute disproportionately to total revenue.

---

### 4. Genre Plays a Major Role

Action, Adventure, Animation, and Sci-Fi genres tend to perform strongly in terms of revenue.

---

# 📈 Sample Visualizations

### Top 10 Genres by Average Revenue

- Bar Chart

### IMDb Rating Distribution

- Histogram

### Rating vs Revenue

- Scatter Plot

---

# 📁 Project Structure

```text
Movie-Analysis-Project/
│
├── movie_analysis.py
├── movie_metadata.csv
├── README.md
│
└── output_images/
     ├── top_genres.png
     ├── rating_distribution.png
     └── rating_vs_revenue.png
```

---

# 🚀 How to Run This Project

### Clone Repository

```bash
git clone https://github.com/Heena84/movie-analysis-project.git
```

### Install Libraries

```bash
pip install pandas matplotlib seaborn
```

### Run Project

```bash
python movie_analysis.py
```

---

# 💡 Future Improvements

- Build interactive dashboard using Streamlit
- Create Tableau Dashboard
- Add Machine Learning model to predict movie revenue
- Deploy project online

---

# 👩‍💻 Author

### Heena Khan

Educator transitioning into Data Analytics.

### Connect With Me

GitHub:
https://github.com/Heena84

LinkedIn:
https://www.linkedin.com/in/your-linkedin-profile

Email:
heenakhan8386@gmail.com

---

## ⭐ If you found this project useful, please give it a star on GitHub.
