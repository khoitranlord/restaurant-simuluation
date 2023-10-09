import numpy as np
import random
import math 

class Customer:
    def __init__(self, arrivalTime, serviceTime, customerEvent, status):
        self.arrivalTime = arrivalTime
        self.serviceTime = serviceTime
        # Event attribute to track whether the customer is an arrival or departure.
        self.customerEvent = customerEvent
        # Status attribute to track whether the customer is waiting in the queue, being served, or has departed. 
        # This would make it easier to keep track of the state of the system in the simRun() method.
        self.status = status
        pass
