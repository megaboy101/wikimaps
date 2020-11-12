import time
from flask import Flask
from wikimap import Wikimap

app = Flask(__name__)

@app.route('/path')
def path():
    wikimap = Wikimap('c:\\path\\to\\data.sqlite')
    src_id = 12345
    dest_id = 54321
    path = wikimap.determine_path(src_id, dest_id)
    return { 'path': path }