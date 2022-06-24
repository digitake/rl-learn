# valueIterationAgents.py
# -----------------------
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


import mdp, util

from learningAgents import ValueEstimationAgent

class ValueIterationAgent(ValueEstimationAgent):
    """
        * Please read learningAgents.py before reading this.*

        A ValueIterationAgent takes a Markov decision process
        (see mdp.py) on initialization and runs value iteration
        for a given number of iterations using the supplied
        discount factor.
    """
    def __init__(self, mdp, discount = 0.9, iterations = 100):
        """
          Your value iteration agent should take an mdp on
          construction, run the indicated number of iterations
          and then act according to the resulting policy.

          Some useful mdp methods you will use:
              mdp.getStates()
              mdp.getPossibleActions(state)
              mdp.getTransitionStatesAndProbs(state, action)
              mdp.getReward(state, action, nextState)
              mdp.isTerminal(state)
        """
        self.mdp = mdp
        self.discount = discount
        self.iterations = iterations
        self.values = util.Counter() # A Counter is a dict with default 0

        # Write value iteration code here
        "*** YOUR CODE HERE ***"
        for i in range(iterations):
           self.iterate_one_step()
           
    def iterate_one_step(self):
        states = self.mdp.getStates()
        temp_counter = util.Counter()
        for state in states:
            max_q = float('-inf')
            for action in self.mdp.getPossibleActions(state):
                value = self.computeQValueFromValues(state, action)
                if value > max_q:
                    max_q = value
                    
            if max_q != float('-inf'):
                temp_counter[state] = max_q
        self.values = temp_counter           

    def getValue(self, state):
        """
          Return the value of the state (computed in __init__).
        """
        return self.values[state]


    def computeQValueFromValues(self, state, action):
        """
          Compute the Q-value of action in state from the
          value function stored in self.values.
        """
        "*** YOUR CODE HERE ***"
        # (state, action) -> float
        # state = [0,0] , action = 'North'
        # transition = [((0, 1), 0.8), ((1, 0), 0.1), ((0, 0), 0.1)]
        total = 0
        transitions = self.mdp.getTransitionStatesAndProbs(state, action)
        
        for (next_state, prob) in transitions:  # next_state=(0,1), prop =0.8
            reward = self.mdp.getReward(state, action, next_state)
            total += prob * (reward + self.discount * self.values[next_state])
        
        return total

    def computeActionFromValues(self, state):
        """
          The policy is the best action in the given state
          according to the values currently stored in self.values.

          You may break ties any way you see fit.  Note that if
          there are no legal actions, which is the case at the
          terminal state, you should return None.
        """
        ## [(0.123, 'North'), (0.55, 'South'), (0.9, 'East'), (0.0, 'West')]
        q_value_and_action = [
            (self.computeQValueFromValues(state, action), action) 
            for action in self.mdp.getPossibleActions(state)
            ]
        best_action = max(q_value_and_action)[1] if q_value_and_action else None
        return best_action

    def getPolicy(self, state):
        return self.computeActionFromValues(state)

    def getAction(self, state):
        "Returns the policy at the state (no exploration). (it's greedy in our case)"
        return self.computeActionFromValues(state)

    def getQValue(self, state, action):
        return self.computeQValueFromValues(state, action)
