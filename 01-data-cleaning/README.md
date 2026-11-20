# 🧹 Section 1: Data Cleaning

Where feature engineering starts: engineer a first feature and measure its effect, find and fix missing values, and detect outliers. All three notebooks work on the loan-applications dataset.

> 📂 The notebooks read their data from `../data/`, so open them from this folder in Jupyter (the default) and everything resolves.

| # | Notebook | What it covers | Dataset |
|:-:|----------|----------------|---------|
| 1 | [`feature-engineering-intro.ipynb`](feature-engineering-intro.ipynb) | Build a debt-to-income ratio, then compare model AUC on the original vs engineered features | `data/loan_applications.csv` |
| 2 | [`lecture-03-handling-missing-values.ipynb`](lecture-03-handling-missing-values.ipynb) | Visualize missing-value patterns with `missingno`, impute columns such as `employment_length` and `credit_score`, validate the imputation with KDE plots | `data/loan_applications.csv` |
| 3 | [`lecture-04-outlier-detection-iqr.ipynb`](lecture-04-outlier-detection-iqr.ipynb) | Outlier detection with the IQR method | `data/loan_applications.csv` |

---

[← Quickstart](../00-quickstart/) &nbsp;·&nbsp; [Feature Transformations →](../02-feature-transformations/)

*Built by [Evgenii Matveev](https://github.com/evgeniimatveev) · Data Analyst / Analytics & MLOps Engineer*
