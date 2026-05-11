from fastapi import FastAPI
import eiscp
from time import sleep
 
app = FastAPI()

@app.get("/")
def read_root():
    return {"This is an api for Onkyo and Integra Receivers xoxo\n You can find docs @ /docs\n"}

@app.get("/api/onkyo/{zone}")
def read_item(zone: str| None = None):
    if zone == "main" or zone == "2":
        status = zone_On(zone)
    else:
        status = "Failure"
    
    return {"zone": zone, "sucess": status}




def zone_On(z):

    commands = {"z1on":"SLI23","z2on":"SLZ12","z1off":"PWR00","z2off":"ZPW00"}
    
    # Create a receiver object, connecting to the host
    receiver = eiscp.eISCP('192.168.1.15')

    #get power status
    if z == "main":
        status = receiver.raw('PWRQSTN')
    else:
        status = receiver.raw('ZPWQSTN')


    if status[-2:] == "00":
        if z == "main":
            # Turn the receiver on, select input
            receiver.raw(commands["z1on"])
          
            
        else:
            receiver.raw(commands["z2on"])
       


    elif status[-2:] == "01":
        if z == "main":
            receiver.raw(commands["z1off"])
        else:
            receiver.raw(commands["z2off"])
        

    #bugg
    #receiver.command('power', 'on', zone ='main')
    #status = receiver.command('CD' 'source', zone='main')

    receiver.disconnect()
    return str(receiver)
