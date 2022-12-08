def vectorComparision(inpA, inpB):
    Output = -1
    #Convert the input list to sets
    inpA = set(inpA)
    inpB = set(inpB)
    #Find intersection between two input sets
    intersectionC = inpA.intersection(inpB)

    if len(intersectionC) > 0 :
       Output = list(intersectionC)[0]
    else :
        print("There are no common intersections between two inputs")
        
    return Output

def test_answer():
    #Test 1
    inpA = [1,2,3,4,5]
    inpB = [1,2,3,4,5]
    assert vectorComparision(inpA, inpB) == inpA[0]
    #Test 2
    inpA = [1,2,3,4,5]
    inpB = [2,2,4,4,5]
    assert vectorComparision(inpA, inpB) == inpB[0]
    #Test 3
    inpA = [1,2,3,4,5]
    inpB = [6,7,8,9,10]
    assert vectorComparision(inpA, inpB) == -1
    #Test 4
    inpA = [1,0,2,4,5]
    inpB = [2,2,4,4,5]
    assert vectorComparision(inpA, inpB) == inpB[0]
    #Test 5
    inpA = [1,0,-1,4,5]
    inpB = [2,2,4,4,5]
    assert vectorComparision(inpA, inpB) == inpB[2]
