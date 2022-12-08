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
    expB = [0,1,1,0]
    assert FlipInversion(inpA, expB) == 2

    #Test Case 2
    inpA = [1,0,1,0]
    expB = [0,0,1,1]
    assert FlipInversion(inpA, expB) == 2

    #Test Case 3
    inpA = [1,0,1,0]
    expB = [0,1,1,1]
    assert FlipInversion(inpA, expB) == 3

    #Test Case 4
    inpA = [0,1,0,1]
    expB = [1,0,1,0]
    assert FlipInversion(inpA, expB) == 4

    #Test Case 5
    inpA = [0,1,1,0]
    expB = [0,1,0,1]
    assert FlipInversion(inpA, expB) == 2



