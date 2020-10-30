import pickle
with open('usr_info.pickle','rb') as file:
    print(pickle.load(file))