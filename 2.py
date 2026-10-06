import matplotlib.pyplot as plt
import matplotlib.animation as animation
from dataclasses import dataclass
import numpy as np



@dataclass
class State:
    xvel:float
    time:float
    xpos:float
    ypos:float

s0 = State(xvel=0.0, time=0.0, xpos=0.0, ypos=0.0)
time_step = 0.1   #0.01

def step (state:State) -> State:
    mass = 300 #kg
    max_torque = 180 #NM
    wheel_radius = 0.216 #m
    gear_ratio = 3 #3:1

    forward_speed = 15    #m/s
    cornering_stiffness = 3600   #N/rad
    lateral_v = 0  #m/s

    if state.time <= 3:
        steer_angle = (pi/180.0)*state.time/3                #input is steering angle
    elif state.time <= 10:
        steer_angle = (pi/180.0)*5.0
    else:
        steer_angle = 0.0

    torque = max_torque * steer_angle
    force_at_wheel = (torque * gear_ratio)/wheel_radius
    acceleration = force_at_wheel/mass

    Slip_angle = steer_angle - (lateral_v/forward_speed)

    Lateral_force = cornering_stiffness * slip_angle

    Lateral_acceleration = lateral_force/mass

    Lateral_velocity = lateral_v + (lateral_acceleration * time_step)



    new_vel = state.xvel + acceleration * time_step
    new_time = state.time + time_step
    new_xpos = state.xpos + state.xvel * time_step

    newState = State(
        xvel = new_vel,
        xpos = new_xpos,
        ypos = 0.0,
        time = new_time,
    )

    return newState

def animate (i):
    global s0
    s0 =step(s0)
    ax.clear()
    ax.scatter([s0.xpos,120],[5,s0.ypos], s= 200, c = 'pink', marker= 's')    #==
    ax.set_xlim(0,300)
    ax.set_ylim(0,10)
    return ax,
    


fig = plt.figure(figsize=(3,3), dpi=150)
ax = fig.add_subplot(111)
ax.grid()
ax.set_xlim(-2, 2)
ax.set_ylim(-2, 2)
# these lines are so the animation doesnt zoom in or out

plt.pause(3)
ani = animation.FuncAnimation(fig, animate, interval=0)
plt.show()
