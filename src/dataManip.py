# file to handle the data
import csv


def readData(mapfile, graph):
    '''read the data and return graph'''
    cities = None

    with open(mapfile, 'r') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=',')
        for idx, row in enumerate(csv_reader):
            if idx == 0:
                cities = row
                graph = {y: {x: 0 for x in cities} for y in cities}
            else:
                for idx, city in enumerate(cities):
                    graph[row[0]][city] = int(row[idx+1])

    print(graph)
