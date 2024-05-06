from flask import Flask, render_template
from dist.Controllers.Lamps_Controller import *
from dist.Controllers.Window_Controller import *

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/climate')
def climate():
    return render_template('climate.html')
@app.route('/lighting')
def lighting():
    lamp = Lamps_Controller()
    state_1 = lamp.state_of_lamps_section(1,1)
    if state_1:
        state_1 = 'Включено'
    else:
        state_1 = 'Выключено'
    state_2 = lamp.state_of_lamps_section(1, 2)
    if state_2:
        state_2 = 'Включено'
    else:
        state_2 = 'Выключено'
    state_all = lamp.state_of_lamps(1)
    if state_all:
        state_all = 'Включено'
    else:
        state_all = 'Выключено'
    windows = Window_Controller()
    windows = windows.window_state(1)
    return render_template('lighting.html',state1 = state_1,state_2 = state_2,state_all = state_all,windows = windows)
@app.route('/lighting/<id>')
def lighting_id(id):
    lamp = Lamps_Controller()
    state1 = lamp.state_of_lamps_section(id, 1)
    if state1:
        state1 = 'Включено'
    else:
        state1 = 'Выключено'
    state2 = lamp.state_of_lamps_section(id, 2)
    if state2:
        state2 = 'Включено'
    else:
        state2 = 'Выключено'
    stateAll = lamp.state_of_lamps(id)
    if stateAll:
        stateAll = 'Включено'
    else:
        stateAll = 'Выключено'
    windows = Window_Controller()
    windows = windows.window_state(id)
    return render_template('lighting.html', state1=state1, state_2=state2, state_all=stateAll, windows=windows)
@app.route('/safety')
def safety():
    return render_template('safety.html')
@app.route('/admin')
def admin():
    return render_template('admin.html')




if __name__ == '__main__':
    app.run(debug=True)