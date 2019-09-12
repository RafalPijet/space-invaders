from livewires import games, color
import random
import pickle, shelve

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
          
                      
          def __init__(self, ghost_type, x, y):
                    super(Ghost, self).__init__(images=ghost_type,
                                                 x=x,y=y,
                                                 dx=.3,
                                                 n_repeats=0,
                                                 repeat_interval=25,
                                                 is_collideable=False)
                    self.create_list()
                                                            
                    
          def update(self):
                    if self.right>games.screen.width:
                              self.dx=-self.dx
                              self.y+=30
                    if self.left<0:
                              self.dx=-self.dx
                              self.y-=30
                    if new_ghost1.y==500:
                              new_ghost1.dy=0
                    if new_ghost2.y==500:
                              new_ghost2.dy=0
                    if new_ghost3.y==540:
                              new_ghost3.dy=0
                    if new_ghost4.y==540:
                              new_ghost4.dy=0
                    self.move_list()
                    

          def create_list(self):
                    f=open('highscore.dat','rb')
                    player_list=pickle.load(f)
                    f.close()
                    entry=player_list[0]
                    score,name=entry
                    self.position1=games.Text(value='1. '+name+': '+str(score),
                                              size=30,
                                              color=color.yellow,
                                              left=500,
                                              bottom=500)
                    entry=player_list[1]
                    score,name=entry
                    self.position2=games.Text(value='2. '+name+': '+str(score),
                                              size=30,
                                              color=color.light_gray,
                                              left=500,
                                              bottom=500)
                    entry=player_list[2]
                    score,name=entry
                    self.position3=games.Text(value='3. '+name+': '+str(score),
                                              size=30,
                                              color=color.brown,
                                              left=500,
                                              bottom=500)
                    entry=player_list[3]
                    score,name=entry
                    self.position4=games.Text(value='4. '+name+': '+str(score),
                                              size=30,
                                              color=color.green,
                                              left=500,
                                              bottom=500)
                    entry=player_list[4]
                    score,name=entry
                    self.position5=games.Text(value='5. '+name+': '+str(score),
                                              size=30,
                                              color=color.green,
                                              left=500,
                                              bottom=500)
                    entry=player_list[5]
                    score,name=entry
                    self.position6=games.Text(value='6. '+name+': '+str(score),
                                              size=30,
                                              color=color.green,
                                              left=500,
                                              bottom=500)
                    entry=player_list[6]
                    score,name=entry
                    self.position7=games.Text(value='7. '+name+': '+str(score),
                                              size=30,
                                              color=color.green,
                                              left=500,
                                              bottom=500)
                    entry=player_list[7]
                    score,name=entry
                    self.position8=games.Text(value='8. '+name+': '+str(score),
                                              size=30,
                                              color=color.green,
                                              left=500,
                                              bottom=500)
                    entry=player_list[8]
                    score,name=entry
                    self.position9=games.Text(value='9. '+name+': '+str(score),
                                              size=30,
                                              color=color.green,
                                              left=500,
                                              bottom=500)
                    entry=player_list[9]
                    score,name=entry
                    self.position10=games.Text(value='10. '+name+': '+str(score),
                                              size=30,
                                              color=color.green,
                                              left=488,
                                              bottom=500)
                    
          def move_list(self):
                    if Ghost.check_list==1:
                              self.position1.dy=-.3
                              games.screen.add(self.position1)
                              Ghost.check_list=2
                    if Ghost.check_list==2 and self.position1.bottom==470:
                              self.position2.dy=-.3
                              games.screen.add(self.position2)
                              Ghost.check_list=3
                    if Ghost.check_list==3 and self.position2.bottom==470:
                              self.position3.dy=-.3
                              games.screen.add(self.position3)
                              Ghost.check_list=4
                    if Ghost.check_list==4 and self.position3.bottom==470:
                              self.position4.dy=-.3
                              games.screen.add(self.position4)
                              Ghost.check_list=5
                    if Ghost.check_list==5 and self.position4.bottom==470:
                              self.position5.dy=-.3
                              games.screen.add(self.position5)
                              Ghost.check_list=6
                    if Ghost.check_list==6 and self.position5.bottom==470:
                              self.position6.dy=-.3
                              games.screen.add(self.position6)
                              Ghost.check_list=7
                    if Ghost.check_list==7 and self.position6.bottom==470:
                              self.position7.dy=-.3
                              games.screen.add(self.position7)
                              Ghost.check_list=8
                    if Ghost.check_list==8 and self.position7.bottom==470:
                              self.position8.dy=-.3
                              games.screen.add(self.position8)
                              Ghost.check_list=9
                    if Ghost.check_list==9 and self.position8.bottom==470:
                              self.position9.dy=-.3
                              games.screen.add(self.position9)
                              Ghost.check_list=10
                    if Ghost.check_list==10 and self.position9.bottom==470:
                              self.position10.dy=-.3
                              games.screen.add(self.position10)
                              Ghost.check_list=11
                    if Ghost.check_list==11 and self.position1.bottom<=220:
                              games.screen.remove(self.position1)
                              Ghost.check_list=12
                    if Ghost.check_list==12 and self.position10.bottom==470:
                              self.position1.bottom=500
                              Ghost.check_list=1
                    if self.position2.bottom<=220:
                              games.screen.remove(self.position2)
                              self.position2.bottom=500
                    if self.position3.bottom<=220:
                              games.screen.remove(self.position3)
                              self.position3.bottom=500
                    if self.position4.bottom<=220:
                              games.screen.remove(self.position4)
                              self.position4.bottom=500
                    if self.position5.bottom<=220:
                              games.screen.remove(self.position5)
                              self.position5.bottom=500
                    if self.position6.bottom<=220:
                              games.screen.remove(self.position6)
                              self.position6.bottom=500
                    if self.position7.bottom<=220:
                              games.screen.remove(self.position7)
                              self.position7.bottom=500
                    if self.position8.bottom<=220:
                              games.screen.remove(self.position8)
                              self.position8.bottom=500
                    if self.position9.bottom<=220:
                              games.screen.remove(self.position9)
                              self.position9.bottom=500
                    if self.position10.bottom<=220:
                              games.screen.remove(self.position10)
                              self.position10.bottom=500
                              
                    

image=games.load_image('score.jpg')
games.screen.set_background(image)

info=games.Text(value='zdobyte punkty: 1580',
                size=40,
                color=color.white,
                left=games.screen.width/2,
                y=100)
games.screen.add(info)
button=games.Text(value='DALEJ: przez Spacja',
                  size=25,
                  color=color.pink,
                  x=600,
                  y=570)
games.screen.add(button)
new_ghost1=Ghost(Ghost.images1,50,40)
games.screen.add(new_ghost1)
new_ghost3=Ghost(Ghost.images3,250,140)
games.screen.add(new_ghost3)
new_ghost2=Ghost(Ghost.images2,games.screen.width-50,340)
games.screen.add(new_ghost2)
new_ghost4=Ghost(Ghost.images4,games.screen.width-250,440)
games.screen.add(new_ghost4)
games.music.load('end.mp3')
games.music.play(-1)


games.screen.mainloop()
