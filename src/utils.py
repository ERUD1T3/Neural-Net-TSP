import math
import numpy as np


def sigmoid(dE, T):
    '''sigmoid activation fuctions'''
    return 1 / (1 + math.exp(dE/T))


def get_distance(states, distances):
    '''
    Returns the distance traveled by a state matrix given the distance matrix
    states (np.matrix): state matrix representing nodes visited along a tour
    distances (np.matrix): distance matrix describing the distance between any two nodes

    Returns distance (float): total distance traveled on the hamiltonian tour
    '''
    tour = get_tour(states)
    distance = 0
    for i, stop in enumerate(tour[1:]):
        distance += distances[stop, tour[i]]

    return distance


def get_tour(states):
    '''
    Create a string sequence cities traveled at each epoch to
    represent the hamiltonian tour

    Returns tour (string): the active tour in the current network
    '''
    if not hamiltonian(states):  # if a HT hasn't been completed, then distance can't be computed
        return 'hamiltonian tour not complete'

    _, epochs = states.shape
    tour = []

    for t in range(epochs):  # for each epoch
        # grab the array describing the states of its nodes
        event = states[:, t].A1
        for i, n in enumerate(event):  # and, for each node within it
            if n == 1:  # if it's active
                tour.append(i)  # add its index to the tour object

    return tour


def print_tour(states, node_map):
    '''
    Prints the tour in a readable format
    states (np.matrix): state matrix
    node_map (dict): dictionary of city titles for each node
    Returns tour (str): string-formatted representation of the your taken
    '''
    insert = '->'
    tour = get_tour(states)
    print_str = f'{node_map[tour[0]]}'
    for i in tour[1:]:
        print_str += (insert + node_map[i])

    return print_str


def hamiltonian(states):
    '''
    Checks that the given state matrix creates a valid hamiltonian tour (HT)
    Returns status (bool): True if the state matrix creates a HT; False otherwise
    '''
    _, epochs = states.shape
    tour = {}
    for t in range(epochs):
        # collects the epoch column containing nodes within a given epoch
        event = states[:, t].A1
        if np.sum(event) != 1:  # if < 1 or > 1 nodes are activated, breaks the HT
            return False

        # all of these epochs below have only one node activated
        for i, n in enumerate(event):
            if n == 1:  # if a node is activated
                if t == epochs - 1:  # is it the last stop in the HT
                    if tour[i] != 0:  # and does it return to the starting locations
                        return False
                elif i in tour:  # or does it repeat another destination
                    return False
                else:  # if not, add it to the tour to review later
                    tour[i] = t

    return True


def consensus(states, network):
    '''
    Consensus function, computing the summated values of weights and states between
    every node (city,epoch) in the network
    states (np.matrix): matrix representing the states of the nodes provided
    network (np.matrix): matrix of nodes holding the weights

    Returns total (int) consensus value
    '''
    get_values = np.vectorize(lambda n: n.get_value(states))
    total = 0.5 * np.sum(get_values(network))
    return total
