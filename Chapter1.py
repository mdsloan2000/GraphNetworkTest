
# Graph Testing



# Main Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sbn 

import sqlalchemy


# Graph Setup

import networkx as nx 
G = nx.Graph()

import random
from numpy import random as nprand
seed = hash("Network Science in Python") % 2**32
nprand.seed(seed)
random.seed(seed)

# Functions


def main():
    try:
        G.add_node('A')
        G.add_nodes_from(['B', 'C'])
        G.add_edge('A', 'B')
        G.add_edges_from([('B', 'C'), ('A', 'C')])
        plt.figure(figsize=(7.5, 7.5))
        nx.draw_networkx(G)
        plt.show()
        G.add_edges_from([('B', 'D'), ('C', 'E')]) 
        nx.draw_networkx(G)
        plt.show()
    except:
      print('Something went wrong')
    finally:
      print('The try except is finished')
    pass





# Main Execution

if __name__ =="__main__":
    main()
    