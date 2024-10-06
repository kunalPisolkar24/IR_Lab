from collections import defaultdict

# Mapper function
def mapper(line): 
    for char in line:
        if char.isalpha():
            yield (char, 1)

# Reducer function
def reducer(key, values):
    return (key, sum(values))

# MapReduce simulation
def map_reduce(input_data):
    intermediate = defaultdict(list)
    for line in input_data:
        for key, value in mapper(line):
            intermediate[key].append(value)
    
    results = []
    for key in intermediate:
        results.append(reducer(key, intermediate[key]))
    
    return results

# Function to read data from a text file and process it
def process_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    output = map_reduce(lines)
    
    for char, count in output:
        print(f"({char}: {count})")

file_path = '/home/kunalpisolkar/Documents/Practicals/IR_Lab/four/document1.txt'  
process_file(file_path)
