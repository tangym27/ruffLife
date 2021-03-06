# ruffLife
# Xiaojie (Aaron) Li, Bo Hui Lu, Michelle Tang, Kaitlin Wan
P #01: ArRESTed Development

## Project Description
Using RESTful APIs to help stressful users relax mentally by looking at various memes, aesthetically pleasing animals(just dogs and cats), or funny jokes. The user will laugh, smile, and appreciate the wonder of animals and our beautiful website. Not to mention there is an animal themed weather site as well! If they enjoy something, they can log in and earmark it for future viewings. Logged in users get to experience this all on a single webpage while guest users will be redirected to a new page each time.

## APIs
**Here are the APIs that we use & how to procure keys:**

API Name | Link | Key & Quota | How to Create Key 
--- | --- | --- | ---
catpic | https://aws.random.cat/meow  | no key needed and unlimited quotas! | N/A
dogpic | https://random.dog | no key needed and unlimited quotas! | N/A
catfact | https://catfact.ninja/ | no key needed and unlimited quotas! | N/A
dogFact | http://kinduff.com/dog-api/ | no key needed and unlimited quotas! | N/A
fun jokes | http://randomuselessfact.appspot.com/ | no key needed and unlimited quotas! | N/A
gif | https://developers.giphy.com/docs/ | key is needed and there is a 10,000 search per day quota limit | Register for a developer account. Then, create an App (access through the dashboard). Fill in all required fields and save it. 
quote of the day | https://favqs.com/api/ | no key and unlimited quotas!| N/A

## Instructions to Run:

1. Check to see if you have python3 installed by running ``` python3 ``` in the terminal. It should produce something like: 
```
Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 20:42:06) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
```
2. Install python3-venv and create your own environment by running the following in terminal. Replace <VENV> with the name of your virtual environment (your choice).
```
$ sudo apt install python3-venv
$ python3 -m venv <VENV>
```
3. Activate the virtual environment by typing ```$ . PATH_TO_VENV/bin/activate``` in the terminal. Make sure you are in the directory which contains the virtual environment. To check, type in ```ls``` to get a current listing of the files in your current working directory.  
4. Upload your API key in the ```/api``` folder. Name the file ```meme.txt```. For instructions on how to get your API key, see the APIs section above.
4. Install the following dependencies:
```
$ sudo pip install wheel
$ sudo pip install Flask
``` 
5. Clone this repo by typing ```$ git clone git@github.com:tangym27/ruffLife.git``` in the terminal. 
6. Change into the repo (```cd ruffLife```)and run the python file by typing ```$ python app.py``` in the terminal. 
7. If successful, the following message will appear in the terminal:
```
* Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
* Restarting with stat
* Debugger is active!
* Debugger PIN: 248-748-502
```
  
Flask: Runs the web application on local host.
Wheel: Used for Flask.
SQLite: Creates databases for storing information.
URLLib3: Receives information from APIs.
 ## Dependencies: 
 1. URLLib3: process apis
 2. sqlite : mangages our database 
 3. python(flask) : runs our web application 
