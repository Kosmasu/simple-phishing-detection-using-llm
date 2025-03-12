from pydantic import BaseModel

from conversations import Conversation
from llm import LLM


class PhishingEvaluation(BaseModel):
    explanation: str
    confidence: float
    is_phishing: bool


def evaluate_phishing(llm: LLM, text: str) -> PhishingEvaluation:
    convo = Conversation.from_system_message("""
    You are a security expert evaluating a text for phishing. You will provide an explanation of why you think the text is or isn't phishing. You will provide the confidence in a float format where 1.0 is very confident about your decision and 0.0 is not confident at all. You will also provide a boolean value indicating whether you think the text is phishing or not where 1 is phishing and 0 is not phishing. The text you need to evaluate is:
    """.strip()).add_user_message(text)
    response = llm.parse(convo, PhishingEvaluation)
    # print(f"{text=}")
    # print(f"{response=}")
    return response

def evaluate_phishing_finetuned(llm: LLM, text: str) -> bool:
    convo = Conversation.from_user_message(f"""
    Below is a string of text. The text could be one of:
    1. URL
    2. SMS messages
    3. Email messages
    4. HTML code

    Determine if the text is phishing or safe! Return a label of "1" if the text is phishing. Return a label of "0" if the text is safe.

    ### Text:
    {text}

    ### Label:
    """)
    response = llm.generate(convo)
    return bool(int(response.strip()))