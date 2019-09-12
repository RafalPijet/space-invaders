import pickle, shelve

player_list=[(19260, 'LOPEZ  '), (12940, 'KOZAK 1'), (12100, 'FAZI123'), (9870, 'WIESIEK'), (6780, 'KOTEK'), (4590, 'STRUNA '), (3160, 'GUMIS 1'), (2870, 'JACKAL '), (1840, 'JOPEK22'), (1500, 'BURAK')]


f=open('highscore.dat','wb')
pickle.dump(player_list,f)
f.close()

