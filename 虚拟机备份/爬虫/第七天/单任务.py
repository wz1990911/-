

import time





def saysirry():
    for i in range(5):
        print('对不起'+str(i))
        time.sleep(1)




def dosome_thing():
    for i in range(5):
        print('捏捏腿'+str(i))
        time.sleep(1)

if __name__ == '__main__':
    stat_time = time.time()
    saysirry()
    dosome_thing()
    end_time = time.time()
    print(end_time-stat_time)

