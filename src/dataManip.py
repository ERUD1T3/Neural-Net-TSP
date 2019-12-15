# file to handle the data
import csv


def readData(mapfile):
    '''
    read data from a csv file
    returns a 2D list
    '''
    graph = []
    with open(mapfile, 'r') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        for index, row in enumerate(csv_reader):
            if index > 0:
                graph.append(row[1:])

    # print(graph)
    for i in range(len(graph)):
        for j in range(len(graph)):
            graph[i][j] = int(graph[i][j])

    return graph
