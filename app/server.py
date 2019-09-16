import os
import json

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/healthcheck')
def healthcheck():
    return "WORKING"


# @app.route('/process/video/<int:video_id>')
# def process_video(video_id):
#     rc = get_sentinel_connect(settings)
#     rc.rpush(settings.LIST_REDIS, video_id)
#     return "processing video"


@app.route('/hello')
def hello():
    return "HELLOOOOOO !!!!"

@app.route('/helloTest', methods=['POST'])
def relloTest():
    user =  request.form['username'];
    return json.dumps({'status':'OK','user':user});

@app.route('/')
def main_page():
    print("aqui !!!: {}".format(os.listdir()))
    return render_template('/index.html')


if __name__ == '__main__':
    app.run(port=(os.getenv("PORT") or 8000))
