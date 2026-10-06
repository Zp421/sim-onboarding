import matplotlib.pyplot as plt
import matplotlib.animation as animation
from dataclasses import dataclass
import numpy as np

@dataclass
class State:
    xvel: float
    time: float
    xpos: float
    ypos: float

# 1. Initialize s0 as a State object, not an integer
s0 = State(xvel=0.0, time=0.0, xpos=0.0, ypos=5.0)

time_step = 0.01

def step(state: State) -> State:
    mass = 300  # kg
    max_torque = 180  # NM
    wheel_radius = 0.216  # m
    gear_ratio = 3  # 3:1

    if state.time <= 7:
        driver_input = state.time / 7
    elif state.time <= 22:
        driver_input = 1.0
    else:
        driver_input = 0.0

    torque = max_torque * driver_input
    force_at_wheel = (torque * gear_ratio) / wheel_radius
    acceleration = force_at_wheel / mass

    # FIXED: Changed state.evel to state.xvel
    new_vel = state.xvel + acceleration * time_step
    new_time = state.time + time_step
    new_xpos = state.xpos + state.xvel * time_step

    newState = State(
        xvel=new_vel,
        xpos=new_xpos,
        ypos=5.0,  # Match your fixed tracking line
        time=new_time,
    )

    return newState

def animate(i):
    global s0
    s0 = step(s0)
    
    ax.clear()
    ax.grid() # Re-add grid since ax.clear() wipes it
    
    # FIXED: Extract the xpos coordinate out of your s0 State object
    # FIXED: Provided a fixed fallback placeholder for xpos/ypos since they weren't defined elsewhere
    moving_x = s0.xpos
    static_x = 150.0  
    static_y = 5.0
    
    scat = ax.scatter([moving_x, static_x], [5, static_y], s=200, c='pink', marker='s')
    
    ax.set_xlim(0, 300)
    ax.set_ylim(0, 10)
    return scat,


fig = plt.figure(figsize=(3,3), dpi=150)
ax = fig.add_subplot(111)
ax.grid()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
# these lines are so the animation doesnt zoom in or out
plt.pause(3)
ani = animation.FuncAnimation(fig, animate, interval=0)
plt.show()