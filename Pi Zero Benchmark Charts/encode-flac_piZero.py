import plotext as plt
#  black, tron, cloud, white, red, tomato, basil, green, yellow
#  gold, blue, indigo, teal, artic, lilac, violet
boards = ["Pi Zero 2", "Pi Zero", "Pi 3 A+", "Pi 3 B", "Pi 4 B"]
nums = [944.506, 1046.871, 682.096, 793.126, 110.209]

plt.bar(boards, nums, color = 'artic', marker = "small")
plt.plotsize(600, 70)

plt.canvas_color('black')

plt.axes_color('lilac')

plt.title("encode-flac (Phoronix - lower is better, single-core test)")
plt.xlabel("Boards")
plt.ylabel("Seconds")
plt.show()