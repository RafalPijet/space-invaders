import pickle, shelve

f=open('highscore.dat','rb')
player_list=pickle.load(f)
f.close()

print(player_list)
