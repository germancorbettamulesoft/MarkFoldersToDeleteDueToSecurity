import os
import csv

# This information is relative to each Support Engineer
directory = "/Users/gcorbetta/Downloads/cases"
csvReport = "/Users/gcorbetta/Downloads/report.csv"
closedTag = ".ready.to.be.closed"

#Function to load my Cases from the local file system
def loadMyCases():
    try:
        folderArray = os.listdir(directory)
        for folder in folderArray:
            if(folder!=".DS_Store"):
                myCases.append(folder)
    except FileNotFoundError:
        print("Cases folder not found")
        exit()

#Function to load the closed cases from the CSV file (UTF-8 required)
#You may get the CSV by exporting the results of the "ClosedCasesForDeletingFolders" report (as UTF-8 CSV)
def loadClosedCases():
    try:
        with open(csvReport, encoding="utf8") as csvfile:
            csvreader = csv.reader(csvfile, delimiter=",")
            for row in csvreader:
                try:
                    closedCases.append(row[0])
                except IndentationError:
                    break
                except IndexError:
                    break
    except FileNotFoundError:
        print("Unable to find CSV file")
        exit()
    except UnicodeDecodeError:
        print("Unable to open CSV file, please check that is UTF-8 CSV")
        exit()

# Function to check arrays and identify folders to be closed
def loadReadyToClose():
    for myfolder in myCases:
        if myfolder in closedCases:
            readyToDelete.append(myfolder)

#Main flow
myCases = []
closedCases = []
readyToDelete = []
loadMyCases()
loadClosedCases()
loadReadyToClose()

print("*"*30)
print("File System has: ", len(myCases), " folders")
print("NA101 CSV file: ", len(closedCases), " folders")
print("Ready to be marked for closure: ", len(readyToDelete), " folders")
print("*"*30)

# Rename the folder
for case in readyToDelete:
    oldCaseFolder = directory + "/" + case
    newCaseFolder = oldCaseFolder + closedTag
    if closedTag not in oldCaseFolder:
        os.rename(oldCaseFolder, newCaseFolder)
