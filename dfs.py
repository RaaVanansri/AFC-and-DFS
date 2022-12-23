import random
channels = {
    36:{"Frequency":"20Mhz","DFS":False,"Availability":random.randint(0,1),"TDWR":False},
    40:{"Frequency":"20Mhz","DFS":False,"Availability":random.randint(0,1),"TDWR":False},
    44:{"Frequency":"20Mhz","DFS":False,"Availability":random.randint(0,1),"TDWR":False},
    48:{"Frequency":"20Mhz","DFS":False,"Availability":random.randint(0,1),"TDWR":False},
    149:{"Frequency":"20Mhz","DFS":False,"Availability":random.randint(0,1),"TDWR":False},
    153:{"Frequency":"20Mhz","DFS":False,"Availability":random.randint(0,1),"TDWR":False},
    157:{"Frequency":"20Mhz","DFS":False,"Availability":random.randint(0,1),"TDWR":False},
    161:{"Frequency":"20Mhz","DFS":False,"Availability":random.randint(0,1),"TDWR":False},
    165:{"Frequency":"20Mhz","DFS":False,"Availability":random.randint(0,1),"TDWR":False},
    52:{"Frequency":"20Mhz","DFS":True,"Availability":random.randint(0,1),"TDWR":False},
    56:{"Frequency":"20Mhz","DFS":True,"Availability":random.randint(0,1),"TDWR":False},
    60:{"Frequency":"20Mhz","DFS":True,"Availability":random.randint(0,1),"TDWR":False},
    64:{"Frequency":"20Mhz","DFS":True,"Availability":random.randint(0,1),"TDWR":False},
    144:{"Frequency":"20Mhz","DFS":True,"Availability":random.randint(0,1),"TDWR":False},
    100:{"Frequency":"20Mhz","DFS":True,"Availability":random.randint(0,1),"TDWR":False},
    104:{"Frequency":"20Mhz","DFS":True,"Availability":random.randint(0,1),"TDWR":False},
    108:{"Frequency":"20Mhz","DFS":True,"Availability":random.randint(0,1),"TDWR":False},
    112:{"Frequency":"20Mhz","DFS":True,"Availability":random.randint(0,1),"TDWR":False},
    116:{"Frequency":"20Mhz","DFS":True,"Availability":random.randint(0,1),"TDWR":False},
    120:{"Frequency":"20Mhz","DFS":True,"Availability":random.randint(0,1),"TDWR":True},
    124:{"Frequency":"20Mhz","DFS":True,"Availability":random.randint(0,1),"TDWR":True},
    128:{"Frequency":"20Mhz","DFS":True,"Availability":random.randint(0,1),"TDWR":True},
    132:{"Frequency":"20Mhz","DFS":True,"Availability":random.randint(0,1),"TDWR":False},
    136:{"Frequency":"20Mhz","DFS":True,"Availability":random.randint(0,1),"TDWR":False},
    140:{"Frequency":"20Mhz","DFS":True,"Availability":random.randint(0,1),"TDWR":False},
    38:{"Frequency":"40Mhz","DFS":False,"Availability":random.randint(0,1),"TDWR":False},
    46:{"Frequency":"40Mhz","DFS":False,"Availability":random.randint(0,1),"TDWR":False},
    54:{"Frequency":"40Mhz","DFS":True,"Availability":random.randint(0,1),"TDWR":False},
    62:{"Frequency":"40Mhz","DFS":True,"Availability":random.randint(0,1),"TDWR":False},
    102:{"Frequency":"40Mhz","DFS":True,"Availability":random.randint(0,1),"TDWR":False},
    110:{"Frequency":"40Mhz","DFS":True,"Availability":random.randint(0,1),"TDWR":False},
    118:{"Frequency":"40Mhz","DFS":True,"Availability":random.randint(0,1),"TDWR":True},
    126:{"Frequency":"40Mhz","DFS":True,"Availability":random.randint(0,1),"TDWR":False},
    134:{"Frequency":"40Mhz","DFS":True,"Availability":random.randint(0,1),"TDWR":False},
    142:{"Frequency":"40Mhz","DFS":True,"Availability":random.randint(0,1),"TDWR":False},
    151:{"Frequency":"40Mhz","DFS":False,"Availability":random.randint(0,1),"TDWR":False},
    159:{"Frequency":"40Mhz","DFS":False,"Availability":random.randint(0,1),"TDWR":False},
    155:{"Frequency":"80Mhz","DFS":False,"Availability":random.randint(0,1),"TDWR":False},
    42:{"Frequency":"80Mhz","DFS":False,"Availability":random.randint(0,1),"TDWR":False},
    58:{"Frequency":"80Mhz","DFS":True,"Availability":random.randint(0,1),"TDWR":False},
    106:{"Frequency":"80Mhz","DFS":True,"Availability":random.randint(0,1),"TDWR":False},
    122:{"Frequency":"80Mhz","DFS":True,"Availability":random.randint(0,1),"TDWR":True},
    138:{"Frequency":"80Mhz","DFS":True,"Availability":random.randint(0,1),"TDWR":False},
    50:{"Frequency":"160Mhz","DFS":True,"Availability":random.randint(0,1),"TDWR":False},
    114:{"Frequency":"160Mhz","DFS":True,"Availability":random.randint(0,1),"TDWR":True},
    }

def randint(chn,country):
    tdwr = {"Australia":True,"India":False,"UK":False,"US":False,"Japan":True,"Canada":True}

    def avail():
        ach = ''
        for i in channels:
            if channels[i]["Availability"] == 1 and channels[i]["TDWR"] == False and tdwr.get(country) == True:
                ach += f"\nChannel {i} with {channels[i]['Frequency']}"
            elif tdwr.get(country) == False and channels[i]["Availability"] == 1:
                ach += f"\nChannel {i} with {channels[i]['Frequency']}"
            
        return ach

    if channels[chn]["TDWR"] and tdwr.get(country) == True:
        availablech = avail() 
        return f"Can\'t transmit data in the Selected channel No.{chn}.It is preoccupied by TDWR in selected country {country}\nThese Channels are available to transmit data:{availablech}"
    elif channels[chn]["DFS"] and channels[chn]["Availability"] == 0:
        availablech = avail() 
        return f"Selected Channel No.{chn} is not available due to occupied by other services.\nThese Channels are available to transmit data:{availablech}"
    elif channels[chn]["Availability"] == 0:
        availablech = avail() 
        return f"Selected Channel No.{chn} is available but interfered by too many networks.\nThese are suggested Channels to transmit data:{availablech}"
    else:
        return f"Selected Channel No.{chn} is available to transmitdata"
