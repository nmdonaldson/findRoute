import argparse

# Handles command line inputs
def input_handler():
    # Command line parser to handle inputs, all of which are required for the program to run
    parser = argparse.ArgumentParser(description='Recieves exactly 3 command line inputs to find a route between any two cities.')
    parser.add_argument('-i', '--input', required=True, type=str, help='The name of the (correctly formatted) input file.')
    parser.add_argument('-o', '--origin', required=True, type=str, help='The name of the starting location/city.')
    parser.add_argument('-t', '--target', required=True, type=str, help='The name of the destination location/city.')

    args = parser.parse_args()

    # Assigning argument information to variables
    input = args.input
    origin = args.origin
    target = args.target

    return input, origin, target

# Models the input file as a graph from an input file
def graph_modeler(input, origin, target):

    # Opens input file
    fileHandler = open(input)

    # Dictionary that represents the graph of the cities
    # Graph is structured as the name of the city as the key and a tuple 
    # of the bordering city and its distance as the value
    cityGraph = {}

    # Reads the first line of the file for the while loop to work
    line = fileHandler.readline()

    # Reading in the contents of the file until the end signifier
    while line != 'END OF INPUT':
        info = line.rstrip('\n').split(' ')

        # If the city exists in the graph already, add the next adjacent city to the value list
        if info[0] in cityGraph:
            cityGraph[info[0]].append((info[1], info[2]))
        # Otherwise, create a new list at this index 
        else:
            cityGraph[info[0]] = [(info[1], info[2])]
            # This graph is undirected, so include both directions
            cityGraph[info[1]] = [(info[0], info[2])]
        
        # Read the next line
        line = fileHandler.readline()
    
    fileHandler.close()
    return cityGraph


# TODO: Verify the graph model
file, start, end = input_handler()
print(graph_modeler(file, start, end))