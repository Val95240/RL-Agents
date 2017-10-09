
ENV = "SpaceInvaders-v0"

LOAD = False
DISPLAY = False


DISCOUNT = 0.99

EPSILON_START = 0.8
EPSILON_STOP = 0.1
EPSILON_STEPS = 100000

LEARNING_RATE = 1e-4

BUFFER_SIZE = 10000
PRIOR_ALPHA = 0.5
PRIOR_BETA_START = 0.4
PRIOR_BETA_STOP = 1
PRIOR_BETA_STEPS = 100000

BATCH_SIZE = 64

# Number of episodes of game environment to train with
TRAINING_STEPS = 10000
PRE_TRAIN_STEPS = 200

# Maximal number of steps during one episode
MAX_EPISODE_STEPS = 300
TRAINING_FREQ = 4

# Rate to update target network toward primary network
UPDATE_TARGET_RATE = 0.001