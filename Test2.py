from random import randbytes
import os
from pathlib import Path
import shutil
import math

FILESIZEBYTES = int(14*math.pow(2,20))

def findFileAttr(filepath):
    #IntializefileName to 0
    fileName = 0
    for root, dirs, files in os.walk(filepath):
        for file in files:
            #Check whether file is executable 
            exePer = os.access(filepath + '/' + file, os.X_OK)
            #Get Owner Name
            ownerName = Path(filepath + "/" + file).owner()
            #size of the file
            sizeOfFile = (os.stat(filepath + "/" + file).st_size)
            
            # Check the logic and return the file that matches the conditions described in the test
            if exePer is True and ownerName == "root" and sizeOfFile < FILESIZEBYTES ) :
                fileName = file
    return fileName

def test_answer():

    #Create Test Directory
    newDirectoryPath=os.getcwd() + "//Test"
    #remove if already a directory with same name exists
    if os.path.exists(newDirectoryPath):
        shutil.rmtree(newDirectoryPath)

    #Create Test Directory
    os.mkdir(newDirectoryPath)

    #Test 1 : Create a file with 4 bytes, no execute permission and owner name is same as user id
    data = randbytes(4)
    path = newDirectoryPath + "//FilewithNoExecPermissions.txt"
    with open(path, "wb") as file:
        file.write(data)
    file.close()
    
    #Test 2 : Create a file with 4 bytes, execute permission and owner name is same as user id
    path = newDirectoryPath + "//FilewithExecPermissions.txt"
    with open(path, "wb") as file:
       file.write(data)
    #Change the file Execution Permissions
    os.chmod(path, 0o777)
    file.close()

    #Test 3 : Create a file with 14680064 bytes, execute permission and owner name is same as user id
    data = randbytes(FILESIZEBYTES)
    path = newDirectoryPath + "//FilewithExecPerand14680064bytes.txt"
    with open(path, "wb") as file:
       file.write(data)
    #Change the file Execution Permissions
    os.chmod(path, 0o777)
    file.close()

    #Test 4 : Create a file with 14680064 bytes, execute permission and owner name is root
    data = randbytes(FILESIZEBYTES)
    path = newDirectoryPath + "//FilewithExact14680064bytes.txt"
    with open(path, "wb") as file:
        file.write(data)
    #Change the file execution permissions
    os.chmod(path, 0o777)
    #Change the ownership of file to root
    os.chown(path,0,-1)
    file.close()

    #Test 5 : Create a file with 14680063 bytes, execute permission and owner name is root
    data = randbytes(FILESIZEBYTES - 1)
    path = newDirectoryPath + "//Filelessthanwith4680063bytes.txt"
    with open(path, "wb") as file:
        file.write(data)
    #Change the file execution permissions
    os.chmod(path, 0o777)
    #Change the ownership of file to root
    os.chown(path,0,-1)
    file.close()

    #Test 6 : Create a file with 14680065 bytes, execute permission and owner name is root
    path = newDirectoryPath + "//Filegreaterthan4680065bytes.txt"
    data = randbytes(FILESIZEBYTES + 1)
    with open(path, "wb") as file:
        file.write(data)
    #Change the file execution permissions
    os.chmod(path, 0o777)
    #Change the ownership of file to root
    os.chown(path,0,-1)
    file.close()

    #Expected Result
    assert findFileAttr(newDirectoryPath) == "Filelessthanwith4680063bytes.txt"

    #Remove the test directory after Execution of the test
    shutil.rmtree(newDirectoryPath)
