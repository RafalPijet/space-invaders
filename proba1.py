from livewires import games, color
import random, pickle, shelve

games.init(screen_width=800, screen_height=600, fps=50)
class Ghost(games.Animation):

          images1=['alien1.bmp','alien1a.bmp']
          images2=['alien2.bmp','alien2a.bmp']
          images3=['alien3.bmp','alien3a.bmp']
          images4=['alien6.bmp','alien6a.bmp']
          images5=['alien4.bmp','alien4a.bmp']
          check1=False
          check2=False
          my_check1=False
          my_check2=False
          my_check3=False
          count=101
          check_list=1
          
                      
          def __init__(self,game, ghost_type, x, y):
                    super(Ghost, self).__init__(images=ghost_type,
                                                 x=x,y=y,
                                                 dx=.3,
                                                 n_repeats=0,
                                                 repeat_interval=25,
                                                 is_collideable=False)
                    self.game=game
                   
                                                            
                    
          def update(self):
                    if self.right>games.screen.width:
                              self.dx=-self.dx
                              self.y+=30
                    if self.left<0:
                              self.dx=-self.dx
                              self.y-=30
                    if self.game.new_ghost1.y==500:
                              self.game.new_ghost1.dy=0
                    if self.game.new_ghost2.y==500:
                              self.game.new_ghost2.dy=0
                    if self.game.new_ghost3.y==540:
                              self.game.new_ghost3.dy=0
                    if self.game.new_ghost4.y==540:
                              self.game.new_ghost4.dy=0
          
                                                            
class Button(games.Sprite):

          image=[games.load_image('left.bmp'),
                 games.load_image('right.bmp'),
                 games.load_image('up.bmp'),
                 games.load_image('down.bmp'),
                 games.load_image('spacja.bmp')]

          letters=('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','R','S','T','U','W','X','Y',
                   'Z',' ','1','2','3','4','5','6','7','8','9','0')
          count=0

          def __init__(self,game,type_image,x,y):
                    super(Button, self).__init__(image=Button.image[type_image],
                                                 x=x,
                                                 y=y,
                                                 is_collideable=False)
                    self.game=game
                    self.new_name=''
                    self.letter1=''
                    self.letter2=''
                    self.letter3=''
                    self.letter4=''
                    self.letter5=''
                    self.letter6=''
                    self.letter7=''
                    

          def update(self):
                    if Button.count>0:
                              Button.count-=1
                    if Button.count<0:
                              Button.count=0
                    if games.keyboard.is_pressed(games.K_RIGHT) and Button.count==0 and self.game.up.x<700:
                              Button.count=100
                              self.game.up.x+=50
                              self.game.down.x+=50
                    if games.keyboard.is_pressed(games.K_LEFT) and Button.count==0 and self.game.up.x>400:
                              Button.count=100
                              self.game.up.x-=50
                              self.game.down.x-=50
                    if games.keyboard.is_pressed(games.K_UP) and Button.count==0:
                              Button.count=100
                              self.my_x=self.game.up.get_x()
                              if self.my_x==400:
                                        self.letter1=self.game.edit1.get_value()
                                        my_index=Button.letters.index(self.letter1)
                                        if my_index<34:
                                                  my_index=my_index+1
                                                  self.letter1=Button.letters[my_index]
                                                  self.game.edit1.set_value(self.letter1)
                              if self.my_x==450:
                                        self.letter2=self.game.edit2.get_value()
                                        my_index=Button.letters.index(self.letter2)
                                        if my_index<34:
                                                  my_index=my_index+1
                                                  self.letter2=Button.letters[my_index]
                                                  self.game.edit2.set_value(self.letter2)
                              if self.my_x==500:
                                        self.letter3=self.game.edit3.get_value()
                                        my_index=Button.letters.index(self.letter3)
                                        if my_index<34:
                                                  my_index=my_index+1
                                                  self.letter3=Button.letters[my_index]
                                                  self.game.edit3.set_value(self.letter3)
                              if self.my_x==550:
                                        self.letter4=self.game.edit4.get_value()
                                        my_index=Button.letters.index(self.letter4)
                                        if my_index<34:
                                                  my_index=my_index+1
                                                  self.letter4=Button.letters[my_index]
                                                  self.game.edit4.set_value(self.letter4)
                              if self.my_x==600:
                                        self.letter5=self.game.edit5.get_value()
                                        my_index=Button.letters.index(self.letter5)
                                        if my_index<34:
                                                  my_index=my_index+1
                                                  self.letter5=Button.letters[my_index]
                                                  self.game.edit5.set_value(self.letter5)
                              if self.my_x==650:
                                        self.letter6=self.game.edit6.get_value()
                                        my_index=Button.letters.index(self.letter6)
                                        if my_index<34:
                                                  my_index=my_index+1
                                                  self.letter6=Button.letters[my_index]
                                                  self.game.edit6.set_value(self.letter6)
                              if self.my_x==700:
                                        self.letter7=self.game.edit7.get_value()
                                        my_index=Button.letters.index(self.letter7)
                                        if my_index<34:
                                                  my_index=my_index+1
                                                  self.letter7=Button.letters[my_index]
                                                  self.game.edit7.set_value(self.letter7)
                    if games.keyboard.is_pressed(games.K_DOWN) and Button.count==0:
                              Button.count=100
                              self.my_x=self.game.up.get_x()
                              if self.my_x==400:
                                        self.letter1=self.game.edit1.get_value()
                                        my_index=Button.letters.index(self.letter1)
                                        if my_index>0:
                                                  my_index=my_index-1
                                                  self.letter1=Button.letters[my_index]
                                                  self.game.edit1.set_value(self.letter1)
                              if self.my_x==450:
                                        self.letter2=self.game.edit2.get_value()
                                        my_index=Button.letters.index(self.letter2)
                                        if my_index>0:
                                                  my_index=my_index-1
                                                  self.letter2=Button.letters[my_index]
                                                  self.game.edit2.set_value(self.letter2)
                              if self.my_x==500:
                                        self.letter3=self.game.edit3.get_value()
                                        my_index=Button.letters.index(self.letter3)
                                        if my_index>0:
                                                  my_index=my_index-1
                                                  self.letter3=Button.letters[my_index]
                                                  self.game.edit3.set_value(self.letter3)
                              if self.my_x==550:
                                        self.letter4=self.game.edit4.get_value()
                                        my_index=Button.letters.index(self.letter4)
                                        if my_index>0:
                                                  my_index=my_index-1
                                                  self.letter4=Button.letters[my_index]
                                                  self.game.edit4.set_value(self.letter4)
                              if self.my_x==600:
                                        self.letter5=self.game.edit5.get_value()
                                        my_index=Button.letters.index(self.letter5)
                                        if my_index>0:
                                                  my_index=my_index-1
                                                  self.letter5=Button.letters[my_index]
                                                  self.game.edit5.set_value(self.letter5)
                              if self.my_x==650:
                                        self.letter6=self.game.edit6.get_value()
                                        my_index=Button.letters.index(self.letter6)
                                        if my_index>0:
                                                  my_index=my_index-1
                                                  self.letter6=Button.letters[my_index]
                                                  self.game.edit6.set_value(self.letter6)
                              if self.my_x==700:
                                        self.letter7=self.game.edit7.get_value()
                                        my_index=Button.letters.index(self.letter7)
                                        if my_index>0:
                                                  my_index=my_index-1
                                                  self.letter7=Button.letters[my_index]
                                                  self.game.edit7.set_value(self.letter7)
                    if games.keyboard.is_pressed(games.K_RETURN) and Button.count==0:
                              Button.count=100
                              self.letter1=self.game.edit1.get_value()
                              self.letter2=self.game.edit2.get_value()
                              self.letter3=self.game.edit3.get_value()
                              self.letter4=self.game.edit4.get_value()
                              self.letter5=self.game.edit5.get_value()
                              self.letter6=self.game.edit6.get_value()
                              self.letter7=self.game.edit7.get_value()
                              self.new_name=self.letter1+self.letter2+self.letter3+self.letter4+self.letter5+self.letter6+self.letter7
                              self.game.add_player()
                              
class Game(object):
          
          def play(self):
                    image=games.load_image('score.jpg')
                    games.screen.set_background(image)

                    info=games.Text(value='zdobyte punkty: 1580',
                                    size=40,
                                    color=color.white,
                                    left=games.screen.width/2,
                                    y=100)
                    games.screen.add(info)
                    button=games.Text(value='ZAPISZ: przez ENTER',
                                      size=25,
                                      color=color.pink,
                                      x=600,
                                      y=570)
                    games.screen.add(button)
                    self.new_ghost1=Ghost(self,Ghost.images1,50,40)
                    games.screen.add(self.new_ghost1)
                    self.new_ghost3=Ghost(self,Ghost.images3,250,140)
                    games.screen.add(self.new_ghost3)
                    self.new_ghost2=Ghost(self,Ghost.images2,games.screen.width-50,340)
                    games.screen.add(self.new_ghost2)
                    self.new_ghost4=Ghost(self,Ghost.images4,games.screen.width-250,440)
                    games.screen.add(self.new_ghost4)
                    games.music.load('end.mp3')
                    games.music.play(-1)
                    f=open('highscore.dat','rb')
                    player_list=pickle.load(f)
                    f.close()
                    self.player_list=player_list
                    self.score=1300
                    print(self.player_list)

          def add_player(self):
                    check=False
                    for entry in self.player_list:
                              score, name=entry
                              if self.score>score:
                                        check=True
                                        entry=self.score,self.up.new_name
                              elif self.score<score:
                                        check=False
                    if check==True:
                              self.player_list.append(entry)
                              self.player_list.sort(reverse=True)
                              del self.player_list[10]
                              f=open('highscore.dat','wb')
                              pickle.dump(self.player_list,f)
                              f.close()
                    

          def edit(self):
                    
                    self.up=Button(self,2,400,300)
                    games.screen.add(self.up)
                    self.down=Button(self,3,400,400)
                    games.screen.add(self.down)
                    self.left=Button(self,0,350,350)
                    games.screen.add(self.left)
                    self.right=Button(self,1,750,350)
                    games.screen.add(self.right)
                    self.edit1=games.Text(value=Button.letters[6],
                                     size=40,
                                     color=color.green,
                                     x=400,
                                     y=350)
                    games.screen.add(self.edit1)
                    self.edit2=games.Text(value=Button.letters[16],
                                     size=40,
                                     color=color.green,
                                     x=450,
                                     y=350)
                    games.screen.add(self.edit2)
                    self.edit3=games.Text(value=Button.letters[0],
                                     size=40,
                                     color=color.green,
                                     x=500,
                                     y=350)
                    games.screen.add(self.edit3)
                    self.edit4=games.Text(value=Button.letters[2],
                                     size=40,
                                     color=color.green,
                                     x=550,
                                     y=350)
                    games.screen.add(self.edit4)
                    self.edit5=games.Text(value=Button.letters[23],
                                     size=40,
                                     color=color.green,
                                     x=600,
                                     y=350)
                    games.screen.add(self.edit5)
                    self.edit6=games.Text(value=Button.letters[24],
                                     size=40,
                                     color=color.green,
                                     x=650,
                                     y=350)
                    games.screen.add(self.edit6)
                    self.edit7=games.Text(value=Button.letters[25],
                                     size=40,
                                     color=color.green,
                                     x=700,
                                     y=350)
                    games.screen.add(self.edit7)


                    games.screen.mainloop()

new=Game()
new.play()
new.edit()
