1.) Name: Nolan Donaldson 10754467

2.) Python 3

3.) Windows 10 (Ubuntu may also be used)

4.) The code is a single file python script. There are 4 functions, not including main, which handle the 
    necessary elements of the program. The first handles the command line arguments needed to run the 
    program. The next takes the contents of the input file and models it as a graph. The penultimate 
    function is the main search function of the graph. It uses Dijkstra's algorithm to find the shortest
    path between two cities. The last function simply prints the results of the search in the desired
    format.

5.) To run this script, first ensure that it is contained within the same folder as the desired input file. 
    No prior compilation is needed. Open Windows PowerShell and navigate to the directory of the script. 
    The command used to run the script will follow this basic premise:

	python3 find_route.py -i [NAME_OF_INPUT_FILE] -o [ORIGIN_CITY] -t [TARGET_CITY]

    Alternatively, long form arguments may be used (this information can be seen with the --help command):

	python3 find_route.py --input [NAME_OF_INPUT_FILE] --origin [ORIGIN_CITY] --target [TARGET_CITY]

    For example, to run the example from the assignment description, one would enter the following:

	python3 find_route.py -i input1.txt -o Bremen -t Frankfurt

    Alternatively, they can use the lengthy argument names. In addition, one can also run this script on a linux
    shell such as Ubuntu. The steps are the same as in PowerShell.