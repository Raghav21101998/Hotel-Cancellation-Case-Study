import streamlit as st

st.title('CALCULATE YOUR BMI')
h = 1
wt =st.number_input('ENTER YOUR WEIGHT IN KGs:')
h =st.number_input('ENTER YOUR HEIGHT IN CM:')
if h==0:
    bmi=0
else:
    bmi = wt/h**2
st.success(f'YOUR BMI is {bmi} KG/cm2')




                