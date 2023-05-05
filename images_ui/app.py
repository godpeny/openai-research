import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        img_req = request.form["img_req"]
        response = openai.Image.create(
            prompt=img_req,
            n=1,
            size="1024x1024"
        )

        image_url = response['data'][0]['url']
        return redirect(url_for("index", result=image_url))

    result = request.args.get("result")
    return render_template("index.html", result=result)

