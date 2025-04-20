import random
from common.base_agent import BaseAgent
from common.move import Move

# Student scipers, will be automatically used to evaluate your code
SCIPERS = ["390899", "Ton sciper"]

#TRUCS A FAIRE:
#COINS _ALEXAN
#POINTS SUR LES BORDURES _ Alexan (Je crois que j'ai resolu le problème: je ne prenais pas en compte la variation de taille de la grille en fonction du nombre de passager)
#ALEXAN_ resoudre le problème de taille de la delivery zone (dans le dossier delivery zone j'arrive pas a comprendre la taille du truc :( ))
#NE PAS SE PRENDRE LES WAGONS _MARYLOU POUR L'INSTANT
#Lorsque x_train == x_position, les train va continuer dans la meme direction _MARYLOU

#INFO:
#J'ai un peut reformuler la fonction pour les passagers les plus proches (les noms etaient droles mais a la fin c plus clair pour le correcteur comme ca je pense :))
"""Petite remarque pour les conventions d'écriture: 
        -pour les noms de variables faut utiliser snake_case
        -je crois que les gens aiment bien quand on mets des espaces si on se sert de +,=,... (du style pos + dist) 
Voila voila :), je suis pas 100% sure que c'est exactement ca mais sinon je conseille de le faire direct en ecrivant le code plutot que de devoir tout relire a la fin
(Après si ca te ralenti dans l'écriture c'est pas un problème ca ne me dérange pas de modifier les trucs quand tu les push (Dis-moi ce que tu préfères ou si y a un problème))"""


class Agent(BaseAgent):

    nickname = "Bob"

    def positions(self):
        """
        Coordinates which a reused several times to determine the train's next move
        """

        #Current Train Coordinates
        self.x_train_position = self.all_trains[self.nickname]['position'][0]
        self.y_train_position = self.all_trains[self.nickname]['position'][1]
        
        #passenger Coordinates
        passenger_pos = self.closest_passenger()
        self.x_passenger_position = passenger_pos[0] 
        self.y_passenger_position = passenger_pos[1]

        #previous train movement
        self.move_vector = tuple(self.all_trains[self.nickname]['direction'])
        self.current_move = Move(self.move_vector)

        #wanted position
        self.wanted_x_pos = (self.move_vector[0] * self.cell_size) + self.x_train_position
        self.wanted_y_pos = (self.move_vector[1] * self.cell_size) + self.y_train_position

        #delivery zone coordinates
        self.x_delivery_position = self.delivery_zone['position'][0]
        self.y_delivery_position = self.delivery_zone['position'][1]
        delivery_zone_height = self.delivery_zone['height']
        delivery_zone_width = self.delivery_zone['width']
        self.x_min_delivery = self.x_delivery_position
        self.x_max_delivery = self.x_delivery_position + delivery_zone_width
        self.y_min_delivery = self.y_delivery_position
        self.y_max_delivery = self.y_delivery_position + delivery_zone_height

    def closest_passenger(self):
        """
        Determines passenger closest to train
        """
        passenger_positions=[]
        for i in range(len(self.passengers)):
            passenger_positions.append(self.passengers[i]['position'])
        closest_dist = float('inf')
        for pos in passenger_positions:
            distance = abs(pos[0] - self.all_trains[self.nickname]['position'][0]) + abs(pos[1] - self.all_trains[self.nickname]['position'][1])
            if distance < closest_dist:
                closest_dist = distance
                closest_passenger = pos
        return closest_passenger
        
    def move_if_walls(self, move):

        self.positions()

        if move == Move.UP:
            #checks if wall above
            if self.y_train_position - self.cell_size < 0: 
                #checks if in top left corner
                if self.x_train_position - self.cell_size < 0:
                    return Move.turn_right(move)    
                return Move.turn_left(move)
                
        elif move == Move.DOWN:
            #checks if wall below
            if self.y_train_position + self.cell_size >= self.game_height:
                #checks if bottom left corner
                if self.x_train_position - self.cell_size < 0:
                    return Move.turn_left(move)
                return Move.turn_right(move)
                
        elif move == Move.LEFT:
            #checks if wall to the left
            if self.x_train_position - self.cell_size < 0:
                #checks if bottom left corner
                if self.y_train_position + self.cell_size >= self.game_height:
                    print("Bottom left corner")
                    return Move.turn_right(move)
                return Move.turn_left(move)
                
        elif move == Move.RIGHT:
            #checks if wall to the right
            if self.x_train_position + self.cell_size >= self.game_width:
                #checks if bottom right corner
                if self.y_train_position + self.cell_size >= self.game_height:
                    print("Bottom right corner")
                    return Move.turn_left(move) 
                return Move.turn_right(move)
        
        return move

    def path_to_passenger(self):
        """
        Determines possible path to collect passenger (not yet optimized)
        """

        self.positions()    

        distance = abs(self.x_passenger_position - self.x_train_position) + abs(self.y_passenger_position - self.y_train_position)
        next_distance = abs(self.x_passenger_position - self.wanted_x_pos) + abs(self.y_passenger_position - self.wanted_y_pos)

        #how to move towards passengers depending on current move
        if self.current_move in (Move.UP, Move.DOWN):
            if self.x_train_position == self.x_passenger_position:
                if distance < next_distance:
                    return Move.turn_left(self.current_move)
                return self.current_move
            elif self.x_train_position > self.x_passenger_position:
                return Move.LEFT
            elif self.x_train_position < self.x_passenger_position:
                return Move.RIGHT
            
        if self.current_move in (Move.RIGHT, Move.LEFT):
            if self.y_train_position == self.y_passenger_position:
                if distance < next_distance:
                    return Move.turn_left(self.current_move)
                return self.current_move
            elif self.y_train_position > self.y_passenger_position:
                return Move.UP
            elif self.y_train_position < self.y_passenger_position:
                return Move.DOWN
    
    def deliver_passengers(self): ##Je suis en train d'ecrire cette fonction
        
        self.positions()
        #print(type(self.x_delivery_position), type(self.delivery_zone_width), type(self.x_train_position))

        distance = max(0, self.x_min_delivery - self.x_train_position, self.x_train_position - self.x_max_delivery) + max(0, self.y_min_delivery - self.y_train_position, self.y_train_position - self.y_max_delivery) 
        next_distance = max(0, self.x_min_delivery - self.wanted_x_pos, self.wanted_x_pos - self.x_max_delivery) + max(0, self.y_min_delivery - self.wanted_y_pos, self.wanted_y_pos - self.y_max_delivery)
        if self.current_move in (Move.UP, Move.DOWN):
            if (self.x_min_delivery) <= self.x_train_position <= (self.x_max_delivery):
                if distance < next_distance:
                    if self.y_train_position > self.y_delivery_position:
                        return Move.turn_right(self.current_move)
                    return Move.turn_left(self.current_move)
                return self.current_move
            elif self.x_train_position > self.x_max_delivery :
                return Move.LEFT
            elif self.x_train_position < self.x_min_delivery :
                return Move.RIGHT
            
        if self.current_move in (Move.RIGHT, Move.LEFT):
            if self.y_min_delivery <= self.y_train_position <= self.y_max_delivery:
                if distance < next_distance:
                    if self.x_train_position < self.x_delivery_position:
                        return Move.turn_right(self.current_move)
                    return Move.turn_left(self.current_move)
                return self.current_move
            elif self.y_train_position > self.y_min_delivery:
                return Move.UP
            elif self.y_train_position < self.y_max_delivery:
                return Move.DOWN
        
        return self.current_move

    def wanted_position(self, move):
        wanted_move = move.value
        wanted_x_pos = (wanted_move[0] * self.cell_size) + self.x_train_position
        wanted_y_pos = (wanted_move[1] * self.cell_size) + self.y_train_position
        wanted_pos =(wanted_x_pos, wanted_y_pos)

        return wanted_pos

    def avoid_wagons_and_trains(self, move):
        #QUESTION: est-ce qu'on fait une fonction pour éviter ses propres wagons et une pour éviter les autres trains ou on combine les deux?
        """
        Moves possible to avoid running into other trains/into the trains own wagons
        """
        #next position depending on wanted move
        
        #defines positions of every train wagon on the grid
        wagon_positions = []
        for train in self.all_trains:
            wagon_positions.append(self.all_trains[train]["position"])
            for wagon_pos in self.all_trains[train]["wagons"]:
                wagon_positions.append(wagon_pos) 

        wanted_position = self.wanted_position(move)
        wanted_pos = []
        wanted_pos.append(wanted_position[0])
        wanted_pos.append(wanted_position[1])
        print(wanted_pos in wagon_positions, wanted_pos) #, wagon_positions)
        #How to avoid other trains
        if wanted_pos in wagon_positions:
            while wanted_position in wagon_positions:
                print("TURN", move)
                move = Move.turn_left(move)
                wanted_pos = self.wanted_position(move)
        return move

    def get_move(self):
        
        ######
        #self.logger.debug(self.all_trains)
        #self.logger.debug(self.passengers)
        #self.logger.debug(self.delivery_zone)
        #####
        """
        Determines Train's next position
        """
        if self.GO == 0:
            move = self.path_to_passenger()
            move = self.avoid_wagons_and_trains(move)
            move = self.move_if_walls(move)
        else:
            move = self.deliver_passengers()
            #MUST BE TRANSFORMED INTO ONE FUNCTION WITH AVOID_ALL_OBSTACLES
            move = self.avoid_wagons_and_trains(move)
            move = self.move_if_walls(move)
        if len(self.all_trains[self.nickname]['wagons'])>=4:
            self.GO = 1
        if len(self.all_trains[self.nickname]['wagons']) == 0:
            self.GO = 0
        #A rajouter: des conditions if,elif,else qui determinent si le train va en direction des passager/évite d'autres trains/dépose des passager,...
        #if len(self.all_trains[self.nickname]['wagons']) > 0: # and self.passed_on_delivery_zone == 0:
        #    move = self.deliver_passengers()
        #    #MUST BE TRANSFORMED INTO ONE FUNCTION WITH AVOID_ALL_OBSTACLES
        #    move = self.avoid_wagons_and_trains(move)
        #    move = self.move_if_walls(move)
        #else:
        #    move = self.path_to_passenger()
        #    move = self.avoid_wagons_and_trains(move)
        #    move = self.move_if_walls(move)
        return move


#def avoid_all(move):
#    wagon_positions = self.wagon_pos()
#    available_positions = self.grid_coordinates()
#    for i in range(4):
#        wanted_pos = self.wanted_pos(move)
#        if wanted_pos not in available_positions or wanted_pos in wagon_positions:
#            move = Move.turn_left(move)
#        if move = current_move * -1 :


            

