Python 3.11.0 (main, Oct 24 2022, 18:26:48) [MSC v.1933 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import  wiotp.sdk.device
... import  time
... import  os
... import  datetime
... import  random
... myconfig = {
...     "identity": {
...         "orgId": "eop5qk",
...         "typeId": "NodeMCU",
...         "deviceId": "12345"
...     },
...     "auth": {
...         "token": "ei0i7Fp@6V!LE5PWdN"
...         }
... }
... client = wiotp.sdk.device.DeviceClient(config=myconfig, logHandlers=None)
... client.connect()
... def myCommandCallback(cmd):
...     print("Message received from IBM IoT platform: %s"  % cmd.data['command'])
...     m=cmd.data['command']
...     if(m=="motoron"):
...         print("motor & sprinkler is switched on")
...     elif(m=="motoroff"):
...         print("motor & sprinkler is switched OFF")
...     print("  ")
... while True:
...     soil=random.randint(0,100)
...     temp=random.randint(-20,125)
...     hum=random.randint(0,100)
...     myData={'soilmoisture':soil, 'temperature' :temp, 'humidity' :hum}
...     client.publishEvent(eventId="status", msgFormat="json", data=myData, qos=0, onPublish=None)
...     print("Published data Successfully: %s", myData)
...     time.sleep(2)
...     client.myCommandCallback = myCommandCallback
