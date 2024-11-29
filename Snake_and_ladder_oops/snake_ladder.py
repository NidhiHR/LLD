import random
class Board:
    def __init__(self,size,snakes,ladders):
        self.board_size=size
        self.snakes=snakes
        self.ladders=ladders

    def pick_position(self,cur_position,dice_roll):
        new_position=cur_position+dice_roll
        if new_position>self.board_size:
            return cur_position
        return self.snakes.get(new_position,self.ladders.get(new_position,new_position))
    
class Player:
    def __init__(self,name):
        self.name=name
        self.position=1

    def move(self,position):
        self.position=position

    def __str__(self):
        return (f" The {self.name} has moved to {self.position}")
    
class Dice:
    def __init__(self,number_of_dice):
        self.number_of_dice=number_of_dice
        
    def roll_dice(self):
        return sum(random.randint(1,6) for _ in range(self.number_of_dice))
    
class game:
    def __init__(self,number_of_dice):
        self.number_of_dice=number_of_dice
        self.players=[]
        self.board=None
        self.position_index=0

    def game_initialization(self,board_size,snakes,ladders,number_of_dice,players):
        self.board=Board(board_size,snakes,ladders)
        self.number_of_dice=number_of_dice
        self.players=[Player(play) for play in players]

    def game_over(self):
        return any(player.position==self.board.board_size for player in self.players)
    
    def start(self):
        print('game has started between')
        print('Players : '''.join(player.name for player in self.players))

        while not self.game_over():
            self.play()
        winner=self.players[self.position_index]
        print(f"\n🎉 {winner.name} wins the game by reaching position {self.board.board_size}!")

    def play(self):
        player=self.players[self.position_index]
        dice=Dice(self.number_of_dice)
        dice_roll=dice.roll_dice()
        print(f" The player {player.name} has got {dice_roll}")
        next_pos=self.board.pick_position(player.position,dice_roll)
        player.move(next_pos)
        print(f"The {player.name} has moved to {next_pos}")
        if next_pos==self.board.board_size:
            return
        
        self.position_index=(self.position_index+1)%len(self.players)

games=game(2)
board_size=36
snakes = {14: 7, 22: 2, 33: 19}
ladders = {3: 11, 6: 17, 20: 29}
player_names = ["Alice", "Bob", "Charlie"]

games.game_initialization(board_size,snakes,ladders,2,player_names)
games.start()