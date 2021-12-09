:warning: Everything between << >> needs to be replaced (remove << >> after replacing)
# CS110 Project Proposal
# << Project Title >>
## CS 110 Final Project
### Fall, 2021
### [Assignment Description](https://docs.google.com/document/d/1H4R6yLL7som1lglyXWZ04RvTp_RvRFCCBn6sqv-82ps/edit#)

https://github.com/bucs110a0fall21/final-project-puzzlers

<< [link to demo presentation slides](#) >>

### Team: Puzzlers
#### Christopher Yu, Young Seo (Esther) Hur, Ashley Yu

***

## Project Description *(Software Lead)*
A lighthearted game where mini-Totoro locates his long-lost friend admist a weekend swim. Navigate mini-Totoro through the spike fish as quick as possible so that
they can once again rejoyce!

***    

## User Interface Design *(Front End Specialist)*
1. Start screen - This is the first screen that opens up and it has a start button that will lead to the actual game. Additionally, it also has an instructions button that will lead to directions on how to play the game.
2. Instructions screen - This has the goal of the game and the key binding for the game. It tells the plays to use the arrow keys, hit return to the menu, and escape to restart the game.
3. Game - This is the actual game which has the timer in the upper left hand corner. Hitting esc will allow the player ot reset its position and hitting the X will close the game. Once the player is spawned and reaches the friend in the right corner the end screen will display
4. Game over screen - This screen appears once you collide with the friend. It will display the high score and your current time. It will allow you to replay the game by pressing esc and return to the menu by hitting return. The game can be closed by hitting the x on the upper right.
* << You should also have a screenshot of each screen for your final GUI >>

***        

## Program Design *(Backend Specialist)*
* Non-Standard libraries
    * Additional libraries or modules used: pygame, random, json, sys
    * For each additional module you should include
        * url for the module documentation
        * a short description of the module
* Class Interface Design
    * ![interface_design](etc/interface_design.jpg)
    * This does not need to be overly detailed, but should show how your code fits into the Model/View/Controller paradigm.
* Classes
    * class Player: creates the main character, totoro and sets move functions
    * class Friend: creates the friend character and sets its position on the screen
    * class SpikeFish: creates the spikefish obstacles that will be called in Controller using randomized x and y values for random spawning within a part of the screen

## Project Structure *(Software Lead)*

The Project is broken down into the following file structure:
* main.py
* src 
    * controller.py
    * Friend.py
    * Player.py
    * SpikeFish.py
* assets
    * background.png
    * block2.png
    * friend.png
    * totoro.png
* etc
    * class_diagram.jpg
    * interface_design.jpg
    * video1818954711.mp4

***

## Tasks and Responsibilities *(Software Lead)*
* You must outline the team member roles and who was responsible for each class/method, both individual and collaborative.

### Software Lead - Christopher Yu

Worked as integration specialist by implementing the controller functions ensuring that all the classes meshed correctly and functioned properly.
Also wrote the SpikeFish and Player class as well as assisted in other controller related integration issues with the Back-end specialist. 
Made sure each group member was on the same page and prevented any miscommunications on the work assigned for each member. 

### Front End Specialist - Ashley Yu

The front end specialist collaborated with the back end specialist to create the GUI. They created the start and instructions screen. Additionally, they implemented the screens into the mainloop and gameloop. The specialist decided on the color scheme and placement of buttons and text.

### Back End Specialist - Young Seo Hur

The back end specialist wrote much of the data classes representing state, location, and behaviour. I drew the sketch of the classes and their purposes and relationships as well as the GUI design plan illustration. Lastly, I was the main debugger as well as functionality improver as I added and improved code to run the characters' movements, start menu, gameover screen, and buttons more smoother and accurately. Worked with software lead in the data permanence feature: storing and reading data, displaying on game over screen and debugging. 

## Testing *(Software Lead)*
* Integrated each feature individually into the controller to pinpoint what was wrong in the event of an error. Also utilized the ATP to ensure that the feature implemented was the correct feature intended.
    * For example, if the timer function was to be implemented, first the timer would be tested to see if it worked (as a timer of course) and then when that was confirmed, it would be tested to see if it displayed on the screen correctly. 

* Your ATP

| Step                  | Procedure     | Expected Results  | Pass/Comments |
| ----------------------|:-------------:| -----------------:| -------------- |
|  1  | Run main()  | Game starts and loads user into the menu  |   |
|  2  | User clicks Instructions button |  Instructions tab opens and says how to play game | |
|  3  | User hits 'return'  | Returns the user into the main menu  |   |
|  4  | User clicks "Play"  | 1) Game opens and starts 2) Timer starts | |
|  5  | Press 'esc'  | 1) Player's position is reset 2) Timer is rest |  |
|  6  | Press left arrow  | Player moves left |  |
|  7  | Hold left arrow |  Player continually moves left |  |
|  8 | Press right arrow  | Player moves right |  |
|  9  | Hold right arrow  |  Player continually moves right |  |
|  10  | Press or hold up or down key | Player moves up or down accordingly and keeps going in direction if key held down |   |
|  11 | Player rect touches SpikeFish rect  | Player is repelled away by 2 units |  |
|  12 |  Player rect touches 'Friend' rect | 1) Game ends 2) The highscore and current score are recorded in the json file 3) End Screen pops up with instructions as well as the highscore and current completion time | |
|  13  | User preses "esc" | 1) The game resets 2) The timer resets  | |
|  14  | User completes the game once again  | Game reloads back into the end menu  |   |
|  15 | User presses "return"  | The game returns to the main menu |  |
|  16 | User presses the "close" button on the screen  | The game closes |  |

   

![Class_Diagram](etc/class_diagram.jpg)
![Interface_Design](etc/interface_design.jpg)
