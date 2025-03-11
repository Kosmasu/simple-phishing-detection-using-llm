from pydantic import BaseModel

from conversations import Conversation
from llm import LLM


class PhishingEvaluation(BaseModel):
    is_phishing: bool
    confidence: float
    explanation: str


def evaluate_phishing(llm: LLM, text: str) -> PhishingEvaluation:
    convo = Conversation.from_system_message("""
    You are a security expert evaluating a text for phishing. You will provide the confidence in a float format where 1.0 is 100 percent confident about your decision and 0.0 is 0 percent confident. You will also provide a boolean value indicating whether you think the text is phishing or not. Finally, you will provide an explanation of why you think the text is or isn't phishing. The text you need to evaluate is:
    """.strip()).add_user_message(text)
    response = llm.parse(convo, PhishingEvaluation)
    print(f"{response=}")
    return response
