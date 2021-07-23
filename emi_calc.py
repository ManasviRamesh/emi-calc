import streamlit as st
def calculated_emi(principal , n , r):
	emi = principal * (r/100) * (1+r/100)**2 / ((1+r/100)**2)-1
	round(emi,3)
	return emi 

def outstanding_balance(principal , n , r , m):
	balance = (principal*((1 + r/100)**n) - ((1 + r/100)**m)) / (1 + r/100)**n - 1
	round(balance,3)
	return balance
st.title('App to calculate emi and outstanding balance')
principal = st.slider('Principal loan amount' , 1000,1000000)
tenure = st.slider('Loan period (in years)' , 1,30)
roi = st.slider('Rate of interest' , 1,15)
m = st.slider('Period after which the Outstanding Loan Balance is calculated (in months)' , 1-(tenure*12))
n = tenure*12
r = roi/12

if st.button('EMI'):
	st.write('The calculated emi is ' , calculated_emi(principal , n , r))


if st.button('OUTSTANDING BALANCE'):
	st.write('The outstanding balance is' , outstanding_balance(principal , n , r , m))
