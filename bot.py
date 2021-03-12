import random
from TF_IDF import *


# tratamento de mensagens de boas-vindas
GREETING_INPUTS = ("hello", "hi", "greetings", "sup", "what's up", "hey",)
GREETING_RESPONSES = ["hi", "hey", "*nods*", "hi there", "hello", "I am glad! You are talking to me"]


def greeting(sentence):
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)


# função que executa o robô
def bot():
    flag = True
    print("ROBOT: My name is Robot.\n - I will talk to you about computers.\n - If you want to exit, type Bye!")
    name = input("what's your name? ")
    print(f"ROBOT: Nice to meet you {name}!!!")
    while flag:
        user_response = input(f"\n{name}: ")
        user_response = user_response.lower()

        if user_response != 'bye':
            if user_response == 'thanks' or user_response == 'thank you':
                print("ROBOT: You are welcome..")
            else:
                if greeting(user_response) is not None:
                    print("ROBOT: " + greeting(user_response))
                else:
                    print("ROBOT: ", end="")
                    print(compare(user_response))
        else:
            flag = False
            print("ROBOT: Bye! take care...")


if __name__ == "__main__":
    bot()
