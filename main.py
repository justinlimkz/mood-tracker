import pickle
import numpy as np
import config

now = np.datetime64('now')
mood_val = input("Hi %s! How are you feeling today (1-10)?\n" % (config.name))
mood_reason = input("Why are you feeling this way?\n")

if int(mood_val) <= 5:
    print("I hope you feel better!", end=" ")
else:
    print("Keep it up!", end=" ")

try:
    history = pickle.load(open("history.pkl", "rb"))
except:
    history = {}

history[now] = (mood_val, mood_reason)
days_logged = np.unique(np.array(list(history.keys())).astype('datetime64[D]')).size
print("You've logged %d times over %d days!" % (len(history), days_logged))
pickle.dump(history, open("history.pkl", "wb"))
