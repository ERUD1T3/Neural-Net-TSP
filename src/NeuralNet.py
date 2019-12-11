# file to build the neural network for solving the Traveling salesman problem

import numpy as np


class Boltzmann:
    def __init__(self, citiesMatrix):
        '''Initialize a Boltzmann machine NN'''
        # n = 26 cities
        # weights n*(n - 1)**2 = 16250
        # total number of connections = 2*number of weights = 32500
        # node units = n*n = 676

    def consensus(self, config):
        '''Given a config return the consensus val'''
        return 0
