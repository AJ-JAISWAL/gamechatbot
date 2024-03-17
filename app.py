import streamlit as st
from sklearn.utils import all_estimators
import re

# App title
st.set_page_config(page_title="😎🧠 ScikitLearn Chatbot")

with st.sidebar:
    st.title('😎🧠 ScikitLearn Chatbot')
    st.write('This chatbot will provide the knowledge about Scikit Learn Models.')
    st.title('Names of all Sckit learn Model')
    st.write([name for name, _ in all_estimators()])

# Store LLM generated responses
if "messages" not in st.session_state.keys():
    st.session_state.messages = [{"role": "assistant", "content": "Write a model name to gain knowledge today?"}]

# Display or clear chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

def clear_chat_history():
    st.session_state.messages = [{"role": "assistant", "content": "Write a model name to gain knowledge today?"}]
st.sidebar.button('Clear Chat History', on_click=clear_chat_history)

# Function for generating Scikit Learn model response.
def get_sklearn_docs(estimator_name):
    for name, estimator_class in all_estimators():
        if name.lower() == estimator_name.lower():
            if hasattr(estimator_class, "__doc__"):
                return estimator_class.__doc__
    return False

def get_output(estimator_name):
  content=str(get_sklearn_docs(estimator_name))
  if content=="False":
      return "Invlid model Name 🤦‍♂️ Go to slidebar for models name in ScikitLearn."
  else:
      matches = re.search(r'Examples\s+(-+\s+.*?)\n\s*(?:[A-Z]|$)', content, re.DOTALL)
      examples_content = matches.group(1)
      return examples_content.strip()

# User-provided prompt
if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

# Generate a new response if last message is not from assistant
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = get_output(prompt)
            placeholder = st.empty()
            full_response = ''
            for item in response:
                full_response += item
                placeholder.markdown(full_response)
            placeholder.markdown(full_response)
    message = {"role": "assistant", "content": full_response}
    st.session_state.messages.append(message)
