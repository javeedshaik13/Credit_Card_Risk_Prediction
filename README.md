# Credit_Card_Risk_Prediction
A machine learning project to predict credit card default risk using customer data. Includes data preprocessing, model training (Logistic Regression, Random Forest, XGBoost), evaluation metrics, and an Streamlit app for real-time predictions



# 📊 Shaik's Finance: Credit Risk Modelling

Project Type: Web App (Machine Learning + Streamlit)

A sleek, interactive web application built using **Streamlit** for predicting **credit default risk**. Powered by machine learning, this app allows users to input key financial and demographic details to assess the probability of loan default, get a credit score, and receive a credit rating.

---

![Credit risk modelling](assets/credit-risk-ui.png)

## 🚀 Features

- 🌐 Responsive UI for desktop and mobile
- 🔒 Predicts **default probability**
- 📈 Calculates **credit score (300–900)**
- ✅ Gives a **rating**: Poor / Average / Good / Excellent
- 🎯 Streamlit-based frontend with a visually appealing background
- 🧠 ML Model powered by `sklearn` and `joblib`

---

## 🧰 Technologies Used

- Streamlit
- Python
- Scikit-learn
- NumPy, Pandas
- Joblib

---
# 📥 Input Fields for Credit Risk Modelling App

This document lists all user inputs used in the application UI, including field names, input types, valid ranges, and their descriptions.

| Field Name                 | Label in UI                             | Input Type     | Allowed Values / Range        | Description                                      |
|---------------------------|------------------------------------------|----------------|-------------------------------|--------------------------------------------------|
| `age`                     | Age (18–100)                             | number_input   | 18 – 100                      | Applicant’s age in years                        |
| `income`                  | Annual Income (₹)                        | number_input   | ≥ 0                           | Gross annual income                             |
| `loan_amount`             | Loan Amount (₹)                          | number_input   | ≥ 0                           | Amount requested for the loan                   |
| `loan_to_income_ratio`    | Loan to Income Ratio (Auto-calculated)  | number_input   | Auto-calculated, disabled     | Computed as loan_amount / income                |
| `loan_tenure_months`      | Loan Tenure (Months)                     | number_input   | ≥ 0                           | Duration of loan in months                      |
| `avg_dpd_per_delinquency` | Average DPD (0–90)                       | number_input   | 0 – 90                        | Average number of days payment is overdue       |
| `delinquency_ratio`       | Delinquency Ratio (%) (0–100)           | number_input   | 0 – 100                       | % of delinquent accounts in credit history      |
| `credit_utilization_ratio`| Credit Utilization Ratio (%) (0–100)    | number_input   | 0 – 100                       | % of credit being used relative to available    |
| `num_open_accounts`       | Open Loan Accounts (1–4)                | number_input   | 1 – 4                         | Number of active/open loan accounts             |
| `residence_type`          | Residence Type                          | selectbox      | Owned / Rented / Mortgage     | Type of housing owned/occupied                  |
| `loan_purpose`            | Loan Purpose                            | selectbox      | Education / Home / Auto / Personal | Reason for the loan                      |
| `loan_type`               | Loan Type                               | selectbox      | Secured / Unsecured           | Indicates if loan is backed by collateral       |

## 🛠️ How to Run Locally

1. **Clone this repository**
   ```bash```
   git clone https://github.com/yourusername/Credit_Card_Risk_Prediction.git
   cd Credit_Card_Risk_Prediction
2.**Install requirements**
   ```bash```
   pip install -r requirements.txt
3.**Run the application**
   ```bash```
   streamlit run app.py

   
