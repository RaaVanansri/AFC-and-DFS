import random

def randint(chn):
    channels = [["20Mhz DFS",52,56,60,64,100,104,108,112,116,120,124,128,132,136,140,144],
    ["20Mhz Non-DFS",36,40,44,48,149,153,157,161,165],
    ["40Mhz DFS",54,62,102,110,118,126,134,142],
    ["40Mhz Non-DFS",38,46,151,159],
    ["80Mhz DFS",58,106,122,138],
    ["80Mhz Non-DFS",42,155],
    ["160Mhz DFS",114],
    ["160Mhz Non-DFS",50]]

    for i in range(len(channels)):
        if channels[i][0].split(' ')[1] in "DFS" and chn in channels[i]:
            k = random.randint(0,1)
            if k == 1 :
                return "Selected Channel is available to transmit data"
            else:
                return "Selected Channel is not available to transmit data"
        elif channels[i][0].split(' ')[1] in "Non-DFS" and chn in channels[i]:
            return "Selected Channel is available to transmit data"
