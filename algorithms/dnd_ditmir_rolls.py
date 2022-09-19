#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

numb_rolls = 1000
roll_sword = np.random.randint(1,11,numb_rolls)
roll_manoeuver = np.random.randint(1,9,numb_rolls)
roll_sneak = np.random.randint(1,7,numb_rolls)

many_rolls = roll_sword + roll_manoeuver + roll_sneak + 6

# stats
print(np.mean(many_rolls), np.median(many_rolls), np.std(many_rolls))

# plot
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.hist(many_rolls, bins=20)
ax.set_xlabel("DMG")
ax.set_ylabel("number of rolls")
ax.set_title("mean="+str(np.mean(many_rolls))+", std="+str(np.std(many_rolls))+", numb of rolls="+str(numb_rolls))
plt.savefig("Ditmir_dmg_stats.png", dpi=150)
plt.show()
