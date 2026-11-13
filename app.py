import streamlit as st

st.title("House Price Estimator")
st.write("Enter the size of the house to get an estimated price.")

# 1. An input box where the user can type a number
sqft = st.number_input("House Size (Square Feet)", min_value=500, max_value=10000, value=1500)

# 2. The trigger button
if st.button("Estimate Price"):
    
    # 3. The "Fake" ML Model 
    # (Pretends to calculate: $200 per square foot + a $50,000 base price)
    predicted_price = (sqft * 200) + 50000
    
    # 4. Show the result in a green box, formatted with commas for thousands
    st.success(f"Estimated Price: ${predicted_price:,}")