import plotext as plt
#  black, tron, cloud, white, red, tomato, basil, green, yellow
#  gold, blue, indigo, teal, artic, lilac, violet
boards = ["Pi Zero 2", "Pi Zero", "Pi 3 A+", "Pi 3 B", "Pi 4 B"]
nums = [99.607757, 40.7459, 115.489967, 105.166047, 443.217292]

plt.bar(boards, nums, color = 'artic', marker = "small")
plt.plotsize(600, 70)

plt.canvas_color('black')

plt.axes_color('lilac')

plt.title("himeno (Phoronix - higher is better, multi-core test)")
plt.xlabel("Boards")
plt.ylabel("mflops")
plt.show()