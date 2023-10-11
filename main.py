import random
import math
import numpy as np
from customer import Customer
from simulations import *
import simpy

if __name__ == '__main__':
    params = ()
    queueSimulation = QueueSimulation(*params)
    queueSimulation.run()
    queueSimulation.stats()
