from time import sleep
import gym
env = gym.make('CartPole-v1')
env.reset()


def song_policy(position, velocity, angle, angular_v):
    
    if abs(angle) < 0.025 and abs(velocity) < 3.2:
        action = 0 if velocity > 0 else 1
    else:
        action = 1 if angle > 0 else 0
        
    return action

position = 0
velocity = 0
angle = 0
angular_v = 0
acc_reward = 0
avg_angular_v = 0.0

avg_final_reward = 0.0

for _ in range(2000):
    env.render()                                        # render the environment
    
    action = song_policy(position, velocity, angle, angular_v)
    
    observation, reward, done, info = env.step(action)  # move to the next step by the chosen action
    
    position = observation[0]
    velocity = observation[1]
    angle = observation[2]
    angular_v = observation[3]
    
    avg_angular_v = (angular_v+avg_angular_v) / 2.0
    
    #print(observation, action)
    acc_reward += reward
    
    if (done):
        env.reset()
        print("Final reward:", acc_reward)
        avg_final_reward = (avg_final_reward + acc_reward) /2
        sleep(2)
        acc_reward = 0

print("Average Final Reward = ", avg_final_reward)        

env.close()
