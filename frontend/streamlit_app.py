import streamlit as st
import requests

st.set_page_config(page_title="College Chatbot", layout="centered")

st.title("🎓 Smart College Chatbot")
query = st.text_input("Ask something about your college")

if st.button("Ask"):
    with st.spinner("Thinking..."):
        try:
            # Send your question as JSON
            res = requests.post("http://localhost:5000/ask", json={"question": query})
            res.raise_for_status()

            # Get the answer from JSON response
            answer = res.json().get("answer")
            if answer:
                st.write("🤖 " + answer)
            else:
                st.error("❌ No 'answer' in response: " + str(res.json()))

        except requests.exceptions.RequestException as e:
            st.error(f"❌ Request failed: {e}")

        except ValueError:
            st.error(f"❌ Failed to parse JSON. Status: {res.status_code}, Text: {res.text}")
