from fastapi import FastAPI

#initialize app
app = FastAPI()

#Write down the routes
"""
If you want to retrieve write app.get
for adding app.post, for updating app.put,
for deleting app.delete
"""

@app.get('/')
def index():
    return {'message':'Hellow,FastAPI'}


"""
2.	Run the start up command
	uvicorn main:app --reload
	Telling uvicorn: Run the app object defined in the main.py file and keep watching for any file changes so you can auto-reload the server

"""