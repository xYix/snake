from flask import Flask,render_template,request
app = Flask(__name__)
# receive wasd from micro bit
# by ljc00118

global 
fresh_s = 2
# snake
# send the map to flask
# by leap_frog

@app.route('/', methods=['GET', 'POST'])
fresh_s = 2
def index() :
    # send fresh_speed
    ansd = request.form.get('sd')
    if ansd == 'speed_down' :
        fresh_s += 0.25
    ansu = request.form.get('su')
    if ansu == 'speed_up' :
        fresh_s -= 0.25
    print(ansd, ansu)
    return render_template('draw.html', fresh_speed=fresh_s)
app.run()