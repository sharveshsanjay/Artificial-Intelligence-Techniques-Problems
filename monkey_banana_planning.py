# Initial state
state = { 
    'monkey_location': 'door', 
    'box_location': 'window', 
    'monkey_on_box': False, 
    'monkey_has_banana': False 
}

# Goal stack and actions
goal_stack = ['has(monkey, banana)']
actions = []


# Action definitions
def walk(x, y):
    state['monkey_location'] = y
    actions.append(f"Walk from {x} to {y}")

def push(x, y):
    state['monkey_location'] = y
    state['box_location'] = y
    actions.append(f"Push box from {x} to {y}")

def climb_up():
    state['monkey_on_box'] = True
    actions.append("Climb up the box")

def grasp():
    state['monkey_has_banana'] = True
    actions.append("Grasp the banana")


# Planning loop
while goal_stack:
    goal = goal_stack.pop()
    
    if goal == 'has(monkey, banana)':
        if not state['monkey_has_banana']:
            goal_stack.append('perform(grasp)')
            goal_stack.append('at(monkey, middle)')
            goal_stack.append('on(monkey, box)')
    
    elif goal == 'perform(grasp)':
        if state['monkey_location'] == 'middle' and state['monkey_on_box']:
            grasp()
    
    elif goal == 'on(monkey, box)':
        if not state['monkey_on_box']:
            if state['monkey_location'] == state['box_location']:
                goal_stack.append('perform(climb_up)')
            else:
                goal_stack.append(f'at(monkey, {state["box_location"]})')
    
    elif goal == 'perform(climb_up)':
        climb_up()

    elif goal.startswith('at(monkey,'):
        target = goal.split(',')[1].strip(' )')
        if state['monkey_location'] != target:
            if state['monkey_location'] == state['box_location']:
                push(state['box_location'], target)
            else:
                walk(state['monkey_location'], target)


# Output actions and final state
print("Monkey-Banana Planning Actions:")
for step in actions:
    print("-->", step)

print("\nFinal State:")
for key, value in state.items():
    print(f"{key}: {value}")
