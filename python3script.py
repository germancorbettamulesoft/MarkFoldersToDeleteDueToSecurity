import os
import csv

# This python 3 script is meant to rename the folders that belong to already closed cases.
# The purpose of this script is to avoid manually searching folders from Support cases that are ready to be deleted and save some time.

# This information is relative to each Support Engineer
directory = "/Users/gcorbetta/Downloads/cases"
csvReport = "/Users/gcorbetta/Downloads/report1667759801204.csv"
closedTag = ".ready.to.be.closed"

#Function to load my Cases from the local file system
def loadMyCases():
    aux = []
    try:
        folderArray = os.listdir(directory)
        for folder in folderArray:
            if(folder!=".DS_Store"):
                aux.append(folder)
    except FileNotFoundError:
        print("Cases folder not found")
        exit()
    return aux

#Function to load the closed cases from the CSV file (UTF-8 required)
#You may get the CSV by exporting the results of the "ClosedCasesForDeletingFolders" report (as UTF-8 CSV)
def loadClosedCases():
    aux = []
    try:
        with open(csvReport, encoding="utf8") as csvfile:
            csvreader = csv.reader(csvfile, delimiter=",")
            for row in csvreader:
                try:
                    aux.append(row[0])
                except IndentationError:
                    break
                except IndexError:
                    break
    except FileNotFoundError:
        print("Unable to find CSV file", csvReport)
        exit()
    except UnicodeDecodeError:
        print("Unable to open CSV file, please check that is UTF-8 CSV")
        exit()
    return aux

# Function to check arrays and identify folders to be closed
def loadReadyToClose(myCasesArray, closedCasesArray):
    aux = []
    for element in myCasesArray:
        if element in closedCasesArray:
            aux.append(element)
    return aux

#Main flow
print("Loading file system...")
myCases = loadMyCases()
print("Loading cases from CSV file...")
closedCases = loadClosedCases()
print("Finding matches...")
readyToDelete = loadReadyToClose(myCases, closedCases)

print("*"*30)
print("File System has: ", len(myCases), " folders")
print("NA101 CSV file: ", len(closedCases), " cases")
print("Ready to be marked for closure: ", len(readyToDelete), " folders")
print("*"*30)

# Rename the folders
for case in readyToDelete:
    oldCaseFolder = directory + "/" + case
    newCaseFolder = oldCaseFolder + closedTag
    if closedTag not in oldCaseFolder:
        os.rename(oldCaseFolder, newCaseFolder)
        print(oldCaseFolder, "was renamed successfully")
