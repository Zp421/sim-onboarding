import matplotlib.pyplot as plt
import matplotlib.animation as animation
from dataclasses import dataclass
import numpy as np

import math


@dataclass
class State:
    
    time:float

    
    Acceleration:float
    Xvelocity:float
    Braking_force:float

# find braking force, acceleration, and velocity.

s0 = State(time=0.0, Acceleration=0.0, Xvelocity=25.0, Braking_force=0.0)
time_step = 0.1  #0.01


time_step_records = [0.0]



Xvelocity_records = [0.0]
Acceleration_records = [0.0]
Braking_force_records = [0.0]


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
    acceleration = 0.0

    maximum_propulsion_force = 2000.0  # N
    vmax = 27.0 #m/s

    maximum_braking_force = 1850.0  # N


    if state.time <= 2:

        driver_input = 0.0


    else:
        driver_input = 1.0
    






    
    braking_force = driver_input * maximum_braking_force
    acceleration = -1 * (braking_force/mass) 
    Xvelocity = state.Xvelocity + (acceleration * time_step)

    
    new_time = state.time + time_step
    

    newState = State(
        
        
        
        time = new_time,



        Acceleration = acceleration,
        Xvelocity = Xvelocity,
        Braking_force = braking_force,
        
        



    )

    return newState

import matplotlib.pyplot as plt








fig, (ax1, ax2, ax3, ) = plt.subplots(3, 1, figsize=(10, 5))
fig.suptitle("Graph")

(line1,) = ax1.plot(time_step_records, Braking_force_records, color="black")
ax1.set_ylabel("Braking Force")
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 2000)
ax1.grid(True)

(line2,) = ax2.plot(time_step_records, Acceleration_records, color="red")
ax2.set_ylabel("Acceleration")
ax2.set_xlim(0, 10)
ax2.set_ylim(-10, 20)
ax2.grid(True)

(line3,) = ax3.plot(time_step_records, Xvelocity_records, color="pink")
ax3.set_ylabel("X Velocity")
ax3.set_xlim(0, 10)
ax3.set_ylim(0, 200)
ax3.grid(True)
ax3.set_xlabel("Time")





def animate (i):
    global s0
    s0 =step(s0)
    time_step_records.append(s0.time)


    Braking_force_records.append(s0.Braking_force)
    Xvelocity_records.append(s0.Xvelocity)
    Acceleration_records.append(s0.Acceleration)

    line1.set_data(time_step_records, Braking_force_records)
    line2.set_data(time_step_records, Acceleration_records)
    line3.set_data(time_step_records, Xvelocity_records)

    if  s0.Xvelocity <= 0: 
        ani.event_source.stop()
        

ani = animation.FuncAnimation(
    fig, animate, frames=10000, interval=0, blit=False, repeat=False
)
plt.show()




