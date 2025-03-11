import streamlit as st

from conversations import Conversation
from llm import LLM, LLMName
from phishing import evaluate_phishing, PhishingEvaluation

st.title("Simple Phishing Detection using LLM")

if "llm" not in st.session_state:
    llm: LLM = LLM(model_name=LLMName.LLAMA_3_1_8B)
    st.session_state["llm"] = llm
else:
    llm: LLM = st.session_state.llm

if "convo" not in st.session_state:
    convo: Conversation = Conversation()
    st.session_state.convo = convo
else:
    convo: Conversation = st.session_state.convo

for message in convo.messages:
    with st.chat_message(message.role):
        st.markdown(message.content)

if user_message := st.chat_input("Type a message..."):
    convo.add_user_message(user_message)
    with st.chat_message("user"):
        st.markdown(user_message)

    phishing_evaluation: PhishingEvaluation = evaluate_phishing(
        llm, user_message)
    response = f"Phishing Evaluation:\n- Is Phishing: {phishing_evaluation.is_phishing}\n- Confidence: {phishing_evaluation.confidence:.2%}\n- Explanation: {phishing_evaluation.explanation}"

    with st.chat_message("assistant"):
        st.markdown(response)
    convo.add_assistant_message(response)
    st.session_state.convo = convo
