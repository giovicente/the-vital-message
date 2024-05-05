import os
import random
import string
import time


def set_difficult():
    valid_input = False
    MINIMUM_DIFFICULT = 4
    MAXIMUM_DIFFICULT = 10

    while valid_input is not True:
        try:
            difficult = int(input('HOW DIFFICULT? (4-10) '
                                  '\n'))
            if difficult >= MINIMUM_DIFFICULT and difficult <= MAXIMUM_DIFFICULT:
                valid_input = True
        except ValueError:
            print('ONLY NUMBERS ALLOWED')

    return difficult


def intercept_message(difficult):
    intercepted_message = ''

    for i in range(difficult):
        intercepted_message += random.choice(string.ascii_uppercase)

    return intercepted_message


def send_intercepted_message(difficult):
    time.sleep(0.5 * difficult)
    os.system('cls||clear')

    return input('').upper()


def verify_intercepted_message(intercepted_message, sent_message):
    if intercepted_message == sent_message:
        print('MESSAGE CORRECT'
              '\n'
              'THE WAR IS OVER')
    else:
        print('YOU GOT IT WRONG')
        print('YOU SHOULD HAVE SENT: '
              '\n'
              + intercepted_message)


if __name__ == '__main__':
    print('THE VITAL MESSAGE')

    difficult = set_difficult()
    intercepted_message = intercept_message(difficult)

    print('SEND THIS MESSAGE:'
          '\n'
          + intercepted_message)

    sent_message = send_intercepted_message(difficult)
    verify_intercepted_message(intercepted_message, sent_message)
