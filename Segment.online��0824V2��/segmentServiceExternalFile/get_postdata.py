# -*- encoding:utf-8 -*-
import gensim
import numpy as np
import sys
import requests
from flask import Flask,request
app = Flask(__name__)
app.debug = True

w2vmodel = gensim.models.Word2Vec.load_word2vec_format('/home/emotibot3/workspace/Segment.online/segmentServiceExternalFile/vectors.bin.skipgram.mergenew.2.3', binary=True,unicode_errors='ignore')

@app.route('/sentence/<sentence>')
def main_run(sentence):
	result=getWordList(sentence)
	return result


if __name__ == "__main__":
	app.run(host='0.0.0.0')
	#app.run(host='192.168.2.49')

def getWordVector(word):
	if word in w2vmodel:
		return w2vmodel[word]
	return np.zeros(300)

def getPOSFromService(text):
	payload = {'src':text.decode('utf-8')}
	r = requests.get('http://192.168.1.126:8085/cuservice/rest/nlp/pos', payload)
	return r.json()

def getWordList(sentence):
	wordlist = []
	wordtaglist=[]
	vectorlist=[]
	pos = getPOSFromService(sentence)
	participles = pos['participleVectors']
	for participle in participles:
		wordlist.append(participle['word'])
		wordtaglist.append(participle['wordTag'])
	for word in wordlist:
		vectorlist.append(getWordVector(word).tolist())
	outstr=""
	reload(sys)
	sys.setdefaultencoding('utf-8')
	for i in range(0, len(wordlist)):
		outstr+=wordlist[i]
		outstr+="\t"
		outstr +=wordtaglist[i]
		outstr +="\t["
		for v in vectorlist[i]:
			outstr +=str(v)
			outstr+=","
		outstr=outstr[:-1]
		outstr +="]|"
	outstr = outstr[:-1]
	return outstr
