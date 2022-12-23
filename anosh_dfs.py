import random
print('1 for 20MHZ, 2 for 40MHZ, 3 for 80MHZ')

def dfs(x):
    if x == 1:
        a = [36,40,44,48,149,153,157,161,165,52,56,60,64,100,104,108,112,116,132,136,140,144,120,124,128]
        d = (a[0:]);e = (a[9:22]);f = (a[0:9]);h = (a[22:])

        print('20MHZ channels are\n',d)
        print('What are the channels are available in DFS\n')
        for i in range(0,len(e)):
            A = e[i]
            B = random.randint(0,1)
            if B == 0:
                print(A,' : This channel is available')
            #else:
                #print(A,' : This is channel is not available')
        print('TWDR channels are not used in our country\n',h)
        print('Non-DFS channels are\n',f)

    elif x == 2:
        b = [38,46,151,159,54,62,102,110,134,142,118,126]
        d = (b[0:]);e = (b[4:10]);f = (b[0:4]);h = (b[10:])

        print('40MHZ channels are\n',d)
        print('What are the channels are available in DFS\n')
        for i in range(0,len(e)):
            A = e[i]
            B = random.randint(0,1)
            if B == 0:
                print(A,' : This channel is available')
            #else:
                #print(A,' : This is channel is not available')
        print('TWDR channels are not used in our country\n',h)
        print('Non-DFS channels are\n',f)



    elif x == 3:
        c = [42,155,58,106,138,122]
        d = (c[0:]);e = (c[2:5]);f = (c[0:2]);h = (c[5:])

        print('80MHZ channels are\n',d)
        print('What are the channels are available in DFS\n')
        for i in range(0,len(e)):
            A = e[i]
            B = random.randint(0,1)
            if B == 0:
                print(A,' : This channel is available')
            #else:
                #print(A,' : This is channel is not available')

        print('TWDR channels are not used in our country\n',h)
        print('Non-DFS channels are\n',f)
    
    else:
        print('Enter valid input')

dfs( x = int(input('choose the bandwidth : ')))