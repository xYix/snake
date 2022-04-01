from flask import Flask,render_template,request
app = Flask(__name__)
# receive wasd from micro bit
# by ljc00118

fresh_s = 2
# snake
# send the map to flask
# by leap_frog

@app.route('/', methods=['GET', 'POST'])
def index() :
    # send fresh_speed
    ansd = request.form.get('sd')
    if ansd == 'speed_down' :
        
    ansu = request.form.get('su')
    print(ansd, ansu)
    return render_template('draw.html', fresh_speed=fresh_s)
app.run()