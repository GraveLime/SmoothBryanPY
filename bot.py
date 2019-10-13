import discord
import os
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

#instantiates a discord client which our bot can run on
client = discord.Client()
#path to the chrome driver executable
CHROME_PATH = os.path.dirname(os.path.realpath(__file__))+"//chromedriver.exe"

    #the event that fires when the bot is fully booted
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    
    
    #the event that fires every time a message is sent in discord
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('?'):
        cmd = message.content.split(' ', 1)
        if '?ping' in message.content:
            await send(message, 'Pong!')
        elif '?say' in message.content:
            await send(message, cmd[1])
        elif '?reddit' in message.content:
            if len(cmd) < 2:
                await send(message, 'please give two parameters')
            else:
                await reddit(message, cmd[1])
        elif '?imgur' in message.content:
            if len(cmd) <2:
                await send(message, 'please give a number of memes')
            else:
                await imgur(message, cmd[1])
        elif '?die' in message.content:
            await client.close()
        elif '?commands' in message.content or '?help' in message.content:
            await send(message, 'The available commands are ?ping: to recieve a pong, ?say: to have smooth bryan parrot you, ?reddit: to ask bryan to go and find memes from a specific subredit, example ?memes 10 dankmemes will give you the top ten dankmemes on r/dankmemes')
                
            
            
    #method for sending messages into discord
async def send(message, string):
    await message.channel.send(string)
    
    #method for grabbing images from reddit
async def reddit(message, string):
    #Splits the incoming string at all spaces
    newstring = string.split(' ')
    #variable to hold the number of memes requested.
    val = 0
    #variable to hold the topic of those memes
    topic = ''
    #checks to make sure that the newstring is atleast two arguments long
    if len(newstring) < 2:
        await send(message,'please pass atleast two parameters. one an integer and one a subReddit')
    #checks if the first argument is an integer
    elif RepresentsInt(newstring[0]):
        val = int(newstring[0])
        topic = newstring[1]
        await send(message, 'you want {} memes of the subReddit: {}'.format(val,topic))
    #checks if the second argument is an integer
    elif RepresentsInt(newstring[1]):
        val = int(newstring[1])
        topic = newstring[0]
        await send(message, 'you want {} memes of the subReddit: {}'.format(val,topic))
    #catches incorrect input
    else:
        await send(message, 'you did not input a number of memes and a subReddit')
        
    #creates an object to hold chrome options
    chrome_options = Options()
    #adds the argument for chrome to run in headless mode
    chrome_options.add_argument("--headless")
    #creates the webdriver in chrome with the created options
    driver = webdriver.Chrome(CHROME_PATH, options=chrome_options)
    #tells the driver to get the reddit page of the desired topic
    driver.get("https://reddpics.com/r/"+topic)
    #sleep to let the page load
    time.sleep(1)
    #scraped the webpage for all elements with a matching css
    images = driver.find_elements_by_css_selector("a[href*='redd']")
    #instantiates an array for curated elements`
    curated = []
    #checks each element in images to be sure its of the desired type
    for element in images:
        if('https://i.redd.it' in element.get_property("href")):
            curated.append(element)
    #removes all odd entries. this is done to remove duplicate entries which occur because of reddits website
    del curated[1::2]
    #itterates from 0 to the given value
    for i in range(val):
        #prints the links into console for debugging
        print(curated[i].get_property("href"))
        #calls the async method send with the link string to be posted in discord
        await send(message,curated[i].get_property("href"))
    #ending of meme posting signal
    await send(message, "Your dank memes sir/madam")
    
    #Method for grabbing images from imgur
async def imgur(message, string):
    #creates a new string from the passed in string that is split at the first space   
    newstring = string.split(' ',1)
    #checks if the first variable passed in is not a number
    if not await RepresentsInt(newstring[0]):
        #assigns default value to number of itterations required
        val = 1
        #takes all of the args and combines them back for the topic
        topic = newstring[0]+ " " + newstring[1]
    #checks if the length of the newstring is greater than one
    elif len(newstring) >1:
        #assigns the first arg to val
        val = int(newstring[0])
        #assigns all of the rest of the args into topic
        topic = newstring[1]
    #catches everything else just in case
    else:
        print("FATAL ERROR: Not sure how you got here but go back.")
    #prints the topic in console for debugging purposes
    print("the topic is: " + topic)
    #creates an object to hold chrome settings
    chrome_options = Options()
    #adds an argument to run chrome in headless mode
    chrome_options.add_argument("--headless")
    #creates a webdriver given the previous options
    driver = webdriver.Chrome(CHROME_PATH, options=chrome_options)
    #tells the driver to open imgur
    driver.get("https://www.imgur.com")
    #finds the search bar at the top
    searchbar = driver.find_element_by_class_name("Searchbar-textInput")
    #sends the topic to the search bar
    searchbar.send_keys(topic)
    #presses enter to begin our search
    searchbar.send_keys(Keys.RETURN)
    #scrapes the webpage for images that match our desired classname
    images = driver.find_elements_by_class_name("image-list-link")
    #itterates through and prints all of the links to the galleries
    for i in range(val):
        #prints the links in console for debugging
        print(images[i].get_property("href"))
        #sends the links into discord
        await send(message,images[i].get_property("href"))
    #end of memes signalling message
    await send(message, "Your dank memes sir/madam")
    
    #checks to see if a string can be converted into an integer
async def RepresentsInt(s):
    #tries to convert string into integer
    try: 
        #convert string into integer
        int(s)
        #if the above is successful return true
        return True
    #triggers if an error has occured above
    except ValueError:
        #returns false when the above exception is trigered
        return False
#runs the client using a token so it knows where to connect
client.run('NjMyNjkxOTcwMDk5MjQ5MTUz.XaJHyQ.6CzlRLn6fm-6hw-GfEEquo5f3mU')