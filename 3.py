import matplotlib.pyplot as plt
import matplotlib.animation as animation
from dataclasses import dataclass
import numpy as np

import math


@dataclass
class State:
    
    time:float

    Drag:float
    Acceleration:float
    Xvelocity:float


s0 = State(time=0.0,Drag=0.0,Acceleration=0.0,Xvelocity=0.0)
time_step = 0.1  #0.01


time_step_records = [0.0]


Drag_records = [0.0]
Xvelocity_records = [0.0]
Net_acceleration_records = [0.0]



def step (state:State) -> State:
    mass = 300 #kg
    max_torque = 180 #NM
    wheel_radius = 0.216 #m
    gear_ratio = 3 #3:1

    forward_speed = 15    #m/s
    cornering_stiffness = 36000   #N/rad
    steer_angle = 0.0

    air_density = 1.2 #kg/m^3
    cross_sectional_area = 1.2 #m^2
    drag_coefficient = 0.7
    Acceleration = 0.0

    if state.time <= 10:

        Acceleration = 5   #acceleration is at 5m/s^2
    else:
        Acceleration = 0
    
    








    new_Drag = 0.5 * cross_sectional_area * drag_coefficient * air_density * state.Xvelocity**2
    new_Net_acceleration = Acceleration - (new_Drag/mass)
    new_xvel = state.Xvelocity + (new_Net_acceleration * time_step)


    
    new_time = state.time + time_step
    

    newState = State(
        

        time = new_time,



        Drag = new_Drag,
        Acceleration = new_Net_acceleration,
        Xvelocity = new_xvel,


    )

    return newState

import matplotlib.pyplot as plt








fig, (ax1, ax2, ax3, ) = plt.subplots(3, 1, figsize=(10, 12))
fig.suptitle("Graph")

(line1,) = ax1.plot(time_step_records, Drag_records, color="black")
ax1.set_ylabel("Drag")
ax1.set_xlim(0, 200)
ax1.set_ylim(-0.2, 1000)
ax1.grid(True)

(line2,) = ax2.plot(time_step_records, Net_acceleration_records, color="red")
ax2.set_ylabel("Net Acceleration")
ax2.set_xlim(0, 200)
ax2.set_ylim(-8, 8)
ax2.grid(True)

(line3,) = ax3.plot(time_step_records, Xvelocity_records, color="pink")
ax3.set_ylabel("X Velocity")
ax3.set_xlim(0, 200)
ax3.set_ylim(-0.02, 50)
ax3.grid(True)
ax3.set_xlabel("Time")





def animate (i):
    global s0
    s0 =step(s0)
    time_step_records.append(s0.time)


    Drag_records.append(s0.Drag)
    Net_acceleration_records.append(s0.Acceleration)
    Xvelocity_records.append(s0.Xvelocity)

    line1.set_data(time_step_records, Drag_records)
    line2.set_data(time_step_records, Net_acceleration_records)
    line3.set_data(time_step_records, Xvelocity_records)

    if  s0.time > 10 and s0.Xvelocity <= 0.1:
        ani.event_source.stop()
        

ani = animation.FuncAnimation(
    fig, animate, frames=10000, interval=0, blit=False, repeat=False
)
plt.show()




