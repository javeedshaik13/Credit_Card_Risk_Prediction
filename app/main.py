import streamlit as st
from prediction_helper import predict

st.set_page_config(page_title="Shaik's Finance: Credit Risk Modelling", page_icon="📊", layout="centered")



st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)),
                    url("https://i.pinimg.com/1200x/7a/6d/ba/7a6dbaf73f961ab38340f349dfea590b.jpg");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
        color: white;
    }

    .form-box {
        background-color: rgba(0, 0, 0, 0.55);
        padding: 2rem;
        border-radius: 1rem;
        box-shadow: 0 0 30px rgba(0,0,0,0.4);
    }

    label, .stTextInput > div > input, .stNumberInput > div > input, .stSelectbox > div > div {
        color: white !important;
    }

    .stSelectbox label, .stNumberInput label {
        font-weight: bold;
        color: #f0f0f0 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("<h1 style='text-align: center;'>Shaik's Finance: Credit Risk Modelling</h1>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

with st.container():
    st.markdown('<div class="form-box">', unsafe_allow_html=True)

    st.subheader("Enter the following details to calculate credit risk:")

    row1 = st.columns(3)
    row2 = st.columns(3)
    row3 = st.columns(3)
    row4 = st.columns(3)

    with row1[0]:
        age = st.number_input('Age (18–100)', min_value=18, max_value=100, step=1, value=28)
        st.caption("Enter your current age.")

    with row1[1]:
        income = st.number_input('Annual Income (₹)', min_value=0, value=1200000)
        st.caption("Gross income per year.")

    with row1[2]:
        loan_amount = st.number_input('Loan Amount (₹)', min_value=0, value=2560000)
        st.caption("Total amount you are applying for.")

    loan_to_income_ratio = loan_amount / income if income > 0 else 0.0

    with row2[0]:
        st.number_input(
            "Loan to Income Ratio (₹)",
            value=float(f"{loan_to_income_ratio:.2f}"),
            format="%.2f",
            disabled=True
        )
        st.caption("Indicates loan burden relative to your income.")

    with row2[1]:
        loan_tenure_months = st.number_input('Loan Tenure (Months)', min_value=0, step=1, value=36)
        st.caption("Number of months to repay the loan.")

    with row2[2]:
        avg_dpd_per_delinquency = st.number_input('Average DPD (0–90)', min_value=0, max_value=90, value=20)
        st.caption("Avg days of delay in repayments.")

    with row3[0]:
        delinquency_ratio = st.number_input('Delinquency Ratio (%) (0–100)', min_value=0, max_value=100, step=1, value=30)
        st.caption("Percentage of delinquent loans in your profile.")

    with row3[1]:
        credit_utilization_ratio = st.number_input('Credit Utilization Ratio (%) (0–100)', min_value=0, max_value=100, step=1, value=30)
        st.caption("How much credit you’re using out of total available.")

    with row3[2]:
        num_open_accounts = st.number_input('Open Loan Accounts (1–4)', min_value=1, max_value=4, step=1, value=2)
        st.caption("Number of currently active loan accounts.")

    with row4[0]:
        residence_type = st.selectbox('Residence Type', ['Owned', 'Rented', 'Mortgage'])
        st.caption("Type of your current residence.")

    with row4[1]:
        loan_purpose = st.selectbox('Loan Purpose', ['Education', 'Home', 'Auto', 'Personal'])
        st.caption("Reason for the loan.")

    with row4[2]:
        loan_type = st.selectbox('Loan Type', ['Unsecured', 'Secured'])
        st.caption("Secured loans have collateral; unsecured don’t.")

    st.subheader("Submit your details to calculate credit risk:")
    st.write("Click the button below to get your credit risk prediction.")

    if st.button('Calculate Risk'):
        probability, credit_score, rating = predict(
            age, income, loan_amount, loan_tenure_months, avg_dpd_per_delinquency,
            delinquency_ratio, credit_utilization_ratio, num_open_accounts,
            residence_type, loan_purpose, loan_type
        )

        st.subheader("Credit Risk Prediction Results:")
        st.write(f"🔁 **Default Probability**: `{probability:.2%}`")
        st.write(f"📉 **Credit Score**: `{credit_score}`")
        st.write(f"📊 **Rating**: `{rating}`")

        if probability < 0.3:
            st.balloons()
            st.success("✅ Congratulations! Low risk detected. 🎉")
        else:
            st.error("⚠️ Warning: High risk detected. 😢")
            st.info("💡 Consider improving your credit profile for better loan approval chances.")

    st.markdown('</div>', unsafe_allow_html=True)
