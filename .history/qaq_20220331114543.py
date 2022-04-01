from ast import Return
import re
from urllib import request
from flask import Flask,render_template
app = Flask(__name__)
# receive wasd from micro bit
# by ljc00118

# snake
# send the map to flask
# by leap_frog

fresh_s = 2
@app.route('/', methods=['GET', 'POST'])
def index() :
    # send fresh_speed
    ansd = request.form.get('sd')
    ansu = request.form.get('su')
    return render_template('draw.html', fresh_speed=fresh_s)
app.run()