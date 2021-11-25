#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @FileName  :forTest.py
# @Time      :2021/11/8 14:13
# @Author    :russionbear
import sys
import os, re, random
from queue import Queue
import pickle


# class Technology:
#     class technology:
#         ancient = 0x1
#         oldStone = 0x2
#         newStone = 0x3
#         bronze = 0x4
#
#     class culture:
#         nature = 0x1
#         creed = 0x2
#         sign = 0x3
#         profit = 0x4
#         heresy = 0x5
#
#     # religion
#     class truth:
#         mercy = 0x1
#         rite = 0x2
#         kingdom = 0x3
#         low = 0x4
#
#     class weapon:
#         none = 0x0
#
#     def __init__(self):
#         pass


# person


class Mood:
    mercy = 0x1
    envy = 0x11

    def __init__(self):
        self.presentBlessing = 0
        self.PresentEvil = 0
        self.quality = {}


class Ability:
    def __init__(self):
        self.hr = 0
        self.argue = 0
        self.military = 0
        self.protocol = 0
        self.finance = 0
        self.subtlety = 0


class Relative:
    clanElder = 0x1
    parent = 0x2
    child = 0x3
    brother = 0x4
    grandparent = 0x5
    grandchild = 0x6
    uncle = 0x7
    nephew = 0x8

    def __init__(self):
        pass


class Person:
    pSoldier = 0x1
    pTrader = 0x2
    pOfficial = 0x3
    pGang = 0x4
    pPolice = 0x5
    pClanElder = 0x6
    pTraveller = 0x7

    RName = 0x1
    RTRust = 0x2

    def __init__(self):
        self.id = 0
        self.name = 0
        self.age = 0
        self.sex = 0
        self.mood = Mood()
        self.health = 0
        self.hometown = 0
        self.relatives = Relative()
        self.friends = set()
        self.branch = set()
        self.header = 0

        self.ability = Ability()

        self.profession = 0
        self.group = set()
        self.prestige = {}
        self.collections = []
        self.properties = set()

        self.resident = 0

    def set_header(self, p0):
        pass


# all blow are about person


class Weather:
    # wind
    WNo = 0x1
    WWave = 0x2
    WFlag = 0x3
    WJam = 0x4
    WTree = 0x5
    WHouse = 0x6

    # temperature
    TBone = 0x1
    TIce = 0x2
    TCold = 0x3
    TCool = 0x4
    TWarm = 0x5
    THot = 0x6
    Ts = [1, 2, 3, 4, 5, 6]

    # dampness
    MWater = 0x1
    MDamp = 0x2
    MWet = 0x3
    MMid = 0x4
    MLittle = 0x5
    MDraught = 0x6

    # sun
    SDock = 0x1
    SWind = 0x2
    SShine = 0x3
    SHot = 0x4
    SSafe = 0x5

    dust = 0x4

    def __init__(self):
        # 0, + 8
        # 暂不控制
        self.windDirection = 1
        self.windStrength = 1
        self.sunshine = 3
        self.pollution = {}

        self.temperature = 0
        # plant,lake, river, sea, tem
        self.moisture = 3

    def add(self, n, strength):
        pass

    def update(self, type_, n):
        pass

    @staticmethod
    def get_weather_name(self, obj):
        pass


class Geo:
    # 地质
    LQSoft = 0x1
    LQClay = 0x2
    LQSand = 0x3
    LQHardI = 0x4
    LQHardII = 0x5
    LQHardIII = 0x6

    LQs = [1, 2, 3, 4, 5, 6]

    # 依海拔分类
    LADeepSea = 0x1
    LAShallow = 0x2
    LAPlain = 0x3
    LAHill = 0x4
    LAMountain = 0x5
    LAPlateau = 0x6
    LAs = [(-21000, -300), (-299, 0), (1, 300), (301, 1200), (1201, 3000), (3001, 8848)]

    # 地貌
    LFSea = 0x1
    LFRiver = 0x2
    LFWetland = 0x3
    LFLake = 0x4

    LFLava = 0x5
    LFVolcano = 0x6

    LFGlacier = 0x7

    # 坡度
    LSPlain = 0x1
    LSHill = 0x2
    LSMountain = 0x3

    # 低中高纬
    LOLow = 0x1
    LOMid = 0x2
    LOHigh = 0x3

    def __init__(self):
        self.altitude = 0
        self.slope = 0
        self.lq = {
            Geo.LQSoft: 100,
            Geo.LQClay: 0,
            Geo.LQSand: 0,
            Geo.LQHardI: 0,
            Geo.LQHardII: 0,
            Geo.LQHardIII: 0,
        }
        # 暂在考虑中
        self.lf = 0
        self.location = 0
        pass

    def hand_lq(self, type_, n=80):
        # for i, j in self.lq.items():
        #     self.lq[i] /= (100 - n)
        # self.lq[type_] += 80
        pass

    @staticmethod
    def get_type_altitude(h):
        for i1, i in enumerate(Geo.LAs):
            if i[0] < h < i[1]:
                return i1+1
        return 0


class Resource:
    PMoss = 0x1
    PGrass = 0x2
    PBush = 0x3
    PTree = 0x4
    PJungle = 0x5
    Ps = [1, 2, 3, 4, 5]

    AArctic = 0x2
    ADessert = 0x1
    APlain = 0x3
    ATree = 0x4
    AJungle = 0x5

    def __init__(self):
        self.water = 1
        # self.plant = {
        #     Resource.PMoss: 100,
        #     Resource.PGrass: 0,
        #     Resource.PBush: 0,
        #     Resource.PTree: 0,
        #     Resource.PJungle: 0
        # }
        self.plant = 0
        # 特殊物品
        self.drug = {}
        # 同plant属性
        self.animal = 1
        self.ore = 1
        self.gas = 1


class Building:
    BDwelling = 0x1
    BProduce = 0x2
    BProcess = 0x3
    BCulture = 0x5
    BMark = 0x6

    BService = 0xb
    BMilitary = 0xa

    TFarm = 5
    TPark = 10
    TWork = 20
    TRoom = 40
    Ts = [0, TFarm, TPark, TWork, TRoom]

    # person
    # group

    def __init__(self):
        self.id = 0, 0
        self.name = 0
        self.exFuncs = set()

        self.tName = 0
        self.areas = 1
        self.height = 10
        self.capacity = 100

        # __stockholder__ owned by people if is -1
        # could be a person or a group
        self.owner = {}

        self.manager = 0
        self.dwellers = set()
        self.storages = set()
        # self.groups = set()
        # self.person = set()

        # self.limitation = set()
        # self.watchdog = 0

    def set_limitation(self):
        pass

    @staticmethod
    def find_building():
        '''produce'''
        BFarmland = 0x3
        BTreeFarm = 0x4
        BLogging = 0x6
        BPasture = 0x1
        BMine = 0x16
        BRare = 0x2
        BGas = 0x17

        BFactory = 0x22

        BBank = 0x33
        BSchool = 0x34
        BLaboratory = 0x35
        BBar = 0x37

        BTemple = 0x2
        BChurch = 0x3
        BStadium = 0x5
        #
        BCasino = 0x6

        '''process'''
        GBasic = 0x11
        GLuxury = 0x12
        GTool = 0x13
        GWeapon = 0x14

        '''server'''

        TRoad = 0x1
        TTrain = 0x2
        THighway = 0x3
        TShip = 0x4
        TPlane = 0x5

        NPost = 0x1
        NPhone = 0x2
        NEmail = 0x3
        NNet = 0x4

        '''army'''
        BStronghold = 0x1
        BStorage = 0x2


class Storage:
    SCollection = 0x1
    SMoney = 0x2
    SGoods = 0x3
    SWeapon = 0x4

    def __init__(self):
        self.type_ = 0
        self.data = set()

    def type(self):
        return self.type_


# class Group:
#     gOfficial = 0x1
#     gTrader = 0x2
#     gTroop = 0x3
#     gGang = 0x4
#     gPolice = 0x5
#     gClan = 0x6
#     gTravel = 0x7
#
#     def __init__(self):
#         self.leader = 0
#         self.usage = 0
#         self.all = set()


class Goods:
    def __init__(self):
        pass


class Unit:
    def __init__(self):
        self.material = {}
        self.attack = 0
        self.attackType = 0
        self.defense = 0
        self.defenseType = 0
        self.mov = 0
        self.movType = 0
        self.view = 0
        self.viewType = 0

    def update_atr(self, material):
        pass


class TopAbc:
    def __init__(self):
        self.data = []

    def add(self, n):
        self.data.append(n)

    def remove(self, n):
        self.data.remove(n)

    def has(self, n):
        return n in self.data


class GAbc(TopAbc):
    gOfficial = 0x1
    gTrader = 0x2
    gTroop = 0x3
    gGang = 0x4
    gPolice = 0x5
    gClan = 0x6
    gTravel = 0x7

    gWatchdog = 0x11
    gImmigrant = 0x12

    def __init__(self):
        super(GAbc, self).__init__()
        self.usage = 0
        self.name = 0
        self.leader = set()
        self.hands = set()
        self.resident = 0
        self.buildings = set()

        self.low = 0

    def startup(self, money):
        pass
        # return goods

    def deliver(self, d0):
        if isinstance(d0, int):
            pass
        else:
            pass


class BAbc(TopAbc):
    def __init__(self):
        super(BAbc, self).__init__()
        self.technology = 0
        self.technology_next = 0


# building


class BManager(TopAbc):
    def __init__(self):
        super(BManager, self).__init__()
        self.freeSpace = 100
        self.road = set()

        self.houses = {}
        self.ages = {}
        self.citizenship = {}

        self.blessing = {}
        self.physique = {}
        self.character = {}

        self.religions = {}

        self.riches = {}
        self.incomes = {}
        self.outcomes = {}
        self.needs = {}


class BDwelling(BAbc):
    villa = 0x1
    tower = 0x2
    factory = 0x3
    cottage = 0x4
    # max capacity: 100;
    # capacity: 10000, 10000, 40000, 200
    # army: 10w

    def __init__(self):
        super(BDwelling, self).__init__()
        self.houses = {}
        self.ages = {}
        self.citizenship = {}

        self.blessing = {}
        self.physique = {}
        self.character = {}

        self.religions = {}

        self.riches = {}
        self.incomes = {}
        self.outcomes = {}
        self.needs = {}

    def fill_needs(self, needs: dict):
        def shopping():
            pass
        for i, j in needs.items():
            self.needs[i] -= j
        money = 0
        # 动乱 太贵
        return money

    def pay_salary(self, n0):
        pass

    def self_update(self):
        # 内部结构
        pass

    @staticmethod
    def get_name():
        pass


class BMark(BAbc):
    pBank = 0

    def __init__(self):
        super(BMark, self).__init__()
        self.producer = set()
        self.consumer = set()

        self.producer_ = set()
        self.consumer_ = set()
        self.volume = 0
        self.canBorrow = 0
        # needs, pay, tax # borrow from bank/government
        # return(money, goods) # 平均+优先级
        # pay, get #拖延

    def run(self):
        pass

    def buy(self, type_, cur, needs, policy=None):
        pass

    def limit_price(self, prices):
        pass


class BService(BAbc):
    TRoad = 0x1
    TTrain = 0x2
    THighway = 0x3
    TShip = 0x4
    TPlane = 0x5

    NPost = 0x1
    NPhone = 0x2
    NEmail = 0x3
    NNet = 0x4

    def __init__(self):
        super(BService, self).__init__()
        self.pOfficial = 0
        self.pHospital = 0
        self.pGym = 0
        self.pPark = 0
        self.pTransport = set()
        self.pNewsletter = set()


class BCulture(BAbc):
    def __init__(self):
        super(BCulture, self).__init__()
        self.impact = {}

    def tribute(self):
        return self.impact

    def update(self):
        pass


# group


class GOfficial(GAbc):
    # road, hospital, gym
    server = 0x1
    mark = 0x2
    culture = 0x3

    def __init__(self):
        super(GOfficial, self).__init__()


class GProduce(GAbc):
    pass


class GProcess(GAbc):
    pass


class GPolice(GAbc):
    pass


class GGang(GAbc):
    pass


class GTroop(GAbc):
    def __init__(self):
        super(GTroop, self).__init__()
        self.body = 0


class GTrader(GAbc):
    pass


class GClan(GAbc):
    pass


# statistic


class Block:
    def __init__(self):
        self.id = 0
        self.name = 0
        self.belong = 0
        self.geo = Geo()
        self.resource = Resource()
        self.weather = Weather()

        self.bManager = BManager()

        self.gOfficial = GOfficial()
        self.gProduce = GProduce()
        self.gProcess = GProcess()
        self.gTrader = GTrader()
        self.gPolice = GPolice()
        self.gGang = GGang()
        self.gTroop = GTroop()
        self.gClan = GClan()

    def update(self):
        pass

    def trading(self):
        pass
    # def __del__(self):
    #     print("it's del")


class Statistic:
    pass


class County(Statistic):
    def __init__(self):
        super(County, self).__init__()
        self.belong = 0
        self.blocks = []
        # self.geo = {}
        # self.weather = Weather()
        # self.resource = Resource()


class Region(Statistic):
    def __init__(self):
        super(Region, self).__init__()
        self.belong = 0
        self.counties = []
        # self.resource = Resource()


class Province(Statistic):
    def __init__(self):
        super(Province, self).__init__()
        self.belong = 0
        self.regions = []
        # self.resource = Resource()


class Force(Statistic):
    def __init__(self):
        super(Force, self).__init__()
        self.lows = set()
        self.header = 0


class Regedit:
    def __init__(self):
        self.data = []

    def add(self, n):
        for cur, da in enumerate(self.data):
            if da == None:
                self.data[cur] = n
                return cur
        else:
            self.data.append(n)
            return len(self.data) - 1

    def pop(self, cur):
        self.data.pop(cur)

    def remove(self, n):
        self.data.remove(n)

    def get(self, cur):
        try:
            rlt = self.data[cur]
            return rlt
        except IndexError:
            return None

    @staticmethod
    def get_name(**kwargs):
        pass


'''暂不考虑list长度问题'''


class RegeditBlock:
    def __init__(self, size: tuple):
        self.buffer = {}
        self.max_buffer = 64
        self.buffer_set = set()
        self.buffer_queue = Queue(self.max_buffer)

        self.height = self.width = 3
        self.resize(size[0], size[1])

    def resize(self, rows, cols):
        for i in os.listdir('run'):
            os.remove('run/'+i)
        new_length = rows * cols
        for i in range(new_length):
            with open('run/'+str(i), 'wb') as f:
                f.write(pickle.dumps(Block()))
        self.height, self.width = rows, cols

    def get(self, y=0, x=0, cur=-1) -> Block:
        # print(len(self.buffer_set))
        if cur == -1:
            cur = y * self.width + x
        if cur >= self.width * self.height:
            raise IndexError
        elif cur in self.buffer_set:
            return self.buffer[cur]
        else:
            with open('run/'+str(cur), 'rb') as f:
                tmp = pickle.load(f)

            self.buffer[cur] = tmp
            self.buffer_set.add(cur)
            self.buffer_queue.put(cur)

            if self.buffer_queue.full():
                cur = self.buffer_queue.get()
                self.buffer_set.remove(cur)
                self.push_disk(cur)
                del self.buffer[cur]

            return tmp

    def push_disk(self, cur):
        # print(cur, self.buffer[cur].geo.altitude, 'push')
        with open('run/'+str(cur), 'wb') as f:
            f.write(pickle.dumps(self.buffer[cur]))


# class RegeditBlock:
#     def __init__(self, size: tuple):
#         self.__width__ = 10000
#         self.data = []
#         self.height = self.width = 0
#         self.resize(size[0], size[1])
#
#     def resize(self, rows, cols):
#         new_length = rows * cols
#         now_length = len(self.data)
#         if now_length >= new_length:
#             # !!! may appear some errors !!!
#             self.data = self.data[0:new_length]
#         else:
#             for i in range(now_length, new_length):
#                 self.data.append(Block(i))
#         self.height, self.width = rows, cols
#
#     def get(self, y=0, x=0, cur=-1) -> Block:
#         if cur == -1:
#             cur = y * self.width + x
#         return self.data[cur]
#
#     def set(self, y, x, n, cur=-1):
#         if cur == -1:
#             cur = y * self.width + x
#         self.data[cur] = n


class RegeditBuilding(Regedit):
    def __init__(self):
        super(RegeditBuilding, self).__init__()


class RegeditGroup(Regedit):
    pass


class RegeditHuman(Regedit):
    pass


class RegeditTrader(Regedit):
    pass


class RegeditGang(Regedit):
    pass


class RegeditPolice(Regedit):
    pass


class RegeditForce(Regedit):
    def __init__(self):
        super(RegeditForce, self).__init__()


class DeviceWeather:
    pass


class DeviceAnimal:
    pass


class GameCore:
    def __init__(self):
        self.blocks = RegeditBlock((10, 10))


class MapBuilder:
    def __init__(self, size):
        # self.size = size
        # self.tmpMap = self.make_map_random0bit(size)
        # self.tmpMap = self.handle_map_scattered(self.tmpMap)
        # self.print(self.tmpMap)
        #
        # map_1 = self.fill_map(self.tmpMap)
        # self.print(map_1)
        # self.print(self.handle_map_scattered(map_1))
        # 
        # map_2 = self.fill_map(self.tmpMap, True)
        # self.print(map_2)
        # self.print(self.handle_map_scattered(map_2))
        # self.print(self.make_map_altitude(size))
        self.print(self.make_map_altitude0ladder((5, 5), [1, 1, 1, 1, 1, 1]), site=6)
        pass

    @staticmethod
    def make_map_random(size, vq=500):
        map_ = [[0 for i in range(size[1])] for j in range(size[0])]
        for i in range(size[0]):
            for j in range(size[1]):
                if random.randint(1, 1000) <= vq:
                    map_[i][j] = 1

        return map_

    @staticmethod
    def make_map_random0bit(size, vq=400, b1=109, b2=1000, rq=800):
        map_ = [[0 for i in range(size[1])] for j in range(size[0])]
        for i in range(size[0]):
            for j in range(size[1]):
                r1 = r2 = 1001
                while r1 > 1000:
                    r1 = random.randint(1, 1000+rq)
                while r2 > 1000:
                    r2 = random.randint(1, 1000+rq)
                r1 = r1 < vq
                r2 = r2 < vq
                r3 = random.randint(1, 1000)
                if r3 > b2:
                    r1 = not r1
                elif r3 > b1:
                    r1 = r1 or r2
                else:
                    r1 = r1 and r2
                if r1:
                    map_[i][j] = 1
                else:
                    map_[i][j] = 0

        return map_

    @staticmethod
    def make_map_altitude0queue(size):
        map_ = [[None for i1 in range(size[0])] for j in range(size[1])]
        rlt = set()
        drct = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = set()
        queue.add((0, 0))

        while queue:
            tem_q = set()
            rlt = rlt.union(queue)

            for i in queue:
                if random.randint(1, 5) >= 3:
                    map_[i[0]][i[1]] = 1
                else:
                    map_[i[0]][i[1]] = 0

                for j in drct:
                    y, x = i[0] + j[0], i[1] + j[1]
                    if x < 0 or y < 0 or y >= size[0] or x >= size[1]:
                        continue
                    if map_[y][x] == None and (y, x) not in rlt:
                        tem_q.add((y, x))

            queue.clear()
            queue = queue.union(tem_q)
            tem_q.clear()

        return map_

    @staticmethod
    def make_map_altitude0ladder(size, ladder):
        sum_ = sum(ladder)
        n = size[0] * size[1] / sum_

        for i in range(len(ladder)):
            ladder[i] = int(n*ladder[i])

        for i in enumerate(ladder):
            if i[1] == 0:
                ladder[i[0]] = -1

        sum_ = 0
        for i in range(1, len(ladder)+1):
            if ladder[-i] == -1:
                continue
            ladder[-i] += sum_
            sum_ = ladder[-i]

        if sum_ < size[0] * size[1]:
            ladder[0] += size[0] * size[1] - sum_

        queue = []
        map_ = []
        rlt = set()
        for i in range(size[0]):
            tmp = []
            for j in range(size[1]):
                queue.append((i, j))
                tmp.append(0)
            map_.append(tmp)

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        prior = []
        for i1, i in enumerate(ladder):
            if i == -1:
                continue
            tem_l = []
            for j in range(i):
                if prior:
                    cur = random.randint(0, len(prior)-1)
                    prior.pop(cur)
                else:
                    cur = random.randint(0, len(queue)-1)
                # map_[queue[cur][0]][queue[cur][1]] = i1
                map_[queue[cur][0]][queue[cur][1]] =\
                    random.randint(Geo.LAs[i1][0], Geo.LAs[i1][1])
                tem_l.append(queue[cur])
                queue.pop(cur)
            MapBuilder.print(map_, site=6)

            if i1 != 0:
                prior.clear()
                rlt = rlt.union(set(queue))

                for k1 in rlt:
                    for k2 in directions:
                        y, x = k2[0] + k1[0], k2[1] + k1[1]
                        if y < 0 or x < 0 or y >= size[0] or x >= size[1] or\
                                (y, x) in rlt:
                            continue
                        prior.append((y, x))
                # print('border', sorted(prior))
                prior = list(set(tem_l).difference(set(prior)))
                # print('no_border', (sorted(prior)))

            rlt.union(queue)

            queue.clear()
            queue.extend(tem_l)
            tem_l.clear()

        return map_

    @staticmethod
    def fill_map(pre_map, center=False, compare=None):
        if not compare:
            compare = lambda a: a == 1

        map_ = [i[:] for i in pre_map]
        print(len(map_))

        rlt = set()
        size = len(map_), len(map_[0])
        drct = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        queue = set()
        for i in range(size[0]):
            if not compare(map_[i][0]):
                queue.add((i, 0))

            if not compare(map_[i][-1]):
                queue.add((i, size[1] - 1))

        for i in range(1, size[1]-1):
            if not compare(map_[0][i]):
                queue.add((0, i))

            if not compare(map_[-1][i]):
                queue.add((size[0]-1, i))

        while queue:
            tem_q = set()
            rlt = rlt.union(queue)

            for i in queue:
                for j in drct:
                    y, x = i[0] + j[0], i[1] + j[1]
                    if x < 0 or y < 0 or y >= size[0] or x >= size[1]:
                        continue
                    if not compare(map_[y][x]) and (y, x) not in rlt:
                        tem_q.add((y, x))

            queue.clear()
            queue = queue.union(tem_q)
            tem_q.clear()

        if center:
            for i in range(size[0]):
                for j in range(size[1]):
                    if (i, j) not in rlt:
                        map_[i][j] = 1
        else:
            for i in rlt:
                map_[i[0]][i[1]] = 1
        print(len(map_))
        return map_

    @staticmethod
    def handle_map_scattered(pre_map, compare=None):
        if not compare:
            compare = lambda a: a == 1
        size = len(pre_map), len(pre_map[0])
        map_ = [j[:] for j in pre_map]
        directions = [(0, 1), (-1, 0), (1, 0), (0, -1)]
        for i in range(0, size[0]):
            for j in range(0, size[1]):
                can = 0
                if not compare(map_[i][j]):
                    continue
                for k in directions:
                    y, x = i + k[0], j + k[1]
                    if y < 0 or x < 0 or y >= size[0] or x >= size[1]:
                        continue
                    if compare(map_[y][x]):
                        can += 1
                if can <= 1:
                    map_[i][j] = 0

        return map_

    @staticmethod
    def make_snack(pre_map):
        size = len(pre_map), len(pre_map[0])
        # map_ = [i[:] for i in pre_map]
        map_ = [[0 for i in range(size[1])] for j in range(size[0])]

    @staticmethod
    def not_map(map_):
        rlt = []
        for i in map_:
            tmp = []
            for j in i:
                if j == 0:
                    c = 1
                else:
                    c = 0
                tmp.append(c)
            rlt.append(tmp)
        return rlt

    @staticmethod
    def print(map_, contrary=False, site=3):
        if contrary:
            for i in map_:
                for j in i:
                    if j == 0:
                        print(("%-"+str(site)+"d") % j, end='')
                    else:
                        print(("%-"+str(site)+"c") % ' ', end='')
                print()
        else:
            for i in map_:
                for j in i:
                    if j != 0:
                        print(("%-"+str(site)+"d") % j, end='')
                    else:
                        print(("%-"+str(site)+"c") % ' ', end='')
                print()
        print()


class MapInit:
    def __init__(self, size, date=None, dimension: tuple=None):
        map_ = RegeditBlock(size)
        self.dimension(map_, (-89, 89))
        # self.altitude0slope(map_)
        # self.landform(map_)

        self.print(map_, lambda a: a.weather.temperature)

        # self.print(map_, lambda a: a.geo.)

    @staticmethod
    def land0quality(map_: RegeditBlock):
        vt = len(Geo.LQs) - 1
        for i in range(map_.width*map_.height):
            for j in Geo.LQs:
                map_.get(cur=i).geo.lq[j] = 0
            map_.get(cur=i).geo.lq[random.randint(0, vt)] = 100

    @staticmethod
    def altitude0slope(map_: RegeditBlock, sea=250, shadow=300, plain=700, mountain=950, plateau=1000):
        # sea=250, shadow=50, plain=400, mountain=250, plateau=50
        # mark = MapBuilder.make_mpa_altitude((map_.height, map_.width))
        for i in range(map_.height):
            for j in range(map_.width):
                n = random.randint(1, 1000)
                if n <= sea:
                    map_.get(i, j).geo.altitude = -random.randint(1, 20)
                elif n <= shadow:
                    map_.get(i, j).geo.altitude = -random.randint(21, 8848)
                elif n <= plain:
                    map_.get(i, j).geo.altitude = random.randint(0, 300)
                elif n <= mountain:
                    map_.get(i, j).geo.altitude = random.randint(301, 2000)
                elif n <= plateau:
                    map_.get(i, j).geo.altitude = random.randint(2001, 8848)
                    # 更新土质
                    map_.get(i, j).geo.hand_lq(80)

                slope = random.randint(1, 10)
                if slope < 4:
                    map_.get(i, j).geo.slope = slope
                else:
                    high = map_.get(i, j).geo.altitude
                    if abs(high) <= 300:
                        map_.get(i, j).geo.slope = Geo.LSPlain
                    elif abs(high) <= 3000:
                        map_.get(i, j).geo.slope = Geo.LSHill
                    else:
                        map_.get(i, j).geo.slope = Geo.LSMountain

        fill_map = MapBuilder.fill_map(MapInit.to_bit(map_, compare=lambda a: a.geo.altitude >= 0))

        # 盆地 海边？
        for i in range(map_.height):
            for j in range(map_.width):
                if fill_map[i][j] == 0 and map_.get(i, j).geo.altitude < 300:
                    map_.get(i, j).geo.altitude = -random.randint(1, 300)


        # plain -300, 300
        # hill 301, 3000
        for i in range(map_.height):
            for j in range(map_.width):
                slope = random.randint(1, 10)
                if slope < 4:
                    map_.get(i, j).geo.slope = slope
                else:
                    high = map_.get(i, j).geo.altitude
                    if abs(high) <= 300:
                        map_.get(i, j).geo.slope = Geo.LSPlain
                    elif abs(high) <= 3000:
                        map_.get(i, j).geo.slope = Geo.LSHill
                    else:
                        map_.get(i, j).geo.slope = Geo.LSMountain

    @staticmethod
    def landform(map_: RegeditBlock, river=100, lake=200, wetland=250, volcano=300):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        fill_map = MapBuilder.fill_map(MapInit.to_bit(map_, compare=lambda a: a.geo.altitude >= 0), True)
        MapBuilder.print(fill_map)

        # count hollow
        hollow_0 = set()
        hollow_1 = set()
        hollow_2 = set()
        hollows = []
        for i in range(map_.height):
            for j in range(map_.width):
                if fill_map[i][j] == 0:
                    continue
                should = []
                for k in directions:
                    x, y = k[0] + j, k[1] + i
                    if x < 0 or y < 0 or x >= map_.width or y >= map_.height:
                        continue
                    elif fill_map[y][x] == 0:
                        # should = -1
                        break
                    elif map_.get(i, j).geo.altitude >= map_.get(y, x).geo.altitude:
                        should.append((y, x))
                else:
                    if not should:
                        hollow_0.add((i, j))
                    elif len(should) == 1:
                        hfg = ((i, j), should[0])
                        hollow_1.add(hfg)
                    elif len(should) == 2:
                        if should[0][0] + should[1][0] == y * 2 and\
                                should[0][1] + should[1][1] == x * 2:
                            continue
                        hfg = ((i, j), should[0], should[1])
                        hollow_2.add(hfg)

        for i in hollow_0:
            tmp = set()
            tmp.add(i)
            hollows.append(tmp)

        while 1:
            can_out = True
            delete = []
            for i in hollow_1:
                for j in range(len(hollows)):
                    if i[1] in hollows[j]:
                        hollows[j].add(i[0])
                        delete.append(i)
                        can_out = False
            for i in delete:
                hollow_1.remove(i)
            delete.clear()

            for i in hollow_2:
                for j in range(len(hollows)):
                    if i[1] in hollows[j] and i[2] in hollows[j]:
                        hollows[j].add(i[0])
                        can_out = False
                        delete.append(i)
            for i in delete:
                hollow_2.remove(i)
            delete.clear()

            if can_out:
                break

        # hollows.sort(key=lambda a: len(a))
        # river, lake, wetland
        for i in hollows:
            cur = random.randint(1, 1000)
            if cur <= river:
                for j in i:
                    map_.get(j[0], j[1]).geo.lf = Geo.LFRiver
            elif cur <= lake:
                for j in i:
                    map_.get(j[0], j[1]).geo.lf = Geo.LFLake
            elif cur <= wetland:
                for j in i:
                    map_.get(j[0], j[1]).geo.lf = Geo.LFWetland

        # ###### check ###### #
        # count = 0
        # rlt = set()
        # for i in hollows:
        #     count += len(i)
        #     for j in i:
        #         rlt.add(j)
        # print(count, len(rlt))
        # print(hollows)
        # return

        del hollows, hollow_1, hollow_2, hollow_0
        # 火山
        hill_0 = set()
        hill_1 = set()
        hill_2 = set()
        hills = []
        for i in range(map_.height):
            for j in range(map_.width):
                if fill_map[i][j] == 0:
                    continue
                should = []
                for k in directions:
                    x, y = k[0] + j, k[1] + i
                    if x < 0 or y < 0 or x >= map_.width or y >= map_.height:
                        continue
                    elif fill_map[y][x] == 0:
                        continue
                    elif map_.get(i, j).geo.altitude < map_.get(y, x).geo.altitude:
                        should.append((y, x))
                else:
                    if not should:
                        hill_0.add((i, j))
                    elif len(should) == 1:
                        hfg = ((i, j), should[0])
                        hill_1.add(hfg)
                    elif len(should) == 2:
                        if should[0][0] + should[1][0] == y * 2 and\
                                should[0][1] + should[1][1] == x * 2:
                            continue
                        hfg = ((i, j), should[0], should[1])
                        hill_2.add(hfg)

        for i in hill_0:
            tmp = set()
            tmp.add(i)
            hills.append(tmp)

        while 1:
            can_out = True
            delete = []
            for i in hill_1:
                for j in range(len(hills)):
                    if i[1] in hills[j]:
                        hills[j].add(i[0])
                        delete.append(i)
                        can_out = False
            for i in delete:
                hill_1.remove(i)
            delete.clear()

            for i in hill_2:
                for j in range(len(hills)):
                    if i[1] in hills[j] and i[2] in hills[j]:
                        hills[j].add(i[0])
                        can_out = False
                        delete.append(i)
            for i in delete:
                hill_2.remove(i)
            delete.clear()

            if can_out:
                break

        for i in hills:
            cur = random.randint(0, 1000)
            if cur <= volcano - wetland:
                tmp = list(i)
                tmp.sort(key=lambda a: map_.get(a[0], a[1]).geo.altitude)
                map_.get(tmp[-1][0], tmp[-1][1]).geo.lf = Geo.LFVolcano
                for j in tmp[:-1]:
                    map_.get(j[0], j[1]).geo.lf = Geo.LFLava

        # ###### check ###### #
        # count = 0
        # rlt = set()
        # for i in hills:
        #     if len(i) > 2:
        #         count += len(i)
        #     for j in i:
        #         rlt.add(j)
        # print(count, len(rlt))
        # print(hills)
        # return

        # 纬度
        ''''''

    @staticmethod
    def dimension(map_: RegeditBlock, dimension=(0, 0)):
        # wind, sun, steam,
        # 30, 60, 90
        reference = [-90, -60, -30, 30, 60, 90]
        sections = []
        ladders = []
        for i in enumerate(reference):
            if dimension[0] < i[1]:
                sections.append((dimension[0], i[1]))
                for j in range(i[0]+1, len(reference)):
                    if reference[j] >= dimension[1]:
                        sections.append((reference[j-1], dimension[1]))
                        break
                    else:
                        sections.append((reference[j-1], reference[j]))
                break
        if sections[-1][0] > sections[-1][1]:
            tmp = (sections[-2][0], sections[-1][1])
            sections.pop(-1)
            sections.pop(-1)
            sections.append(tmp)
        for i in sections:
            ladders.append(i[1]-i[0])
        if len(sections) == 1 and sections[0][0] == sections[0][1]:
            ladders = [(0, map_.height)]
        else:
            n = map_.height/sum(ladders)
            max_c = 0
            for i in enumerate(ladders):
                ladders[i[0]] = round(ladders[i[0]] * n)
                if ladders[i[0]] > ladders[max_c]:
                    max_c = i[0]
            ladders[max_c] += map_.height - sum(ladders)
            max_c = 0
            for i in enumerate(ladders):
                ladders[i[0]] = max_c, i[1] + max_c
                max_c += i[1]

        for i, j in zip(ladders, sections):
            max_c = max(abs(j[0]), abs(j[1]))
            print(max_c)
            if max_c > 60:
                interval = 0, 1, Geo.LOHigh, 0, 1
            elif max_c > 30:
                interval = 1, 3, Geo.LOMid, 2, 3
            else:
                interval = 4, 5, Geo.LOLow, 3, 4
            for k in range(i[0], i[1]):
                for p in range(map_.width):
                    map_.get(k, p).weather.temperature =\
                        Weather.Ts[random.randint(interval[0], interval[1])]
                    map_.get(k, p).geo.location = interval[2]
                    map_.get(k, p).resource.plant =\
                        Resource.Ps[random.randint(interval[3], interval[4])]
                    map_.get(k, p).resource.animal =\
                        Resource.Ps[random.randint(interval[3], interval[4])]

        #     print(i, j)
        # print(ladders)
        # print(sections)

    @staticmethod
    def resource0weather(map_: RegeditBlock, ore=200, gas=200):
        for i in range(map_.width * map_.height):
            cur1 = random.randint(1, 1000)
            if cur1 > ore:
                cur1 = 0
            else:
                cur1 %= 6
            map_.get(cur=i).resource.ore = cur1
            cur1 = random.randint(1, 1000)
            if cur1 > gas:
                cur1 = 0
            else:
                cur1 %= 6
            map_.get(cur=i).resource.gas = cur1

    @staticmethod
    def people(map_: RegeditBlock, low=50, mid=500, high=200, top=250):
        #
        pass

    @staticmethod
    def mark():
        pass

    @staticmethod
    def to_bit(pre_map: RegeditBlock, compare=None):
        if not compare:
            pass
        map_ = []
        for i in range(pre_map.height):
            tmp_map = []
            for j in range(pre_map.width):
                tmp_map.append(int(compare(pre_map.get(i, j))))
            map_.append(tmp_map)
        return map_

    @staticmethod
    def print(map_: RegeditBlock, func):
        if not func:
            func = lambda a: a
        for i in range(map_.height):
            for j in range(map_.width):
                print('%-6s' % str(func(map_.get(i, j))), end='')
            print()


class AI:
    pass


class Role:
    def __init__(self, nickname, job):
        self.nickname = nickname
        pass

    def run(self):
        saved = True
        while 1:
            input_ = input("["+self.nickname+"]# ")
            input_ = re.sub(' +', ' ', input_)
            cmc = input_.split(' ')
            if cmc[0] == 'exit':
                if not saved and '-f' not in cmc:
                    input_ = input("exit without save?(tip: input yes for save)\n")
                    if input_ == 'yes':
                        self.save()
                print('\nbye')
                break
            elif hasattr(self, cmc[0]):
                eval('self.'+cmc[0]+"(cmc[1:])")

    def lscmds(self):
        print(self.__doc__)

    def save(self):
        print('saved')

    def speed(self):
        pass


class RoleOfficial(Role):
    def search(self):
        pass

    def news(self):
        pass


if __name__ == "__main__":
    import time
    start_time = time.time()

    exMap = MapInit((9, 9))
    print(time.time() - start_time)
    pass




