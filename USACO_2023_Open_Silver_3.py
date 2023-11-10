string = input()
l = len(string)
states = [[0,[]],[0,[]],[0,[]],[0,[]],[0,[]],0]
runs = []
free = []
prv = -1
for i,char in enumerate(string):
    if char == 'b':
        tally = i-prv
        for f in free:
            tally += runs[f]
        states[0][1] += free
        free = []
        states[0][1].append(len(runs))
        runs.append(i-prv)
        states[0][0] += tally
        prv = i
    elif char == 'e':
        states[1][0] += states[0][0]
        states[1][1] += states[0][1]
        states[0][0] = 0
        states[0][1].clear()
        
        states[5] += states[4][0]*(l-i)
        free += states[4][1]
        states[4][0] = 0
        states[4][1].clear()
    elif char == 's':
        states[3][0] += states[2][0]
        states[3][1] += states[2][1]
        states[2] = states[1]
        states[1] = [0,[]]
    elif char == 'i':
        states[4][0] += states[3][0]
        states[4][1] += states[3][1]
        states[3][0] = 0
        states[3][1].clear()
print(states[5])
