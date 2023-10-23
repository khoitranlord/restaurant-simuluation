import random
import math
import numpy as np
from customer import Customer
from simulations import *
from MMCKQueue import *
from threading import Thread

if __name__ == '__main__':
    totalServedCustomers = 0
    EntranceCustomerEvent = CustomerEvent(0.5)
    FoodCustomerEvent = CustomerEvent(0.5)
    drinkCustomerEvent = CustomerEvent(0.5)

    customerEvent.timeGenerate(simulationTime = 1000, arrivalTime = 0)
    
    drinkMMCK = MMCKQueue("drink_queue",0.5, 10, 100)
    foodMMCK = MMCKQueue("food_queue",0.5, 10, 100)
    entranceMMCK= MMCKQueue("entrance_queue",0.4, 5, 100, customerEvent, nextQueueList = [ foodMMCK, drinkMMCK], queueRatio = [1, 1])
    
    threads     = [None, None, None]
    threads[0]  = Thread(target=entranceMMCK.run)
    threads[1]  = Thread(target=drinkMMCK.run)
    threads[2]  = Thread(target=foodMMCK.run)
    
    for thread in threads:
        thread.start()
        
    while True:    
        if entranceMMCK.queueStatus == QueueStatus.IDLE and drinkMMCK.queueStatus == QueueStatus.IDLE and foodMMCK.queueStatus == QueueStatus.IDLE:
            entranceMMCK.stop()
            drinkMMCK.stop()
            foodMMCK.stop()
            break
   
    for thread in threads:
        thread.join()
        
    for queue in [entranceMMCK, drinkMMCK, foodMMCK]:
        queue.stats()
        print("-------------------------------------------------")
        print("queueName=",queue.name, "\nstats:")
        print("avgWaitTime=", queue.avgWaitTime)
        print('awgWaitLen=', queue.avgWaitLen)
        print('avgWaitQuTime=', queue.avgWaitQuTime)
        print('avgWaitQuLen=', queue.avgWaitQuLen)
        print('totalServedCustomers=', queue.totalServedCustomers)
    print("-------------------------------------------------")
    # print('totalServedCustomers of the system: ')
    # for queue in [entranceMMCK, drinkMMCK, foodMMCK]:
    #     totalServedCustomers += queue.totalServedCustomers
    # print('totalServedCustomers=', totalServedCustomers)
