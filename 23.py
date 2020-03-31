import time
import numpy as np

start_time = None

def ConsecutiveSumExists(numsArr, sumValue):
    global start_time
    start_time = time.time()
    if numsArr is None or len(numsArr) == 0:
        return -1

    temp_sum = None
    temp_ix = None
    ix = 0

    # for num in numsArr:
    while ix < len(numsArr):
        if temp_sum is None:
            temp_ix = ix
            temp_sum = numsArr[ix]
        else:
            temp_sum += numsArr[ix]

        if temp_sum == sumValue:
            return temp_ix
        if ix == len(numsArr) - 1:
            ix = temp_ix
            temp_ix = None
            temp_sum = None
        ix += 1

    return -1

def ConsecutiveSumExists2(numsArr, sumValue):
    global start_time
    start_time = time.time()

    if numsArr is None or len(numsArr) == 0:
        return -1

    results = []

    for ix, num in enumerate(numsArr):
        if num == sumValue:
            return ix
        for ix2 in range(len(results)):
            results[ix2] += num
            # print(results)
            if results[ix2] == sumValue:
                return ix2

        results.append(num)

    return -1

def ConsecutiveSumExists3(numsArr, sumValue):
    global start_time
    start_time = time.time()

    if numsArr is None or len(numsArr) == 0:
        return -1

    results = []

    for num in range(len(numsArr)):
        if num == sumValue:
            return len(results)
        for ix2 in range(len(results)):
            results[ix2] += num
            # print(results)
            if results[ix2] == sumValue:
                return ix2

        results.append(num)

    return -1

entry_array = ([np.random.rand() for x in range(1000)], -1)
# entry_array = ([0, -1, -2, 4], 4)
# entry_array = ([0,1,5,5,1,1,2,1,8,6], 7) # return 3: The sequence [5,1,1] has a sum of 7 at start index 3.
# entry_array = ([0,1,5,5,45,1,2,1,2,6], 7) # -1

print("testing for an array of {} entries".format(len(entry_array[0])))
print("result: " + str(ConsecutiveSumExists(*entry_array)))
print("ConsecutiveSumExists --- %s seconds ---" % (time.time() - start_time))
print("result: " + str(ConsecutiveSumExists2(*entry_array)))
print("ConsecutiveSumExists2--- %s seconds ---" % (time.time() - start_time))
print("result: " + str(ConsecutiveSumExists3(*entry_array)))
print("ConsecutiveSumExists3--- %s seconds ---" % (time.time() - start_time))