# WEATHER API APP

This is an app that allows you to know the forecast for a region in the coming days. To do this, it consumes a third-party service, through the API -> [WeatherAPI](https://www.weatherapi.com/) 

## USAGE

You will find all the documentation about the API through to the Swagger tool, in the following link

### CORE

If you want to take a look at the code, I recommend starting with the **thrd_api** directory, this contains the entire core of the requests to the API and the abstractions of the models.

### FLASK MODULES

The app module contains all the necessary configurations, if you want to change something make sure you understand how this micro-framework works. I leave you the official documentation -> [Flask](https://flask.palletsprojects.com/en/stable/quickstart/)

### GUNICORN 

Flask runs on the gunicorn WSGI server. It was deployed here as there are plans to deploy it to a remote Nginx server in the future -> [Gunicorn](https://gunicorn.org/#docs)