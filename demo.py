import streamlit as st
import yaml
from yaml.loader import SafeLoader
import streamlit_authenticator as stauth

secrets_dict = {key: dict(value) for key, value in st.secrets.items()}

authenticator = stauth.Authenticate(
    secrets_dict['credentials'],
    secrets_dict['cookie']['name'],
    secrets_dict['cookie']['key'],
    secrets_dict['cookie']['expiry_days'],
)

# Interface de connexion
try:
    authenticator.login()
except Exception as e:
    st.error(e)

if st.session_state['authentication_status']:
    authenticator.logout()
    #st.write(f'Welcome *{st.session_state["name"]}*')
    st.title('Some content')
elif st.session_state['authentication_status'] is False:
    st.error('Username/password is incorrect')
elif st.session_state['authentication_status'] is None:
    st.warning('Please enter your username and password')