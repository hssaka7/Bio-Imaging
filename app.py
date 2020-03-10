from flask import Flask

app = Flask(__name__)

def home():
    return "WIP for the Bio imaging app home page"

if  __name__ == "__main__":
   app.run()



