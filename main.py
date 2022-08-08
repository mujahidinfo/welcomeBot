# import data file
from data import *

def welcomeBot():
    name = str(input("Enter your name here: "))
    print("Assalamualaikum! ", name ," How are you?")

    # get user answer and convert to list
    user_answer = str(input("Enter how you feel right now: "))
    cvt_list = list(user_answer.split(" "))
    print(cvt_list)

    # matching words
    if good_word_list in cvt_list:
        print("Alhumdulillah! Glad to hear that ", name)
    elif bad_word_list in cvt_list :
        print("I'm so sorry for this!", name)
    else:
        print("i didn't get you! please try again ", name)
        welcomeBot()

print(welcomeBot())