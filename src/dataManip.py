# file to handle the data
import csv


def readData(mapfile):
    '''read data and return list graph'''
    graph = []
    with open(mapfile, 'r') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        for index, row in enumerate(csv_reader):
            if index > 0:
                graph.append(row[1:])

    # print(graph)
    return graph
