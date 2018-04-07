from util import manhattanDistance
from game import Directions
import random, util
from alphaBetaAgent import *
from game import Agent

class ReflexAgent(Agent):
  """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.
  """
  def __init__(self):
    self.lastPositions = []
    self.dc = None


  def getAction(self, gameState):
    """
    getAction chooses among the best options according to the evaluation function.

    getAction takes a GameState and returns some Directions.X for some X in the set {North, South, West, East, Stop}
    ------------------------------------------------------------------------------
    Description of GameState and helper functions:

    A GameState specifies the full game state, including the food, capsules,
    agent configurations and score changes. In this function, the |gameState| argument
    is an object of GameState class. Following are a few of the helper methods that you
    can use to query a GameState object to gather information about the present state
    of Pac-Man, the ghosts and the maze.

    gameState.getLegalActions():
        Returns the legal actions for the agent specified. Returns Pac-Man's legal moves by default.

    gameState.generateSuccessor(agentIndex, action):
        Returns the successor state after the specified agent takes the action.
        Pac-Man is always agent 0.

    gameState.getPacmanState():
        Returns an AgentState object for pacman (in game.py)
        state.configuration.pos gives the current position
        state.direction gives the travel vector

    gameState.getGhostStates():
        Returns list of AgentState objects for the ghosts

    gameState.getNumAgents():
        Returns the total number of agents in the game

    gameState.getScore():
        Returns the score corresponding to the current state of the game


    The GameState class is defined in pacman.py and you might want to look into that for
    other helper methods, though you don't need to.
    """
    # Collect legal moves and successor states
    legalMoves = gameState.getLegalActions()

    # Choose one of the best actions
    scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
    bestScore = max(scores)
    bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
    chosenIndex = random.choice(bestIndices) # Pick randomly among the best


    return legalMoves[chosenIndex]

  def evaluationFunction(self, currentGameState, action):
    """
    The evaluation function takes in the current and proposed successor
    GameStates (pacman.py) and returns a number, where higher numbers are better.

    The code below extracts some useful information from the state, like the
    remaining food (oldFood) and Pacman position after moving (newPos).
    newScaredTimes holds the number of moves that each ghost will remain
    scared because of Pacman having eaten a power pellet.
    """
    # Useful information you can extract from a GameState (pacman.py)
    successorGameState = currentGameState.generatePacmanSuccessor(action)
    newPos = successorGameState.getPacmanPosition()
    oldFood = currentGameState.getFood()
    newGhostStates = successorGameState.getGhostStates()
    newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

    return successorGameState.getScore()


def scoreEvaluationFunction(currentGameState):
  """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
  """
  return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
  """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
  """

  def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
    self.index = 0 # Pacman is always agent index 0
    self.evaluationFunction = util.lookup(evalFn, globals())
    self.depth = int(depth)

######################################################################################
# Implementing minimax

class MinimaxAgent(MultiAgentSearchAgent):
  """
    Your minimax agent
  """

  def getAction(self, gameState):
    """
      Returns the minimax action from the current gameState using self.depth
      and self.evaluationFunction. Terminal states can be found by one of the following:
      pacman won, pacman lost or there are no legal moves.

      Here are some method calls that might be useful when implementing minimax.

      gameState.getLegalActions(agentIndex):
        Returns a list of legal actions for an agent
        agentIndex=0 means Pacman, ghosts are >= 1

      Directions.STOP:
        The stop direction, which is always legal

      gameState.generateSuccessor(agentIndex, action):
        Returns the successor game state after an agent takes an action

      gameState.getNumAgents():
        Returns the total number of agents in the game

      gameState.getScore():
        Returns the score corresponding to the current state of the game

      gameState.isWin():
        Returns True if it's a winning state

      gameState.isLose():
        Returns True if it's a losing state

      self.depth:
        The depth to which search should continue
    """
    def computeScore(gameState, depth, agentIndex):
        if gameState.isWin() | gameState.isLose():
            return gameState.getScore()
        
        ''' When you reach a depth of 0, you need to approximate the future reward from that state. This is where you use the evaluationFunction
        '''
        if depth == 0:
            return self.evaluationFunction(gameState)
        
        ## get all valid actions for the game state. 
        ## Hint: You might find gameState.getLegalActions() useful here.
        actions = None # TODO

        ## Your Pacman agent should try to maximize its score.
        if agentIndex == self.index:
            #Initialize it here
            maxScore = 0 # TODO
            for action in actions:
                ''''
                get the successor state from the game state for the given action. 
                Hint: You might find gameState.generateSuccessor() useful here.
                gameState.generateSuccessor(agentIndex, action):
                Returns the successor state after the specified agent takes the action.
                Pac-Man is always agent 0.
                '''
                successor = None # TODO
                maxScore = max(maxScore, None)  # TODO
            return maxScore
        # When you reach the last ghost, the next agent would be pacman, and the depth of the game tree will reduce by 1.
        # For the other ghosts, depth will remain the same, but the agent index will increment by 1.
        else:
            minScore = 0 # TODO
            for action in actions:
                ''''
                get the successor state from the game state for the given action. 
                Hint: You might find gameState.generateSuccessor() useful here.
                gameState.generateSuccessor(agentIndex, action):
                Returns the successor state after the specified agent takes the action.
                Pac-Man is always agent 0.
                '''
                successor = None # TODO
                if agentIndex != (gameState.getNumAgents()-1):
                    minScore = min(minScore, None)# TODO
                else:
                    minScore = min(minScore, None) # TODO
            return minScore
    '''Candidate legal actions that the pacman can take e.g DIRECTIONS.WEST, DIRECTIONS.EAST etc.
    '''
    maxScore = float('-inf')
    '''Fetching all the legal moves for the Pacman agent.
    In this game, we have a pacman and multiple ghosts. Pacman is identified
    with index 0, and the rest of the ghosts are index > 0.
    '''
    actions = gameState.getLegalActions(self.index)
    ## If there are no legal actions that you can take, you just stop the pacman.
    if len(actions) == 0:
        return Directions.STOP

    bestAction = actions[0]

    for action in actions:
        ## Hint: You might find generateSuccessor() useful here.
        successor = None # TODO
        ## Hint: You need to implement and call computeScore() function here.
        score = 0 # TODO
        # Choose the best action that maximizes your score.
        if score > maxScore:
            pass
    return bestAction
    
    # END_YOUR_CODE

######################################################################################
# Alpha-beta pruning
class AlphaBetaAgent(MultiAgentSearchAgent):
    def getAction(self, gameState):
        bestAction = ""
        actions = gameState.getLegalActions(self.index)
        alpha = float('-inf')
        beta = float('inf')
        maxScore = float('-inf')
        if len(actions) == 0:
            return Directions.STOP
        for action in actions:
            successor = gameState.generateSuccessor(self.index, action)
            score = computeAlphaBetaScore(self.index, successor, self.depth, self.index + 1, alpha, beta)
            if score > maxScore:
                maxScore = score
                bestAction = action
            alpha = max(alpha, maxScore)
        return bestAction


# class ExpectimaxAgent(MultiAgentSearchAgent):
#   """
#     Your expectimax agent
#   """
#   def getAction(self, gameState):
#     """
#       Returns the expectimax action using self.depth and self.evaluationFunction

#       All ghosts should be modeled as choosing uniformly at random from their
#       legal moves.
#     """
#     def computeScore(gameState, depth, agentIndex):
#         if gameState.isWin() | gameState.isLose():
#             return gameState.getScore()
        
#         if depth == 0:
#             return self.evaluationFunction(gameState)
        
#         ## get all valid actions for the game state. 
#         ## Hint: You might find getLegalActions() useful here.
#         actions = None # TODO

#         ## Your Pacman agent should try to maximize its score.
#         if agentIndex == self.index:
#             #Initialize it here
#             maxScore = 0 # TODO
#             for action in actions:
#             ## get the successor state from the game state for the given action. 
#             ## Hint: You might find generateSuccessor() useful here.
#             ## This generateSuccessor() function returns the successor state after the specified agent ## takes the action.
#                 successor = None # TODO
#                 maxScore = 0 # TODO

#             return maxScore
#         ## When you reach the last ghost, the next agent would be pacman, and the depth of the game tree will reduce by 1
#         elif agentIndex == (gameState.getNumAgents()-1):
#             minScore = 0 # TODO
#             for action in actions:
#                 ## get the successor state from the game state for the given action. 
#                 ## Hint: You might find generateSuccessor() useful here.
#                 ## This generateSuccessor() function returns the successor state after the specified agent ## takes the action.
#                 minScore = 0 # TODO
#             return minScore
#         ## For the other ghosts, depth will remain the same, but the agent index will increment by 1.
#         else:
#             minScore = 0 # TODO
#             for action in actions:
#                 ## get the successor state from the game state for the given action. 
#                 ## Hint: You might find generateSuccessor() useful here.
#                 ## This generateSuccessor() function returns the successor state after the specified agent ## takes the action.
#                 minScore = 0 # TODO
#             return minScore
        
#     bestAction = ""
#     maxScore = float('-inf')
#     actions = gameState.getLegalActions(self.index)
    
#     if len(actions) == 0:
#         return Directions.STOP

#     for action in actions:
#         successor = None # TODO
#         score = 0 # TODO
#         # Choose the best action that maximizes your score.
#         if score > maxScore:
#             pass # TODO
#     return bestAction

######################################################################################