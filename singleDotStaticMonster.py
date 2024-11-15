from SingleDotProblemStaticMonster import Agent, State, Problem
from problemGraphics import pacmanGraphic
import random

p = Problem('singleDotSmall.txt')
#p = Problem('singleDotMedium.txt')

def prt(V):
    for k in V:
        print(k.agentPos, V[k])

# Complete your code here for
# value iteration and extract policy
 

V = {}  
policy = {} 

start_state = p.getStartState()
states_to_explore = [start_state]
explored = set()

while states_to_explore:
    current_state = states_to_explore.pop()
    state_obj = State(current_state.agentClass.pos)
    
    if state_obj in explored:
        continue
        
    explored.add(state_obj)
    V[state_obj] = 0.0
 
    transitions = p.transition(current_state)
    for next_state, _ in transitions:
        next_state_obj = State(next_state.agentClass.pos)
        if next_state_obj not in explored:
            states_to_explore.append(next_state_obj)

discount = 0.9
iterations = 100

for _ in range(iterations):
    new_V = {}
    
    for state in V.keys():
        if p.isTerminal(state):
            new_V[state] = p.reward(state)
            policy[state] = None
            continue
            

        transitions = p.transition(state)
        
        if not transitions:
       