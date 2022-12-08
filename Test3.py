def flipCoinsProblem(inarray):
    #Create an Alternating sequence based on number of inputs
    seq1 = [0,1] * (len(inarray)-2)
    seq2 = [1,0] * (len(inarray)-2)
    print(seq1)
    print(seq2)
    #Subtract the input arrays from alternating array
    #To find number of flips from input array to temporary sequence array 
    def findTotalDifferences(inpA,inpB):
        totalDiff = 0
        for idx in range(len(inpA)):
            diff = abs(inpA[idx] - inpB[idx])
            totalDiff += diff
        return totalDiff
    prob1 = findTotalDifferences(inarray, seq1[:len(inarray)])
    prob2 = findTotalDifferences(inarray, seq2[:len(inarray)])
    print(prob1, prob2)
    #Find the minimum steps required for flipping the coins
    return min(prob1, prob2)

def test_answer():
    #Test Case 1
    inpA = [1,0,1,0]
    assert flipCoinsProblem(inpA) == 0

    #Test Case 2
    inpA = [0,1,0,1]
    assert flipCoinsProblem(inpA) == 0

    #Test Case 3
    inpA = [0,1,1,0]
    assert flipCoinsProblem(inpA) == 2

    #Test Case 4
    inpA = [0,1,1,0,1]
    assert flipCoinsProblem(inpA) == 2

    #Test Case 5
    inpA = [1,0,1,0,0]
    assert flipCoinsProblem(inpA) == 1

    #Test Case 6
    inpA = [1,1,1,1]
    assert flipCoinsProblem(inpA) == 2
    
    #Test Case 6
    inpA = [0,0,0,0]
    assert flipCoinsProblem(inpA) == 2
