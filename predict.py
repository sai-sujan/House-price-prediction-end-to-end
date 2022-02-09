import numpy as np
import pickle

model = pickle.load(open('pre_model.pkl', 'rb'))


def Predict(c):
	c = np.array(c).reshape(1, -1)
	return model.predict(c)


