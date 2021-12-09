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
A lighthearted game where mini-Totoro travels the world in search of a long lost friend. It is amongst the waters where
he locates his long lost buddy. In utter excitement Totoro races through the spike-fish herd to reach his friend. Help Totoro reach his friend
in the fastest time possible so that they can rejoyce once again!


***    

## User Interface Design *(Front End Specialist)*
* << A wireframe or drawing of the user interface concept along with a short description of the interface. You should have one for each screen in your program. >>
    * For example, if your program has a start screen, game screen, and game over screen, you should include a wireframe / screenshot / drawing of each one and a short description of the components
* << You should also have a screenshot of each screen for your final GUI >>

***        

## Program Design *(Backend Specialist)*
* Non-Standard libraries
    * Additional libraries or modules used: pygame, random, json, sys
    * For each additional module you should include
        * url for the module documentation
        * a short description of the module
* Class Interface Design
    * ![class_diagram](etc/class_diagram.jpg)
    * This does not need to be overly detailed, but should show how your code fits into the Model/View/Controller paradigm.
* Classes
    * class Player: creates the main character, totoro and sets move functions 
    * class Friend: creates the friend character and sets its position
    * class SpikeFish: creates the spikefish obstacles that will be called using randomized x and y values

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
    * high_scores.json
* etc
    * class_diagram.jpg
    * interface_design.jpg

***

## Tasks and Responsibilities *(Software Lead)*
* You must outline the team member roles and who was responsible for each class/method, both individual and collaborative.

### Software Lead - Christopher Yu

Worked as integration specialist by ensuring all functions worked correctly 
in the controller and wrote the Player and Spikefish class. Ensured that all group members understood their tasks and assisted where needed.


### Front End Specialist - << name >>

<< Front-end lead conducted significant research on... >>

### Back End Specialist - Young Seo Hur

<< The back end specialist... >>

## Testing *(Software Lead)*
* Implemented each new feature into the controller one at a time
    * For example, if the timer was to be implemented, I would create the timer,
  then display it to make sure it worked before moving onto another feature. 

* Your ATP

| Step                  | Procedure     | Expected Results  | Pass/Comments |
| ----------------------|:-------------:| -----------------:| -------------- |
|  1  | Run main()  | Game starts and loads user into the menu  |   |
|  2  | User clicks Instructions button |  Instructions tab opens and says how to play game | |
|  3  | User clicks "Start"  | 1) Game opens and starts 2) Timer starts | |
|  4  | User hits 'esc'  | Game resets |  |
|  5  | Press left arrow  | Player moves left |  |
|  6  | Hold left arrow |  Player continually moves left |  |
|  7  | Press right arrow  | Player moves right |  |
|  8  | Hold right arrow  |  Player continually moves right |  |
|  9  | Press or hold up or down key | Player moves up or down accordingly and keeps going in direction if key held down |   |
|  10  | User touches the 'SpikeFish' rect | The player is 'repelled' by displacing the player's rect 2 units in either/both the x and y coordinates  | |
|  11  |  Player rect touches 'Friend' rect | 1) Game ends 2) A scoreboard is displayed showing current completion time & quickest completion time 3) Displays 'hitting return will return you to main menu' and 'hitting esc will restart the game' | |


   

![Controller Image](https://github.com/bucs110a0fall21/final-project-puzzlers/blob/master/assets/Controller.pdf)
![Interface](https://github.com/bucs110a0fall21/final-project-puzzlers/blob/master/assets/interface%20full-1.jpg)
![Interface2](https://github.com/bucs110a0fall21/final-project-puzzlers/blob/master/assets/interface%20full-2.jpg)
![Interface3](https://github.com/bucs110a0fall21/final-project-puzzlers/blob/master/assets/interface%20full-3.jpg)
