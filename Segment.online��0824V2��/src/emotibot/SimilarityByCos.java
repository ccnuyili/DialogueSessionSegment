package emotibot;

public class SimilarityByCos {

	public static double getVectorSimilarity(double[] vector1, double[] vector2) {
		if (vector1 == null || vector2 == null || vector1.length != vector2.length)
			System.exit(-1);
		double vector1Modulo = 0;// 向量1的模
		double vector2Modulo = 0;// 向量2的模
		double vectorProduct = 0; // 向量积

		for (int i = 0; i < vector1.length; i++) {
			vector1Modulo += vector1[i] * vector1[i];
			vector2Modulo += vector2[i] * vector2[i];
			vectorProduct += vector1[i] * vector2[i];
		}
		vector1Modulo = Math.sqrt(vector1Modulo);
		vector2Modulo = Math.sqrt(vector2Modulo);
		return (vectorProduct / (vector1Modulo * vector2Modulo));
	}

	public static double getSentenceSimilarity(Sentence s1, Sentence s2) {
		/* ave{max} */
		if (s1 != null && s1.wordsList.size() != 0 && s2 != null && s2.wordsList.size() != 0) {
			double finalsimilarity = 0;
			Sentence temp_s1 = s1;
			Sentence temp_s2 = s2;
			if (s1.wordsList.size() > s2.wordsList.size()) {
				temp_s1 = s2;
				temp_s2 = s1;
			}
			for (Word word1 : temp_s1.wordsList) {
				double[] vector1 = word1.vector;
				double maxsimilarity = 0;
				double cur_similarity = 0;
				for (Word word2 : temp_s2.wordsList) {
					double[] vector2 = word2.vector;
					cur_similarity = SimilarityByCos.getVectorSimilarity(vector1, vector2);
					if (cur_similarity > maxsimilarity) {
						maxsimilarity = cur_similarity;
					}
				}
				finalsimilarity += maxsimilarity;
			}
			finalsimilarity /= temp_s1.wordsList.size();
			return finalsimilarity;
		} else
			return 0;
	}
}
