import matplotlib.pyplot as plt
import matplotlib.animation as animation
from dataclasses import dataclass
import numpy as np
#use Numpy array
import math


@dataclass
class State:
    
    time:float
    xpos:float
    ypos:float
    Lateral_velocity:float
    Slip_angle:float
    Lateral_force:float
    Lateral_acceleration:float
    Drag:float
    Acceleration:float
    Xvelocity:float


s0 = State(time=0.0, xpos=0.0, ypos=0.0,Lateral_velocity=0.0,Lateral_force=0.0,Slip_angle=0.0,Lateral_acceleration=0.0,Drag=0.0,Acceleration=0.0,Xvelocity=0.0)
time_step = 0.1  #0.01


time_step_records = [0.0]
lateral_velocity_records = [0.0]
lateral_acceleration_records = [0.0]
slip_angle_records = [0.0]
lateral_force_records = [0.0]

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

    if state.time <= 1:

        Acceleration = state.Acceleration + 0.5   #timestep is 0.1 so 5m/s is added in 10 times  , now timesetp is 0.5 so +2.5 accel instead
    elif state.time <= 10:
        Acceleration = 5

    else:
        Acceleration = 0
    




    torque = max_torque * steer_angle
    force_at_wheel = (torque * gear_ratio)/wheel_radius
    #acceleration = force_at_wheel/mass

    new_Slip_angle = steer_angle - (state.Lateral_velocity/forward_speed)
    new_Lateral_force = cornering_stiffness * new_Slip_angle
    new_Lateral_acceleration = new_Lateral_force/mass
    new_Lateral_velocity = state.Lateral_velocity + (new_Lateral_acceleration * time_step)

    new_Drag = 0.5 * cross_sectional_area * drag_coefficient * air_density * state.Xvelocity**2
    new_Net_acceleration = Acceleration - (new_Drag/mass)
    new_xvel = state.Xvelocity + (new_Net_acceleration * time_step)


    #new_yvel = state.Xvelocity + Acceleration * time_step
    new_time = state.time + time_step
    new_xpos = state.xpos + state.Xvelocity * time_step

    newState = State(
        
        xpos = new_xpos,
        ypos = 0.0,
        time = new_time,

        Slip_angle = new_Slip_angle,
        Lateral_force = new_Lateral_force,
        Lateral_acceleration = new_Lateral_acceleration,
        Lateral_velocity = new_Lateral_velocity,

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
ax1.set_xlim(0, 100)
ax1.set_ylim(-0.2, 1000)
ax1.grid(True)

(line2,) = ax2.plot(time_step_records, Net_acceleration_records, color="red")
ax2.set_ylabel("Net Acceleration")
ax2.set_xlim(0, 100)
ax2.set_ylim(-8, 8)
ax2.grid(True)

(line3,) = ax3.plot(time_step_records, Xvelocity_records, color="pink")
ax3.set_ylabel("X Velocity")
ax3.set_xlim(0, 100)
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
        print(len(time_step_records))

ani = animation.FuncAnimation(
    fig, animate, frames=100, interval=5, blit=False, repeat=False
)
plt.show()




