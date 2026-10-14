# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util 
from game import Directions
from typing import List
from util import Stack
from util import Queue
from util import PriorityQueue

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """
    
    

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()




def tinyMazeSearch(problem: SearchProblem) -> List[Directions]:
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem) -> List[Directions]:
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    # frontier για αποθήκευση καταστάσεων με υλοποίηση στοίβας
    frontier = Stack()
    frontier.push((problem.getStartState(), []))  # βάζω στην στοίβα την αρχική κατάστση
                                                  # και άδεια λίστας κινήσεων
    # Set για unique στοιχεία για να κρατάει τις επισκεπτόμενες καταστάσεις
    expanded = set()

    # Όσο υπάρχουν καταστάσεις στο frontier
    while not frontier.isEmpty():
        # Πετάει την κατάσταση και τις κινήσεις για αυτή την κατάσταση
        state, moves = frontier.pop()

        # Εάν βρει την κατάσταση στόχου που θέλουμε τότε επιστρέφει τις κινήσεις
        if problem.isGoalState(state):
            return moves

        # εάν δεν έχουμε επισκεφθέι την κατάσταση
        if state not in expanded:
            expanded.add(state)  # την προσθέτει στις επισκέψιμες

            # ελέγχει για την επόμενη κατάσταση και την κίνηση αν υπάρχουν στα επισκέψιμα
            for next_state, move, _ in problem.getSuccessors(state):
                if next_state not in expanded:
                    # τα τοποθετεί στην στοίβα 
                    frontier.push((next_state, moves + [move]))

    # επιστρέφει κενή λίστα σε περίπτωση αποτυχίας
    return []
    util.raiseNotDefined()

def breadthFirstSearch(problem: SearchProblem) -> List[Directions]:
    """Search the shallowest nodes in the search tree first."""
    # frontier για αποθήκευση καταστάσεων με υλοποίηση ουράς
    frontier = Queue()
    frontier.push((problem.getStartState(), []))  # βάζω στην ουρά την αρχική κατάστση
                                                  # και άδεια λίστας κινήσεων
    # Set για unique στοιχεία για να κρατάει τις επισκεπτόμενες καταστάσεις
    expanded = set()

    # Όσο υπάρχουν καταστάσεις στο frontier
    while not frontier.isEmpty():
        # Πετάει την κατάσταση και τις κινήσεις για αυτή την κατάσταση
        state, moves = frontier.pop()

        # Εάν βρει την κατάσταση στόχου που θέλουμε τότε επιστρέφει τις κινήσεις
        if problem.isGoalState(state):
            return moves

        # εάν δεν έχουμε επισκεφθέι την κατάσταση
        if state not in expanded:
            expanded.add(state)  # την προσθέτει στις επισκέψιμες

            # ελέγχει για την επόμενη κατάσταση και την κίνηση αν υπάρχουν στα επισκέψιμα
            for next_state, move, _ in problem.getSuccessors(state):
                if next_state not in expanded:
                    # τα τοποθετεί στην ουρά
                    frontier.push((next_state, moves + [move]))

    # επιστρέφει κενή λίστα σε περίπτωση αποτυχίας
    return []
    util.raiseNotDefined()

def uniformCostSearch(problem: SearchProblem) -> List[Directions]:
    """Search the node of least total cost first."""
    
    # frontier με υλοποίηση ουράς προτεραιότητας για αποθήκευση καταστάσεων
    frontier = PriorityQueue()
    
    # Βάζουμε στην ουρά την αρχική κατάσταση, την άδεια λίστα κινήσεων και συνολικό κόστος 0
    frontier.push((problem.getStartState(), [], 0), 0)  #(συνήθη ορίσματα, προτεραιότητα)

    # Set για να αποθηκεύουμε τις επισκέψιμες καταστάσεις
    expanded = set()

    # Όσο υπάρχουν καταστάσεις στο frontier
    while not frontier.isEmpty():
        # Αφαιρούμε την κατάσταση με το μικρότερο κόστος
        state, moves, cost_so_far = frontier.pop()

        # Εάν βρούμε την κατάσταση στόχου, επιστρέφουμε τις κινήσεις που κάναμε
        if problem.isGoalState(state):
            return moves

        # Αν δεν έχουμε επισκεφθεί αυτή την κατάσταση ακόμα
        if state not in expanded:
            expanded.add(state)  # Προσθέτουμε την κατάσταση στις επισκέψιμες

            # Για κάθε επόμενη κατάσταση, κίνηση και κόστος της μετάβασης
            for next_state, move, step_cost in problem.getSuccessors(state):
                if next_state not in expanded:
                    new_cost = cost_so_far + step_cost  # Υπολογίζουμε το συνολικό κόστος μέχρι το επόμενο βήμα
                    
                    # Ενημερώνουμε την ουρά προτεραιότητας εάν η κατάσταση υπάρχει ήδη με υψηλότερο κόστος ή την προσθέτουμε
                    frontier.update((next_state, moves + [move], new_cost), new_cost)

    # Επιστρέφουμε κενή λίστα σε περίπτωση αποτυχίας
    return []

    util.raiseNotDefined()

def nullHeuristic(state, problem=None) -> float:
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0
    
def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic) -> List[Directions]:
    """Search the node that has the lowest combined cost and heuristic first."""
    
    # frontier με υλοποίηση ουράς προτεραιότητας για αποθήκευση καταστάσεων
    frontier = PriorityQueue()
    
    # Βάζουμε στην ουρά την αρχική κατάσταση, την άδεια λίστα κινήσεων και συνολικό κόστος 0
    start_state = problem.getStartState()
    frontier.push((start_state, [], 0), 0)  # (κατάσταση, κινήσεις, κόστος) με προτεραιότητα το συνολικό κόστος

    # Set για να αποθηκεύουμε τις καλύτερες διαδρομές κόστους προς κάθε κατάσταση
    best_costs = {start_state: 0}   #χαμηλότερο κόστος

    # Όσο υπάρχουν καταστάσεις στο frontier
    while not frontier.isEmpty():
        # Αφαιρούμε την κατάσταση με το μικρότερο κόστος
        state, moves, cost_so_far = frontier.pop()

        # Εάν βρούμε την κατάσταση στόχου, επιστρέφουμε τις κινήσεις που κάναμε
        if problem.isGoalState(state):
            return moves

        # Για κάθε επόμενη κατάσταση, κίνηση και κόστος της μετάβασης
        for next_state, move, step_cost in problem.getSuccessors(state):
            new_cost = cost_so_far + step_cost  # Υπολογίζουμε το συνολικό κόστος μέχρι το επόμενο βήμα
            if next_state not in best_costs or new_cost < best_costs[next_state]:
                # Ενημερώνουμε αν βρήκαμε καλύτερη διαδρομή με χαμηλότερο κόστος
                best_costs[next_state] = new_cost
                total_cost = new_cost + heuristic(next_state, problem)  # Κόστος + ευρετική
                # Προσθέτουμε στην ουρά προτεραιότητας
                frontier.push((next_state, moves + [move], new_cost), total_cost)

    # Επιστρέφουμε κενή λίστα σε περίπτωση αποτυχίας
    return []

    util.raiseNotDefined()

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
