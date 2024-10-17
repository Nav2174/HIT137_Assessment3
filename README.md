**Question 1**
##Overview

This is a simple Translation Application built using Tkinter for the GUI and googletrans library to perform language translations. The application allows users to select source and target languages, input text in the source language, and view the translated result in the target language.
##Features

    User-friendly interface with a dark theme.
    Dropdown selection for both source and target languages.
    Text input box for entering text to be translated.
    Displays translated text in a separate text box.
    Alerts in case of empty input or translation errors.

##Requirements
###Dependencies

    Python 3.x
    Tkinter (built-in with Python)
    googletrans==4.0.0-rc1

###Installation

To run this application, you need to install the googletrans package. You can install it using pip:


```pip install googletrans==4.0.0-rc1```

###Usage

    Clone or download this repository.
    Ensure you have all the required dependencies installed.
    Run the Python file using:



```python Q1-TranslationScriptApp.py```

    The application window will appear with the following elements:
        Source Language Dropdown: Select the language of the input text.
        Target Language Dropdown: Select the language to translate the text into.
        Text Input Box: Enter the text you want to translate.
        Translate Button: Click to perform the translation and display the result.

###Application Layout

    Source Language: A dropdown to select the language of the text you want to translate.
    Target Language: A dropdown to select the language you want the text to be translated into.
    Source Text Box: Enter the text to be translated here.
    Target Text Box: The translated text will be displayed here.
    Translate Button: Click this button to perform the translation.

Example Usage

    Select "English" as the Source Language and "Spanish" as the Target Language.
    Type some text (e.g., "Hello World!") in the Source Text Box.
    Click the Translate Button.
    The translated text (e.g., "¡Hola Mundo!") will appear in the Target Text Box.

Error Handling

    If no text is entered in the input box, an error message will prompt the user to enter text.
    If any error occurs during translation (e.g., connectivity issues), an error dialog will display the issue.

###Customization

    You can change the default languages by modifying the self.src_lang_combo.set("English") and self.tgt_lang_combo.set("Spanish") in the create_widgets() function.

**Question 2**

#Side Scrolling Game

This is a simple side-scrolling game built using Pygame. The player navigates through three challenging levels while avoiding obstacles and achieving high scores. The game is designed to keep the player engaged without offering an "Exit" option during gameplay.
###Features

    Three levels with increasing difficulty.
    Side-scrolling mechanics with smooth transitions.
    Engaging gameplay with no exit option, immersing the player until all levels are completed.
    Simple and intuitive controls.

###Prerequisites
  Pygame: This game uses the pygame library. 

This is a basic game menu for your side-scrolling game where the player can choose levels, shoot, move, and jump using specific controls. Based on this, I'll integrate this information into your README.md file to clarify how to navigate the menu and play the game.
Side Scrolling Game

This is a simple side-scrolling game built using Pygame. The player navigates through three challenging levels while avoiding obstacles and achieving high scores. The game includes both horizontal and vertical shooting mechanics and a main menu to select levels.
Features

    Three levels with increasing difficulty.
    Shooting mechanics: Horizontal and vertical shooting options.
    Side-scrolling mechanics with smooth transitions.
    Intuitive main menu for level selection.
    Simple and intuitive controls for navigation, shooting, and jumping.

###Prerequisites
    Pygame: This game uses the pygame library




Navigate to the Game Directory:

```cd side-scrolling-game```

Install Pygame: Run the following command to install pygame:

```pip install pygame```

Run the Game: After the installation is complete, you can start the game by running:



    ```python game.py```

#How to Play
##Menu Navigation

    Press 1: Start Level 1
    Press 2: Start Level 2
    Press 3: Start Level 3
    Press Q: Exit the game

###In-Game Controls

    Arrow keys or WASD: Move the character left and right.
    Spacebar: Jump.
    F key: Shoot horizontally.
    G key: Shoot vertically.

###Shooting Mechanics

    Horizontal Shooting: Press F to shoot projectiles horizontally, helping you clear obstacles or defeat enemies in front of you.
    Vertical Shooting: Press G to shoot vertically, useful for taking out enemies above.

###Game Levels

The game includes three levels of increasing difficulty. Select the desired level from the main menu:

    Level 1: Introduction level with basic obstacles and enemy types.
    Level 2: More challenging with additional enemies and obstacles.
    Level 3: The hardest level with the toughest challenges.

There is no exit option during the levels, but you can press Q to quit from the main menu.

  
