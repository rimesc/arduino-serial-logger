import csv
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import serialdata

matplotlib.use("tkAgg")

# Columns in the serial data
TIME = 0
YAW = 1
VA = 2
VB = 3

time_data = np.array([], np.float32)
yaw_data = np.array([], np.float32)
va_data = np.array([], np.float32)
vb_data = np.array([], np.float32)

plt.ion()
fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
ax1.set_ylabel('Yaw (°)')
ax1.set_ybound(-30, 30)
ax2.set_xlabel('Time (s)')
ax2.set_ylabel('Speed')
ax2.set_ybound(-300, 300)
yaw, = ax1.plot(time_data, yaw_data, scaley=False)
va, = ax2.plot(time_data, va_data, scaley=False)
vb, = ax2.plot(time_data, vb_data, scaley=False)


def update_line(line, data):
    line.set_xdata(time_data)
    line.set_ydata(data)


def redraw():
    for ax in fig.get_axes():
        ax.relim()
        ax.autoscale_view(scaley=False)
    fig.canvas.draw()
    fig.canvas.flush_events()


with open("data.csv", "x") as f:
    writer = csv.writer(f)

    for data in serialdata.read():
        time_data = np.append(time_data, data[TIME] / 1000)
        yaw_data = np.append(yaw_data, data[YAW])
        va_data = np.append(va_data, data[VA])
        vb_data = np.append(vb_data, data[VB])
        writer.writerow(data)
        update_line(yaw, yaw_data)
        update_line(va, va_data)
        update_line(vb, vb_data)
        redraw()
