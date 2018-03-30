from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

def scoreEvaluationFunction(currentGameState):
  """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
  """
  return currentGameState.getScore()

def computeAlphaBetaScore(pacmanIndex, gameState, depth, agentIndex, alpha, beta):
    if gameState.isWin() | gameState.isLose():
        return gameState.getScore()
    
    if depth == 0:
        evalFn = 'scoreEvaluationFunction'
        evaluationFunction = util.lookup(evalFn, globals())
        return evaluationFunction(gameState)
    
    ## get all valid actions for the game state
    actions = gameState.getLegalActions(agentIndex)

    if len(actions) == 0:
        return gameState.getScore()
    
    ## Your pacman agent should try to maximize its score
    if agentIndex == pacmanIndex:
        maxScore = float('-inf')
        for action in actions:
            successor = gameState.generateSuccessor(agentIndex, action)
            maxScore = max(maxScore, computeAlphaBetaScore(pacmanIndex, successor, depth, agentIndex + 1, alpha, beta))
            ## NEW CHANGE: Prune scores greater than beta
            if maxScore > beta:
                return maxScore
            alpha = max(alpha, maxScore)
        return maxScore
    
    ## When you reach the last ghost, the next agent would be pacman, and the depth of the game tree will reduce by 1
    elif agentIndex == (gameState.getNumAgents()-1):
        minScore = float('inf')
        for action in actions:
            successor = gameState.generateSuccessor(agentIndex, action)
            minScore = min(minScore, computeAlphaBetaScore(pacmanIndex, successor, depth - 1, pacmanIndex, alpha, beta))
            ## NEW CHANGE: Prune scores less than alpha
            if minScore < alpha:
                return minScore
            beta = min(beta, minScore)
        return minScore
    ## For the other ghosts, depth will remain the same, but the agent index will increment by 1.
    else:
        minScore = float('inf')
        for action in actions:
            successor = gameState.generateSuccessor(agentIndex, action)
            minScore = min(minScore, computeAlphaBetaScore(pacmanIndex, successor, depth, agentIndex + 1, alpha, beta))
            ## NEW CHANGE: Prune scores less than alpha
            if minScore < alpha:
                return minScore
            beta = min(beta, minScore)
        return minScore
    
