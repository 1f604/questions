#Ethernet capture effect simulator to show what happens when number of nodes increases on a network
#configurable options:
cycles = 200  # How many cycles to run. Note that this simulator does not emulate timeout or capping behavior so when collision counter > 10 it becomes inaccurate
numnodes = 100 # How many nodes on the network.



from random import randint
turn = 0 #what turn it is right now
node=[] #data structure: node[i][0] is the turn this node will transmit on next, node[i][1] is the maximum wait time, node[i][2] is number of frames transmitted
transmitting = 0 #number of nodes transmitting this turn
transmittingnodes = [] #set of nodes transmitting this turn
def delay(i):
    node[i][0] = turn+1+(randint(0,node[i][1]-1))
    node[i][1] *= 2

def reset(i):
    print("node "+str(i)+" successfully transmitted")
    node[i][0] = turn+1 #set to transmit on next turn
    node[i][1] = 2 #reset collision counter
    node[i][2] += 1 #increment number of successfully transmitted frames

def transmit():
    global transmitting
    global transmittingnodes
    for i in range(numnodes): #Check how many nodes are transmitting this turn
        if turn == node[i][0]:
            transmitting+=1
            transmittingnodes.append(i)
    if transmitting == 1:
        reset(transmittingnodes[0])
    elif transmitting > 1:#collision occurred, everyone back off
        print("collision occurred")
        for i in transmittingnodes:
            delay(i)
    elif transmitting ==0:
        print("nothing transmits this turn")
    transmitting = 0
    transmittingnodes=[]

for i in range(numnodes): #initialize nodes
    node.append([0,2,0])

for i in range(cycles):
    print("turn "+str(turn))
    print(node)
    transmit()
    turn+=1

print("Frames successfully transmitted by node (zeroes not counted):")
success = []
for i in range(numnodes):
    if node[i][2] >0:
        success.append(node[i][2])
print(success)