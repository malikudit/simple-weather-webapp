# Weather webapp
This is a simple Flask-based weather app written in Python that uses the Openweathermap API.

## Running the webapp locally
To run the application locally, type the following in your terminal to clone the repository:
```
$ git clone https://github.com/malikudit/weather-webapp.git
```

Create a virtual environment to run the app in:
```
$ python -m venv venv
$ venv\Scripts\activate
```
There should now be a (venv) prefixed before all your commands in the terminal.

You can now proceed to install the dependencies needed to run the app:
```
$ pip install -r requirements.txt
```

To run the app locally, you will need to obtain an API key from Openweathermap - you can do so [here.](https://home.openweathermap.org/api_keys)
Once you do so, edit line 8 in weather.py with your newly obtained API key:
```
api_key = "INSERT_API_KEY_HERE"
```

Finally, in your terminal, type the following to run the app:
```
$ py main.py
```

You should now see the app running in your browser if you go to the following link:
```
localhost:5000
```
