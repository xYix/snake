from flask import Flask,render_template,request
app = Flask(__name__)

# receive wasd from micro bit
# by ljc00118

# snake
# send the map to flask
# by leap_frog

fresh_s = 2
now_hint = 'welcome'
@app.route('/', methods=['GET', 'POST'])
def index() :
    # send fresh_speed
    global fresh_s
    global now_hint
    ansd = request.form.get('sd')
    if ansd == 'speed_down' :
        fresh_s += 0.25
    ansu = request.form.get('su')
    if ansu == 'speed_up' :
        fresh_s -= 0.25
        if fresh_s < 0.25 :
            fresh_s = 0.25
            now_hint = 'speed limit exceeded'
        fresh_s = max(fresh_s, 0.25)
    # print(ansd, ansu)
    return render_template('draw.html', fresh_speed=fresh_s, hint = now_hint)
app.run()