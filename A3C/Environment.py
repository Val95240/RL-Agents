
import gym
from parameters import ENV


class Environment:

    def __init__(self):

        self.env = gym.make(ENV)
        self.render = False

    def get_state_dims(self):
        return list(self.env.observation_space.shape)

    def set_render(self, render):
        self.render = render

    def reset(self):
        self.env.reset()

    def act(self, action):
        assert self.env.action_space.contains(action)
        if self.render:
            self.env.render()
        return self.env.step(action)

    def close(self):
        self.env.render(close=True)
        self.env.close()