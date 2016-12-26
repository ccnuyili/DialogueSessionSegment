# -*- encoding:utf-8 -*-
from weightDict import *
from run import *
from test import *

if __name__ == '__main__':
    #solution可选Solution_A()或Solution_B()
    #
    # 处理单个指定的ID：
    #test(solution=Solution_B(), userId='W48', URL='http://192.168.1.125:8089/memory/rest/query/post')
    #
    # 批量处理文件的所有ID：
    run(solution=Solution_A(), userId="AllUserId126.txt", URL='http://192.168.1.125:8089/memory/rest/query/post')

    # URL = 'http://192.168.1.125:8089/memory/rest/query/post'
    # URL = 'http://192.168.1.132:8089/memory/rest/query/post'
    # URL = 'http://192.168.1.134:8089/memory/rest/query/post'
