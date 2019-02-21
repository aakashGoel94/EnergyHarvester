import pandas as pd

"""Node states"""
GATHERING = "gathering"
SLEEPING = "sleeping"
CHARGING = "charging"
IDLE = "idle"

class Node:
    """Represents a node in the network"""
    def __init__(self, id, energy_level = 0, state = SLEEPING, threshold_upper = 2.5, threshold_lower = 2, charge_rate = 0.1, discharge_rate = 0.2):
        self.id = id #The id of the node
        self.energy_level = energy_level #
        self.state = state
        self.threshold_upper = threshold_upper
        self.threshold_lower = threshold_lower
        self.charge_rate = charge_rate
        self.discharge_rate = discharge_rate

    def update(self): 
        """For simulation purposes. Update the states of the node."""
        if (CHARGING):
            self.energy_level += self.charge_rate
        elif (GATHERING):
            self.energy_level -= self.discharge_rate

        if (self.energy_level < self.threshold_lower):
            self.state = SLEEPING
        elif (self.energy_level > self.threshold_upper):
            self.state = IDLE


class NodeManager:
    """Manages a table of nodes contained in the network"""
    def __init__(self):
        self.number_of_nodes = 0
        self.nodes = pd.DataFrame(columns=['id','energy'])
        self.nodes.set_index('id', inplace=True, verify_integrity=True)
    
    def remove_node(self, id):
        self.nodes = self.nodes.drop(index=id)

    def add_node(self, node):
        self.nodes.loc[node.id] = node.energy_level

    def update_node(self, node):
        self.nodes.loc[node.id] = node.energy_level

    def get_node(self, id):
        return self.nodes.loc[id]

    def node_is_in_system(self, id):
        try:
            value = self.nodes.loc[id]
        except KeyError:
            return False

        return value is not None
