# -*- encoding:utf-8 -*-
from postData import *

def getUserScore(responseResult, solution):
    userScore = 0.0
    if responseResult=='' or responseResult==[]:
        return userScore
    resultDict=responseResult[0].get('result')
    labelDict=resultDict.get(u'labels')
    propertyDict=resultDict.get(u'properties')
    relationDictlist=resultDict.get(u'relations')
    if type(propertyDict) == type(None) or type(relationDictlist)==type(None) or type(labelDict) == type(None):
        return userScore

    nonelist = [None, 'null', 'NULL', '', 'None', 0]

    print 'userID:'+resultDict.get(u'userid').encode('utf-8')
    print "--------labels-------"
    for each in labelDict:
        print each.encode('utf-8'),
    lableNum=len(labelDict)-1
    print "\nlabel num",
    print lableNum
    print "label score:",
    labelStar=solution.weightDict.get('labels')
    if lableNum in solution.labelNumRange_1:
        userScore+=solution.label_star_1*labelStar
        print solution.label_star_1*labelStar
    elif lableNum in solution.labelNumRange_2:
        userScore+=solution.label_star_2*labelStar
        print solution.label_star_2*labelStar
    elif lableNum in solution.labelNumRange_3:
        userScore+=solution.label_star_3*labelStar
        print solution.label_star_3*labelStar

    print "\n--------properties-------"
    for proterty_key in propertyDict:
        proterty_value=propertyDict[proterty_key]
        print proterty_key,
        print proterty_value,
        if not nonelist.__contains__(proterty_value):
            userScore+=solution.weightDict.get(proterty_key.encode('utf-8'))
            print solution.weightDict.get(proterty_key.encode('utf-8'))
        else:
            print "0"

    print "\n--------relations-------"
    specialRelationTypes = [u'喜欢', u'不喜欢', u'女朋友', u'男朋友']
    hobbyNum = 0
    loverMark = False  # False表示没有
    for relationDict in relationDictlist:
        relationType = relationDict.get('relation')
        relationValue = relationDict.get('value')
        print ""
        print relationType,
        if type(relationValue) != type(None):
            for each in relationValue:
                each = each.encode('utf-8')
                print each,
        else:
            print "None",
        if specialRelationTypes.__contains__(relationType):
            # 需要特殊处理的
            if (relationType == u'喜欢' or relationType == u'不喜欢') and len(relationValue) > 0:
                hobbyNum += len(relationValue)
                continue

            if (relationType == u'女朋友' or relationType == u'男朋友') and len(relationValue) > 0:
                loverMark = True
                continue
        else:
            # 只要不为空就加分
            if len(relationValue) > 0:
                score = solution.weightDict.get(relationType.encode('utf-8'))
                if type(score) != type(None):
                    userScore += score
                    print score,
                else:
                    print score,
            else:
                print "0",

    hobbyStar = solution.weightDict.get('喜好')
    print "\n(hobby num:",
    print hobbyNum,
    print "  hobby score:",
    if hobbyNum in solution.hobbyNumRange_1:
        userScore += solution.hobby_star_1 * hobbyStar
        print solution.hobby_star_1 * hobbyStar,
    elif hobbyNum in solution.hobbyNumRange_2:
        userScore += solution.hobby_star_2 * hobbyStar
        print solution.hobby_star_2 * hobbyStar,
    elif hobbyNum in solution.hobbyNumRange_3:
        userScore += solution.hobby_star_3 * hobbyStar
        print solution.hobby_star_3 * hobbyStar,
    elif hobbyNum in solution.hobbyNumRange_4:
        print solution.hobby_star_4 * hobbyStar,
        userScore += solution.hobby_star_4 * hobbyStar
    else:
        userScore += solution.hobby_star_5 * hobbyStar
        print solution.hobby_star_5 * hobbyStar,
    print ')'
    if loverMark == True:
        userScore += solution.weightDict.get('对象')
        print "对象(男\女朋友):",
        print  solution.weightDict.get('对象')

    print "\nuser score:",
    print userScore
    print "total score",
    DictTotalScore=solution.getDictTotalScore()
    print DictTotalScore
    return userScore / DictTotalScore * 100


def test(solution,userId,URL):
    responseResult = postData(userId,URL)
    print responseResult
    print ""
    score = getUserScore(responseResult,solution)
    print "final score",
    print score

