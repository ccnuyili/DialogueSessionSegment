# -*- encoding:utf-8 -*-
import numpy as np

MAXN = 9999
class AbstractSolution():
    def __init__(self):
        self.star_0 = 0
        self.star_1 = 0
        self.star_2 = 0
        self.star_3 = 0

        #hobby
        self.hobbyNumRange_1 = np.arange(1, MAXN)
        self.hobbyNumRange_2 = np.arange(1, MAXN)
        self.hobbyNumRange_3 = np.arange(1, MAXN)
        self.hobbyNumRange_4 = np.arange(1, MAXN)
        self.hobbyNumRange_5 = np.arange(1, MAXN)
        self.hobby_star_1 = 1.0  # in hobbyNumRange_1
        self.hobby_star_2 = 1.0  # in hobbyNumRange_2
        self.hobby_star_3 = 1.0  # in hobbyNumRange_3
        self.hobby_star_4 = 1.0  # in hobbyNumRange_4
        self.hobby_star_5 = 1.0  # in hobbyNumRange_5
        self.specialStar_Hobby = 0

        # label
        self.labelNumRange_1 = np.arange(1, MAXN)
        self.labelNumRange_2 = np.arange(1, MAXN)
        self.labelNumRange_3 = np.arange(1, MAXN)
        self.label_star_1 = 1.0
        self.label_star_2 = 1.0
        self.label_star_3 = 1.0
        self.specialStar_Labels = 0

        self.weightDict={}

    def getDictTotalScore(self):
        score = 0.0
        for each_key in self.weightDict:
            score += self.weightDict[each_key]
        return score



#*********打分机制 a **********：
class Solution_A(AbstractSolution):
    def __init__(self):
        AbstractSolution.__init__(self)
        self.star_0 = 0
        self.star_1 = 10
        self.star_3 = 30

        '''
        除了以下special relations，其它都与postData中命名一致。
        special relations:
        喜好：即喜欢\不喜欢，系统中有的有多个同时存在，但只打一个分。
        对象：即男\女朋友，系统中有的2者同时存在，但只打一个分。
        '''
        self.weightDict={
            # properties
            'nickName': self.star_1,
            'age': self.star_1,
            'birth': self.star_0,
            'datingAttitude': self.star_1,
            'crushExist': self.star_0,
            'tags': self.star_0,
            'lbs': self.star_0,
            'homeAddress': self.star_0,
            'companyAddress': self.star_0,
            'sleep': self.star_0,
            'wakeup': self.star_0,
            'nap': self.star_0,
            'breakfast_time': self.star_0,
            'lunch_time': self.star_0,
            'afternoon_tea_time': self.star_0,
            'dinner_time': self.star_0,
            'supper_time': self.star_0,
            'film_time': self.star_0,
            'cinema': self.star_0,

            # relations
            '性别': self.star_1,
            '星座': self.star_1,
            '生肖': self.star_0,
            '恋爱状态': self.star_3,
            '家乡':self.star_0,
            '喜好': self.star_1,  # special
            '不舒服': self.star_0,
            '职业': self.star_1,
            '对象': self.star_0,  # special
            '饮食习惯': self.star_0,

            'labels': self.star_0
        }
#end 打分机制 a


#*********打分机制 b **********：
class Solution_B(AbstractSolution):
    def __init__(self):
        AbstractSolution.__init__(self)

        self.star_1=3
        self.star_2=5
        self.star_3=6

        #喜好
        self.hobbyNumRange_1=np.arange(1, 6)
        self.hobbyNumRange_2=np.arange(6, 21)
        self.hobbyNumRange_3=np.arange(21, 51)
        self.hobbyNumRange_4=np.arange(51, 100)
        self.hobbyNumRange_5=np.arange(100, MAXN)
        self.hobby_star_1 = 0.2 # in hobbyNumRange_1
        self.hobby_star_2 = 0.4 # in hobbyNumRange_2
        self.hobby_star_3 = 0.6 # in hobbyNumRange_3
        self.hobby_star_4 = 0.8 # in hobbyNumRange_4
        self.hobby_star_5 = 1.0 # in hobbyNumRange_5
        self.specialStar_Hobby=12

        #label
        self.labelNumRange_1=np.arange(1, 3)
        self.labelNumRange_2=np.arange(3, 10)
        self.labelNumRange_3=np.arange(10, MAXN)
        self.label_star_1 = 0.3
        self.label_star_2 = 0.6
        self.label_star_3 = 1.0
        self.specialStar_Labels=8

        '''
        除了以下special relations，其它都与postData中命名一致。
        special relations:
        喜好：即喜欢\不喜欢，按照数量的范围打不同的分。
        对象：即男\女朋友，系统中有的2者同时存在，但只打一个分。
        '''
        self.weightDict={
            #properties
            'nickName':self.star_1,
            'age':self.star_3,
            'birth':self.star_2,
            'datingAttitude': self.star_2,
            'crushExist': self.star_3,
            'tags': self.star_3,
            'lbs': self.star_3,
            'homeAddress': self.star_3,
            'companyAddress': self.star_3,
            'sleep': self.star_2,
            'wakeup': self.star_2,
            'nap': self.star_2,
            'breakfast_time': self.star_2,
            'lunch_time': self.star_2,
            'afternoon_tea_time': self.star_2,
            'dinner_time': self.star_2,
            'supper_time':self.star_2,
            'film_time': self.star_2,
            'cinema': self.star_2,

            #relations
            '性别':self.star_3,
            '星座':self.star_2,
            '生肖': self.star_2,
            '恋爱状态': self.star_3,
            '家乡': self.star_2,
            '喜好': self.specialStar_Hobby,#special
            '不舒服': self.star_3,
            '职业': self.star_2,
            '对象': self.star_3,           #special
            '饮食习惯': self.star_3,

            #labels
            'labels': self.specialStar_Labels    #special
        }
#end 打分机制 b




