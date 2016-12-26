package emotibot;

import java.util.*;

public class Sentence {
	protected String rawSentence; // original whole sentence
	protected ArrayList<Word> words; // words in rawSentence sentence

	Sentence(String s) {
		rawSentence = s;
		setWords();
	}

	// get all words in rawSentence
	private void setWords() {		
		String url = "http://127.0.0.1:5000/sentence/" + rawSentence;
		// String url = "http://192.168.2.49:5000/sentence/"+rawSentence;
		String urlContentStr = getURLContent.getURLContent(url);
		String[] contentArray = urlContentStr.split("\\|");
		words = new ArrayList<Word>();
		for (String word : contentArray) {
			String[] s = word.split("\t");
			if (s.length == 3 && !Filter.stopwords.contains(s[0]) && Filter.tagDict.containsKey(s[1])) {
				String rawvector[] = (s[2].replace("[", "")).replace("]", "").split(",");
				int i = 0;
				double[] vector = new double[300];
				for (String value : rawvector) {
					vector[i++] = Double.parseDouble(value);
				}
				words.add(new Word(vector));
			}
		}
	}
}
