from conversations import Conversation, Message, Role, MessageType


def test_add_user_message():
    conversation = Conversation()
    conversation.add_user_message("Hello")
    assert len(conversation.messages) == 1
    assert conversation.messages[0].role == Role.user
    assert conversation.messages[0].content == "Hello"
    assert conversation.messages[0].type == MessageType.text


def test_add_assistant_message():
    conversation = Conversation()
    conversation.add_assistant_message("Hi, how can I help you?")
    assert len(conversation.messages) == 1
    assert conversation.messages[0].role == Role.assistant
    assert conversation.messages[0].content == "Hi, how can I help you?"
    assert conversation.messages[0].type == MessageType.text


def test_add_system_message():
    conversation = Conversation()
    conversation.add_system_message("System initialized")
    assert len(conversation.messages) == 1
    assert conversation.messages[0].role == Role.system
    assert conversation.messages[0].content == "System initialized"
    assert conversation.messages[0].type == MessageType.text


def test_from_system_message():
    conversation = Conversation.from_system_message("System initialized")
    assert len(conversation.messages) == 1
    assert conversation.messages[0].role == Role.system
    assert conversation.messages[0].content == "System initialized"
    assert conversation.messages[0].type == MessageType.text


def test_from_user_message():
    conversation = Conversation.from_user_message("Hello")
    assert len(conversation.messages) == 1
    assert conversation.messages[0].role == Role.user
    assert conversation.messages[0].content == "Hello"
    assert conversation.messages[0].type == MessageType.text


def test_from_assistant_message():
    conversation = Conversation.from_assistant_message(
        "Hi, how can I help you?")
    assert len(conversation.messages) == 1
    assert conversation.messages[0].role == Role.assistant
    assert conversation.messages[0].content == "Hi, how can I help you?"
    assert conversation.messages[0].type == MessageType.text


def test_add_message():
    conversation = Conversation()
    message = Message(role=Role.user, content="Hello")
    conversation.add_message(message)
    assert len(conversation.messages) == 1
    assert conversation.messages[0] == message


def test_to_openai_messages():
    conversation = Conversation()
    conversation.add_user_message("Hello")
    conversation.add_assistant_message("Hi, how can I help you?")
    openai_messages = conversation.to_openai_messages()
    assert len(openai_messages) == 2
    assert openai_messages[0]["role"] == "user"
    assert openai_messages[0]["content"] == "Hello"
    assert openai_messages[1]["role"] == "assistant"
    assert openai_messages[1].get("content") == "Hi, how can I help you?"
