Python Web Development Frameworks

1. Flask - Lightweight
2. FastAPI - Preferred
3. Djnago - Most Preferred for Web


FastAPI Development

FastAPI is a modern, high-performance Python web framework 
used to build RESTful APIs quickly and reliably. 

It is designed specifically for API-first development 
and is widely adopted for deploying 
Machine Learning, NLP, LLM, and Generative AI models as 
production services.

To use FastAPI we need to install fastapi and uvicorn libraries.

To serve web app we must have web server - for fastapi 
we are using uvicorn.

pip install fastapi uvicorn

First App


from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "FastAPI is running"}
	
To run execute command

uvicorn main:app --reload

1. Create folder first-app

2. Create venv

python -m venv venv

It creates venv folder which has many subfolders.

3. Activate venv

venv\Scripts\activate

4. Create requirements.txt file and add libraries to install

5. Execute command to install libraries

pip install -r requirements.txt

If we installed modules/libraries on our own without requirements.txt file.
We can generate requirements.txt file

pip freeze > requirements.txt

API receives data through parameters or body(JSON format).

JSON is JavaScript Object Notation.

It is same as dict in python.

Web APIs are served through HTTP / HTTPS protocol.

Web APIs are served using different methods

1. GET - To receive data
2. POST - To insert data
3. PUT - To update data
4. DELETE - To delete data

Only GET method can be accessed through browser.

All methods are accessed as API.

To test APIs we use Postman software.
To call APIs in JavaScript we use fetch API.

To run project

uvicorn main:app --reload

To connect with mysql database we need to install 2 libraries
sqlalchemy pymysql

pip install sqlalchemy pymysql

To keep information about database

1. host 2. username 3. password 4. database name

use environment file

pip install python-dotenv

To keep password safe 

pip install passlib[bcrypt]

To validate email

pip install pydantic[email]
