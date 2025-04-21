import random
from common.base_agent import BaseAgent
from common.move import Move

# Student scipers, will be automatically used to evaluate your code
SCIPERS = ["390899", "Ton sciper"]

#INFO:
# Nouvelle version qui marche mieux parce qu'elle évite les autres trains mais je pense qu'elle sera moins efficace que l'autre une fois que l'autre evitera les trains
#En revanche le code de mise en place est plus simple
class Agent(BaseAgent):
    nickname = "Bob"
    GO = 0
    def positions(self):
        """
        Cordinates which are reused several times throughout the movement choice
        """

        #train coordinates
        self.x_train_position = self.all_trains[self.nickname]["position"][0]
        self.y_train_position = self.all_trains[self.nickname]["position"][1]

        #passenger coordinates
        
        #latest train movement
        self.move_vector = self.all_trains[self.nickname]["direction"]
        self.previous_move = Move(tuple(self.move_vector))
        
        #wanted position
        self.wanted_x_position = 0
        self.wanted_y_position = 0

        #delivery zone coordinates
        self.x_delivery_position = self.delivery_zone['position'][0]
        self.y_delivery_position = self.delivery_zone['position'][1]
        delivery_zone_height = self.delivery_zone['height']
        delivery_zone_width = self.delivery_zone['width']

        #delivery edges
        self.x_min_delivery = self.x_delivery_position
        self.x_max_delivery = self.x_delivery_position + delivery_zone_width
        self.y_min_delivery = self.y_delivery_position
        self.y_max_delivery = self.y_delivery_position + delivery_zone_height

    #determine closest passanger
    #determine if they need to be delivered
    #choose next position
    #check if there is another train
    #check if there is a wall
    
    def distance_to_point(self, train_x, train_y, point_x, point_y):
        """
        Calculates shortest distance between train and point
        """
        return abs(train_x - point_x) + abs(train_y - point_y)

    def available_grid_coordinates(self):
        """
        Determines all grid coordinates which have no obstacle
        """
        grid_coordinates = []
        for x in range(0, self.game_width, self.cell_size):
            for y in range(0, self.game_height, self.cell_size):
                grid_coordinates.append((x,y))
        #print("GRIIIIIIIIID", grid_coordinates)
        print("TRAIN POS", self.all_trains[self.nickname]["position"], tuple(self.all_trains[self.nickname]["position"]) in grid_coordinates)
        for train in self.all_trains:
            train_pos = tuple(self.all_trains[train]["position"])
            if train_pos in grid_coordinates:
                grid_coordinates.remove(train_pos)
            for wagon_pos in self.all_trains[train]["wagons"]:
                print("WAGON_POS", wagon_pos, tuple(wagon_pos) in grid_coordinates)
                if tuple(wagon_pos) in grid_coordinates:
                    grid_coordinates.remove(tuple(wagon_pos))
        
        return grid_coordinates
    
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
    
    
    def path_to_point(self, point):
        """
        Determines direction to take to get to closest passenger
        """
        #########################################################################33
        self.positions()
    
        moves = [Move.UP.value, Move.DOWN.value, Move.LEFT.value, Move.RIGHT.value]
        previous_m = tuple(-i for i in self.move_vector)
        moves.remove(previous_m)
        shortest_distance = float('inf')
        best_move = None
        for move in moves:
            new_x = self.x_train_position + move[0] * self.cell_size
            new_y = self.y_train_position + move[1] * self.cell_size
            distance = self.distance_to_point(new_x, new_y, point[0], point[1])
            new_pos = []
            new_pos.append(new_x)
            new_pos.append(new_y)
            available_positions = self.available_grid_coordinates()
            if tuple(new_pos) in available_positions:
                possible_move = move
                if distance < shortest_distance:
                    shortest_distance = distance
                    best_move = move  
        return best_move if best_move is not None else possible_move
        

    def get_move(self):
        
        
        if self.GO == 0:
            passenger_pos = self.closest_passenger()
            move = self.path_to_point(passenger_pos)
        else:
            delivery_zone_pos = self.delivery_zone['position']
            move = self.path_to_point(delivery_zone_pos)
        if len(self.all_trains[self.nickname]['wagons'])>=4:
            self.GO = 1
        if len(self.all_trains[self.nickname]['wagons']) == 0:
            self.GO = 0
            
        return Move(move)

    