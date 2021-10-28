import plotext as plt
#  black, tron, cloud, white, red, tomato, basil, green, yellow
#  gold, blue, indigo, teal, artic, lilac, violet
boards = ["Pi Zero 2", "Pi Zero", "Pi 3 A+", "Pi 3 B", "Pi 4 B"]
nums = [8.53, 14.24, 6.20, 7.24, 3.42]

plt.bar(boards, nums, color = 'artic', marker = "small")
plt.plotsize(600, 70)

plt.canvas_color('black')

plt.axes_color('lilac')

plt.title("Calculate Pi (10K spaces, realtime (lower is better))")
plt.xlabel("Boards")
plt.ylabel("Minutes")
plt.show()