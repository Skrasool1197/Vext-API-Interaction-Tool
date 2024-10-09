import requests
import streamlit as st

# Set up Streamlit page config
st.set_page_config(
    page_title="Vext API Query Interface",
    page_icon="💡",
    layout="centered",
)

st.markdown(
    """
    <style>
    body {
        background-color: #f7f7f7;
    }
    .stTextInput input, .stTextArea textarea {
        background-color: #e9ecef;
        border-radius: 8px;
        border: 1px solid #ced4da;
        font-size: 16px;
        padding: 10px;
        color: #495057;
    }
    .stTextInput label, .stTextArea label {
        font-weight: bold;
        font-size: 16px;
        color: #343a40;
    }
    .stButton button {
        background-color: #28a745; /* Green background */
        color: white;
        font-size: 18px;
        padding: 12px 20px; /* More padding */
        border-radius: 10px; /* Rounded corners */
        border: none; /* Remove border */
        width: 100%; /* Full width */
        transition: background-color 0.3s, transform 0.3s; /* Smooth transitions */
    }
    .stButton button:hover {
        background-color: #218838; /* Darker green on hover */
        color: white;
        transform: scale(1.05); /* Slightly enlarge on hover */
    }
    .stTextInput, .stTextArea {
        margin-bottom: 20px;
    }
    .title {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        text-align: center;
        font-size: 2.5rem;
        color: #333;
        padding-bottom: 20px;
    }
    .description {
        text-align: center;
        font-size: 1.2rem;
        color: #555; /* Softer color for description */
        padding-bottom: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Page title
st.markdown('<div class="title"><strong>Vext API Query Interface 💬</strong></div>', unsafe_allow_html=True)
st.markdown('<div class="description"><strong>Easily interact with research papers by entering the paper name, query, and API key.</strong></div>', unsafe_allow_html=True)

with st.form(key='query_form'):
    api_key = st.text_input("**Enter Vext API Key**", type="password", help="Your secret API key for authentication.")
    query = st.text_area("**Question here...**", help="Input the text query to send to the Vext API.", height=100)
    submit_button = st.form_submit_button(label="Submit Query")

# Function to call the API
def call_vext_api(api_key, query):
    headers = {
        'Content-Type': 'application/json',
        'Apikey': f'Api-Key {api_key}',
    }

    data = {
        'payload': query,
    }

    # URL and POST request
    url = 'https://payload.vextapp.com/hook/5A1RX1CNR0/catch/$(RS7)'
    response = requests.post(url=url, headers=headers, json=data)

    if response.status_code == 200:
        return response.json()
    else:
        return {"error": f"API request failed with status code {response.status_code}"}

if submit_button:
    if not api_key:
        st.error("API key is required.")
    elif not query:
        st.error("Query cannot be empty.")
    else:
        with st.spinner("Fetching response from Vext API..."):
            response_json = call_vext_api(api_key, query)
        
        if 'error' in response_json:
            st.error(response_json['error'])
        else:
            text_value = response_json.get('text', 'No text found in the response')
            st.success("API request successful!")
            st.write("**Response from API:**")
            st.info(text_value)

# Footer
st.markdown("<br><br><center><strong>Made by Rasool Shaikh</strong></center>", unsafe_allow_html=True)
