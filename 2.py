import matplotlib.pyplot as plt
import matplotlib.animation as animation
from dataclasses import dataclass
import numpy as np

import math


@dataclass
class State:
    xvel:float
    time:float
    xpos:float
    ypos:float
    Lateral_velocity:float
    Slip_angle:float
    Lateral_force:float
    Lateral_acceleration:float


s0 = State(xvel=0.0, time=0.0, xpos=0.0, ypos=0.0,Lateral_velocity=0.0,Lateral_force=0.0,Slip_angle=0.0,Lateral_acceleration=0.0)
time_step = 0.1  #0.01


time_step_records = [s0.time]
lateral_velocity_records = [s0.Lateral_velocity]
lateral_acceleration_records = [s0.Lateral_acceleration]
slip_angle_records = [s0.Slip_angle]
lateral_force_records = [s0.Lateral_force]


def step (state:State) -> State:
    mass = 300 #kg
    max_torque = 180 #NM
    wheel_radius = 0.216 #m
    gear_ratio = 3 #3:1

    forward_speed = 15    #m/s
    cornering_stiffness = 3600   #N/rad
    
    steer_angle = 0.0

    if state.time <= 3:
        steer_angle = (math.pi/180.0)*state.time/3   
    elif state.time <= 10:
        steer_angle = (math.pi/180.0)*5.0
    else:
        steer_angle = 0.0




    torque = max_torque * steer_angle
    force_at_wheel = (torque * gear_ratio)/wheel_radius
    acceleration = force_at_wheel/mass

    new_Slip_angle = steer_angle - (state.Lateral_velocity/forward_speed)
    new_Lateral_force = cornering_stiffness * new_Slip_angle
    new_Lateral_acceleration = new_Lateral_force/mass
    new_Lateral_velocity = state.Lateral_velocity + (new_Lateral_acceleration * time_step)



    new_vel = state.xvel + acceleration * time_step
    new_time = state.time + time_step
    new_xpos = state.xpos + state.xvel * time_step

    newState = State(
        xvel = new_vel,
        xpos = new_xpos,
        ypos = 0.0,
        time = new_time,

        Slip_angle = new_Slip_angle,
        Lateral_force = new_Lateral_force,
        Lateral_acceleration = new_Lateral_acceleration,
        Lateral_velocity = new_Lateral_velocity,

    )

    return newState

import matplotlib.pyplot as plt

x = time_step_records

y = lateral_velocity_records



# function to show the plot
(line1,) = plt.plot(
    time_step_records,
    lateral_velocity_records,
    color="black",
    linestyle="dashed",
    linewidth=1,
    marker="o",
    markerfacecolor="black",
    markersize=2,
)

(line2,) = plt.plot(
    time_step_records,
    lateral_acceleration_records,
    color="red",
    linestyle="dashed",
    linewidth=1,
    marker="o",
    markerfacecolor="black",
    markersize=2,
)

(line3,) = plt.plot(
    time_step_records,
    slip_angle_records,
    color="green",
    linestyle="dashed",
    linewidth=1,
    marker="o",
    markerfacecolor="black",
    markersize=2,
)

(line4,) = plt.plot(
    time_step_records,
    lateral_force_records,
    color="green",
    linestyle="dashed",
    linewidth=1,
    marker="o",
    markerfacecolor="black",
    markersize=2,
)


plt.xlim(0, 15)
plt.ylim(-10.0, 20.0)

plt.xlabel("time(measured in seconds)")
plt.ylabel("magnitude")
plt.title("Some cool customizations!")

def animate (i):
    global s0
    s0 =step(s0)
    time_step_records.append(s0.time)
    lateral_velocity_records.append(s0.Lateral_velocity)
    lateral_acceleration_records.append(s0.Lateral_acceleration)
    slip_angle_records.append(s0.Slip_angle)
    lateral_force_records.append(s0.Lateral_force)
    line1.set_data(time_step_records, lateral_velocity_records)
    line2.set_data(time_step_records, lateral_acceleration_records)
    line3.set_data(time_step_records, slip_angle_records)
    line4.set_data(time_step_records, lateral_force_records)
    if s0.time >= 14:
        ani.event_source.stop()

ani = animation.FuncAnimation(
    plt.gcf(), animate, frames=150, interval=50, blit=False, repeat=False
)

plt.show()




