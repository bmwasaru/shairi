import os
import re
from datetime import datetime

from flask import Flask, render_template

app = Flask(__name__)


def get_date_from_filename(filename):
    # Assuming the date is in the format "DD-MM-YY"
    pattern = r'\d{2}-\d{2}-\d{2}'
    match = re.search(pattern, filename)
    if match:
        return match.group()
    else:
        return None

def process_text_files(directory_path):

    txt_files_content = {}

    txt_files = [f for f in os.listdir(directory_path) if f.endswith('.txt')]
    # Sort files based on the date extracted from the filename
    sorted_files = sorted(txt_files, key=lambda x: datetime.strptime(get_date_from_filename(x), "%d-%m-%y"))

    for filename in sorted_files:
        file_path = os.path.join(directory_path, filename)
        with open(file_path, 'r') as file:
            content = file.read()
            txt_files_content.update({filename: content})

    return txt_files_content


@app.route('/')
def index():
    content = process_text_files("../mashairi/")
    
    return render_template("index.html", files_content=content)

if __name__ == "__main__":
    app.run()
