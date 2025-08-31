# Puppy Toy Planning using Goal Stack

# Grid coordinates: (x, y)
toy_position = (2, 2)         # Toy is placed at center ceiling
box_position = [0, 0]         # Initial box position
puppy_position = [0, 1]       # Puppy starts in corner
has_toy = False
on_box = False

# Action log
actions = []

# Define room size (optional for visualization)
room_size = 3  # 3x3 grid

# ---------------- Helper Functions ---------------- #
def walk(to):
    global puppy_position
    actions.append(f"Walk from {tuple(puppy_position)} to {to}")
    puppy_position[0], puppy_position[1] = to

def push_box(to):
    global puppy_position, box_position
    actions.append(f"Push box from {tuple(box_position)} to {to}")
    box_position[0], box_position[1] = to
    puppy_position[0], puppy_position[1] = to  # Puppy moves with box

def climb_box():
    global on_box
    actions.append("Climb on box")
    on_box = True

def grab_toy():
    global has_toy
    actions.append("Grab the toy")
    has_toy = True

# ---------------- Goal Stack Planner ---------------- #
def goal_stack_planning():
    stack = ['HasToy']
    while stack:
        goal = stack.pop()

        if goal == 'HasToy':
            if has_toy:
                continue
            # Preconditions for grabbing toy
            if puppy_position == box_position == list(toy_position) and on_box:
                grab_toy()
            else:
                stack.append('HasToy')  # Retry after subgoals
                stack.append('OnBox')
                stack.append(('MoveBoxUnderToy', toy_position))

        elif goal == 'OnBox':
            if on_box:
                continue
            if puppy_position == box_position:
                climb_box()
            else:
                stack.append('OnBox')
                stack.append(('WalkTo', tuple(box_position)))

        elif isinstance(goal, tuple) and goal[0] == 'MoveBoxUnderToy':
            if box_position == list(goal[1]):
                continue
            stack.append(('MoveBoxUnderToy', goal[1]))
            stack.append(('WalkTo', tuple(box_position)))
            stack.append(('PushBoxTo', goal[1]))

        elif isinstance(goal, tuple) and goal[0] == 'WalkTo':
            if puppy_position == list(goal[1]):
                continue
            walk(goal[1])

        elif isinstance(goal, tuple) and goal[0] == 'PushBoxTo':
            if box_position == list(goal[1]):
                continue
            push_box(goal[1])

# ---------------- Run the Planner ---------------- #
goal_stack_planning()

# ---------------- Output ---------------- #
print("\nPlan to achieve goal:")
for step in actions:
    print("->", step)  # replaced arrow with ASCII "->"

print("\nFinal State:")
print("Puppy Position:", tuple(puppy_position))
print("Box Position:", tuple(box_position))
print("On Box:", on_box)
print("Has Toy:", has_toy)
