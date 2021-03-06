import numpy as np
from collections import defaultdict
import random
class Agent:

    def __init__(self, nA=6):
        """ Initialize agent.
        Params
        ======
        - nA: number of actions available to the agent
        """
        self.nA = nA
        self.Q = defaultdict(lambda: np.zeros(self.nA))
        #init epsilon, alpha, gamma
        self.eps = 1.0
        self.alpha = 0.05
        self.gamma = 0.9

    def select_action(self, state,i_episode):
        """ Given the state, select an action.
        Params
        ======
        - state: the current state of the environment
        Returns
        =======
        - action: an integer, compatible with the task's action space
        """
        # Define probability distrb. for eps-greedy policy for state
        epsilon = self.eps = 1.0/i_episode
        policy_state = np.ones(self.nA) * epsilon / self.nA
        action_greedy = np.argmax(self.Q[state])
        policy_state[action_greedy] = 1 - epsilon + (epsilon / self.nA)
        
        # Define action from eps-greedy policy
        action = np.random.choice(self.nA, p=policy_state)        
        return action

    def step(self, state, action, reward, next_state, done,i_episode):
        """ Update the agent's knowledge, using the most recently sampled tuple.
        Params
        ======
        - state: the previous state of the environment
        - action: the agent's previous choice of action
        - reward: last reward received
        - next_state: the current state of the environment
        - done: whether the episode is complete (True or False)
        """
        # Get the next action for the next state
        next_action = self.select_action(next_state,i_episode)
        # Calculate discounted reward for next state & next action
        G_t  = reward + self.gamma * self.Q[next_state][next_action]
        # Update knowledge
        self.Q[state][action] += self.alpha * (G_t - self.Q[state][action])
