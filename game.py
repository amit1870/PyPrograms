import random
import time
import os
import re
from levels import *

class Position(object):
    """
    Position class representing position of players
    """

    def __init__(self, n):
        self.value = n

    def getPosition(self):
        return self.value

    def setPosition(self, n):
        self.value = n

    def UpdatePosition(self, dice_outcome):        
        self.value = self.value + dice_outcome

    def __unicode__(self):
        return self.value
    
class Player(object):
    """
    Player class representing a player
    This is an abstract class, actual player will be of different types
    """

    def __init__(self, pos):
        self.pos = Position(pos)
        self.solved = [] #contains list of level instances

    def append_solved(self, level_instance):
        self.solved.append(level_instance)

    def get_solved_levels(self):
        return len(self.solved)

    def get_position(self):
        return self.pos.getPosition()

    def set_position(self, new_pos):
    	self.pos.setPosition(new_pos)

    def update_position(self, dice_outcome):
    	self.pos.UpdatePosition(dice_outcome)

    def roll_dice(self):
     	return random.choice([1,2,3,4,5,6])

class Human(Player):
    """
    human player
    """

    def check_ladder(self, question, answer):
    	"""
    	Checks the ladder type regex Puzzle
    	"""
        matches_outcome = True
        non_matches_outcome = False

        for match in question['matches'] :
            matches_outcome = matches_outcome & bool(re.search(answer, match))   #using bitwise &, because even if one is False, the whole match should fail and come out as false
        for non_match in question['non-matches']:
            non_matches_outcome = non_matches_outcome | bool(re.search(answer, non_match))     #using bitwise |, because even if one is true, the whole match should become true which is a fail
        if matches_outcome and not non_matches_outcome:
            return True
        else:
            return False
    

    def check_snake(self, question, answer):
    	"""
    	Checks the snake type puzzle
    	"""
        if re.search(question['pattern'], answer):
            return True  #time fraction
        else:
            return False



class AI(Player):
    """
    computer player
    """

    def check_ladder(self):
    	"""
    	Checks the ladder type regex Puzzle
    	"""
        if random.random() < 0.5:
            return True
        else:
            return False
    

    def check_snake(self):
    	"""
    	Checks the snake type puzzle
    	"""
        if random.random() < 0.5:
            return True  #time fraction
        else:
            return False


class Board(object):

    def __init__(self):
        self.ai = AI(0)
        self.human = Human(0)
        self.board_string = ""
        self.update_board_string()

    def get_board_key(self, number):
        """
        returns a board key from its integer number
        12-> '12', 22-> '22', 1->'01'
        """
        A = self.ai.get_position()
        H = self.human.get_position()
        if A == H == number:
            return '-CH-'
        elif A == number:
            return '-C-'
        elif H == number:
            return '-H-'
        elif number < 10:
            return '0{0}'.format(number)
        else:
            return '{0}'.format(number)

    def update_board_string(self):
        self.board_string = ""
        for i in range(0,10):
            numbers = range((9-i)*10, (9-i)*10 + 10)
            numbers_str = [self.get_board_key(n) for n in numbers]
            self.board_string = self.board_string + "\t".join(numbers_str) + '\n'

    def display(self):
    	self.update_board_string()
        print self.board_string
  
class LevelInstance():

	def __init__(self, data):
		self.solved = False
		self.id = data['id']
		self.time_taken = -1
		self.type = ""
		self.answer = ""

	def set_answer(self, answer, time_taken):
		self.answer = answer
		self.time_taken = time_taken

	def set_score(self, passed):
		self.solved = bool(passed)



class GamePlay():

    def __init__(self):
        self.exit = False
        self.b = Board()
        
        self.snakes = {99:96, 93:26, 70:38, 55:42, 38:12, 23:16, 15:6, 7:2, 12:2, 22:2, 28:4, 32:5}
        self.ladders = {2:22, 11:22, 25:60, 37:24, 68:22, 79:18, 49:22, 5:2, 10:2, 16:1, 32:1, 48:2}
        self.run()


    def input_manager(self, msg):
        if msg is None:
            print 'Enter Command, press H for help'
        else:
            print msg
        #self.valid_inputs = ['H', 'P', 'X'] 
        #self.commandMap = {'H' : self.menu, 'X':self.close, 'P':self.play}
        key = raw_input()
        if key in ['H', 'h', 'help', 'man']:
            menu()
            return 1

        elif key in ['x', 'X', 'close', 'exit']:
            self.exit = True
            return 1

        else:
            return key

    def get_snake(self):
    	"""
    	Fetch a snake level, show it to user, take input and return as (q, a)
    	"""
        question = random.choice(SNAKES)
        print 'Enter a string that matches regex - \n ' + question['text']
        answer = self.input_manager('\n')
    	return (question, answer)

    def get_ladder(self):
    	"""
    	Fetch a ladder level, show it to user, take input and return as (q, a)
    	"""
        question = random.choice(LADDERS)
        print 'You need to specify regex that matches all the matchers and should not match all the non matchers'
        print  "Matchers : " + ", ".join(question["matches"])
        print "Non Matchers : " + ", ".join(question["non-matches"])
        answer = self.input_manager('\n')
    	return (question, answer)


    def ai_play(self):
        print 'Computer is at {0} position and rolling the dice'.format(self.b.ai.get_position())
        dice_outcome = self.b.ai.roll_dice()
        self.b.ai.update_position(dice_outcome)
        time.sleep(1)
        new_position = self.b.ai.get_position()
        print 'Computer Rolled {0} on its dice. \n It is now on {1} position'.format(dice_outcome, new_position)
        if self.snakes.has_key(new_position):
        	print 'Bit by snake..oops. To escape computer needs to solve this regex puzzle'
        	result = self.b.ai.check_snake()
        	if not result:
        		slide = self.snakes[new_position]
        		print 'Ohh, could not escape snake. Computer sliding by {0} steps'.format(slide)
        		self.b.ai.update_position(-1*slide)
        		new_position = self.b.ai.get_position()
        		print "Computer's new position is {0}".format(new_position)
        		self.input_manager('Press Enter to continue....  ')
        	else:
        		print 'Yo!! Mofos, computer killed the snake. Its position is unaffected.'
        		self.input_manager('Press Enter to continue....  ')
        elif self.ladders.has_key(new_position):
        	print 'There is a ladder on this position, solve this regex to ride this ladder'
        	result = self.b.ai.check_ladder()
        	if result:
        		steps = self.ladders[new_position]
        		print 'Computer has used the ladder to raise its position by {0} steps'.format(steps)
        		self.b.ai.update_position(steps)
        		new_position = self.b.ai.get_position()
        		print "Computer's new position is {0}".format(new_position)
        		self.input_manager('Press Enter to continue....  ')
        	else:
        		print 'Computer failed the ladder level. Position remains unchanged'
        		self.input_manager('Press Enter to continue....  ')
        return 0

    def human_play(self):
    	key = self.input_manager('Press ENTER to roll the dice')
    	print 'You are at {0} position and rolling the dice'.format(self.b.human.get_position())

    	dice_outcome = self.b.human.roll_dice()
    	self.b.human.update_position(dice_outcome)
    	time.sleep(2)
    	new_position = self.b.human.get_position()
    	print 'You got {0} on roll of the dice. You are now on {1} position'.format(dice_outcome, new_position)
        if self.snakes.has_key(new_position):
        	print 'Bit by snake..oops. To escape you need to solve this regex puzzle. '
        	(question, answer) = self.get_snake()
        	self.input_manager('You supplied {0} as answer to problem: {1}. Press Enter to continue...'.format(answer, question))
        	result = self.b.human.check_snake(question, answer)
        	if not result:
        		slide = self.snakes[new_position]
        		print 'Ohh, you could not escape snake. You are sliding by {0} steps'.format(slide)
        		self.b.human.update_position(-1*slide)
        		new_position = self.b.human.get_position()
        		print "Your new position is {0}".format(new_position)
        		self.input_manager('Press Enter to continue...')
        	else:
        		print 'Yo!! Mofos, You killed the snake. Your position is unaffected.'
        		self.input_manager('Press Enter to continue...')
        elif self.ladders.has_key(new_position):
        	print 'There is a ladder on this position, solve this regex to ride this ladder. Press Enter to try'
        	(question, answer) = self.get_ladder()
            #[TODO] : regex will not be printed properly and needs some processing
        	self.input_manager('You supplied "{0}" as answer to regex puzzle. Press Enter to continue...'.format(answer))
        	result = self.b.human.check_ladder(question, answer)
        	if result:
        		steps = self.ladders[new_position]
        		print 'You have used the ladder to raise position by {0} steps'.format(steps)
        		self.b.human.update_position(steps)
        		new_position = self.b.human.get_position()
        		print "Your new position is {0}".format(new_position)
        		self.input_manager('Press Enter to continue...')
        	else:
        		print 'You failed the ladder level. Position remains unchanged'
        		self.input_manager('Press Enter to continue...')
    	return 0

    def menu(self):
        print '------------------Help----------------'
        print ' Press "P" to start playing'
        print 'Press "X" to exit and get your score'
        print 'Press "S" to check your score'


    def run(self):
        #[TODO] - this is not clearing the page
    	os.system('cls' if os.name == 'nt' else 'clear')
        self.b.display()
        key = self.input_manager(None)
        while(not self.exit):    
    	    self.ai_play()
    	    self.b.display()
    	    self.human_play()

new = GamePlay()