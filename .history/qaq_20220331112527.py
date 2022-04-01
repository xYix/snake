from ast import Return
from urllib import request
from flask import Flask,render_template
app = Flask(__name__)
# receive wasd from micro bit
# by leap_frog

# snake
# send the map to flask
# by ljc00118

fresh_s = 20
@app.route('/', methods=['GET', 'POST'])
def index() :
    # send fresh_speed
    # ans = request.form.get()
    return render_template('draw.html', fresh_speed=fresh_speed)
app.run()