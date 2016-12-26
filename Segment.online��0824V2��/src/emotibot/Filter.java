package emotibot;

import java.io.BufferedReader;
import java.io.File;
import java.io.FileInputStream;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.HashSet;
import java.util.Map;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Filter {
	final static String externalPath = "/home/emotibot3/workspace/Segment.online/segmentServiceExternalFile/";
	//final static String externalPath = "./externalFile/";
	protected static HashSet<String> stopwords;
	protected static Map<String, String> tagDict;

	static {
		setStopWords(externalPath + "20160519-stoplist.txt");
		setTagDict(externalPath + "tagDict_01.txt");
	}

	public static void setStopWords(String stopWordsfile) {
		stopwords = new HashSet<String>();
		try {
			String encoding = "utf8";
			File file = new File(stopWordsfile);
			if (file.isFile() && file.exists()) {
				InputStreamReader read = new InputStreamReader(new FileInputStream(file), encoding);// 考虑到编码格式
				BufferedReader bufferedReader = new BufferedReader(read);
				String lineTxt = null;
				while ((lineTxt = bufferedReader.readLine()) != null) {
					stopwords.add(lineTxt.trim());
				}
				read.close();
			} else {
				System.out.println("找不到指定的文件");
			}
		} catch (Exception e) {
			System.out.println("读取文件内容出错");
			e.printStackTrace();
		}
	}

	public static void setTagDict(String tagDictfile) {
		tagDict = new HashMap<String, String>();
		try {
			String encoding = "utf8";
			File file = new File(tagDictfile);
			if (file.isFile() && file.exists()) {
				InputStreamReader read = new InputStreamReader(new FileInputStream(file), encoding);// 考虑到编码格式
				BufferedReader bufferedReader = new BufferedReader(read);
				String lineTxt = null;
				while ((lineTxt = bufferedReader.readLine()) != null) {
					String[] wordtag = lineTxt.trim().split("\t");
					if (wordtag.length == 3) {
						if (wordtag[2].equals("1")) {
							tagDict.put(wordtag[0], wordtag[1]);
						}
					}
				}
				read.close();
			} else {
				System.out.println("找不到指定的文件");
			}
		} catch (Exception e) {
			System.out.println("读取文件内容出错");
			e.printStackTrace();
		}
	}

	public static String replaceBlank(String str) {
		String dest = "";
		if (str != null) {
			Pattern p = Pattern.compile("\\s*|\t|\r|\n");
			Matcher m = p.matcher(str);
			dest = m.replaceAll("");
		}
		return dest;
	}
}
