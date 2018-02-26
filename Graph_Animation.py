from matplotlib import animation, pyplot as plt
def update_radius(i,c):
    c.radius = i*0.2

fig = plt.gcf()
ax = plt.axes(xlim=(-10,10),ylim=(-10,10))
ax.set_aspect('equal')
c = plt.Circle((0,0), 0.05, fc='r', ec='b')
ax.add_patch(c)
anim = animation.FuncAnimation(fig, update_radius, fargs = (c,), frames = 50, interval = 80)
plt.title('Simple Circle Animation')
plt.show()