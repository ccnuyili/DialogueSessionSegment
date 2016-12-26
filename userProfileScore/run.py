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

    # **************labels:*******************
    lableNum=len(labelDict)-1
    labelStar=solution.weightDict.get('labels')
    if lableNum in solution.labelNumRange_1:
        userScore+=solution.label_star_1*labelStar
    elif lableNum in solution.labelNumRange_2:
        userScore+=solution.label_star_2*labelStar
    elif lableNum in solution.labelNumRange_3:
        userScore+=solution.label_star_3*labelStar

    # **************proterties:*******************
    for proterty_key in propertyDict:
        proterty_value = propertyDict[proterty_key]
        if not nonelist.__contains__(proterty_value):
            userScore += solution.weightDict.get(proterty_key.encode('utf-8'))

    #**************relations:**************
    specialRelationTypes = [u'喜欢', u'不喜欢', u'女朋友', u'男朋友']
    hobbyNum = 0
    loverMark = False  # False表示没有
    for relationDict in relationDictlist:
        relationType = relationDict.get('relation')
        relationValue = relationDict.get('value')
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
                userScore += solution.weightDict.get(relationType.encode('utf-8'))

    hobbyStar = solution.weightDict.get('喜好')
    if hobbyNum in solution.hobbyNumRange_1:
        userScore += solution.hobby_star_1 * hobbyStar
    elif hobbyNum in solution.hobbyNumRange_2:
        userScore += solution.hobby_star_2 * hobbyStar
    elif hobbyNum in solution.hobbyNumRange_3:
        userScore += solution.hobby_star_3 * hobbyStar
    elif hobbyNum in solution.hobbyNumRange_4:
        userScore += solution.hobby_star_4 * hobbyStar
    elif hobbyNum in solution.hobbyNumRange_5:
        userScore += solution.hobby_star_5 * hobbyStar

    if loverMark == True:
        userScore += solution.weightDict.get('对象')

    DictTotalScore = solution.getDictTotalScore()
    return userScore / DictTotalScore * 100

def run(solution,userId,URL):
    completed = 0
    s0 = s1 =s2 = s3 = s4 =s5 =s6 = 0
    scorefile=userId+"_score"
    logfile=userId+"_log"
    writer=open(scorefile,'a')
    logwriter=open(logfile,'a')
    i=0
    for id in open(userId, 'r'):
        i += 1
        if i <= completed:
            continue
        if i % 100 == 0:
            print "current processing:",
            print i
        responseResult=postData(id.strip(),URL)
        score = getUserScore(responseResult, solution)
        writer.write("%s:%s\n" % (id.strip(),score))
        logwriter.write("%s  %s\n" % (score, responseResult))
        if score == 0.0:
            s0+=1
        elif score > 0.0 and score < 30:
            s1+=1
        elif score >= 30.0 and score < 50:
            s2 += 1
        elif score >= 50.0 and score < 70:
            s3 += 1
        elif score >= 70.0 and score < 90:
            s4 += 1
        elif score >=90 and score <100:
            s5 += 1
        else:
            s6+=1
    print "------count:-------\nscore == 0:",
    print s0
    print "score > 0.0 and score < 30:",
    print s1
    print "score >= 30.0 and score < 50:",
    print s2
    print "score >= 50.0 and score < 70:",
    print s3
    print "score >= 70.0 and score < 90:",
    print s4
    print "score >=90 and score <100:",
    print s5
    print "100:",
    print s6
