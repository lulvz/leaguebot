# leaguebot - Voice controlled league of legends

LeagueBot is a voice-controlled bot for the popular online game, League of Legends. It is designed with modularity in mind, allowing for easy extension and addition of new champions.

## Modularity

The bot is designed in a modular fashion, which allows for easy addition of new champions. Each champion is implemented as a separate Python class (for example, see [`YuumiBot`](yuumi.py)) that extends the base bot functionality. 

To add a new champion, you simply need to create a new class for that champion and implement the specific behaviors for that champion. The bot's main file, [`bot.py`](bot.py), imports the champion classes and uses a variable to determine which champion to use. This makes it easy to switch between different champions by just changing a single variable.

## Clicks.py

The [`clicks.py`](clicks.py) file is a crucial part of the bot's functionality. It contains functions and classes for simulating mouse and keyboard input, which the bot uses to interact with the game.

The file uses the `ctypes` library to interact with the Win32 API, allowing it to simulate input in a way that the game will recognize. It defines several classes that represent different types of input, such as `MouseInput` and `KeyBdInput`, as well as functions for sending this input to the game.

The `clicks.py` file also includes a dictionary of key codes for simulating keyboard input. This allows the bot to simulate pressing any key on the keyboard, which is used for issuing commands in the game.

## Running the Bot

To run the bot, simply execute the `start_bot.bat` file. This will start the Python script that runs the bot.

## Requirements

- Python 3.6
- League of Legends installed
- Windows 10/11
- Win32 API for Python
- speech_recognition library for Python
- pyautogui library for Python

Please ensure that all the necessary Python libraries are installed and that you have the correct version of Python installed. Also, make sure that League of Legends is installed and properly configured.

## Disclaimer

This bot is intended for educational purposes only. Please use responsibly and in accordance with the League of Legends terms of service.

## Project Status

This was a learning project for me, and I have no plans to continue working on it. I learned a lot about how speech recognition works, how the windows API is structured, and how to simulate input in Windows. I also learned a lot about how to structure a modular program, and how to use Python classes to implement this modularity.