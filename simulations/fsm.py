#Find all finite state machines of a certain type...and see the length of their shortest distinguishing sequence 
import itertools
from itertools import product
from itertools import combinations_with_replacement
from collections import defaultdict
from collections import Counter
num_arrows_from_each_state = 2
input_alphabet = "ab"
output_alphabet = "xy"

def generate_labels(input_alphabet, output_alphabet):
    return product(input_alphabet,output_alphabet)
    
def generate_transition_target_states(n,num_arrows_from_each_state):
    return combinations_with_replacement(range(n),r=num_arrows_from_each_state)
    
def generate_label_transitions(input_alphabet, output_alphabet, n,num_arrows_from_each_state):
    for states in generate_transition_target_states(n,num_arrows_from_each_state):
        yield target_state_label_generator(states,product(generate_labels(input_alphabet, output_alphabet),repeat=2))

def target_state_label_generator(states, labels):
    for label in labels:
        yield tuple([(states[i],label[i]) for i in range(len(states))])

def generate_transitions(n): 
    outs = test_fst(n,sample_fsm(n),n)
    for gen in generate_label_transitions(input_alphabet, output_alphabet, n,num_arrows_from_each_state):
        for g in gen:
            m = {}
            for t in g:
                m[t[1][0]] = (t[0],t[1][1])
            yield m
def generate_transitions_print(n): 
    outs = test_fst(n,sample_fsm(n),n)
    print(outs)
    for gen in generate_label_transitions(input_alphabet, output_alphabet, n,num_arrows_from_each_state):
        for g in gen:
            print(g)

def generate_fsms(n):
    for transition_triple in product(generate_transitions(n),repeat=n):
        yield transition_triple

def generate_inputs(n):
    for roll in product("ab", repeat = n):
        yield ''.join(roll)
        
def run_fsm(fsm,state,inp):
    output = []    
    for i in inp:
        output.append(fsm[state][i][1])
        state = fsm[state][i][0]
    return ''.join(output)
        
def test_fst(fsm, max_test_length):
    outputs = defaultdict(lambda: defaultdict(str))
    ds = None
    def find_ds(fsm,max_test_length):
        for i in range(2**max_test_length+1): 
            for j in generate_inputs(i):
                for state in range(len(fsm)):                
                    outputs[j][state] = run_fsm(fsm,state,j)
                if len(outputs[j].values()) == len(set(outputs[j].values())):
                    ds = j
                    #print("distinguishing sequence found for fsm:", fsm, ds)
                    return ds
        return None
    ds = find_ds(fsm,max_test_length)
    if not ds:
        return None 
    return ds
      
        
    

def generate_label_transitions(input_alphabet, output_alphabet, n):
    possible_labels = product(product(range(n),output_alphabet), repeat=len(input_alphabet))
    return [{input_alphabet[i]:label[i] for i in range(len(input_alphabet))} for label in possible_labels ]

def generate_fsms(input_alphabet, output_alphabet, n):
    transitions = generate_label_transitions(input_alphabet, output_alphabet, n)
    return product(transitions, repeat=n)

fsms = list(generate_fsms("ab","xy",3))
ones = []
for fsm in fsms:
    outs = test_fst(fsm,3) 
    if outs and len(outs) > 3:
        ones.append(outs)
print(ones)
#print(fsms)
#sample = ({'b': (2, 'y'), 'a': (2, 'y')}, {'b': (2, 'y'), 'a': (2, 'y')}, {'b': (2, 'x'), 'a': (2, 'y')})

#outs = test_fst(sample,2)
#print(outs['b'][2])
#evaluate(outs)
#for fsm in generate_fsms(2):
#    print(fsm)


