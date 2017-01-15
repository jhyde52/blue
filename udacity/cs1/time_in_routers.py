# Need to find the time spent in the routers
# which doesn't include the time spent on the wires


# Info
total_time = 75 # ms
one_way_distance = float(2500) # km
optic_speed = 200000 # km per second
ms_per_second = 1000

# Calculations
# time = distance/speed

time_on_the_wires = ((2*one_way_distance) /optic_speed) * ms_per_second

total_time_at_routers = total_time - time_on_the_wires
print total_time_at_routers

# 50