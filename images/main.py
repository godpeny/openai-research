from flask import Flask, render_template, request
app = Flask(__name__)
import os
import openai
from dotenv import load_dotenv
import requests

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
@app.route('/')
def hello_world():  # put application's code here
    print(openai)
    response = openai.Image.create(
        prompt="a white siamese cat",
        n=1,
        size="256x256"
    )
    image_url = response['data'][0]['url']

    return image_url

if __name__ == '__main__':
    app.run()
