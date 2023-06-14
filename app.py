from flask import Flask
import requests

app = Flask(__name__)


@app.route('/')
def main_route():  # put application's code here
    return 'How dare you not specify a route!!! There is nothing but ghosts here, begone...'

@app.route('/randompic')
def random_pic():
    pic = requests.get(url='https://picsum.photos/seed/picsum/200/300')

    return {'pic':pic}, 200

if __name__ == '__main__':
    app.run()
