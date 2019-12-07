import dataManip as dm


if __name__ == "__main__":
    graph = dict()
    inputfile = './data/map.csv'
    dm.readData(inputfile, graph)
    # print(graph.keys())
    testdist = graph['BocaRaton']
    print(f'Distance from Boca Raton to Clearwater is {testdist} mile')
