import json


def send_message_to_mourner(name, email_or_ph_number, message):
    with open('messages.txt', 'a+') as f:
        text = f'''{name}:\n{message}\n\n{email_or_ph_number}\n{"-"*80}\n'''
        f.write(text)


def read_data_from_json(file_path):
    with open(file_path, 'rb') as f:
        return json.load(f)

def create_template_data_from_data(data,view_data):
    bio = {"name":data["Name"],"biography":data["Biography"],"background_img_path":data["BackgroundImagePath"]}
    quotes = []

    for quote in data["Quotes"]:
        quotes.append(
            {"text":quote["Text"],"author":quote["Author"]}
        )

    images = []

    for img in data["Images"]:
        images.append(
            {"path":img["Path"],"description":img["Description"]}
        )
    musics = []

    for music in data["Musics"]:
        musics.append(
            {"path":music["Path"],"description":music["Description"],"cover_path":music["CoverPath"]}
        )

    view_data["info"] = bio
    view_data["quotes"] = quotes
    view_data["images"] = images
    view_data["musics"] = musics

def contact_as_dict(name,email,mes):
    return {"name":name,"email":email,"message":mes}