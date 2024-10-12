import math
import networkx as nx
import itertools
import numpy as np
import pyts
import ts2vg


def my_visibility_graph(time_series):
    """
    Function to create visibility graph from time series data
    :param time_series: list of time series data
    :return: networkx graph object
    """
    G = nx.Graph()
    n = len(time_series)

    for (t1, n1), (t2, n2) in itertools.combinations(enumerate(time_series), 2):
        slope = (n2 - n1) / (t2 - t1)
        y_intercept = n2 - slope * t2

        obstructed = any(
            n >= slope * t1 + y_intercept
            for t, n in enumerate(time_series[t1 + 1:t2], start=t1 + 1)
        )

        if not obstructed:
            G.add_edge(t1, t2)

    return G


def my_reccurance_graph(time_series, threshold):
    """
    Function to create reccurance graph from time series data
    :param time_series: list of time series data
    :param threshold: threshold value for reccurance
    :return: networkx graph object
    """
    G = nx.Graph()
    n = len(time_series)
    for i in range(n):
        for j in range(i+1, n):
            if abs(time_series[j] - time_series[i]) <= threshold:
                G.add_edge(i, j)
    return G


def reccurance_graph(time_series, threshold):
    rp = pyts.image.RecurrencePlot(threshold=threshold)
    X_rp = rp.fit_transform([time_series])
    X_rp = X_rp[0]
    X_rp -= np.eye(X_rp.shape[0])
    G = nx.from_numpy_array(X_rp)


vg = ts2vg.NaturalVG()
def visibility_graph(time_series, vg=vg):
    vg.build(time_series)
    G = vg.as_networkx()
    return G


def get_sensor_values(data, sensor_name):
    sensor_values = []
    for row in data:
        if row[1] == sensor_name:
            sensor_values.append(row[3])
    return sensor_values


"""
Features Requred : 
Entropy
Clustering Coefficient Sequence
Global Efficiency
Small-Worldness
Graph Index Complexity (GIC)
Size of Max Clique
Cost of Traveling Salesman Problem (TSP)
Independence Number
Size of Minimum Cut
Vertex Coloring Number
"""


# def graph_entropy(G):
#     def node_entropy(G, node):
#         neighbours = list(G.neighbours(node))
#         degree_sum = sum(G.degree(neighbour) for neighbour in neighbours)

#         if degree_sum == 0:
#             return 0

#         entropy = 0
#         for neighbour in neighbours:
#             p = G.degree(neighbour) / degree_sum
#             entropy += p * np.log(p)

def GraphIndexComplexity(G):
    lamda_max = max(np.linalg.eig(nx.to_numpy_array(G))[0])
    n = G.number_of_nodes()

    c = (lamda_max - 2 * np.cos(np.pi/(n + 1))) / \
        (n - 1 - np.cos(np.pi/(n + 1)))
    C = 4 * c * (1 - c)

    return C


def VertexColoringNumber(G):
    greedy_color = nx.coloring.greedy_color(G)
    return len(set(greedy_color.values()))


def degree_distribution(G):
    vk = dict(G.degree())
    vk = list(vk.values())  # We get only the degree values
    maxk = np.max(vk)
    kvalues = np.arange(0, maxk + 1)  # Possible values of k
    Pk = np.zeros(maxk + 1)  # P(k)
    for k in vk:
        Pk[k] += 1
    Pk = Pk / sum(Pk)  # The sum of the elements of P(k) must be equal to one

    return kvalues, Pk


def shannon_entropy(G):
    k, Pk = degree_distribution(G)
    H = 0
    for p in Pk:
        if p > 0:
            H -= p * math.log(p, 2)
    return H


def features(G):
    
    # avg_degree = np.mean([d for n, d in G.degree()])
    # density = nx.density(G)
    clustering_coeff = nx.average_clustering(G)

    # Centrality measures
    degree_centrality = np.mean(
        list(nx.degree_centrality(G).values()))
    betweenness_centrality = np.mean(
        list(nx.betweenness_centrality(G).values()))
    closeness_centrality = np.mean(
        list(nx.closeness_centrality(G).values()))
    pagerank = np.mean(list(nx.pagerank(G).values()))

    # Other Graph properties
    degree_distribution = np.mean(
        np.array(nx.degree_histogram(G)))
    average_path_length = nx.average_shortest_path_length(G)
    assortativity = nx.degree_assortativity_coefficient(G)
    # Updated to compute diameter
    longest_path = nx.diameter(G)

    
    no_of_edges = nx.number_of_edges(G)

    clustering_coeff = nx.average_clustering(G)

    global_efficiency = nx.global_efficiency(G)

    # small_worldness = nx.sigma(G)  # small worldness

    graph_index_complexity = np.abs(GraphIndexComplexity(G))

    max_clique_size = len(next(nx.find_cliques(G)))  # size of max clique

    # cost of TSP
    # tsp_cost = len(nx.approximation.traveling_salesman_problem(G))

    # independence_number = len(
    #     nx.maximal_independent_set(G))  # independence number

    min_cut_size = len(nx.minimum_edge_cut(G))  # size of minimum cut

    vertex_coloring_number = VertexColoringNumber(G)

    entropy = shannon_entropy(G)

    return (
        degree_centrality,
        betweenness_centrality,
        closeness_centrality,
        pagerank,
        degree_distribution,
        average_path_length,
        assortativity,
        longest_path,
        no_of_edges,
        clustering_coeff,
        global_efficiency,
        # small_worldness,
        graph_index_complexity,
        max_clique_size,
        # tsp_cost,
        # independence_number,
        min_cut_size,
        vertex_coloring_number,
        entropy
    )
