def adjacentElementsProduct(inputArray):
    a = len(inputArray)
    b = []
    for i in range(a-1):
        b.append(inputArray[i] * inputArray[i+1])
    return max(b)
