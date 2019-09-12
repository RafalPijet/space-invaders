from livewires import games, color
import random, pickle, shelve

games.init(screen_width=800, screen_height=600, fps=50)

class Collider(games.Sprite):

          def update(self):
                    if self.overlapping_sprites:
                              for sprite in self.overlapping_sprites:
                                        sprite.die()
                              self.die()
                    if self.top>games.screen.height:
                              self.destroy()
                    if self.bottom<0:
                              self.destroy()
                    
          def die(self):
                    new_explosion=Explosion(x=self.x, y=self.y)
                    games.screen.add(new_explosion)
                    self.destroy()

class Ship_missile(Collider):

          sound=games.load_sound('pocisk.wav')
          image=games.load_image('pocisk.bmp')
          BUFFER=40

          def __init__(self, ship_x, ship_y):
                    Ship_missile.sound.play()
                    x=ship_x
                    y=ship_y-Ship_missile.BUFFER
                    dy=-3
                    super(Ship_missile, self).__init__(image=Ship_missile.image,
                                                       x=x,y=y,dy=dy)
          def update(self):
                    super(Ship_missile, self).update()

class Alien_missile(Collider):
          sound=games.load_sound('alien_missile.wav')
          image=games.load_image('alien_missile.bmp')

          def __init__(self, alien_x, alien_y, speed):
                    Alien_missile.sound.play()
                    super(Alien_missile, self).__init__(image=Alien_missile.image,
                                                        x=alien_x, y=alien_y, dy=speed,
                                                        is_collideable=False)
          def update(self):
                    if self.y>500:
                              self.is_collideable=True
                    if self.top>games.screen.height:
                              self.destroy()
                   
class Boss_alien(Collider):

          sound=games.load_sound('boss_alien.wav')
          image=games.load_image('alien4.bmp')
          TIME_WAIT=100

          def __init__(self, game, alien_x, alien_y, speed):
                    super(Boss_alien, self).__init__(image=Boss_alien.image,
                                                     x=alien_x, y=alien_y, dx=speed)
                    self.time_wait=0
                    self.game=game
                    Boss_alien.sound.play(-1)
                    
                                             
                                             
          def update(self):
                    super(Boss_alien, self).update()
                    self.fire()
                    if self.right>games.screen.width:
                              self.destroy()
                              Boss_alien.sound.stop()                              
                    if self.left<0:
                              self.destroy()
                              Boss_alien.sound.stop()
                    self.time_wait-=1
                    if self.time_wait<0:
                              self.time_wait=0

          def fire(self):
                    distance=10
                    step=Ship.ship_position+distance
                    if self.x==Ship.ship_position or self.left==Ship.ship_position or self.right==Ship.ship_position and self.time_wait==0:
                              new_missile=Alien_missile(self.x, self.y,5)
                              games.screen.add(new_missile)
                              self.time_wait=Boss_alien.TIME_WAIT
          
          def die(self):
                    self.destroy()
                    self.game.score.value+=300
                    self.info=games.Message(value='300',
                                             size=25,
                                             x=self.x,
                                             y=self.y,
                                             color=color.yellow,
                                             lifetime=4*games.screen.fps,
                                             is_collideable=False)
                    games.screen.add(self.info)
                    Boss_alien.sound.stop()

class Aliens(games.Animation):    

          images1=['alien1.bmp','alien1a.bmp']
          images2=['alien2.bmp','alien2a.bmp']
          images3=['alien3.bmp','alien3a.bmp']
          images4=['alien6.bmp','alien6a.bmp']
          TIME_WAIT=500
          fire_list=[]
          total=0
          check1=1
          check2=1
          check_y1=None
          check_y2=None
          check_y3=None
          check_y4=None
          check_y5=None
          count=0
          break_time=0

          def __init__(self, game, alien_type, x, y):
                    super(Aliens, self).__init__(images=alien_type,
                                                 x=x,y=y,
                                                 dx=.3,
                                                 n_repeats=0,
                                                 repeat_interval=25)
                    self.wait=100
                    self.game=game
                                                           

          def update(self):
                    if Aliens.total==40 and Aliens.check2==1:
                              boss=Boss_alien(self.game,50,70,1)
                              games.screen.add(boss)
                              Aliens.check2+=1
                    if Aliens.total==25 and Aliens.check2==2:
                              boss=Boss_alien(self.game,games.screen.width-50,70,-1)
                              games.screen.add(boss)
                              Aliens.check2+=1
                    if Aliens.total==12 and Aliens.check2==3:
                              boss=Boss_alien(self.game,50,70,1)
                              games.screen.add(boss)
                              Aliens.check2+=1
                    if Aliens.total==10 and Aliens.check1==1:
                              self.accelerate(1)
                              Aliens.check1+=1
                    if Aliens.total==5 and Aliens.check1==2:
                              self.accelerate(2)
                              Aliens.check1+=1
                    if Aliens.total==1 and Aliens.check1==3:
                              self.accelerate(4)
                              Aliens.check1+=1
                    if self.right>games.screen.width:
                               self.change_aliens()                                       
                    if self.left<0:
                               self.change_aliens()
                    self.fire()
                    if Aliens.break_time>0:
                              Aliens.break_time-=1
                    if Aliens.break_time<0:
                              Aliens.break_time=0
                    if Aliens.break_time==0 and Ship.ship_count==0:
                              self.end()                             

          def fire(self):
                    distance=5
                    if self.wait>0:
                              self.wait-=1
                    for i in range(5):
                              fire_x=random.randrange(0,games.screen.width)
                              fire_y=random.randrange(150,450)
                              buffer_x=fire_x+distance
                              buffer_y=fire_y+distance
                              if self.x>=fire_x and self.x<=buffer_x and self.wait==0 and self.y>=fire_y and self.y<=buffer_y:
                                        new_missile=Alien_missile(self.x, self.y, 2)
                                        games.screen.add(new_missile)
                                        self.wait=Aliens.TIME_WAIT
                    if self.x==Ship.ship_position or self.left==Ship.ship_position or self.right==Ship.ship_position:
                              Aliens.fire_list.append(self.y)
                              alien_y=random.choice(Aliens.fire_list)
                              if self.y==alien_y:
                                        new_missile=Alien_missile(self.x, self.y, 2)
                                        games.screen.add(new_missile)
                                        fire_list=[]
                                        self.wait=Aliens.TIME_WAIT

          def change_aliens(self):
                    for i in range(10):
                              entry=Game.list_alien1[i]
                              i,Game.new_alien1=entry
                              Game.new_alien1.dx=-Game.new_alien1.dx
                              Game.new_alien1.y+=20
                    Aliens.check_y1+=20
                    for i in range(10):
                              entry=Game.list_alien2[i]
                              i,Game.new_alien2=entry
                              Game.new_alien2.dx=-Game.new_alien2.dx
                              Game.new_alien2.y+=20
                    Aliens.check_y2+=20
                    for i in range(10):
                              entry=Game.list_alien3[i]
                              i,Game.new_alien3=entry
                              Game.new_alien3.dx=-Game.new_alien3.dx
                              Game.new_alien3.y+=20
                    Aliens.check_y3+=20
                    for i in range(10):
                              entry=Game.list_alien4[i]
                              i,Game.new_alien4=entry
                              Game.new_alien4.dx=-Game.new_alien4.dx
                              Game.new_alien4.y+=20
                    Aliens.check_y4+=20
                    for i in range(10):
                              entry=Game.list_alien5[i]
                              i,Game.new_alien5=entry
                              Game.new_alien5.dx=-Game.new_alien5.dx
                              Game.new_alien5.y+=20
                    Aliens.check_y5+=20

          def accelerate(self, speed):
                    
                    for i in range(10):
                              entry=Game.list_alien1[i]
                              i,Game.new_alien1=entry
                              Game.new_alien1.set_dx(speed)
                    for i in range(10):
                              entry=Game.list_alien2[i]
                              i,Game.new_alien2=entry
                              Game.new_alien2.dx=speed
                    for i in range(10):
                              entry=Game.list_alien3[i]
                              i,Game.new_alien3=entry
                              Game.new_alien3.dx=speed
                    for i in range(10):
                              entry=Game.list_alien4[i]
                              i,Game.new_alien4=entry
                              Game.new_alien4.dx=speed
                    for i in range(10):
                              entry=Game.list_alien5[i]
                              i,Game.new_alien5=entry
                              Game.new_alien5.dx=speed
                              
                                                            
          def die(self):
                    alien_y=self.get_y()
                    if alien_y==Aliens.check_y1 or alien_y==Aliens.check_y5:
                              self.game.score.value+=10
                    if alien_y==Aliens.check_y2:
                              self.game.score.value+=40
                    if alien_y==Aliens.check_y3:
                              self.game.score.value+=30
                    if alien_y==Aliens.check_y4:
                              self.game.score.value+=20
                    new_explosion=Explosion(x=self.x, y=self.y)
                    games.screen.add(new_explosion)
                    self.destroy()
                    Aliens.total-=1
                    if Aliens.total==0:
                              end_level=games.Message(value='Koniec poziomu: '+str(self.game.level),
                                                      size=40,
                                                      x=games.screen.width/2,
                                                      y=games.screen.height/2,
                                                      color=color.yellow,
                                                      lifetime=6*games.screen.fps,
                                                      is_collideable=False)
                              games.screen.add(end_level)
                              Aliens.count=500

          def end(self):
                    Boss_alien.sound.stop()
                    games.screen.clear()
                    image=games.load_image('score.jpg')
                    games.screen.set_background(image)
                    info=games.Text(value='zdobyte punkty: '+str(Ship.end_score),
                                    size=40,
                                    color=color.white,
                                    x=games.screen.width/2,
                                    y=100)
                    games.screen.add(info)
                    button=games.Text(value='DALEJ: przez Spacja',
                                          size=25,
                                          color=color.pink,
                                          x=600,
                                          y=570)
                    games.screen.add(button)
                    games.music.load('end.mp3')
                    games.music.play(-1)
                    Ghost.my_check2=True
                    self.game.ghost()
                                                                                                    
                                        
class Ship(Collider):

          image=games.load_image('ship.bmp')
          MISSILE_DELAY=25
          ship_position=0
          ship_count=4
          wait_ship=0
          end_score=0
          
          def __init__(self, game, x):
                    super(Ship, self).__init__(image=Ship.image,
                                               x=x,
                                               y=games.screen.height-20)
                    self.missile_wait=0
                    self.game=game
                    
                    
          def update(self):
                    self.game.level_info.value='Poziom: '+str(self.game.level)
                    if self.right>games.screen.width:
                              self.right=games.screen.width
                    if self.left<0:
                              self.left=0
                    if games.keyboard.is_pressed(games.K_LEFT):
                              self.x-=2
                              Ship.ship_position=self.get_x()
                    if games.keyboard.is_pressed(games.K_RIGHT):
                              self.x+=2
                              Ship.ship_position=self.get_x()
                    if self.missile_wait>0:
                              self.missile_wait-=1
                    if games.keyboard.is_pressed(games.K_SPACE) and self.missile_wait==0:
                              new_missile=Ship_missile(self.x, self.y)
                              games.screen.add(new_missile)
                              self.missile_wait=Ship.MISSILE_DELAY
                    Ship.wait_ship-=1
                    if Ship.wait_ship<0:
                              Ship.wait_ship=0
                    if Ship.wait_ship==0:
                                        super(Ship, self).update()
                    if Aliens.count<=500 and Aliens.count!=0:
                              Aliens.count-=1
                              if Aliens.count<0:
                                        Aliens.count=0
                              if Aliens.count==300:
                                        games.music.fadeout(2000)
                              if Aliens.count==0:
                                        self.game.advance()                                       

          def die(self):
                    super(Ship, self).die()
                    if self.game.info2 and Ship.ship_count==3:
                              self.game.info2.destroy()
                    if self.game.info1 and Ship.ship_count==2:
                              self.game.info1.destroy()
                    if Ship.ship_count==3 or Ship.ship_count==2 or Ship.ship_count==1:
                              if Ship.ship_count>1:
                                        Ship.wait_ship=200
                                        x=random.randrange(50,games.screen.width-50)
                                        my_ship=Ship(self.game,x)
                                        games.screen.add(my_ship)
                              Ship.ship_count-=1
                    if Ship.ship_count==0:
                              Ship.end_score=self.game.score.value
                              end_message=games.Message(value='KONIEC GRY',
                                              size=90,
                                              color=color.red,
                                              x=games.screen.width/2,
                                              y=games.screen.height/2,
                                              lifetime=10*games.screen.fps,
                                              is_collideable=False)
                              games.screen.add(end_message)
                              Aliens.break_time=5000
                              games.music.fadeout(3000)
                    if Ship.ship_count==0 and Aliens.total==0:
                              Aliens.end(self)
                              Ship.end_score=self.game.score.value
                              end_message=games.Message(value='KONIEC GRY',
                                              size=90,
                                              color=color.red,
                                              x=games.screen.width/2,
                                              y=games.screen.height/2,
                                              lifetime=10*games.screen.fps,
                                              is_collideable=False)
                              games.screen.add(end_message)
                              
                              
class Shield(Collider):
          
          images={1:games.load_image('shield.bmp'),
                  2:games.load_image('shield1.bmp'),
                  3:games.load_image('shield2.bmp'),
                  4:games.load_image('shield3.bmp'),
                  5:games.load_image('shield4.bmp'),
                  6:games.load_image('shield5.bmp'),
                  7:games.load_image('shield6.bmp'),
                  8:games.load_image('shield7.bmp'),
                  9:games.load_image('shield8.bmp'),
                  10:games.load_image('shield9.bmp')}
          count=1

          def __init__(self, shield_type, x):
                    super(Shield, self).__init__(image=Shield.images[shield_type],
                                                 x=x,
                                                 y=games.screen.height-80)
                    
                    
          def update(self):
                    super(Shield, self).update()
                    if Aliens.total==0:
                              if Aliens.count==1:
                                        self.destroy()
                                        Shield.count=1
                              
          def die(self):
                    thing=self.get_image()
                    my_bottom=self.get_bottom()
                    list=Shield.images.items()
                    for entry in list:
                              key, value=entry
                              if value==thing and key<10:
                                        Shield.count=key+1
                                        x=self.x
                                        self.destroy()
                                        new_shield=Shield(Shield.count,x=x)
                                        new_shield.bottom=542
                                        games.screen.add(new_shield)
                              else:
                                        self.destroy()                             
                    

class Explosion(games.Animation):

          sound=games.load_sound('eksplozja.wav')
          images=['eksplozja1.bmp','eksplozja2.bmp','eksplozja3.bmp','eksplozja4.bmp',
                 'eksplozja5.bmp','eksplozja6.bmp','eksplozja7.bmp','eksplozja8.bmp',
                 'eksplozja9.bmp']

          def __init__(self, x, y):
                    super(Explosion, self).__init__(images=Explosion.images,
                                                    x=x, y=y,
                                                    repeat_interval=4,
                                                    n_repeats=1,
                                                    is_collideable=False)
                    Explosion.sound.play()

class Ship_info(games.Sprite):
          
          image=games.load_image('ship.bmp')

          def __init__(self, game, x):
                    super(Ship_info, self).__init__(image=Ship_info.image,
                                                    x=x,
                                                    top=5,
                                                    is_collideable=False)
                    self.game=game

class Button(games.Sprite):

          image=[games.load_image('left.bmp'),
                 games.load_image('right.bmp'),
                 games.load_image('up.bmp'),
                 games.load_image('down.bmp'),
                 games.load_image('spacja.bmp')]

          def __init__(self, game, type_image,x,y):
                    super(Button, self).__init__(image=Button.image[type_image],
                                                 x=x,
                                                 y=y,
                                                 is_collideable=False)                   

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
                      
          def __init__(self, game, ghost_type, x, y):
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
                    if games.keyboard.is_pressed(games.K_SPACE) and Ghost.my_check2==True:
                              games.screen.clear()
                              games.music.stop()
                              self.game.start()
                              Ghost.my_check2=False
                              Ghost.my_check1=False
                              Ghost.count=100
                    if games.keyboard.is_pressed(games.K_SPACE) and Ghost.my_check1==False:
                              if Ghost.my_check3==False:
                                        self.game.button.destroy()
                                        self.game.run_ghost()
                                        Ghost.my_check3=True
                    if self.game.new_ghost1.y==500:
                              self.game.new_ghost1.dy=0
                    if self.game.new_ghost2.y==500:
                              self.game.new_ghost2.dy=0
                    if self.game.new_ghost3.y==540:
                              self.game.new_ghost3.dy=0
                    if self.game.new_ghost4.y==540:
                              self.game.new_ghost4.dy=0
                    if Ghost.check1==True:
                              if self.game.new_ghost5.x>games.screen.width/2:
                                        games.screen.add(self.game.info6)
                                        games.screen.add(self.game.button1)
                                        games.screen.add(self.game.button2)
                                        games.screen.add(self.game.button3)
                                        Ghost.check1=False
                                        games.music.fadeout(6000)
                    if Ghost.check2==True:
                              if self.game.new_ghost5.x>games.screen.width-30:
                                        Ghost.check2=False                              
                                        games.screen.clear()
                                        self.game.play()
                    if Ghost.count<=100:
                              Ghost.count-=1
                              if Ghost.count<0:
                                        Ghost.count=0
                    if Ghost.count==0:
                              Ghost.my_check3=False
                              Ghost.count=101
                    
class Game(object):
          
          images=(games.load_image('kosmos1.jpg'),
                  games.load_image('kosmos2.jpg'),
                  games.load_image('kosmos3.jpg'),
                  games.load_image('kosmos4.jpg'),
                  games.load_image('kosmos5.jpg'))
          music=('game_music1.mp3','game_music2.mp3','game_music3.mp3')                   
                                        

          def play(self):
                    self.level=0
                    Ship.ship_count=4
                    Shield.count=1
                    Aliens.total=0
                    Aliens.count=0
                    Game.list_alien1=[]
                    Game.list_alien2=[]
                    Game.list_alien3=[]
                    Game.list_alien4=[]
                    Game.list_alien5=[]
                    Aliens.fire_list=[]
                    Aliens.check1=1
                    Aliens.check2=1
                    self.sound=games.load_sound('poziom.wav')
                    self.score=games.Text(value=0,
                                          size=33,
                                          color=color.white,
                                          top=5,
                                          right=games.screen.width/2,
                                          is_collideable=False)
                    games.screen.add(self.score)
                    self.level_info=games.Text(value=0,
                                          size=33,
                                          color=color.white,
                                          top=5,
                                          right=games.screen.width-65,
                                          is_collideable=False)
                    games.screen.add(self.level_info)
                    self.info1=Ship_info(game=self,x=30)
                    self.info2=Ship_info(game=self,x=70)
                    games.screen.add(self.info1)
                    games.screen.add(self.info2)   
                    x=games.screen.width/2
                    self.my_ship=Ship(game=self,x=x)
                    games.screen.add(self.my_ship)
                    Ship.ship_count-=1
                    f=open('highscore.dat','rb')
                    player_list=pickle.load(f)
                    f.close()
                    self.player_list=player_list
                    self.advance()
                    games.screen.mainloop()
                                        
          def advance(self):
                    Game.list_alien1=[]
                    Game.list_alien2=[]
                    Game.list_alien3=[]
                    Game.list_alien4=[]
                    Game.list_alien5=[]
                    Aliens.fire_list=[]
                    Aliens.check1=1
                    Aliens.check2=1
                    self.level+=1
                    self.sound.play()
                    level_message=games.Message(value='Poziom: '+str(self.level),
                                                size=40,
                                                x=games.screen.width/2,
                                                y=70,
                                                color=color.yellow,
                                                lifetime=4*games.screen.fps,
                                                is_collideable=False)
                    games.screen.add(level_message)
                    if self.level==1:
                              self.prepare(100)
                    if self.level==2:
                              self.prepare(120)
                    if self.level==3:
                              self.prepare(140)
                    if self.level==4:
                              self.prepare(160)
                    if self.level==5:
                              self.prepare(180)
                    if self.level==6:
                              self.prepare(200)
                    if self.level==7:
                              self.prepare(220)
                    if self.level==8:
                              self.prepare(240)
                    if self.level==9:
                              self.prepare(260)
                    if self.level==10:
                              self.prepare(280)
                    if self.level==11 or self.level==12 or self.level==13 or self.level==14 or self.level==15:
                              self.prepare(300)
                    
          def prepare(self,y):
                    picture=random.choice(Game.images)
                    games.screen.background=picture
                    game_music=random.choice(Game.music)
                    games.music.load(game_music)
                    games.music.play(-1)
                    y=y
                    count=60
                    for i in range(10):
                              i+=1
                              x=i*count
                              Aliens.total+=1
                              new_alien1=Aliens(self,Aliens.images1,x,y)
                              entry=i,new_alien1
                              Game.list_alien1.append(entry)
                              games.screen.add(new_alien1)
                    Aliens.check_y1=new_alien1.get_y()
                    y+=40
                    for i in range(10):
                              i+=1
                              x=i*count
                              Aliens.total+=1
                              new_alien2=Aliens(self,Aliens.images2,x,y)
                              entry=i,new_alien2
                              Game.list_alien2.append(entry)
                              games.screen.add(new_alien2)
                    Aliens.check_y2=new_alien2.get_y()
                    y+=40
                    for i in range(10):
                              i+=1
                              x=i*count
                              Aliens.total+=1
                              new_alien3=Aliens(self,Aliens.images3,x,y)
                              entry=i,new_alien3
                              Game.list_alien3.append(entry)
                              games.screen.add(new_alien3)
                    Aliens.check_y3=new_alien3.get_y()
                    y+=40
                    for i in range(10):
                              i+=1
                              x=i*count
                              Aliens.total+=1
                              new_alien4=Aliens(self,Aliens.images4,x,y)
                              entry=i,new_alien4
                              Game.list_alien4.append(entry)
                              games.screen.add(new_alien4)
                    Aliens.check_y4=new_alien4.get_y()
                    y+=40
                    for i in range(10):
                              i+=1
                              x=i*count
                              Aliens.total+=1
                              new_alien5=Aliens(self,Aliens.images1,x,y)
                              entry=i,new_alien5
                              Game.list_alien5.append(entry)
                              games.screen.add(new_alien5)
                    Aliens.check_y5=new_alien5.get_y()
                    distance=games.screen.width/5
                    number=0
                    for i in range(4):
                              x=games.screen.width-distance-number
                              new_shield=Shield(Shield.count,x)
                              games.screen.add(new_shield)
                              number+=distance
          def ghost(self):
                    new_ghost1=Ghost(self,Ghost.images1,50,40)
                    games.screen.add(new_ghost1)
                    self.new_ghost3=Ghost(self,Ghost.images3,250,140)
                    games.screen.add(self.new_ghost3)
                    self.new_ghost2=Ghost(self,Ghost.images2,games.screen.width-50,340)
                    games.screen.add(self.new_ghost2)
                    self.new_ghost4=Ghost(self,Ghost.images4,games.screen.width-250,440)
                    games.screen.add(self.new_ghost4)

          def run_ghost(self):
                    self.new_ghost1.dy=4
                    self.new_ghost2.dy=4
                    self.new_ghost3.dy=4
                    self.new_ghost4.dy=4
                    self.info1=games.Text(value='10 pkt',
                                          size=30,
                                          color=color.yellow,
                                          x=120,
                                          y=502)
                    games.screen.add(self.info1)
                    self.info2=games.Text(value='40 pkt',
                                          size=30,
                                          color=color.yellow,
                                          x=games.screen.width-120,
                                          y=502)
                    games.screen.add(self.info2)
                    self.info4=games.Text(value='20 pkt',
                                          size=30,
                                          color=color.yellow,
                                          x=games.screen.width-120,
                                          y=542)
                    games.screen.add(self.info4)
                    self.info3=games.Text(value='30 pkt',
                                          size=30,
                                          color=color.yellow,
                                          x=120,
                                          y=542)
                    games.screen.add(self.info3)
                    self.info5=games.Text(value='300 pkt',
                                          size=30,
                                          color=color.yellow,
                                          x=10,
                                          y=100,
                                          dx=.6)
                    games.screen.add(self.info5)
                    self.info6=games.Text(value='Przygotuj się!',
                                          size=40,
                                          color=color.white,
                                          x=games.screen.width/2,
                                          y=200)
                    self.new_ghost5=Ghost(self,Ghost.images5,90,100)
                    self.new_ghost5.dx=.6
                    games.screen.add(self.new_ghost5)
                    self.button1=Button(self,4,340,games.screen.height-50)
                    self.button2=Button(self,0,500,games.screen.height-50)
                    self.button3=Button(self,1,550,games.screen.height-50)
                    Ghost.check1=True
                    Ghost.check2=True
                    Ghost.my_check1=True
                    
          def start(self):
                    image=games.load_image('start.jpg')
                    games.screen.background=image
                    sound=games.music.load('start.mp3')
                    games.music.play(-1)
                    self.button=games.Text(value='START: przez Spacja',
                                      size=25,
                                      color=color.pink,
                                      x=600,
                                      y=570,
                                      is_collideable=False)
                    games.screen.add(self.button)
                    self.new_ghost1=Ghost(self,Ghost.images1,50,40)
                    self.new_ghost1.dx=0
                    games.screen.add(self.new_ghost1)
                    self.new_ghost2=Ghost(self,Ghost.images2,games.screen.width-50,40)
                    self.new_ghost2.dx=0
                    games.screen.add(self.new_ghost2)
                    self.new_ghost3=Ghost(self,Ghost.images4,50,80)
                    self.new_ghost3.dx=0
                    games.screen.add(self.new_ghost3)
                    self.new_ghost4=Ghost(self,Ghost.images3,games.screen.width-50,80)
                    self.new_ghost4.dx=0
                    games.screen.add(self.new_ghost4)
                                                                                                                                                                
def main():
          
          new_game=Game()
          new_game.start()
          games.screen.mainloop()
          
main()
                  

