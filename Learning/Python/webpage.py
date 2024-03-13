# this are similar to the #include used in c or cpp
# here you can import a full library or just some functions from that library
# here we are importing the functions Flask, render_template, send_from_directory from the library (or module) Flask, these are used to create a web page
from flask import Flask, render_template, send_from_directory
# here I imort the whole module os (operative system) it is usefull for example to join paths regardless on the OS, for example, in linux the paths are sss/fff/ggg and in windows they are sss\fff\ggg
# so this library lets us do it automatically
import os
# now this library is used to create plots
import matplotlib.pyplot as plt
#this one is used to get the path of the current file
from pathlib import Path


def ensure_static_folder_exists():
    static_folder = os.path.join(app.root_path, 'static')
    if not os.path.exists(static_folder):
        os.makedirs(static_folder)


def create_image():
    # Ensure the static folder exists
    ensure_static_folder_exists()
    plt.plot([1, 2, 3, 4])
    plt.ylabel('some numbers')
    image_path=os.path.join(Path(__file__).parent.absolute(),"static",'plot.png')
    plt.savefig( image_path)  # Save the plot as a PNG file

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

if __name__ == '__main__':
    create_image()
    app.run(host='0.0.0.0', port=5000, debug=True)