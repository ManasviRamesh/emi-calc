import streamlit as st 
def calculated_emi(principal , n , r):
	emi = principal * (r/100) * (1+r/100)**2 / ((1+r/100)**2)-1
	sround(emi,3)
	return emi 

st.title('App to calculate emi')
principal = st.slider('Principal loan amount' , 1000,1000000)
tenure = st.slider('Loan period (in years)' , 1,30)
roi = st.slider('Rate of interest' , 1,15)
n = tenure*12
r = roi/12
if st.button('EMI'):
	st.write('The calculated emi is ' , calculated_emi(principal , n , r))