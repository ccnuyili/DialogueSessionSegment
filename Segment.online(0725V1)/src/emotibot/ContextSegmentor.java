package emotibot;

import java.util.ArrayList;

public class ContextSegmentor {
	public ArrayList<Sentence> m_session;
	public int m_contextStart;//从m_contextStart开始的句子与当前句属于同一个segment
	private double[] m_scorelist;
	private boolean[] m_taglist; // false: 表示中间穿插的部分不切, 默认设置为: true
	private double[] m_depthlist;
	private double m_threshold;
	
	ContextSegmentor(ArrayList<String> sentencelist) {
		m_session = new ArrayList<Sentence>();
		for (String str : sentencelist) {
			Sentence s = new Sentence(str);			
			m_session.add(s);
		}
		m_contextStart=0; //default
	}

	public int getContext(double param, int up_num, double sameTopic_tr) {
		//m_session contains at least 2 sentences
		setScorelist(up_num, sameTopic_tr);
		setDepthScore();
		setThreshold(param);
		setContext();
		return m_contextStart;
	}

	/*
	 * utility functions:
	 */

	/*
	 * set scorelist and taglist based on history
	 */
	private void setScorelist(int up_num, double sameTopic_tr) {
		// 至少向前看up_num句
		double[] scorelist = new double[m_session.size() - 1];
		boolean[] taglist = new boolean[m_session.size() - 1];
		for (int i = 0; i < taglist.length; i++)
			taglist[i] = true;
		int sentenno = 1; // 当前句子编号，从第二句开始向前看
		while (sentenno < m_session.size()) {
			double similarity = 0;
			double temp_similarity;
			int best_k = 1;
			for (int k = 1; k <= up_num; k++) {
				if (sentenno - k < 0)
					break;
				else
					temp_similarity = SimilarityByCos.getSentenceSimilarity(m_session.get(sentenno - k), m_session.get(sentenno));
				if (temp_similarity >= similarity) {
					similarity = temp_similarity;
					best_k = k;
				}
			}
			if (similarity >= sameTopic_tr) {
				int times = 0;
				while (times < best_k) {
					taglist[sentenno - 1 - times] = false;
					times += 1;
				}
			}
			scorelist[sentenno - 1] = similarity;
			sentenno += 1;
		}
		this.m_scorelist = scorelist;
		this.m_taglist = taglist;
	}

	/*
	 * set depth based on score
	 */
	private void setDepthScore() {
		double[] depthlist = new double[m_scorelist.length];
		for (int gap = 0; gap < m_scorelist.length; gap++) {
			double depth = scanleft(gap) + scanright(gap);
			depthlist[gap] = depth;
		}
		this.m_depthlist = depthlist;
	}

	/*
	 * set m_threshold
	 */
	private void setThreshold(double param) {
		double sum = 0;
		for (double depth : m_depthlist) {
			sum += depth;
		}
		double meanDepth = sum / m_depthlist.length;
		
		double differ = 0;
		sum = 0;
		for (double depth : m_depthlist) {
			differ = depth - meanDepth;
			sum += differ * differ;
		}
		double sigmaDepth = Math.sqrt(sum) / m_depthlist.length;
		
		m_threshold = meanDepth + param * sigmaDepth;
	}

	/*
	 * set m_contextStart
	 */
	private void setContext() {
		int gap = m_depthlist.length - 1;
		while (gap >= 0)
			if (m_depthlist[gap] > m_threshold && m_taglist[gap] == true) {
				m_contextStart=gap+1;
				break;
			} else
				gap -= 1;
	}

	/*
	 * return the depth in left
	 */
	private double scanleft(int gap) {
		double currentSimScore = m_scorelist[gap];
		double peakScore = currentSimScore;
		int leftgap = gap - 1;
		while (leftgap >= 0)
			if (m_scorelist[leftgap] > peakScore) {
				peakScore = m_scorelist[leftgap];
				leftgap -= 1;
			} else
				break;
		return peakScore - currentSimScore;
	}

	/*
	 * return the depth in right
	 */
	private double scanright(int gap) {
		double currentSimScore = m_scorelist[gap];
		double peakScore = currentSimScore;
		int rightgap = gap + 1;
		while (rightgap < m_scorelist.length)
			if (m_scorelist[rightgap] > peakScore) {
				peakScore = m_scorelist[rightgap];
				rightgap += 1;
			} else
				break;
		return peakScore - currentSimScore;
	}

}