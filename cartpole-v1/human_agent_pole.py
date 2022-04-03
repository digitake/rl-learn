from time import sleep
import gym
import pygame
import math
env = gym.make('CartPole-v1')
env.reset()

action = 0
accumulative_reward = 0

for _ in range(1000):
    
    env.render()                                        # render the environment
    
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                action = 0
            if event.key == pygame.K_RIGHT:
                action = 1
                
    #action = env.action_space.sample()                  # select random action
    observation, reward, done, info = env.step(action)  # move to the next step by the chosen action
    accumulative_reward += reward
    print(int(accumulative_reward), end='\r')
    
    if (done):
        print(f"Game over with total reward {accumulative_reward:.0f}")
        print(f"Restart in 2 seconds...")
        env.reset()
        sleep(2)
        accumulative_reward = 0
        print("\nGo!")
env.close()
