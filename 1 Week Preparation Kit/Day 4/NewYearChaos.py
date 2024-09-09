def minimumBribes(q):
    #bribes can affect the position of up to 2 numbers it bribed
    #any more and it's Too chaotic
    sumBribes = 0
    modifiedExpectedPosNumDict = {}
    i = 0
    for i in range(len(q) - 1):
        expectedNum = i + 1
        if modifiedExpectedPosNumDict.get(i, 0) != 0:
            expectedNum = modifiedExpectedPosNumDict[i]
        currNum = q[i]
        if expectedNum != currNum:
            currNumExpectedPos = currNum - 1
            numBribes = currNumExpectedPos - i
            if numBribes > 2:
                print("Too chaotic")
                break
            elif numBribes == 0:
                if modifiedExpectedPosNumDict.get(i, 0) != 0:
                    modifiedExpectedPosNumDict.pop(i)
            else:
                if i == len(q) - 2:
                    sumBribes += 1
                else:
                    sumBribes += numBribes
                    for j in range(1, numBribes + 1):
                        modifiedExpectedPosNumDict[i + j] = modifiedExpectedPosNumDict.pop(i) if modifiedExpectedPosNumDict.get(i, 0) != 0 else i + j
        else:
            if modifiedExpectedPosNumDict.get(i, 0) != 0:
                modifiedExpectedPosNumDict.pop(i)
    if i == len(q) - 2:
        print(sumBribes)

def minimum_bribes(queue):
    total_bribes = 0
    n = len(queue)

    # Iterate over each person in the queue
    for i in range(n):
        # Check if any person has moved more than two positions ahead
        if queue[i] - (i + 1) > 2:
            print("Too chaotic")
            return

    # Counting the number of bribes
    for i in range(n):
        # A person can only move at most 2 positions ahead of their initial position
        # So, we only need to check from max(0, queue[i] - 2) to i
        for j in range(max(0, queue[i] - 2), i):
            if queue[j] > queue[i]:
                total_bribes += 1

    print(total_bribes)

minimum_bribes([3, 4, 5, 2, 1])