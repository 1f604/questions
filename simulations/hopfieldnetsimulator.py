#hopfield net simulator
#enter patterns and number of nodes
import itertools
patterns = [(1,0,0),(0,1,0)]
numnodes = 3 #pattern size is same as number of nodes

weight = {}
threshold = {}
energy={}
transition={}
next={}

def generate_pairs(n):
    result = []
    for i in range(n):
        for j in range(i+1,n):
            result.append((i,j))
    return result

def generate_states(n):
    return list(itertools.product([0, 1], repeat=n))

def get_weight(i,j):
    ans = 0
    for p in patterns:
        ans += (2*p[i]-1)*(2*p[j]-1)
    return ans

def get_threshold(i):
    ans = 0
    for p in patterns:
        ans += (2*p[i]-1)
    return -ans

def get_energy(state):
    energy = 0
    for i,j in generate_pairs(numnodes):
        energy += weight[(i,j)]*state[i]*state[j]
    energy *= -1
    for i in range(numnodes):
        energy += threshold[i]*state[i]
    return energy

def print_H():
    s = ""
    for i,j in generate_pairs(numnodes):
        if -weight[(i,j)]>1:
            s+="+"+str(-weight[(i,j)])+"x"+str(i+1)+"x"+str(j+1)
        if -weight[(i,j)]==1:
            s+="+"+"x"+str(i+1)+"x"+str(j+1)
        if -weight[(i,j)]<0:
            s+=str(-weight[(i,j)])+"x"+str(i+1)+"x"+str(j+1)
    for i in range(numnodes):
        if threshold[i]>1:
            s+="+"+str(threshold[i])+"x"+str(i+1)
        if threshold[i]==1:
            s+="+"+"x"+str(i+1)
        if threshold[i]<0:
            s+=str(threshold[i])+"x"+str(i+1)
    print s

def get_next(state,i):
    h = 0
    for j in range(numnodes):
        if j!=i:
            h+=weight[(i,j)]*state[j]
    h -= threshold[i]
    if h > 0:
        return 1
    if h < 0:
        return 0
    if h == 0:
        return state[i]


for i,j in generate_pairs(numnodes):
    weight[(i,j)] = get_weight(i,j)
    weight[(j,i)] = get_weight(i,j)

for i in range(numnodes):
    threshold[i] = get_threshold(i)

for state in generate_states(numnodes):
    energy[get_energy(state)] = state
    for i in range(numnodes):
        next[(state,i)] = get_next(state,i)


m = ""
for state in generate_states(numnodes):
    m+=str(state)+str(get_energy(state))+'\n'
    for i in range(numnodes):
        k = list(state)
        k[i] = next[(state,i)]
        m+=str(k)
        m+='\n'
    m+="\n"
print m