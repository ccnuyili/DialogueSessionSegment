package emotibot;

import java.io.IOException;
import java.io.PrintWriter;
import java.net.URLDecoder;
import java.time.Clock;
import java.util.ArrayList;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

/*	
 * 	main function:
 *
 *	input:
 * 		history sentences and current sentence
 *	output:
 * 		the last segment including the current sentence 
 */

public class myServlet extends HttpServlet {
	private static final long serialVersionUID = 1L;

	protected void doGet(HttpServletRequest request, HttpServletResponse response)
			throws ServletException, IOException {
		Clock clock = Clock.systemDefaultZone();
		long millis1 = clock.millis();
		response.setContentType("text/html;charset=UTF-8");
		PrintWriter out = response.getWriter();
		
		//test service status
		String url = "http://127.0.0.1:5000/sentence/test";
		String urlContentStr = getURLContent.getURLContent(url);
		if (urlContentStr.equals("")) {
			out.println("http://127.0.0.1:5000 服务异常！");
			return;
		}
		
		String query = request.getQueryString();
		if (query == null || query.equals(""))
			return;
		query = URLDecoder.decode(query, "ISO-8859-1");
		query = new String(query.getBytes("ISO-8859-1"), "utf-8");
		String[] rawSentencelist = query.split("\\|");
		ArrayList<String> sentencelist = new ArrayList<String>();
		for (String s : rawSentencelist) {
			// 去除句中的空白字符，去除只有空白字符的句子
			s = Filter.replaceBlank(s);
			if (!s.equals("")) {
				sentencelist.add(s);
			}
		}
		if (sentencelist.size() == 1) {
			// 只有当前句
			out.print(sentencelist.get(0));
			return;
		}

		double alpha = 0;
		int up_num = 3;
		double sameTopic_tr = 0.5;
		ContextSegmentor contextSegmentor = new ContextSegmentor(sentencelist);
		int contextStart = contextSegmentor.getContext(alpha, up_num, sameTopic_tr);
		
		
		while (contextStart < contextSegmentor.m_session.size()) {
			Sentence s = contextSegmentor.m_session.get(contextStart);
			out.println(s.rawSentence + "|");
			contextStart++;
		}
		
		//for test		
		System.out.println("test:");
		System.out.print("\nsentence: isNull scorelist depthlist ttag\n");		
		Sentence s = contextSegmentor.m_session.get(0);
		System.out.print(s.rawSentence);
		if (!s.wordsList.isEmpty())
			System.out.println(" notNull ");
		else 
			System.out.println(" null ");
		
		contextStart=1;
		int index = 0;		
		while (contextStart < contextSegmentor.m_session.size()) {
			s = contextSegmentor.m_session.get(contextStart);
			System.out.print(s.rawSentence);
			if (!s.wordsList.isEmpty())
				System.out.print(" notNull ");
			else 
				System.out.print(" null ");			
			System.out.print(contextSegmentor.m_scorelist[index]);
			System.out.print(" ");
			System.out.print(contextSegmentor.m_depthlist[index]);
			System.out.print(" ");
			System.out.println(contextSegmentor.m_taglist[index]);			
			index++;			
			contextStart++;
		}
		System.out.println("\nthreshold:" + contextSegmentor.m_threshold);
		long millis2 = clock.millis();
		long time = (millis2 - millis1);
		System.out.println("时间：" + time + "毫秒.");
		//end of test
	}
}