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
<< Give an overview of your project >>

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
    * ![class_diagram](assets/class_diagram.jpg)
    * This does not need to be overly detailed, but should show how your code fits into the Model/View/Controller paradigm.
* Classes
    * class Player: creates the main character, totoro and sets move functions 
    * class Friend: creates the friend character and sets its position
    * class SpikeFish: creates the spikefish obstacles that will be called using randomized x and y values

## Project Structure *(Software Lead)*

The Project is broken down into the following file structure:
* main.py
* bin
    * <all of your python files should go here>
* assets
    * <all of your media, i.e. images, font files, etc, should go here)
* etc
    * <This is a catch all folder for things that are not part of your project, but you want to keep with your project. Your demo video should go here.>

***

## Tasks and Responsibilities *(Software Lead)*
* You must outline the team member roles and who was responsible for each class/method, both individual and collaborative.

### Software Lead - << name >>

<< Worked as integration specialist by... >>

### Front End Specialist - << name >>

<< Front-end lead conducted significant research on... >>

### Back End Specialist - Young Seo Hur

<< The back end specialist... >>

## Testing *(Software Lead)*
* << Describe your testing strategy for your project. >>
    * << Example >>

* Your ATP

| Step                  | Procedure     | Expected Results  | Pass/Comments |
| ----------------------|:-------------:| -----------------:| -------------- |
|  1  | Run main()  | Game starts and loads user into the menu  |   |
|  2  | User clicks Instructions button |  Instructions tab opens and says how to play game | |
|  3  | User clicks "Play"  | 1) Game opens and starts 2) Timer starts | |
|  4  | Press left arrow  | Player moves left |  |
|  5  | Hold left arrow |  Player continually moves left |  |
|  6  | Press right arrow  | Player moves right |  |
|  7  | Hold right arrow  |  Player continually moves right |  |
|  8  | Press or hold up or down key | Player moves up or down accordingly and keeps going in direction if key held down |   |
|  9  |  Player rect touches 'Friend' rect | 1) Game ends 2) A scoreboard is displayed showing past completion times & play again directions | |
|  10  | Tap "r" | The game resets (only works when the game is over)  | |

   

![Controller Image](https://github.com/bucs110a0fall21/final-project-puzzlers/blob/master/assets/Controller.pdf)
![Interface](https://github.com/bucs110a0fall21/final-project-puzzlers/blob/master/assets/interface%20full-1.jpg)
![Interface2](https://github.com/bucs110a0fall21/final-project-puzzlers/blob/master/assets/interface%20full-2.jpg)
![Interface3](https://github.com/bucs110a0fall21/final-project-puzzlers/blob/master/assets/interface%20full-3.jpg)
