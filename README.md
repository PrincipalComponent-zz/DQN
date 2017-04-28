# Assignment 3: Deep Reinforcement Learning

![Pong.gif](https://github.com/compgi13/assignment-3-reinforcement-learning-PrincipalComponent/blob/master/videos/Pong.gif)
![Boxing.gif](https://github.com/compgi13/assignment-3-reinforcement-learning-PrincipalComponent/blob/master/videos/Boxing.gif)
![Pacman.gif](https://github.com/compgi13/assignment-3-reinforcement-learning-PrincipalComponent/blob/master/videos/MsPacman.gif)

## Environment

`python 2.7`

`tensorflow 1.0`

`gym 0.8.1`

`tqdm 4.11.2` (simply `pip install tqdm` if missing)

## Folder structure

    /code     code base
        -- /cartpole    Problem A code base
        -- /atari       Problem B code base
    /models   saved models
       -- /cartpole
       -- /atari
    /report   report .pdf

## Loading trained agents

The final checkpoints for all trained agents exist in `/models`. Each agent can be loaded and its control performance
evaluated (by default using 20 episodes).

To load an agent from exercise A go to the folder `./code/cartpole` and run:

      python evaluate.py --exercise a3          # exercise A3
      python evaluate.py --exercise a4          # exercise A4
      python evaluate.py --exercise a5          # exercise A5
      python evaluate.py --exercise a6          # exercise A6
      python evaluate.py --exercise a7          # exercise A7
      python evaluate.py --exercise a8          # exercise A8

To load an agent from exercise B go to the folder `./code/atari` and run:

     python evaluate.py --env Pong-v3           # Pong agent, exercise B
     python evaluate.py --env Boxing-v3         # Boxing agent, exercise B
     python evaluate.py --env MsPacman-v3       # MsPacman agent, exercise B


If you want to increase the number of test episodes use the `--n_episodes` argument, e.g.

     python evaluate.py --env Pong-v3 --n_episodes 100    # 100 test episodes


