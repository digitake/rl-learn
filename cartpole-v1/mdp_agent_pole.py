from time import sleep
import gym
import numpy as np
env = gym.make('CartPole-v1')
env.reset()

def reward_prediction(state, action):
    """
    Given the state s and action a, return the reward r.
    s: state
    a: action
    return r: reward
    """
    reward = 0
    x_position, x_velocity, pole_angle, pole_angular_velocity = state
    
    # add incentive for moving the cart to the same direction as the pole
    if abs(pole_angle) > 0.03:
        reward += int(pole_angle > 0) == action
    
    # reduce incentive for moving the cart to the opposite direction to the pole if angular velocity is low
    if abs(pole_angular_velocity) < 2.0:
        reward -= int(pole_angular_velocity > 0) != action
        
    # try to get the cart back to the center
    if abs(x_velocity) > 0.6 and abs(x_position) > 0.1:
        reward -= int(x_velocity >= 0) != action
        
    # try to get the cart back to the center
    if abs(x_velocity) > 0.25 and abs(pole_angular_velocity) < 0.99:
        reward += int(x_position >= 0) == action
        
    return reward

def agent_action(state):
    """
    Given the state s, return the action to take.
    s: state
    return action: 0 - push cart to the left or 1 - push cart to the right
    """
    rewards = [reward_prediction(state, a) for a in range(env.action_space.n)]
    
    # rewards [ +2, -1 ]
    # rewards [ -1, +2 ]
    
    print("prediction", rewards, ", action=>", np.argmax(rewards) and "right" or "left")
    action = np.argmax(rewards)
    
    return action


action = 0                                              # Initial action
acc_reward = 0                                          # Accumulative reward

for _ in range(2000):                                   # Loop for simulations
    env.render()                                        # render the environment
    
    state, reward, game_over, _ = env.step(action)      # move to the next step by the chosen action
    action = agent_action(state)    # action  <-- set of Actions(0,1)
    
    acc_reward += reward
    
    if (game_over):
        env.reset()
        print("Final reward:", acc_reward)
        sleep(1)        # Pauses for 1 seconds
        acc_reward = 0    

env.close()
