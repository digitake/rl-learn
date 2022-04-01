from time import sleep
import gym
env = gym.make('CartPole-v1')
env.reset()

for _ in range(1000):
    env.render()                                        # render the environment
    action = env.action_space.sample()                  # select random action
    observation, reward, done, info = env.step(action)  # move to the next step by the chosen action
    
    print(observation, reward, done, info)
    if (done):
        env.reset()
        sleep(2)
env.close()
