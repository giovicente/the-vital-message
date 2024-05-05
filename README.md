# The Vital Message

## About the game

This program is a reproduction of the game "The Vital Message", published in the book "Computer Battlegames" by Usborne Computer Games in 1982. 

I became aware of this book and the game through the YouTube channel of the creator Kari Lawler (https://www.youtube.com/@karilawler), who programmed this game in the following video: https://www.youtube.com/watch?v=3kdM9wyglnw.

This is my rendition of the game, which basically uses the same logic and commands used by Kari in the video, but with two significant differences:
- Dividing the game logic into smaller functions
- Changing variable names

In the video, the creator opted to remain faithful to the book version by naming variables and adhering to the program logic as instructed in the book. This enhances the fidelity of her algorithm.

This is the program description as stated in the book "Computer Battlegames":

> You are a laser communications operator. Your job is to intercept robot messages and relay them to Command HQ. A vital code message is expected. If you relay it correctly, the Robot attack will be crushed. This game tests your skill at remembering a group of letters which you see for only a very short time. The computer will ask you for a difficulty from 4 to 10. When you have typed in your answer, letters will appear top left of your screen and disappear again fairly quickly. Memorize them and then type them into the computer and see if you were right.

## Gameplay
You can check out the gameplay of 'The Vital Message' on Kari's video. Here's a link with the exact moment she's playing it: https://www.youtube.com/watch?v=3kdM9wyglnw&t=145s

## Technologies used
- Python 3.11.9
- pip 24.0

## Installing and running the game
1. Clone the repository
```bash
git clone https://github.com/giovicente/the-vital-message.git
```

2. Ensure you have Python 3 installed by using the command below.
```bash
python --version
```
If it returns any version of Python starting with 3, such as the example below, you're good to go.
```commandline
Python 3.11.9
```
Here you can install the latest version of Python: https://www.python.org/downloads/

3. Since the program is compatible with Python 3.x, it should work with any version of pip that is compatible with Python 3.x. However, it's generally a good practice to ensure that you have the latest version of pip installed for your Python environment. You can upgrade pip using the following command:
```bash
python -m pip install --upgrade pip
```

4. Run the program in a terminal by executing the command below in the same folder where the file `the_vital_message.py` is located.
```commandline
python the_vital_message.py
```
**Important Notice: if you run the program through PyCharm using the Run function, the screen clearing command, crucial for the proper experience and execution of the game, will not work. This game was designed to be run in terminals.**
