from __future__ import print_function # WalabotAPI works on both Python 2 an 3.
from sys import platform
from os import system
from imp import load_source
from os.path import join
from configparser import ConfigParser
import requests
import relay
import time


if platform == 'win32':
	modulePath = join('C:/', 'Program Files', 'Walabot', 'WalabotSDK',
		'python', 'WalabotAPI.py')
elif platform.startswith('linux'):
    modulePath = join('/usr', 'share', 'walabot', 'python', 'WalabotAPI.py')     

wlbt = load_source('WalabotAPI', modulePath)
wlbt.Init()

check = True

# Config file


def Writeconfig():
    
#Configuration files in python
    config = ConfigParser()
    config.read('config.ini')
# Arena section
    config.set('WalabotSettings','minradiuscm','10')
    config.set('WalabotSettings','maxradiuscm','50')
    config.set('WalabotSettings','resradiuscm','3')
    config.set('WalabotSettings','mintheta','-15')
    config.set('WalabotSettings','maxtheta','15')
    config.set('WalabotSettings','restheta','5')
    config.set('WalabotSettings','minphi','-60')
    config.set('WalabotSettings','maxphi','60')
    config.set('WalabotSettings','resphi','5')
    config.set('WalabotSettings','mtimode','true')
    config.set('WalabotSettings','threshold','30')
    config.set('WalabotSettings','energythreshold','100')
# Address section
    config.set('WalabotSettings','ipaddress','Raspberry Address')
    config.set('WalabotSettings','port','8089')
# Action section               
    config.set('WalabotSettings','iftttkey key)
    config.set('WalabotSettings','iftrig', 'true')
    config.set('WalabotSettings','dPort', 'true')
    config.set('WalabotSettings','aPort', 'false')
    config.set('WalabotSettings','repeat','once')
    config.set('WalabotSettings','objdetect','in')
        
    with open('config.ini', 'w') as f:
        config.write(f)    
    
def  DoActions(targets):
    global check
    config = ConfigParser()
    config.read('config.ini')
    # Get Action
    iftrig = config.get('WalabotSettings','iftrig')
    aport = config.get('WalabotSettings','aport')
    dport = config.get('WalabotSettings','dport')
    repeat = config.get('WalabotSettings','repeat')
    
    if aport == "True":
        relay.TurnOn ('aport')
    if aport == "False":
        relay.TurnOff ('aport')
    if dport == "True":
        relay.TurnOn ('dport')        
    if dport == "False":
        relay.TurnOff ('dport')
    if iftrig == "True":
        print ("Trig IFTTT")
        TrigIfTTT(targets)
    if repeat == "repeat":
        check = True
    else:
        check = False
   
     
    
def TrigIfTTT(targets):
    config = ConfigParser()
    config.read('config.ini')
    headers = {
    'Content-Type': 'application/json',
    }
    url = 'https://maker.ifttt.com/trigger/wallabot_detect/with/key/'+config.get('WalabotSettings','iftttkey')
    print ('URL : ',url)
    #if disable walabot targets have not value !!
    data = targets    
    print (data)
    response = requests.post(url, headers=headers, data=data)
    print (response.text)
        
def GetEnergy(energy):
    global check
    system('clear')
    config = ConfigParser()
    config.read('config.ini')
# Print Energy
    print (' Energy =  '+ str(energy))
    objdetect =  config.get('WalabotSettings','objdetect')
    engthreshold = int(config.get('WalabotSettings','energythreshold'))
    if objdetect == "increaseEnergy":
        if energy > engthreshold:
            data = '{"value1" : "Energy "'+', "value2" : "'+str(energy)+'"}'
            DoActions(data)
    if objdetect == "decreaseEnergy":
        if energy < engthreshold:
            data = '{"value1" : "Energy "'+', "value2" : "'+str(energy)+'"}'
            DoActions(data)
        

    
    
def GetTrackerTargets(targets):
    global check
    system('clear')
    config = ConfigParser()
    config.read('config.ini')
# Get detect object mode
    objdetect =  config.get('WalabotSettings','objdetect')
    numtargets = len(targets)
    print ('Detect Mode : '+ objdetect + '   Num targets : '+str(numtargets) )
    if objdetect == "in" and numtargets > 0:
    #if targets:
        for i, target in enumerate(targets):
            print('Target #{}:\nx: {}\ny: {}\nz: {}\namplitude: {}\n'.format(
                i + 1, target.xPosCm, target.yPosCm, target.zPosCm,
                target.amplitude))
            v1 = "Target X : "+str(targets[0].xPosCm)
            v2 = "Target Y : "+str(targets[0].yPosCm)
            v3 = "Target Z : "+str(targets[0].zPosCm)    
            # Send the last object in target
            data = '{"value1" : "'+ v1 +'", "value2" : "'+v2+'", "value3" : "'+v3+'"}'
        DoActions(data)
       
    else:
        print('No Target Detected')
        return

    if objdetect == "out"  and  numtargets == 0:
        data = '{"value1" : "Target missing !!" }'
        DoActions(data)
    else: 
        print ('Target exists ')
    

def WalabotApp():
#    Writeconfig()
    global check
    config = ConfigParser()
    config.read('config.ini')
    
    repeat =  config.get('WalabotSettings','repeat')
    if repeat != 'disable':
        print ('Start Walabot Tracking .....')
    # Get Areana
        minInCm = int(config.get('WalabotSettings','minradiuscm'))
        maxInCm = int(config.get('WalabotSettings','maxradiuscm'))
        resInCm = int(config.get('WalabotSettings','resradiuscm'))
    # Get Theta
        minIndegrees = int(config.get('WalabotSettings','mintheta'))
        maxIndegrees = int(config.get('WalabotSettings','maxtheta'))
        resIndegrees = int(config.get('WalabotSettings','restheta'))
    # Get Phi
        minPhiInDegrees = int(config.get('WalabotSettings','minphi'))
        maxPhiInDegrees = int(config.get('WalabotSettings','maxphi'))
        resPhiInDegrees = int(config.get('WalabotSettings','resphi'))
    # Get MTI mode
        mtiMode = config.get('WalabotSettings','mtimode')
    # Get Threshold
        threshold = int(config.get('WalabotSettings','threshold'))
        engthreshold = int(config.get('WalabotSettings','energythreshold'))
    #  Get  Detect mode
        objdetect =  config.get('WalabotSettings','objdetect')
        wlbt.Initialize()
    
    # Initializes walabot lib
        try:
    # 1) Connect : Establish communication with walabot.
            wlbt.ConnectAny()
    # 2) Configure: Set scan profile and arena
    # Set Profile - to Tracker.
            if objdetect == 'increaseEnergy' or objdetect == 'decreaseEnergy':
                wlbt.SetProfile(wlbt.PROF_SENSOR)
            else:
                wlbt.SetProfile(wlbt.PROF_TRACKER)
    # Set threshold
            wlbt.SetThreshold(threshold)
    # Setup arena - specify it by Cartesian coordinates.
            wlbt.SetArenaR(minInCm, maxInCm, resInCm)
    # Sets polar range and resolution of arena (parameters in degrees).
            wlbt.SetArenaTheta(minIndegrees, maxIndegrees, resIndegrees)
    # Sets azimuth range and resolution of arena.(parameters in degrees).
            wlbt.SetArenaPhi(minPhiInDegrees, maxPhiInDegrees, resPhiInDegrees)
    # Moving Target Identification: standard dynamic-imaging filter
            if mtiMode == "True":
                filterType = wlbt.FILTER_TYPE_MTI
            else:
                filterType = wlbt.FILTER_TYPE_NONE
            wlbt.SetDynamicImageFilter(filterType)
    # 3) Start: Start the system in preparation for scanning.
            wlbt.Start()
            if mtiMode == "False":  # if MTI mode is not set - start calibrartion
        # calibrates scanning to ignore or reduce the signals
                wlbt.StartCalibration()
                while wlbt.GetStatus()[0] == wlbt.STATUS_CALIBRATING:
                    wlbt.Trigger()
            while check:
                appStatus, calibrationProcess = wlbt.GetStatus()
        # 5) Trigger: Scan(sense) according to profile and record signals
        # to be available for processing and retrieval.
                wlbt.Trigger()
        # 6) Get action: retrieve the last completed triggered recording
                if objdetect == 'increaseEnergy' or objdetect == 'decreaseEnergy':
                    energy  = int(wlbt.GetImageEnergy()*10000000)
                    GetEnergy(energy)
                else:
                    targets = wlbt.GetTrackerTargets()
        # Get TrackerTargets(targets)
        #          rasterImage, x, y, sliceDepth, power = wlbt.GetRawImageSlice()
        #            col_sum = [sum([rasterImage[i][j] for i in range(x)]) for j in range(y)]
        #            left_sum = sum(col_sum[:y//2])
        #            right_sum = sum(col_sum[y//2:])
        #            print_data = '{:<130} Left Energy: {:<10} Right Energy: {:<10}'.format(str(col_sum), left_sum, right_sum)
        #            print(print_data)
                    GetTrackerTargets(targets)
        #        time.sleep (1)     # For prevent libusb error  not sure it's help
    
    # 7) Stop and Disconnect.
        except WalabotAPI.WalabotError as err:
            print("Failed to connect to Walabot.\nerror code: " + str(err.code))
        finally:
            wlbt.Stop()
            wlbt.Disconnect()
            wlbt.Clean()
            check = True
            print('Terminate successfully')
    else:   # Disable Walabot
        msg = '{"value1" : "Disable Walabot"}'
        DoActions(msg)
       

if __name__ == '__main__':
    WalabotApp()
