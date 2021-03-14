import numpy as np


class P:
    """
    A class that stores the state transition probabilities for an MDP
    """
    def __init__(self, n_states: int, n_actions: int):
        """
        The state transition probabilities are stored as a nested dict of dicts of lists where keys are the numerical
        states and actions. For each state and action, a list of tuples of next states and the probability of ending
        there should be stored.

        p = P(n_states, n_actions)
        p[state, action] == [(next_state, probability), ...]

        :param n_states: number of states of the MDP
        :param n_actions: number of actions of the MDP
        """
        self._p = {s: {a: [] for a in range(n_actions)} for s in range(n_states)}

    def __getitem__(self, state_action):
        state = state_action[0]
        action = state_action[1]
        return self._p[state][action]


class MDP(object):
    def __init__(self, discount: float, world_dim: tuple, n_actions: int, desc: list = None):
        self.gamma = discount
        self.world_dim = world_dim
        self.n_states = int(np.prod(world_dim))  # number of states
        self.n_actions = n_actions  # number of actions
        self.stp = P(self.n_states, self.n_actions)  # state transition probabilities, initialized empty
        self.rewards = np.zeros(self.n_states)
        self.desc = desc  # 2D array specifying what each grid cell means (used for plotting)
