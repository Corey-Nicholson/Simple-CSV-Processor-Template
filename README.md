
# Simple CSV Processor Template

A VERY simple CSV processor template since it comes in 
handy.

Process: The script runs through each row in a CSV and performs an action on it.

Input: A CSV with a single column of raw data.

Output: A CSV with the input column and a second output column.





## Usage

1. Modify the 'action()' function with the desired output/action. 

2. Run your new script
```bash
python CSVProcessor.py [filename.csv] [headers exist (y/n)]

# Example:
python CSVProcessor.py file.csv y
```

3. A new output CSV will be created with the output.

    