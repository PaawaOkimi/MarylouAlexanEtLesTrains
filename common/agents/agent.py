import random
from common.base_agent import BaseAgent
from common.move import Move

# Student scipers, will be automatically used to evaluate your code
SCIPERS = ["390899", "Ton sciper"]

#INFO:
#J'ai créé une première fonction pour éviter de devoir remettre les coordonnées a chaque nouvelle fonction
#Je suis en train de faire qu'il aille chercher les passager ou les déposer. Mon idée'
#c'est qu'on mette ensuite le choix de mouvement dans le get_move() du style, si c'est le plus proche on fait passenger sinon delivery...'


class Agent(BaseAgent):
    def positions(self):
        """
        Coordinates which a reused several times to determine the train's next move
        """

        #Train Coordinates
        self.x_train_position = self.all_trains['Bob']['position'][0]
        self.y_train_position = self.all_trains['Bob']['position'][1]

        #passenger Coordinates
        self.x_passenger_position = self.passengers[0]['position'][0]
        self.y_passenger_position = self.passengers[0]['position'][1]

        #previous train movement
        self.current_move = Move(tuple(self.all_trains['Bob']['direction']))

        #delivery zone coordinates
        self.x_delivery_zone = 0


    def path_to_passenger(self):
        """
        Determines possible path to collect passenger (not yet optimized)
        """

        self.positions()

        #how to move towards passengers depending on current move
        if self.current_move in (Move.UP, Move.DOWN):
            if self.x_train_position == self.x_passenger_position:
                return self.current_move
            elif self.x_train_position > self.x_passenger_position:
                return Move.LEFT
            elif self.x_train_position < self.x_passenger_position:
                return Move.RIGHT
        if self.current_move in (Move.RIGHT, Move.LEFT):
            if self.y_train_position == self.y_passenger_position:
                return self.current_move
            elif self.y_train_position > self.y_passenger_position:
                return Move.UP
            elif self.y_train_position < self.y_passenger_position:
                return Move.DOWN
    
    def deliver_passengers(self): ##Je suis en train d'ecrire cette fonction
        """if move in (Move.UP, Move.DOWN):
            if x_train_position == x_:
                return move
            elif x_train_position > x_passenger_position:
                return Move.LEFT
            elif x_train_position < x_passenger_position:
                return Move.RIGHT
        if move == Move.RIGHT or move == Move.LEFT:
            if y_train_position == y_passenger_position:
                return move
            elif y_train_position > y_passenger_position:
                return Move.UP
            elif y_train_position < y_passenger_position:
                return Move.DOWN"""

        pass

    def avoid_wagons(self):
        #QUESTION: est-ce qu'on fait une fonction pour éviter ses propres wagons et une pour éviter les autres trains ou on combine les deux?
        """
        Moves possible to avoid running into other trains/into the trains own wagons
        """
        pass

    def get_move(self):
        ######
        #self.logger.debug(self.all_trains)
        #self.logger.debug(self.passengers)
        #self.logger.debug(self.delivery_zone)
        #####
        """
        Determines Train's next position
        """
        #A rajouter: des conditions if,elif,else qui determinent si le train va en direction des passager/évite d'autres trains/dépose des passager,...
        move = self.path_to_passenger()
        return move



            

