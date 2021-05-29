from flask import Flask, render_template, send_file, request, jsonify, url_for
from flask import has_request_context


import logging
from flask.logging import default_handler
import werkzeug
import random
import giphy_client 
import json
from urllib.parse import unquote

app = Flask(__name__)
giphy_api_instance = giphy_client.DefaultApi()

FIRST="👫👩‍❤️‍👨➡️👰💍🤵"
FIRSTBIS="👫👩‍❤️‍👨➡️👰‍♀️💍🤵‍♂️"

SECOND="👨‍🎓➡️🇫🇷✈️🇺🇸"
THIRD= "📖🍰➡️👩‍🍳"
FORTH= "🛏️🍆💦🍑🎯➡️👩‍⚕️"
FORTHBIS= "🛏🍆💦🍑🎯➡️👩‍⚕️"
BAD = "__➡️___/_➡️___/__➡️_/_____➡️_/"
BADBIS = "__>___/_>___/__>_/_____>_/"

ALL = [FIRST,SECOND,THIRD,FORTH]
ALLBIS = [FIRSTBIS,SECOND,THIRD,FORTH]
ALLTER = [FIRSTBIS,SECOND,THIRD,FORTHBIS]
ALLQUAT = [FIRST,SECOND,THIRD,FORTHBIS]

VIDEO_NAME = "🎥👶.mp4"
PICTURE_NAME = "🤰🧸🍼.png"
GIPHY_API_KEY = 'McE84nsFWgLGXTcGYnP5AR9qaVlYmuSW'

# load failure quotes
with open("./failures_messages.txt") as f:
    failures_messages = f.readlines()
# you may also want to remove whitespace characters like `\n` at the end of each line
failures_messages = [x.strip() for x in failures_messages] 

print('/'.join(ALL[:4]))

@app.before_request
def before_request_func():
    print("TOTO", unquote(request.url))

@app.route("/")
def index():
    return render_template("intro.html", host="http://localhost:5000/")

@app.route(f"/{BAD}")
def bad():
    return render_template("badsolution.html", host="http://localhost:5000/")


@app.route(f"/{'/'.join(ALL[:1])}/")
@app.route(f"/{'/'.join(ALLBIS[:1])}/")
@app.route(f"/{'/'.join(ALLTER[:1])}/")
@app.route(f"/{'/'.join(ALLQUAT[:1])}/")
def level1():
    try:
        gif_query = giphy_api_instance.gifs_random_get(GIPHY_API_KEY, tag="success")
        image_url = gif_query.data.image_url
    except Exception as e:
        image_url = url_for('static', filename='success.webp')

    return render_template("level1.html", host="http://localhost:5000/", image_url=image_url)

@app.route(f"/{'/'.join(ALL[:2])}/")
@app.route(f"/{'/'.join(ALLBIS[:2])}/")
@app.route(f"/{'/'.join(ALLTER[:1])}/")
@app.route(f"/{'/'.join(ALLQUAT[:1])}/")
def level2():
    try:
        gif_query = giphy_api_instance.gifs_random_get(GIPHY_API_KEY, tag="success")
        image_url = gif_query.data.image_url
    except Exception as e:
        image_url= url_for('static', filename='success.webp')
    return render_template("level2.html", host="http://localhost:5000/", image_url=image_url)

@app.route(f"/{'/'.join(ALL[:3])}/")
@app.route(f"/{'/'.join(ALLBIS[:3])}/")
@app.route(f"/{'/'.join(ALLTER[:3])}/")
@app.route(f"/{'/'.join(ALLQUAT[:3])}/")
def level3():
    try:
        gif_query = giphy_api_instance.gifs_random_get(GIPHY_API_KEY, tag="success")
        image_url = gif_query.data.image_url
    except Exception as e:
        image_url= url_for('static', filename='success.webp')
    return render_template("level3.html", host="http://localhost:5000/", image_url=image_url)

@app.route(f"/{'/'.join(ALL[:4])}/")
@app.route(f"/{'/'.join(ALLBIS[:4])}/")
@app.route(f"/{'/'.join(ALLTER[:4])}/")
@app.route(f"/{'/'.join(ALLQUAT[:4])}/")
def solution():
    return render_template("solution.html", host="http://localhost:5000/")

@app.route(f"/{'/'.join(ALL)}/{VIDEO_NAME}")
@app.route(f"/{'/'.join(ALLBIS)}/{VIDEO_NAME}")
def video():
    return app.send_static_file("🎥👶.mp4")

@app.route(f"/{'/'.join(ALL)}/{PICTURE_NAME}")
@app.route(f"/{'/'.join(ALLBIS)}/{PICTURE_NAME}")
@app.route(f"/{'/'.join(ALLTER)}/{PICTURE_NAME}")
@app.route(f"/{'/'.join(ALLQUAT)}/{PICTURE_NAME}")
def photo():
    return app.send_static_file("🤰🧸🍼.png")


@app.errorhandler(404)
def handle_bad_request(e):
    path = request.path
    spath = path.split("/")[1:]
    lvl = 0
    p = ""
    only_bad_order = False
    for i,p in enumerate(spath):
        if i < len(ALL) and (p == ALL[i] or p == ALLBIS[i] or p == ALLTER[i] or p == ALLQUAT[i]):
            lvl +=1
        else:
            if set(ALL[i]) == set(p) or set(ALLBIS[i]) == set(p) or set(ALLTER[i]) == set(p) or set(ALLQUAT[i]) == set(p):
                only_bad_order = True
            break
    quote = random.choice(failures_messages)
    query_giphy = "fail"
    if only_bad_order:
        lvl = str(lvl) + ": ... presque, peut-etre les symboles ne sont pas dans l'ordre?"
        query_giphy = "almost"
    try: 
        gif_query = giphy_api_instance.gifs_random_get(GIPHY_API_KEY, tag=query_giphy)
        image_url = gif_query.data.image_url
    except Exception as e:
        image_url= url_for('static', filename='100.webp')
    return render_template("fail.html", quote=quote, image_url=image_url, lvl=lvl, host="http://localhost:5000/", answer=p)
    return f'f', 404
