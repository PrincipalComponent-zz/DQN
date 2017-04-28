"""
Contains pre-processing settings for the three environments

    MsPacman-v3
    Pong-v3
    Boxing-v3

Each dict contains a bounding box of the screen and a list with valid actions.
"""

PREPROCESSING = {
    'Pong-v3':          {'bbox':     (35,0,160,160) },
    'MsPacman-v3':      {},
    'Boxing-v3':        {}
}
