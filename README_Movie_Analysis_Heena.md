# 🎬 Movie Revenue & Rating Analysis (IMDb Dataset)

This project analyzes the top 1000 IMDb movies dataset to uncover trends related to movie revenue, genre, and ratings. It demonstrates how to clean, group, and visualize data using Python, pandas, and matplotlib/seaborn.

---

## 🎯 Objective

- Analyze how genres influence box office gross
- Understand the relationship between IMDb rating and revenue
- Identify which years or genres perform best on average

---

## 📁 Dataset

**Source**: [IMDb Top 1000 Movies Dataset – Kaggle](https://www.kaggle.com/datasets/PromptCloudHQ/imdb-data)  
**File Used**: `IMDb Top 1000.csv`

---

## 🛠 Tools & Technologies

- Python 3.12
- pandas for data manipulation
- seaborn and matplotlib for visualization

---

## 📊 Key Steps & Insights

- Cleaned columns like `Gross`, `Genre`, and `Year`
- Converted currency strings to numeric
- Extracted the year using regex
- Grouped data by genre and exploded combinations
- Visualized top genres and revenue distribution

---

## ▶️ How to Run

1. Install dependencies:
```bash
pip install pandas matplotlib seaborn
```

2. Run the script:
```bash
python movie_analysis.py
```

---

## 🔍 Sample Output

- Top 10 Genres by Average Gross:
  - Action
  - Adventure
  - Animation
  - Sci-Fi
  - Comedy

- Visuals:
  - Bar chart of top genres
  - Scatter plot: IMDb Rating vs Gross
  - Histogram: Distribution of Ratings

---

## 📂 Project Structure

```
movie-analysis-project/
├── IMDb Top 1000.csv
├── movie_analysis.py
└── README.md
```

---

## 🙋‍♀️ About Me

**Heena Khan**  
📌 Educator turned data analyst  
📧 heenakhan8386@gmail.com  
🔗 [GitHub Profile](https://github.com/Heena84)  
🔗 [LinkedIn](https://www.linkedin.com)

---

⭐ If you liked this project, feel free to star it and connect on LinkedIn!