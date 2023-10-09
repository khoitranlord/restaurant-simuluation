import random

class MMCKQueue:
    def __init__(self, arrival_rate, service_rate, serverNum, capacity):
        self.arrival_rate = arrival_rate
        self.service_rate = service_rate
        self.serverNum = serverNum
        self.capacity = capacity
        self.queue = []
        self.clock = 0
        self.total_customers_served = 0
        self.total_waiting_time = 0

    def arrival(self):
        pass

    def departure(self):
        pass

