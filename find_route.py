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