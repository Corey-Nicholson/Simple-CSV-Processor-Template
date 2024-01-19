# A VERY simple template CSV processor

import sys
import csv
import random

# Generate a random number
randNum = random.randrange(1000000000)

# Define the output CSV file name
outputFile = 'output-file-' +  str(randNum) + '.csv'

# Print help menu 
def displayHelpMenu():
    print("\nSimple CSV Processor Template")
    print("Usage: python CSVProcessor.py [filename.csv] [headers exist (y/n)]")
    print("\nExample to pass all rows in file.csv with headers:")
    print("$ python CSVProcessor.py file.csv y")
    print("\nThe output will be saved as a .csv in the CWD.")

# Iterate through CSV
def iterateCSV():
    with open(filename, 'r') as csvfile:
        datareader = csv.reader(csvfile)
        next(datareader)  # Skip the header if it exists
        for row in datareader:
            action(row)

# Perform action on the data
def action(row):
    # !!!
    # ADD CODE HERE TO BE PROCESSED FOR EACH ROW
    processedOutput = row[0]  # Modify this line based on your processing logic
    # !!!

    # Print the current input and processed output
    print(f"Input: {row[0]}, Output: {processedOutput}")
    
    # Save the output to CSV
    outputToCSV(row[0], processedOutput)

# Save output to CSV
def outputToCSV(currentInput, processedOutput):
    with open(outputFile, 'a', newline='') as csvfile:
        csvwriter = csv.writer(csvfile)

        # If the file is new, write headers
        if csvfile.tell() == 0:
            csvwriter.writerow(["Input", "Output"])

        csvwriter.writerow([currentInput, processedOutput])

# Check arguments
if len(sys.argv) > 2:
    # Get command arguments
    filename = str(sys.argv[1])
    headers = str(sys.argv[2])
    iterateCSV()
    print("\nOutput saved as " + outputFile)
else:
    displayHelpMenu()
