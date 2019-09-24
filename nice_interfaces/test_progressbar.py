from progressbar import * 
import time
import numpy as np

widgets = ['Test: ', Percentage(), ' ', Bar(marker='#',left='[',right=']'), ' ', ETA(), ' ', FileTransferSpeed()] #see docs for other options

print("Using progressbar")

pbar = ProgressBar(widgets=widgets, maxval=500)
pbar.start()

num_steps = 100
progress_range = np.linspace(100,500,num=num_steps)
durations = [10.0 *(0.2+np.random.random_sample())/num_steps for i in progress_range]

import matplotlib.pyplot as plt

plt.plot(progress_range, durations)
#plt.plot(progress_range)
#plt.plot(durations)
plt.show()

count=0
for i in progress_range:
    # here do something long at each iteration
    time.sleep(durations[count])
    count += 1
    pbar.update(i) #this adds a little symbol at each iteration
pbar.finish()

print
print("Using tqdm")

from tqdm import tqdm
count=0
for i in tqdm(progress_range):
    #print(type(i))
    #print(type(tqdm(progress_range)))
    time.sleep(durations[count])
    count += 1

print("Using tqdm_gui")

from tqdm import tqdm_gui
count=0
for i in tqdm_gui(progress_range):
    time.sleep(durations[count])
    count += 1
