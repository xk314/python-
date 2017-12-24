'''
枪：     型号 model
        杀伤力 damage
        子弹数量 bullet_count   add_bullet加子弹   shoot射击 
        
玩家 ：  姓名 name   血量 hp  枪gun      伤害hurt  开火fire
'''

'''
通过继承来获取别的类中的属性和方法，以完善本类实例化对象的功能。通过这种方式既可以继承属性
和方法，必要时又可以重写属性和方法。    我是
如果只是想简单的拥有一些属性和方法，可以通过让实例化对象以拥有属性的方式
拥有别的类的实例化对象（包含特殊的属性和方法），从而拥有属性和方法。 我有

继承  ：  相当于我是什么
属性 = 某实例化对象： 我拥有什么
'''

class Gun(object):
    __damage_dict = {'ak47': 3, 'm16': 2}
    __bullet_count_dict = {'ak47': 30, 'm16': 45}
    __instance = None


    def __new__(cls, *args, **kwargs):  #单例模式
        if args[0] not in Gun.__damage_dict.keys():
            print('枪支初始化失败，请重新选择!')
            return False
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self, model):
        self.model = model
        self.damage = Gun.__damage_dict[model]
        self.bullet_count = Gun.__bullet_count_dict[model]
        print('枪支初始化完成！')
        self.test()

    def add_bullet(self, num):
        while num > 0:
            if self.model == 'ak47' and self.bullet_count <= 100:
                self.bullet_count += 1
            if self.model == 'm16' and self.bullet_count <= 150:
                self.bullet_count += 1
            num -= 1
    def test(self):
        print(id(self))
        print('枪支类型： %s' % self.model)
        print('伤害： %d' % self.damage)
        print('子弹数： %d' % self.bullet_count)
    def shoot(self,enemy):
        if self.bullet_count == 0:
            print('子弹耗尽！')
            return False
        if enemy is None:
            self.bullet_count -= 1
            return
        if enemy.model == 'bad':
            enemy.hurt(self.damage)
            self.bullet_count -= 1
            return



# 玩家 ：  姓名 name   血量 hp  枪gun      伤害hurt  开火fire

class Player(object):
    __player_num = 0    #私有类属性
    __player_limit_num = 5
    __player_police_num = 0
    __player_bad_num = 0
    model_list = ['police', 'bad']
    @classmethod    #类方法
    def show_player(cls):
        print('当前共 %d 个玩家！' % cls.__player_num)
        print('警察： %d 个' % cls.__player_police_num)
        print('土匪   %d 个' % cls.__player_bad_num)
    def __new__(cls, *args, **kwargs):   #重写new方法
        if args[1] not in cls.model_list or len(args) != 2:
            print('请正确输入玩家姓名及类型！')
            return False
        if cls.__player_num >= cls.__player_limit_num:
            print('玩家数已到达限制！')
            return False
        if args[1] == 'police':
            cls.__player_num += 1
            cls.__player_police_num += 1
        if args[1] == 'bad':
            cls.__player_num += 1
            cls.__player_bad_num += 1
        return object.__new__(cls)

    def __init__(self, name, model):
        self.name = name
        self.hp = 100
        self.model = model
        self.gun = None
        print('%s   %s 初始化完成！' % (self.name, self.model))

    def own_gun(self, model):
        if self.model == 'police':
            self.gun = Gun(model)
        else:
            print('当前玩家不可以拥有枪！')
            return False

    def show_gun(self):
        if self.gun is None:
            print('当前用户无枪！')
            return
        self.gun.test()

    def fire(self, enemy):
        if self.gun is None:
            print('当前用户无枪,无法射击！')
            return False
        self.gun.shoot(enemy)

    def hurt(self, damage):
        if self.hp <= 0:
            print(' %s game over !' % self.name)
            return
        self.hp -= damage
        if self.hp <= 0:
            print(' %s game over !' % self.name)









men = Player('x', 'police')
men.own_gun('ak47')
bad = Player('b', 'bad')

while True:
    str = input('w 射击 q 加子弹')
    if str is 'w':
        men.fire(bad)
    if str is 'q':
        men.gun.add_bullet(30)
    if str is 'n':
        men.fire(None)
    print(bad.hp)
    print(men.gun.bullet_count)