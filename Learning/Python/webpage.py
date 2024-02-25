from flask import Flask, render_template, send_from_directory
import os
import matplotlib.pyplot as plt
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