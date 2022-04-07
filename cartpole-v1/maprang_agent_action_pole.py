from time import sleep
import gym
env = gym.make('CartPole-v1')
env.reset()

angle = 0
for _ in range(1000):
    env.render()                                        # render the environment
    if angle > 0:
        action = 1
    else:
        action = 0
        
    observation, reward, done, info = env.step(action)  # move to the next step by the chosen action
    angle = observation[2]
    
    print(observation, reward, done, info)
    if (done):
        env.reset()
        sleep(2)
env.close()
