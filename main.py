from random import randrange
from flask import Flask, redirect, render_template,request
from utiliti import *
from typing import *
import re

# load data from json file
data = read_data_from_json('data.json')

# some important information or static
PROJECT_NAME_EN = data['ProjectNameEN']
WEBSITE_TITLE = data['Title']
VIEW_DATA = {"title":WEBSITE_TITLE}
VIEW_DATA["project_name"] = PROJECT_NAME_EN
VIEW_DATA["name"] = data["Name"]
IS_ERROR_SHOWED = False

QUOTES_LEN = 0

app = Flask(PROJECT_NAME_EN, static_url_path="",
            static_folder="static/", template_folder="static/template/")


@app.route("/")
def home():
    global IS_ERROR_SHOWED

    # select a random quote from quotes
    VIEW_DATA["quote"] = VIEW_DATA["quotes"][randrange(QUOTES_LEN)]


    # if there is result for submitted contact form, delete it (IF WAS SENT)
    # view_data = template data
    if "contact" in VIEW_DATA:
        if "was sent" in VIEW_DATA["result"]:
            del VIEW_DATA["contact"]

    # again the same
    if IS_ERROR_SHOWED:
        if "contact" in VIEW_DATA:
            del VIEW_DATA["contact"]
        if "result" in VIEW_DATA:
            # result is form result
            del VIEW_DATA["result"]
    
    if "result" in VIEW_DATA:
        IS_ERROR_SHOWED = True

    
    return render_template("index.html",data = VIEW_DATA)

@app.route("/sendMessage/",methods=['POST'])
def send_message():
    global IS_ERROR_SHOWED
    IS_ERROR_SHOWED = False
    name = request.form['name']
    # email or phone number
    email_phone_number = request.form['email']
    message = request.form['message']
    if name == "" or email_phone_number == "" or message == "":
            VIEW_DATA["result"] = "Fill all fields"
            VIEW_DATA["contact"] = contact_as_dict(name,email_phone_number,message)
            return redirect('/#contact')
    # email validation
    match = re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+',email_phone_number)
    if len(match) < 1:
        if match[0] == '':
            VIEW_DATA["result"] = "The Email is invalid"
            VIEW_DATA["contact"] = contact_as_dict(name,email_phone_number,message)
            return redirect('/#contact')

    if len(name) < 3:
            VIEW_DATA["result"] = "The name is too short"
            VIEW_DATA["contact"] = contact_as_dict(name,email_phone_number,message)
            return redirect('/#contact')
    if len(message) < 3:
            VIEW_DATA["result"] = "The Message is too short"
            VIEW_DATA["contact"] = contact_as_dict(name,email_phone_number,message)
            return redirect('/#contact')

    send_message_to_mourner(name,email_phone_number,message)

    VIEW_DATA["result"] = "The message was sent"
    return redirect('/#contact')


if __name__ == "__main__":
    # create view data from json data (dict to dict)
    create_template_data_from_data(data,VIEW_DATA)
    del data
    # get len of quotes
    QUOTES_LEN = len(VIEW_DATA["quotes"])
    app.run("", 8080,debug=True)
