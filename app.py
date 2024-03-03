from dotenv import load_dotenv
import google.generativeai as genai
import os
import streamlit as st

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))
model=genai.GenerativeModel(model_name="gemini-pro")
id=0

#Initialize messgaes and id
if "messages" not in st.session_state:
    st.session_state["messages"] = []
if "id" not in st.session_state:
    st.session_state["id"] = 0

#chat model
chat=model.start_chat(history=[])

#function to show the history
def show_history():
    for msg in st.session_state["messages"]:
        st.write(f"""{msg["user"]} : {msg["message"]}""")


def main():
    user_message = st.text_input("Enter your message:")
    if st.button("send"):
        id = st.session_state["id"] + 1
        st.session_state["id"] += 1

        #storing message from the user
        st.session_state["messages"].append(
                                            {"id":id,
                                             "user":"You",
                                             "message":user_message}
                                             )
        response=chat.send_message(user_message)

        #storing reply from the bot
        st.session_state["messages"].append(
                                        {"id":id+1,
                                         "user":"Bot",
                                         "message":response.text}
                                         )
        st.write(response.text)
    
    
    if st.button("Show history"):
        show_history()

if __name__ == "__main__":
    main()
    


    
    

