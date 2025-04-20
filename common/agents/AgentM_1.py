"""
Fichier a ignorer il ne sert a rien...
"""



import random
from common.base_agent import BaseAgent
from common.move import Move

# Student scipers, will be automatically used to evaluate your code
SCIPERS = ["390899", "Ton sciper"]

class Agent(BaseAgent):

    nickname = "Bob"

    def positions(self):
        """
        Coordinates which are reused several times to determine the next move
        """

        #Current Train Coordinates
        self.x_train_position = self.all_trains[self.nickname]['position'][0]
        self.y_train_position = self.all_trains[self.nickname]['position'][1]

        #Previous Train Movement
        self.move_vector = tuple(self.all_trains[self.nickname]['direction'])
        self.previous_move = Move(self.move_vector)

        #Delivery Zone Position


    def wanted_coordinates(self, move): 
        wanted_x = self.x_train_position + move[0] * self.cell_size
        wanted_y = self.y_train_position + move[1] * self.cell_size   
        return (wanted_x, wanted_y)
    
    def distance_to_point(self, train_x, train_y, point_x, point_y):
        """
        Calculates shortest distance between train and point
        """
        return abs(train_x - point_x) + abs(train_y - point_y)
    
    def closest_passenger(self):
        """
        Determines distance to closest passenger
        """
        passenger_positions = []
        for i in range(len(self.passengers)):
            passenger_positions.append(self.passengers[i]['position'])
        closest_distance = float('inf')
        for pos in passenger_positions:
            distance = abs(pos[0] - self.all_trains[self.nickname]['position'][0]) + abs(pos[1] - self.all_trains[self.nickname]['position'][1])
            if distance < closest_distance:
                closest_distance = distance
                closest_passenger = pos
        return closest_passenger   
    
    def move_if_walls():

