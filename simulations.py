class EventSimulationList:
    def __init__(self, status):

        pass
    
    def addEvent(self, event):
        pass
    
    def printList(self):
        print('+------------+------------+------------+')
        print('| Arrival | Service | Event       |')
        print('+------------+------------+------------+')
        for customer in self.list:
            print('| {} | {} | {} |'.format(customer.arrivalTime, customer.serviceTime, customer.event))
        print('+------------+------------+------------+')


# We will simulate the system for a given time period. The system will have 3 queues (entrances, food, drink), each with its own arrival rate, service rate, and capacity.

class QueueSimulation:
    def __init__(self, simulation_time, lambda1, mu1, k1, c1, lambda2, mu2, k2, c2, lambda3, mu3, k3, c3, drinkRatio, simTime):
        self.avgWaitTime = 0
        self.avgWaitQuTime = 0
        self.avgWaitLen = 0
        self.avgWaitQuLen = 0
		# self.eventList = EventSimulationList(lam, mu, n)
        self.currentTime = 0
        self.waitTimeAcc = 0
        self.waitQuTimeAcc = 0
        self.waitLenAcc = 0
        self.waitQuLenAcc = 0
        self.completedNum = 0
        self.servingNum = 0
        self.previousTime = 0
    
    def stats(self):
        print('Simulation Results:')
        print('Average wait time:', self.avgWaitTime)
        print('Average wait queue time:', self.avgWaitQuTime)
        print('Average wait length:', self.avgWaitLen)
        print('Average wait queue length:', self.avgWaitQuLen)
        pass
    
    def stats(self):
        pass
     
    def run(self):
        # Execute system simulation until simulation time is reached.
        # Implement the simulation logic here.
        #
        # 1. Generate a random number to determine the next event.
        # 2. If the next event is an arrival, generate the next arrival time and add the customer to the queue.
        # 3. If the next event is a departure, generate the next departure time and remove the customer from the queue.
        # 4. Update the system state and statistics.
        # 5. Repeat until simulation time is reached.
        # Generate stats for simulation
        self.avgWaitTime = self.waitTimeAcc/self.completedNum
        self.avgWaitQuTime = self.waitQuTimeAcc/self.completedNum
        self.avgWaitLen = (self.waitLenAcc/self.currentTime)
        self.avgWaitQuLen = (self.waitQuLenAcc/self.currentTime)
        pass
