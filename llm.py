import enum
from typing import TypeVar
from openai import AsyncOpenAI, OpenAI, Stream
from openai.types.chat.chat_completion import ChatCompletion
from openai.types.chat.chat_completion_chunk import ChatCompletionChunk
from openai.types.chat.parsed_chat_completion import ParsedChatCompletion, ParsedChatCompletionMessage
from pydantic import BaseModel

from conversations import Conversation

T = TypeVar("T", bound=BaseModel)

client = OpenAI(
    base_url='http://localhost:11434/v1/',
    api_key='ollama',
)


class LLMName(str, enum.Enum):
    LLAMA_3_1_8B = "llama3.1"
    LLAMA_3_1_8B_FINETUNED = "hf.co/Kosmasu/llama3.1-8B-phishing-email-finetuned-gguf"


class LLM:
    def __init__(self, model_name: LLMName):
        self.model_name = model_name

    def stream(self, convo: Conversation):
        stream: Stream[ChatCompletionChunk] = client.chat.completions.create(
            model=self.model_name,
            messages=convo.to_openai_messages(),
            stream=True,
        )
        for chunk in stream:
            response: str | None = chunk.choices[0].delta.content
            if response:
                print(f"{response=}")
                yield response

    def generate(self, convo: Conversation) -> str:
        chat_completion: ChatCompletion = client.chat.completions.create(
            model=self.model_name,
            messages=convo.to_openai_messages(),
            stream=False,
        )
        response: str | None = chat_completion.choices[0].message.content
        print(f"{response=}")
        if not response:
            raise ValueError("Empty response from model")
        return response

    def parse(self, convo: Conversation, response_format: type[T]) -> T:
        completion: ParsedChatCompletion[T] = client.beta.chat.completions.parse(
            temperature=0,
            model=self.model_name,
            messages=convo.to_openai_messages(),
            response_format=response_format,
        )
        response: ParsedChatCompletionMessage[T] = completion.choices[0].message
        if response.parsed:
            return response.parsed
        else:
            raise ValueError("Failed to parse response")


if __name__ == "__main__":
    convo = Conversation()
    convo.add_user_message("Hello")
    convo.add_assistant_message("Hi, how can I help you?")
    convo.add_user_message("Can you say `Hello World`?")
    llm = LLM(LLMName.LLAMA_3_1_8B)
    response = llm.generate(convo)
    print(response)
