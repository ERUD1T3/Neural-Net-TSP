import dataManip as dm


def main():
    inputfile = './data/map.csv'
    graph = dm.readData(inputfile)
    # print(graph.keys())
    testdist = graph['BocaRaton']['Clearwater']
    print(f'Distance from Boca Raton to Clearwater is {testdist} mile')


if __name__ == "__main__":
    main()
