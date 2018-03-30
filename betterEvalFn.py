from util import manhattanDistance
from game import Directions
import random, util

from game import Agent


# Creating a better evaluation function

def betterEvaluationFunction(currentGameState):
    """
    Your extreme, unstoppable evaluation function
    """
    # Useful information you can extract from a GameState (pacman.py)
    
    N = currentGameState.getNumAgents()
    
    pacmanPos = currentGameState.getPacmanPosition()
    
    foodPos = currentGameState.getFood().asList()
    capsulePos = currentGameState.getCapsules()
    numberOfCapsules = len(capsulePos)
    
    distancesToFood = [manhattanDistance( pos, pacmanPos ) for pos in foodPos]
    distancesToCapsule = [manhattanDistance( pos, pacmanPos ) for pos in capsulePos]
    
    if len(distancesToCapsule) == 0:
        distancesToCapsule = [0]
    
    minDistToFood = min(distancesToFood) + 1
    sumDistToCapsule = sum(distancesToCapsule) + 1
    
    score = 0
    
    ghostStates = currentGameState.getGhostStates()
    
    scaredGhostPos = []
    index = 1;
    for ghostState in ghostStates:
        pos = currentGameState.getGhostPosition(index)
        if ghostState.scaredTimer > 0:
            scaredGhostPos.append(manhattanDistance( pos, pacmanPos ))
        index += 1
    
    minDistToScaredGhost = 0
    if len(scaredGhostPos) > 0:
        minDistToScaredGhost = min(scaredGhostPos)
    
    score = currentGameState.getScore() + 20.0/(currentGameState.getNumFood() + 1) + \
            22.0/sumDistToCapsule + 10.0/minDistToFood + \
            20.0/(numberOfCapsules+1) + 22.0/(sum(distancesToFood) + 1)
        
    if minDistToScaredGhost > 0:
        score += 155.0/minDistToScaredGhost
    
    return score

better = betterEvaluationFunction