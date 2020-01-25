import argparse
import sys
import heapq

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
def graph_modeler(input):

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
            cityGraph[info[0]].append((info[1], int(info[2])))
            if info[1] in cityGraph:
                cityGraph[info[1]].append((info[0], int(info[2])))
            else:
                cityGraph[info[1]] = [(info[0], int(info[2]))]
        # Otherwise, create a new list at this index 
        else:
            cityGraph[info[0]] = [(info[1], int(info[2]))]
            # This graph is undirected, so include both directions
            cityGraph[info[1]] = [(info[0], int(info[2]))]
        
        # Read the next line
        line = fileHandler.readline()
    
    fileHandler.close()
    return cityGraph


# Uses Dijkstra's algorithm to search the maze for the shortest path between the
# start and target cities using a priority queue
# Refrences: https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm and
# https://towardsdatascience.com/introduction-to-priority-queues-in-python-83664d3178c3
def dijkstra_search(graph, start, end):
    # Initializing the needed data structures
    distances = {vertex: sys.maxsize for vertex in graph}
    distances[start] = 0

    # Record of path taken
    previous = {vertex: '' for vertex in graph}

    # Priority queue of vertices used to find the solution
    bigQ = [(0, start)]

    while True:
        # If the queue runs out of cities without reaching the end, the distance is infinite
        # And the path does not exist
        if len(bigQ) == 0:
            return distances, previous
            #return [], []

        distance, current = heapq.heappop(bigQ)

        # #If the end city is reached, stop the loop
        # if current == end:
        #     break
        # Compares the distance between adjacent vertices and alternate paths
        # if distance > distances[current]:
        #     continue

        for adjacent, cost in graph[current]:
            alternate = distance + cost
            # If a new, better, path among the adjacent vertices is found, switch to it
            if alternate < distances[adjacent]:
                distances[adjacent] = alternate
                previous[adjacent] = current
                heapq.heappush(bigQ, (alternate, adjacent))

    return distances, previous



# Prints the results
def print_results(distances, prev, start, end):
    distance = ''
    path = ''

    # If a valid path does not exist, indicate an infinite distance with no possible route
    if len(distances) == 0:
        distance = 'infinity'
        path = 'none'
    # Otherwise, print the path and the distance
    else:
        # Tracing the previous city record for the cities traveled
        traceback = end
        temp = 0
        while True:
            temp += distances[traceback]
            path += prev[traceback] + ' to ' + traceback + ' ' + str(distances[traceback]) + ' km\n'
            traceback = prev[traceback]
            if traceback == start:
                break
        distance = str(temp) + ' km'
        
    print('distance: ', distance, '\nroute:\n', path, sep='', end = '')
        
file, start, end = input_handler()
pickles = graph_modeler(file)
#dists, prevs = dijkstra_search(graph_modeler(file), start, end)
#print(dists)
#print_results(dists, prevs, start, end)