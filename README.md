![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)


## Introduction 
----
Hidden Secrets is a text-based adventure game that takes place on a remote place where the game is created to be from the users perspective. Inside the game the user is confronted with different questions where depending on the answer different path can be taken. 
----
## UX
---
### User story 
----
* When i was creating this game I was wonering about what I wanted to be able to play. For me is the most important thing the storyline. I want to be intrigued and I want to have the feeling that I really have to finish the storyline. 
* When making this game I focused on the storyline and what the different choices would do to the story. 
---
### Site goals and strategy
---
* My goal with this game and site is to give the player a new type of game to play. 
* I want to provide the player with a interesting and intriguing storyline that will make the player want to play it through. 
---
### Structure
---
* In the beginning of the game the player has an opportunity to leave or continue. For further visual effects a self-made picture of a house has been created. This will hopefully give the user a chance to visualize the story. 
---
#### Mindmap / Flow chart 
---
* The following mindmap have been drawn using [lucidcharts](https://www.lucidchart.com/pages/). The information it contains is how the game have been displayed. 
![Mindmap](https://workspace/PP3/assets/images/Mindmap.PP3.png)
---
### Design 
---
* The main design of the game follows the same pattern. First it is a shorter text which gives the player a piece to the puzzle. Second there are two options to choose from. The story places out in different fictive rooms, the greenhouse, library, hidden room and then has two types of endings. 
---
### Technologies 
---
#### OS 
* I used this to create a function called clear_terminal. Which made it possible for me to clear the terminal before it was filled up with new text. 
#### SYS
* I used this to create a so called system exit. So that the player would be able to exit the loop that was created. 
---
### Test validation 
----
#### PEP8 validator 
* For validation purposes I used [PEP8Online](http://pep8online.com/) which came back with zero errors.
* (https://workspace/PP3/assets/images/PEP8.validation.png)

---- 
### Deployment using Heroku
----
* Visit the Heroku site.
* Sign in.
* Click the "New" button - Click the "Create new app" button.
* Provide a name for the app in the App name input field.
* Select your region from the choose region dropdown menu.
* Click the "Create App" button - Once redirected, proceed to the settings tab.
* Click on the "config vars" button.
* Supply a KEY of PORT and it's value of 8000. The click the "add" button.
* Next step is to add Buildpacks - Click the "Add buildpack" button.
* * The python buildpack needs to be added first then the nodejs buildpack.
* Once both of the buildpacks have finished being added, proceed to the deploy tab.
* Once in the deploy screen, select GitHub as the deployment method and connect your GitHub profile.
* Search for the repository that you wish to deploy to Heroku and click "connect".
* Once your repository is connected to Heroku you can choose to either manually or automatically deploy your app.
* By selecting automatic deploys, Heroku will build a new version of the app each time a change has been pushed to the repository.
* Manual deploys allow you to build a new version of your app whenever you click manual deploy.
* If your build is successful you will then be able to visit the live site by clicking the link that is provided to you by Heroku.
---
### Credits 
---
* I want to give a big thank you(!!) to Jack Conroy who has a big patience with all my questions and allways make the feel less stressed. 
---
