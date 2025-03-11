import pytest
from pydantic import ValidationError
from phishing import evaluate_phishing, PhishingEvaluation
from llm import LLM, LLMName

class MockLLM(LLM):
    def parse(self, convo, response_format):
        if "phishing" in convo.messages[-1].content.lower():
            return response_format(is_phishing=True, confidence=0.95, explanation="The text contains typical phishing language.")
        else:
            return response_format(is_phishing=False, confidence=0.90, explanation="The text does not contain phishing language.")

@pytest.fixture
def mock_llm():
    return MockLLM(LLMName.LLAMA_3_1_8B)

def test_evaluate_phishing_positive(mock_llm):
    text = "You have won a prize! Click here to claim. This is a phishing attempt."
    result = evaluate_phishing(mock_llm, text)
    assert result.is_phishing is True
    assert result.confidence == 0.95
    assert result.explanation == "The text contains typical phishing language."

def test_evaluate_phishing_negative(mock_llm):
    text = "Let's schedule a meeting for next week."
    result = evaluate_phishing(mock_llm, text)
    assert result.is_phishing is False
    assert result.confidence == 0.90
    assert result.explanation == "The text does not contain phishing language."