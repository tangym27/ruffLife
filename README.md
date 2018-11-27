# ruffLife
# Xiaojie (Aaron) Li, Bo Hui Lu, Michelle Tang, Kaitlin Wan
P #01: ArRESTed Development

## Instructions to Run:

1. Check to see if you have python3 installed by running ``` python3 ``` in the terminal. It should produce something like: 
```
Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 26 2018, 20:42:06) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
```
2. Install virtualenv and create your own environment by running the following in terminal. Replace <VENV> with the name of your virtual environment (your choice).
```
$ sudo pip install virtualenv
$ virtualenv <VENV>
```
3. Activate the virtual environment by typing ```$ . <VENV>/bin/activate``` in the terminal. Make sure you are in the directory which contains the virtual environment. To check, type in ```ls``` to get a current listing of the files in your current working directory.  
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
