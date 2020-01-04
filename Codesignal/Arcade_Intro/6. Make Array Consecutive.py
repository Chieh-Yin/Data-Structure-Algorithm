def makeArrayConsecutive2(statues):
    a = max(statues)
    b = min(statues)
    length = len(statues)
    
    return a-b-length+1
