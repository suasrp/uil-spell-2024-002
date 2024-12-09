import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader

# Load the credentials from the YAML file
with open("credentials.yaml", "r") as file:
    config = yaml.load(file, Loader=SafeLoader)

# Set up the authenticator
authenticator = stauth.Authenticate(
    config["credentials"]["users"],      # username-password pair from YAML
    config["cookie"]["key"],             # secret key for cookie encryption
    config["cookie"]["expiry_days"],     # cookie expiry duration
    config["preauthorized"]["email"]     # preauthorized emails
)

# Check if the user is authenticated
name, authentication_status, username = authenticator.login("Login", "main")

# If authenticated, show the app content
if authentication_status:
    st.title(f"Welcome {name}")
    st.write("You have successfully logged in!")

    # Optionally: Redirect to another URL after successful login
    # st.experimental_redirect("https://spulflaskt05df.vercel.app")  # Redirect to main app

elif authentication_status is False:
    st.error("Invalid username or password")

elif authentication_status is None:
    st.info("Please log in")

# Log out functionality
if st.button("Logout"):
    authenticator.logout("main")
    st.experimental_rerun()  # Re-run the app to go back to login page
