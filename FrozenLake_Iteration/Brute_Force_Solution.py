"""
    Behailu Dereje     LuCy.ai
            @sept 2018         Behailu04@gmail.com
    Solve FrozenLake problem using Brute Force Method.
            FrozenLake
        It consists of 16 and 4 possible moves that gives as 4**16
        possible policies to choose from. for Brute Force Method,
        choose few cases randomly and select the best among them.

"""
import gym
import time
import numpy

"""
    Execution
    
"""

def execute(env,policy,episodeLength=100, render=True):
    totalReward = 0
    start = env.reset()
    for t in range(episodeLength):
        if render:
            env.render()
        action = policy[start]
        start,reward, done, _ = env.step(action)
        totalReward += reward
        if done:
            break
    return totalReward
"""
        
        Evaluation

"""

def evaluatePolicy(env, policy, n_episodes=100):
    totalReward = 0.0
    for _ in range(n_episodes):
        totalReward += execute(env, policy)
    return totalReward/n_episodes

"""

        Function for a random policy

"""

def gen_random_policy():
    return numpy.random.choice(4,size=((16)))


if __name__ == '__main__':
    env = gym.make('FrozenLake-v0')
    ## policy search
    n_policies = 100
    startTime = time.time()
    policy_set = [gen_random_policy() for _ in range(n_policies)]
    print(len(policy_set))
    policy_store = [evaluatePolicy(env,p) for p in policy_set]
    endTime = time.time()
    print(type(policy_set))
    print(policy_set)
    print("Best score = %0.2f. Time taken = %4.4f seconds" %(numpy.max(policy_store), endTime-startTime))