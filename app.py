import streamlit as st
import pandas as pd
from backend import add_expense, get_expenses, delete_expense, clear_expenses
from database import create_table
from utils import convert_to_dataframe, calculate_total

# Initialize DB
create_table()

st.set_page_config(page_title="Expense Tracker", page_icon="💰", layout="wide")

st.title("💰 Expense Tracker Dashboard")

col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("➕ Add Expense")

    with st.form("expense_form"):
        title = st.text_input("Title")
        amount = st.number_input("Amount", min_value=0.0, step=0.01)
        category = st.selectbox("Category",["Food", "Travel", "Shopping", "Groceries", "Entertainment", "Other"])

        submit = st.form_submit_button("Add")

        if submit:
            if title.strip() and amount > 0:
                add_expense(title, amount, category)
                st.success("Expense added ✅")
                st.rerun()
            else:
                st.error("Enter valid details")

with col2:
    st.subheader("📊 Expenses Overview")

    data = get_expenses()
    df = convert_to_dataframe(data)

    total = calculate_total(df)
    st.metric("Total Spending", f"₹{total:.2f}")

    if not df.empty:
        st.dataframe(df, use_container_width=True)

        # Filter
        category_filter = st.selectbox("Filter by Category",["All"] + list(df["Category"].unique()))

        if category_filter != "All":
            filtered_df = df[df["Category"] == category_filter]
            st.dataframe(filtered_df)

        # Delete option
        st.subheader("🗑 Delete Expense")
        expense_id = st.number_input("Enter Expense ID", min_value=1, step=1)

        if st.button("Delete"):
            delete_expense(expense_id)
            st.warning("Expense deleted")
            st.rerun()

        # Clear all
        if st.button("Clear All"):
            clear_expenses()
            st.error("All expenses cleared")
            st.rerun()

    else:
        st.info("No expenses added yet")