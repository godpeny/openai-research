from flask import Flask, render_template, request

app = Flask(__name__)
import os
import openai
from dotenv import load_dotenv
from io import BytesIO
from PIL import Image


load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route('/show')
def show():
    try:
        response = openai.Image.create(
            prompt="white dogs",
            n=1,
            size="256x256"
        )
        image_url = response['data'][0]['url']
        return image_url
    except openai.error.OpenAIError as e:
        return e.http_status + e.error


@app.route('/edit')  # TODO(@godpeny) : not working properly. guessed it is 'openai''s issue.
def edit():
    try:
        response = openai.Image.create_edit(
            image=open("img.png", "rb"),
            mask=open("mask.png", "rb"),
            prompt="A sunlit indoor lounge area with a pool containing a chair",
            n=1,
            size="256x256"
        )
        image_url = response['data'][0]['url']
        return image_url
    except openai.error.OpenAIError as e:
        return e.http_status + e.error


@app.route('/variation')
def variation():
    try:
        response = openai.Image.create_variation(
            image=open("corgi_and_cat_paw.png", "rb"),
            n=1,
            size="1024x1024"
        )
        image_url = response['data'][0]['url']
        return image_url
    except openai.error.OpenAIError as e:
        return e.http_status + e.error


@app.route('/byte')
def byte():
    try:
        # Read the image file from disk and resize it
        image = Image.open("corgi_and_cat_paw.png")
        width, height = 256, 256
        image = image.resize((width, height))

        # Convert the image to a BytesIO object
        byte_stream = BytesIO()
        image.save(byte_stream, format='PNG')
        byte_array = byte_stream.getvalue()

        response = openai.Image.create_variation(
            image=byte_array,
            n=1,
            size="1024x1024"
        )
        image_url = response['data'][0]['url']
        return image_url
    except openai.error.OpenAIError as e:
        return e.http_status + e.error


if __name__ == '__main__':
    app.run()
