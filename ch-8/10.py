text_messages = [
    "Hello, how are you?",
    "I'm fine, thank you. And you?",
    "I'm fine too.",
    "That's good to hear.",
    "Bye."
]

sent_messages = []

def send_messages(text_messages, sent_messages):
    text_messages.reverse()

    while text_messages:
        current_message = text_messages.pop()
        print(current_message)
        sent_messages.append(current_message)


send_messages(text_messages, sent_messages)

print('\n')

print(f"Sent messages: {sent_messages}")
print(f"Text messages: {text_messages}")