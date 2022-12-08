def FlipInversion(inpA, inpB):
    #Stores the count of steps
    step = 0
    #Iterate over both until inputs are unequal
    for index in range(len(inpA)):
        #Check till end the right most bit that are unequal
        if inpA[index] != inpB[index] :
            #Flip inpA bit at the last index
            inpA[index] = inpB[index]
            #Increasing steps by one
            step +=1 
    return step

def test_answer():
    #Test Case 1
    inpA = [1,0,1,0]
    inpB = [0,1,1,0]
    assert FlipInversion(inpA, inpB) == 2

    #Test Case 2
    inpA = [1,0,1,0]
    inpB = [0,0,1,1]
    assert FlipInversion(inpA, inpB) == 2

    #Test Case 3
    inpA = [1,0,1,0]
    inpB = [0,1,1,1]
    assert FlipInversion(inpA, inpB) == 3

    #Test Case 4
    inpA = [1,1,1,1]
    inpB = [0,0,0,0]
    assert FlipInversion(inpA, inpB) == 4

    #Test Case 5
    inpA = [1,1,0,0]
    inpB = [0,0,0,0]
    assert FlipInversion(inpA, inpB) == 2

    #Test Case 6
    inpB = [1,1,1,1]
    inpA = [0,0,0,0]
    assert FlipInversion(inpA, inpB) == 4

    #Test Case 7
    inpA = [0,0,0,0]
    inpB = [0,0,1,1]
    assert FlipInversion(inpA, inpB) == 2

    #Test Case 8
    inpA = [1,1,1,0]
    inpB = [0,0,0,1]
    assert FlipInversion(inpA, inpB) == 4

    #Test Case 9
    inpA = [1,0,1,0]
    inpB = [1,0,1,0]
    assert FlipInversion(inpA, inpB) == 0

    #Test Case 10
    inpA = [1,1,0,0]
    inpB = [0,0,1,1]
    assert FlipInversion(inpA, inpB) == 4
