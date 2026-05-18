import streamlit as st
import requests

st.title("💳 Fraud Detection System")

amount = st.number_input("Transaction Amount")

hour = st.number_input(
    "Hour (0-23)",
    min_value=0,
    max_value=23
)

features = {}

for i in range(1, 29):
    features[f"V{i}"] = st.number_input(f"V{i}")

if st.button("Check Fraud"):

    payload = {
        **features,
        "Amount": amount,
        "Hour": hour
    }

    res = requests.post(
        "http://127.0.0.1:8000/predict",
        json=payload
    )

    if res.status_code == 200:

        data = res.json()

        st.subheader("Result")

        st.write(f"Fraud Probability: {data['fraud_probability']}")
        st.write(f"Risk Level: {data['risk_level']}")
        st.write(f"Verdict: {data['verdict']}")

        if data['risk_level'] == "HIGH":
            st.error("🚨 High Risk Transaction")
        else:
            st.success("✅ Safe Transaction")

    else:
        st.write(res.text)