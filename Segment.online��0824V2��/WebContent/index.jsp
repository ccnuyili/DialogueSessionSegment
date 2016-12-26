<%@ page language="java" contentType="text/html; charset=utf-8"
    pageEncoding="utf-8"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<title>ContextSegmentor</title>
</head>
<body>
Example:<br><br>
http://localhost:8080/Segment.online/segment.do?推荐北京的美食吧！|听说北京烤鸭不错哦|明天会不会下雨阿|明天雷阵雨，注意带伞哇！|怎么天天下雨阿!
<br><br><br><br>
input:<br><br>
&ensp;&ensp;&ensp;&ensp;推荐北京的美食吧！<br>
&ensp;&ensp;&ensp;&ensp;听说北京烤鸭不错哦<br>
&ensp;&ensp;&ensp;&ensp;明天会不会下雨阿<br>
&ensp;&ensp;&ensp;&ensp;明天雷阵雨，注意带伞哇！<br>
&ensp;&ensp;&ensp;&ensp;<b>怎么天天下雨阿!</b><br><br><br>

output:<br><br>
&ensp;&ensp;&ensp;&ensp;明天会不会下雨阿<br>
&ensp;&ensp;&ensp;&ensp;明天雷阵雨，注意带伞哇！<br>
&ensp;&ensp;&ensp;&ensp;<b>怎么天天下雨阿!</b><br><br>
<br>

</body>
</html>