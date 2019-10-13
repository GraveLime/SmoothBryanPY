# Smooth Bryan: "The Meme Machine" Project
This project was undertaken at the 2019 HackNC event in Chapel Hill

# Features
The ability to pull a number of images from Imgur given a specific tag to pull from.
The ability to pull a number of images from Reddit given a specific subreddit to pull from.
The ability to parrot the user given a flag 

# Required packages
    Python 3
	Selenium
	Discord.py
	chrome version 75.0.3770.80
	

## Setup Instructions
Following the instructions below create your bot up to the point where you get your token
[https://www.digitaltrends.com/gaming/how-to-make-a-discord-bot/](https://www.digitaltrends.com/gaming/how-to-make-a-discord-bot/)

Download our repo and edit the token at the top of the file after imports.
Navigate to the place you cloned the repo and run ``python bot.py`` this will launch the meme machine

## Commands
All commands are preceded by a question mark
A list of the accepted commands are:
## ?ping - returns Pong!
```
User:
?ping
Bot:
Pong!
```
## ?say - returns anything after the flag
```
User:
?say hello world
Bot:
hello world
```
## ?reddit - returns memes from a given subredit
```
User:
?reddit 3 aww
Bot:
Link to meme
Link to meme
Link to meme
Your dank memes Sir/Madam
```
## ?imgur - returns memes from a given tag
```
User:
?imgur 3 cats
Bot:
Link to meme
Link to meme
Link to meme
Your dank memes Sir/Madam
```
## ?leave - causes the bot to logout

## Creators
Jonathan Bacon and Brandon Pozil
