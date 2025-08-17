import streamlit as st
import chatbot as demo

# set the title and description https://docs.streamlit.io/library/api-reference/layout/st.title
st.title("Chatbot Demo")

# langchain memory to the session state session state - https://docs.streamlit.io/library/api-reference/session-state
if 'memory' not in st.session_state:
    st.session_state.memory = demo.demo_memory()

# add the UI chat history to the session state https://docs.streamlit.io/library/api-reference/session-state#session-state-chat-history
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []


for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["text"])

# input text box for user input
if prompt := st.chat_input("Ask a question:"):
    # add user message to chat history
    st.session_state.chat_history.append({"role": "user", "text": prompt})

    # display user message in the chat
    with st.chat_message("user"):
        st.markdown(prompt)

    # invoke the conversation chain with the input text and memory
    response = demo.demo_conversation_chain(input_text=prompt, memory=st.session_state.memory)

    # add bot response to chat history
    st.session_state.chat_history.append({"role": "assistant", "text": response})

    # display bot response in the chat
    with st.chat_message("assistant"):
        st.markdown(response)