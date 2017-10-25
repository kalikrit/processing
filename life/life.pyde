"""
life simulation

human objects can move, couple, produce children, die
children can be only in a couple
couple can be only from the age of 18 with a person of opposite sex with age from 18 till 60
couple with relatives till 3th root cannot be formed
a single man is searching for single woman and moves towards her
one woman can have random(4) children
life duration is a random(100)
death occures only from the age, no deseases so far

authors: Konstantin Kononenko (Moscow, Russia), Reshetina Natalya (Moscow, Russia)
date: 18.10.2017
update: 24.10.2017
version: 2.1.3
"""
import random as rnd
import uuid

def setup():
    frameRate(10)
    size(1500,950)
    stroke(255)
    textSize(24)
    
    global humans
    humans = list()
    global childrenN
    childrenN = 0
    global deadN
    deadN = 0
    global men, woman
    men = ['Aleksandr', 'Aleksey', 'Anatoly', 'Andrey', 'Anton', 'Arkady', 'Artem', 'Boris', 'Vadim', 'Valeriy', 'Vasily', 'Viktor', 'Vitaly', 'Vladimir', 'Vladislav', 'Gennady', 'Georgy', 'Gleb', 'Grigory', 'Daniil', 'Denis', 'Dmitry', 'Yevgeny', 'Egor', 'Zahar', 'Ivan', 'Igor', 'Ilya', 'Kirill', 'Konstantin', 'Lev', 'Leonid', 'Maksim', 'Matvey', 'Mikhail', 'Nikita', 'Nikolay', 'Oleg', 'Pavel', 'Pyotr', 'Roman', 'Ruslan', 'Semyon', 'Sergey', 'Stepan', 'Timofey', 'Timur', 'Tihon', 'Fedor', 'Yury', 'Yakov']
    woman = ['Alexandra', 'Alisa', 'Alina', 'Alla', 'Albina', 'Anastasia', 'Angelina', 'Anzhela', 'Anna', 'Antonina', 'Valentina', 'Valeria', 'Varvara', 'Vera', 'Veronika', 'Viktoria', 'Galina', 'Darya', 'Diana', 'Dina', 'Evgenia', 'Ekaterina', 'Elena', 'Elizaveta', 'Zhanna', 'Zinaida', 'Zoya', 'Inna', 'Irina', 'Karina', 'Kira', 'Klara', 'Kristina', 'Ksenia', 'Larisa', 'Lidia', 'Lia', 'Lyubov', 'Lyudmila', 'Margarita', 'Marina', 'Maria', 'Nadezhda', 'Natalya', 'Nina', 'Oksana', 'Olesya', 'Olga', 'Polina', 'Raisa', 'Rosa', 'Svetlana', 'Sofya', 'Tamara', 'Tatyana', 'Ulyana', 'Yulia', 'Yana']
    
    global W
    fn = "life_%s%s%s%s%s.gv" % (year(),month(),day(),hour(),minute())
    W = createWriter(fn)
    W.print("digraph {")
    
    init()
    #init_pairs()
    
def init():
    for _ in range(30):
        human = Human(int(random(2)), random(100,width-100), random(50, height-200), (random(255),random(255),random(255)))
        humans.append(human)
        
def init_pairs():
    pairs = 3
    x,y = random(100,width-100), random(50, height-200)
    for _ in range(pairs):
        human = Human(0, x,y, (random(255),random(255),random(255)))
        humans.append(human)
        human = Human(1, x+2,y+2, (random(255),random(255),random(255)))
        humans.append(human)        
     
def draw():
    background(120)
    if len(humans) == 0:
        noLoop()
        W.print("}")
        W.close()
    for human in humans:
        human.live()
        human.move()
        human.show()
    fill(255,200)
    text("ages: %i | humans: %i | children born: %i" % (frameCount/frameRate, len(humans), childrenN), 10, 30)
    text("died: "+str(deadN), 10, 55) 

def keyPressed():
    global go
    if key == 'i':
        init()
    if key == 's':
        noLoop()
    if key == 'c':
        loop()

def mouseClicked():
    x,y = mouseX,mouseY
    for h in humans:
        l = dist(x,y,h.x,h.y)
        if l <= h.d/2:
            print(h)

def mouseDragged():
    x,y = mouseX,mouseY
    for h in humans:
        l = dist(x,y,h.x,h.y)
        if l <= h.d/2:
            h.x,h.y = mouseX,mouseY   

class Human(object):

    def __init__(self, sex, x, y, (r,g,b)):
        self.uid = str(uuid.uuid4())
        self.sex = sex
        self.name = rnd.choice(men) if self.sex == 0 else rnd.choice(woman)
        self.preg = int(random(4)) if self.sex == 1 else 0
        self.age_give_birth = 0
        self.pair = 0 # сюда пишем экземпляр Human мужа/жены
        self.relatives = list()
        self.max_age = random(100)
        self.age = 0 
        self.x = x
        self.y = y
        self.d = 1
        self.r = r
        self.g = g
        self.b = b
        self.stroke = random(255)
        
    def __str__(self):
        return ("object: %s, sex: %s, age: %i, pair with: %s, pregN: %i, relatives: %s" % (self.uid, "M" if self.sex == 0 else "W", self.age, "no pair" if self.pair == 0 else self.pair.uid, self.preg, str(self.relatives)))    
    
    def live(self):
        global deadN, childrenN
        self.age += 0.1
        if self.age <= self.max_age:
            if self.age < 18:
                self.d += 0.5
            if self.age > 60:
                self.d -= 0.1
        # смерть от возраста    
        else:
            if self.pair:
                self.pair.pair = 0
            humans.remove(self)
            deadN += 1
            
        # рождение
        if self.sex == 1 and self.pair and self.preg > 0 and self.age < 60 and (self.age - self.age_give_birth) >= 1:
            self.preg -= 1
            self.age_give_birth = self.age
            human = Human(int(random(2)), random(self.x-self.d,self.x+self.d), random(self.y-self.d, self.y+self.d), (random(255),random(255),random(255)))
            # регистрация родственых связей
            human.relatives.extend((self.uid,self.pair.uid)) # добавляем маму и папу
            # у мамы и папы берем по 6 первых родственников
            rel = []
            rel.extend(self.relatives[:6])
            rel.extend(self.pair.relatives[:6])
            human.relatives.extend(rel)        
            
            humans.append(human)
            childrenN += 1
            #print('%s has produced a child! Happy Birthday!!!' % self.uid)
            
            # пишем рождение ребенка
            W.print("\n")
            W.print('"%s" [label="%s %s"]' % (self.uid, self.name, self.age))
            W.print("\n")
            W.print('"%s" [label="%s %s"]' % (self.pair.uid, self.pair.name, self.pair.age))
            W.print("\n")
            W.print('"%s" [label="%s"]' % (human.uid, human.name))
            W.print("\n")
            W.print('"%s" -> "%s"' % (self.uid, human.uid))
            W.print("\n")
            W.print('"%s" -> "%s"' % (self.pair.uid, human.uid))
            W.print("\n")                  
                       
    def show(self):
        stroke(self.stroke)
        fill(self.r, self.g, self.b)
        # мужчины квадраты, женщины кружки
        if self.sex == 0:
            rect(self.x, self.y, self.d/2, self.d/2)
        else:
            ellipse(self.x, self.y, self.d/2, self.d/2)
    
    def make_couple(self, other):
        # если объект уже в паре
        if self.pair or other.pair:
            return
        
        # проверяем родственников до 3его колена
        # если есть пересечение, - т.е. общие родственники, то пару не образуем
        my_rel = set([self.uid])
        my_rel = my_rel.union(set(self.relatives))
        other_rel = set([other.uid])
        other_rel = other_rel.union(set(other.relatives))
        if len(my_rel.intersection(other_rel)) != 0:
            return
        
        # проверяем возраст от 18 до 60
        if (self.age >=18 and self.age <= 60) and (other.age >=18 and other.age <= 60):
            # делаем пару - записываем себе uid партнера
            self.pair = other
            other.pair = self
            #print('couple: %s | %s'%(self.uid, other.uid))

                                        
    def move(self):
        dst = []
        if len(humans) > 1:
            for h in humans:
                l = dist(self.x, self.y, h.x, h.y)
                if l <= self.d and self.sex != h.sex:
                    self.make_couple(h)
        
        # одинокий мужик ищет незамужнюю женщину не родственницу
        wd = {}
        if self.sex == 0 and self.pair == 0 and self.age > 17 and self.age < 58:
            for h in humans:
                if h.sex == 1 and h.age < 58 and len(set(self.relatives).intersection(set(h.relatives))) == 0:
                    l = dist(self.x,self.y,h.x,h.y)
                    wd[l] = h
            if len(wd) > 0:         
                dst = wd[min(wd.keys())]        
                if dst.x > self.x:
                    self.x += self.d*0.04
                else:
                    self.x -= self.d*0.04
                if dst.y > self.y:
                    self.y += self.d*0.04
                else:
                    self.y -= self.d*0.04        
                                            
        else:                                                        
            to = int(random(4))
            # up
            if to == 0 and self.y - self.d/2 > 0: 
                self.y -= self.d*0.07
            # right    
            elif to == 1 and self.x + self.d/2 < width:
                self.x += self.d*0.07
            # down    
            elif to == 2 and self.y + self.d/2 < height:
                self.y += self.d*0.07
            # left    
            elif to == 3 and self.x - self.d/2 > 0:
                self.x -= self.d*0.07

        