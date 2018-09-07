from flask import Flask, render_template
from os import system
from flask_socketio import SocketIO, emit
from configparser import ConfigParser
import json


import walabotIF

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('walabot.html')

@socketio.on('my event', namespace='/test')
def test_message(message):
    emit('my response', {'data': message['data']})

@socketio.on('my broadcast event', namespace='/walabot')
def test_message(message):
    emit('my response', {'data': message['data']}, broadcast=True)

@socketio.on('connect', namespace='/walabot')
def test_connect():
    emit('my response', {'data': 'Connected'})

@socketio.on('disconnect', namespace='/walabot')
def test_disconnect():
    print('Client disconnected')
 # Register for event message    
@socketio.on('message')
def handle_message(message):
    system('clear')
    print ('Get message : '+ str(message))
    json_to_config (message) 
    walabotIF.WalabotApp()
     

    
def json_to_config(message):
    config = ConfigParser()
    config.read('config.ini')
    wconfig = json.loads(str(message))
# Arena section    
    config.set('WalabotSettings','minradiuscm',str(wconfig['walabotArena']['radiusMin']))
    config.set('WalabotSettings','maxradiuscm',str(wconfig['walabotArena']['radiusMax']))
    config.set('WalabotSettings','resradiuscm',str(wconfig['walabotArena']['radiusRes']))  
    config.set('WalabotSettings','mintheta',str(wconfig['walabotArena']['thetaMin']))
    config.set('WalabotSettings','maxtheta',str(wconfig['walabotArena']['thetaMax']))
    config.set('WalabotSettings','restheta',str(wconfig['walabotArena']['thetaRes']))
    config.set('WalabotSettings','minphi',str(wconfig['walabotArena']['phiMin']))
    config.set('WalabotSettings','maxphi',str(wconfig['walabotArena']['phiMax'])) 
    config.set('WalabotSettings','resphi',str(wconfig['walabotArena']['phiRes']))
    config.set('WalabotSettings','mtimode',str(wconfig['walabotArena']['mti']))
    config.set('WalabotSettings','threshold',str(wconfig['walabotArena']['threshold']))
    config.set('WalabotSettings','energythreshold',str(wconfig['walabotArena']['energythreshold']))
# Address section    
    config.set('WalabotSettings','ipaddress', wconfig['walabotAddress']['ip'])
    config.set('WalabotSettings','port',str(wconfig['walabotAddress']['port']))
# Action section               
    config.set('WalabotSettings','iftttkey',str(wconfig['walabotAction']['ifKey']))
    config.set('WalabotSettings','iftrig',str(wconfig['walabotAction']['iftttTrig']))
    config.set('WalabotSettings','dPort',str(wconfig['walabotAction']['dPort']))
    config.set('WalabotSettings','aPort',str(wconfig['walabotAction']['aPort']))
    config.set('WalabotSettings','repeat',wconfig['walabotAction']['repeat'])
    config.set('WalabotSettings','objdetect',wconfig['walabotAction']['objDetect'])
#Write config
    with open('config.ini', 'w') as f:
        config.write(f)    

if __name__ == '__main__':
     socketio.run(app,host='Raspberry Pi Address',port=8089,debug=True)
    

     