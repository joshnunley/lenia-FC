from lenia import Lenia

import numpy as np

import matplotlib

matplotlib.use("tkagg")
import matplotlib.pyplot as plt
from matplotlib import animation

world_size = 64
radius = 5
time_step = 0.05
growth_mean = 0.135
growth_std = 0.015

kernel_size = 2 * radius + 1

world = np.random.uniform(size=(world_size, world_size, world_size))
kernel = np.ones(shape=(kernel_size, kernel_size, kernel_size))
kernel[radius, radius, radius] = 0
kernel = kernel / np.sum(kernel)

# Use all the previously defined stuff to create a 2 dimensional
# instance of Lenia
lenia3d = Lenia(world, kernel, time_step, growth_mean, growth_std)

for i in range(20):
    lenia3d.update()