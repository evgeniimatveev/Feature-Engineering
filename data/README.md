# 📂 Datasets

| File | Rows × columns | Used by | Target |
|---|:-:|---|---|
| [`loan_applications.csv`](loan_applications.csv) | 50,000 × 17 | every notebook except pipeline v2 | `default` (28.8% of applications) |
| [`Housing.csv`](Housing.csv) | 545 × 13 | `data-preprocessing-pipeline-v2` | `price` |

## `loan_applications.csv`

`application_id`, `application_date`, `age`, `gender`, `education`, `occupation`, `employment_length`, `income`, `loan_amount`, `loan_term`, `interest_rate`, `monthly_payment`, `credit_score`, `existing_loans`, `previous_defaults`, `city`, `default`

**Missing values** (this is what the cleaning notebooks work on):

| Column | Missing | Share |
|---|--:|--:|
| `employment_length` | 7,160 | 14.3% |
| `income` | 2,445 | 4.9% |
| `credit_score` | 2,578 | 5.2% |
| `existing_loans` | 2,513 | 5.0% |

## `Housing.csv`

`price`, `area`, `bedrooms`, `bathrooms`, `stories`, `mainroad`, `guestroom`, `basement`, `hotwaterheating`, `airconditioning`, `parking`, `prefarea`, `furnishingstatus`. No missing values.

---

*Built by [Evgenii Matveev](https://github.com/evgeniimatveev) · Data Analyst / Analytics & MLOps Engineer*
