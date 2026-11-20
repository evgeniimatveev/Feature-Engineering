# 🎯 Section 4: Preprocessing Pipelines

Bonus: everything from the earlier sections wrapped into one reusable `preprocess_data()` function. Version 2 adds outlier handling, a log transform and feature selection.

> 📂 The notebooks read their data from `../data/`, so open them from this folder in Jupyter (the default) and everything resolves.

| # | Notebook | What it covers | Dataset |
|:-:|----------|----------------|---------|
| 1 | [`data-preprocessing-pipeline-v1.ipynb`](data-preprocessing-pipeline-v1.ipynb) | Load, impute, encode categoricals and scale numerics in one function (loan data) | `data/loan_applications.csv` |
| 2 | [`data-preprocessing-pipeline-v2.ipynb`](data-preprocessing-pipeline-v2.ipynb) | Adds outlier handling, log transform, `RobustScaler` and feature selection by variance threshold and VIF (housing data) | `data/Housing.csv` |

---

[← Advanced Feature Engineering](../03-advanced-feature-engineering/) &nbsp;·&nbsp; [Datasets →](../data/)

*Built by [Evgenii Matveev](https://github.com/evgeniimatveev) · Data Analyst / Analytics & MLOps Engineer*
