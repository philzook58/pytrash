import gym
env = gym.make('BipedalWalker-v2')
env.reset()

for _ in range(1000):
    env.render()
    
    action = env.action_space.sample()
    observation, reward, done, info = env.step(action)
    print(observation)




def ppo():
	advantage = Q(s,a) - V(s)
	min(keras.log(prob) * Advantage, clip(prob, 1-eps, 1+eps) * advatnage)
