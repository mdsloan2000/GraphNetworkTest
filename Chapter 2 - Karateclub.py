
 ## Main Imports
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt 
import seaborn as sbn 

import sqlalchemy


# Graph Setup

import networkx as nx 



def main():
    G = nx.karate_club_graph()
    karate_pos = nx.spring_layout(G, k=0.3)
    nx.draw_networkx(G, karate_pos)
    return 1



if __name__ =="__main__":
    main()