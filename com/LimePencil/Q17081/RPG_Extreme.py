import sys

def print_end():
    for i in range(n):
        st=""
        for j in range(m):
            if player.x==i and player.y==j and player.health!=0:
                st+="@"
            else:
                st+=grid[i][j]
        print(st)
    print("Passed Turns : {}".format(turns))
    print("LV : {}".format(player.level))
    print("HP : {}/{}".format(player.health,player.max_health))
    print("ATT : {}+{}".format(player.attack,player.attack_weapon))
    print("DEF : {}+{}".format(player.defense,player.defense_armor))
    print("EXP : {}/{}".format(player.exp,player.level*5))
    print(player.message)
      
class Monster:
    def __init__(self,name,attack,defense,max_health,exp) -> None:
        self.name=name
        self.attack=attack
        self.defense=defense
        self.max_health=max_health
        self.exp=exp
        self.current_health=max_health

class Player:
    def __init__(self,x,y,starting_x,starting_y) -> None:
        self.health=20
        self.max_health=20
        self.done=False
        self.attack=2
        self.attack_weapon=0
        self.defense=2
        self.defense_armor=0
        self.level=1
        self.exp=0
        self.weapon=None
        self.armor=None
        self.accesories=[]
        self.x=x
        self.y=y
        self.starting_x=starting_x
        self.starting_y=starting_y
        self.message="Press any key to continue."
    
    def move(self,order):
        dx=0
        dy=0
        if order=="L":
            dy=-1
        elif order=="R":
            dy=1
        elif order=="U":
            dx=-1
        elif order=="D":
            dx=1
        nx=self.x+dx
        ny=self.y+dy
        if 0<=nx<n and 0<=ny<m and grid[nx][ny]!="#":
            self.x=nx
            self.y=ny
            self.do_action(nx,ny)
        elif not(0<=nx<n and 0<=ny<m and grid[nx][ny]!="#") and grid[self.x][self.y]=="^":
            self.do_action(self.x,self.y)

    def do_action(self,nx,ny):
        t=grid[nx][ny]
        self.x=nx
        self.y=ny
        if t==".":
            pass
        elif t=="^":
            amount =5
            if "DX" in self.accesories:
                amount=1
            self.health-=amount
            self.check_dead(t)
        elif t=="B":
            item=item_pos[nx][ny]
            grid[nx][ny]="."
            if item.types=="W":
                self.attack_weapon=item.attack_plus
            elif item.types=="A":
                self.defense_armor=item.defense_plus
            elif item.types=="O":
                if len(self.accesories)<4 and item.effect not in self.accesories:
                    self.accesories.append(item.effect)
        elif t=="&":
            self.fight(monster_pos[nx][ny])
            a=self.check_dead(t,monster_pos[nx][ny])
            if not a:
                if "HR" in self.accesories:
                    self.health=min(self.health+3,self.max_health)
                grid[nx][ny]="."
                self.earn_exp(monster_pos[nx][ny].exp)
        elif t=="M":
            if "HU" in self.accesories:
                self.health=self.max_health
            self.fight_boss(monster_pos[nx][ny])
            a=self.check_dead(t,monster_pos[nx][ny])   
            if not a:
                grid[nx][ny]="."
                self.done=True
                self.message="YOU WIN!"
                if "HR" in self.accesories:
                    self.health=min(self.health+3,self.max_health)
                self.earn_exp(monster_pos[nx][ny].exp)
    
    def earn_exp(self,amount):
        if "EX" in self.accesories:
            amount=int(amount*1.2)
        self.exp+=amount
        self.check_level_up()

    def fight(self,mon:Monster):
        player_turn=True
        first=True
        while self.health>0 and mon.current_health>0:
            if player_turn:
                if first:
                    mul=1
                    if "CO" in self.accesories:
                        mul=2
                        if "DX" in self.accesories:
                            mul=3
                    
                    mon.current_health-=max(1,(self.attack+self.attack_weapon)*mul-mon.defense)
                else:
                    mon.current_health-=max(1,self.attack+self.attack_weapon-mon.defense)
            else:
                self.health-=max(1,mon.attack-(self.defense+self.defense_armor))
            first=False
            player_turn=not player_turn
        
    def fight_boss(self,mon:Monster):
        player_turn=True
        first=True
        not_damage=False
        if "HU" in self.accesories:
            not_damage=True
        while self.health>0 and mon.current_health>0:
            if player_turn:
                if first:
                    mul=1
                    if "CO" in self.accesories:
                        mul=2
                        if "DX" in self.accesories:
                            mul=3
                    
                    mon.current_health-=max(1,(self.attack+self.attack_weapon)*mul-mon.defense)
                else:
                    mon.current_health-=max(1,self.attack+self.attack_weapon-mon.defense)
            else:
                if not_damage:
                    not_damage=False
                else:
                    self.health-=max(1,mon.attack-(self.defense+self.defense_armor))
            first=False
            player_turn=not player_turn

    def check_dead(self,types,*arg:Monster):
        if self.health<=0:
            self.health=0
            if "RE" in self.accesories:
                self.health=self.max_health
                self.x=self.starting_x
                self.y=self.starting_y
                self.accesories.remove("RE")
                try:
                    arg[0].current_health=arg[0].max_health
                except:
                    pass
                return True
            self.done=True
            if types=="^":
                self.message="YOU HAVE BEEN KILLED BY SPIKE TRAP.."
            elif types=="M" or types=="&":
                self.message="YOU HAVE BEEN KILLED BY {}..".format(arg[0].name)
            return True
        return False
                
    def check_level_up(self):
        if self.exp>=5*self.level:
            self.level+=1
            self.max_health+=5
            self.health=self.max_health
            self.attack+=2
            self.defense+=2
            self.exp=0
            

        


class Item:
    def __init__(self,types,attributes) -> None:
        self.types=types
        if types=="W":
            self.attack_plus=attributes
        elif types=="A":
            self.defense_plus=attributes
        elif types=="O":
            self.effect=attributes

input = sys.stdin.readline
n,m = list(map(int,input().split()))
k=0
l=0
grid=[["."]*m for _ in range(n)]
monster_pos=[[None]*m for _ in range(n)]
item_pos=[[None]*m for _ in range(n)]
player=None
for i in range(n):
    row=input().rstrip()
    for j in range(m):
        if row[j]=="@":
            player=Player(i,j,i,j)
            continue
        elif row[j]=="&" or row[j]=="M":
            k+=1
        elif row[j]=="B":
            l+=1
        grid[i][j]=row[j]
s=input().rstrip()
for i in range(k):
    x,y,name,attack,defense,max_health,exp=input().split()
    x=int(x)-1
    y=int(y)-1
    attack=int(attack)
    defense=int(defense)
    max_health=int(max_health)
    exp=int(exp)
    monster_pos[x][y]=Monster(name,attack,defense,max_health,exp)

for i in range(l):
    x,y,types,attribute=input().split()
    x=int(x)-1
    y=int(y)-1
    if types=="W" or types=="A":
        attribute=int(attribute)
    item_pos[x][y]=Item(types,attribute)
turns=0
for i in range(len(s)):
    turns+=1
    player.move(s[i])
    if player.done:
        break
print_end()

