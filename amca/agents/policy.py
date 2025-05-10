# -*- coding: utf-8 -*-
#!/usr/bin/env python3
"""
    Amca: The RL-Based Backgammon Agent
    https://github.com/ardabbour/amca/

    Abdul Rahman Dabbour, Omid Khorsand Kazemy, Yusuf Izmirlioglu
    Cognitive Robotics Laboratory
    Faculty of Engineering and Natural Sciences
    Sabanci University

    The Policy agent takes an action according to a DNN.
"""

import os

from stable_baselines3 import A2C, DDPG, DQN, SAC, PPO


class PolicyAgent:
    def __init__(self, algorithm, model):
        if algorithm.lower() == 'a2c':
            self.algorithm_class = A2C
        elif algorithm.lower() == 'ddpg':
            self.algorithm_class = DDPG
        elif algorithm.lower() == 'dqn':
            self.algorithm_class = DQN
        elif algorithm.lower() == 'ppo':
            self.algorithm_class = PPO
        elif algorithm.lower() == 'sac':
            self.algorithm_class = SAC
        else:
            raise ValueError('Unidentified algorithm chosen')

        if not os.path.exists(model):
            self.__policy = None
        else:
            self.__policy = self.algorithm_class.load(model)

    def make_decision(self, observation):
        """Returns the action according to the policy and observation."""

        action, _ = self.__policy.predict(observation)

        return action
