# fuelwatchcav
A cavorite and historygraph based implementation of fuelwatch

First create a virtual environment

virtualenv venv 

source venv/bin/activate

pip install --upgrade pip 

pip install --upgrade setuptools urllib3[secure]

pip install fabric3==1.13.1.post1  # We use fabric3 to automate tasks
pip install django==1.11.10  # We need django in the venv to create apps in our project

