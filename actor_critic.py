import keras
from keras.models import Sequential
from keras.layers import Dense, Activation
import keras.backend as K

#I am making a bad sketch of what we need
#Is sketching a really bad technique?


def train


action_dim = 4
state_dim = 3

policymodel = Sequential([
    Dense(32, input_shape=(state_dim,)),
    Activation('relu'),
    Dense(action_dim),
    Activation('softmax'),
])

def policy_loss(y_true, y_pred):
	return K.log(y_pred) * y_true  
policymodel.compile(optimizer='rmsprop', loss=policy_loss, )




valuemodel = Sequential([
    Dense(32, input_shape=(state_dim,)),
    Activation('relu'),
    Dense(10),
    Activation('relu'),
    Dense(1)
])

valuemodel.compile(optimizer='rmsprop', loss='mse' )


#SARSA is a lower hanging fruit


def policyTrain():
	vsprime = valuemodel.predict(self, next_states, batch_size=32, verbose=0)
	rs = lookahead_reward(state)
	vs = valuemodel.predict(self, states, batch_size=32, verbose=0)
	vsprime = vs[lookahead:] 
	policymodel.fit(states , rs + gamma * vsprime - vs, epochs = 1)

    # max ln p(s,a) (r + gamma * V(s') - V(s))

def valueTrain(lookahead, states):

	vs = valuemodel.predict(self, states, batch_size=32, verbose=0)
	rs = rewards(states, lookahead)
	vsprime = vs[lookahead+1:]
	valuemodel.fit(states , rs + gamma * vsprime, epochs = 1)

	# train V(s) = r + gamma * V(s')


def lookahead_reward(n):
	reward = rewards(states)
	for i in range(n):
		reward[:-i] += gamma * reward[i:] 
	return reward[:-n]