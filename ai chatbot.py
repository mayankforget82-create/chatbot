print("chatbot:hello! I am your chatbot.")
print("chatbot:how can i help you!")
while True:
    user=input("You:").lower()
    if user=="hello" or user=="hi":
        print("Chatnot:hello!Nice to meet you!")
    elif user=="how are you":
        print("Chatbot: I am fine Thank you!")
    elif user=="bye":
        print("Chatbot: Goodbye! Have a nice day")
    elif user=="what do you think what kind of a person i am":
        print("Chatbot:I think as per your previous response after analyzing them i can say you are a calm,curious, want to know more kinda guy and per personality you are very careing,emotional supporter type of a person.")
        print("Chatbot:Thanku for sharing! have a nice day, bye")
        break
    else:
        print("Chatbot:sorry i don't understand")
        


