# -*- encoding:utf-8 -*-
import json
import requests

def postData(userId,URL):
    if userId=='':
        return ''
    data = {
        'type': 'userProfile',
        'operation': 'query',
        'userid': '',
        'invoker': 'memory',
        'labels':'need',
        'properties': ['nickName','age','datingAttitude','birth','lbs','crushExist','tags','homeAddress',
                       'companyAddress','sleep','wakeup','nap','breakfast_time','lunch_time','supper_time',
                       'afternoon_tea_time','dinner_time','film_time','cinema'],
        #'limit': 1,
        'relations': [
            {
                'relation': "性别"
            },
            {
                'relation': "星座"
            },
            {
                'relation': "生肖"
            },
            {
                'relation': "恋爱状态"
            },
            {
                "relation": "家乡"
            },
            {
                "relation": "喜欢"
            },
            {
                "relation": "不喜欢"
            },
            {
                "relation": "不舒服"
            },
            {
                "relation": "职业"
            },
            {
                "relation": "女朋友"
            },
            {
                "relation": "男朋友"
            },
            {
                "relation": "饮食习惯"
            }
        ]
    }
    data['userid']=userId
    headers = {"Content-Type": "application/json", "Accept": "application/json"}
    r = requests.post(URL, data=json.dumps(data), headers=headers)
    response_result = ''
    if r.status_code == 200:
        response_result = json.loads(r.text)
    return response_result
