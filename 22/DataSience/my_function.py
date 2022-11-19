import matplotlib.pyplot as plt

fig, ax = plt.subplots(2, 2, figsize=(6, 6))

ax[0,0].plot(range(10), 'r')
ax[1,0].plot(range(10), 'b')
ax[0,1].plot(range(10), 'g')
ax[1,1].plot(range(10), 'k')

plt.show()
