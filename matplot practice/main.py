# Matplotlib practice

import matplotlib.pyplot as plt


xs = []
y1s = [] # quadratic

y2s = [] # linear


for x in range(-10, 10):
    xs.append(x)
    y = x**2
    y1s.append(y)
    y2s.append(10*x)

plt.plot(xs, y1s, color="r", linestyle="--", marker="*")
plt.plot(xs, y2s, color="b", linestyle="-", marker="^")
plt.xlabel("x value")
plt.ylabel("y value")
plt.title("y vs x")
plt.grid(True)
xgrid = []
for i in range(0, 11):
    xgrid.append(-10+2*i)
ygrid = []
for i in range(0,11):
    ygrid.append(10*i)
plt.xticks(xgrid)
# plt.yticks(ygrid)
plt.legend(["quadratic", "linear"])
plt.savefig("functions.png", dpi=300)

plt.show()

