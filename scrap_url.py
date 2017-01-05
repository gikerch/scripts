#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'acer-zhou'
"""
@version: ??
@license: Apache Licence 
@file: scrap_url.py
@time: 2016/11/16 22:34
"""

import requests
from lxml import etree
from bs4 import BeautifulSoup
# s = range(1,31)
#
# for i in s:
#
#     r = requests.get('http://202.120.82.17:8080/ldb/typeindex.jsp?typeid=%s' %i)
#     file = open('url_%s.html' % i, 'w')
#     html = r.text.encode('utf-8')
#     file.write(html)
#     file.close()

#file = open('scrap_html/url_1.html','r')
#soup = BeautifulSoup(file)
#re = soup.html.body.div.table.tbody
#print re\
file = """<html><head>

<title>电子资源导航-华东师范大学</title>

<meta content="text/html; charset=utf-8" http-equiv="Content-Type"><link rel="stylesheet" type="text/css" href="images/xserver.css">

<style type="text/css">



</style>







<script type="text/javascript" async="" src="http://www.google-analytics.com/ga.js"></script><script src="//hm.baidu.com/hm.js?d6fb4d76442df0362263e3ea01ab7b91"></script><script language="javascript">



var _hmt = _hmt || [];

(function() {

  var hm = document.createElement("script");

  hm.src = "//hm.baidu.com/hm.js?d6fb4d76442df0362263e3ea01ab7b91";

  var s = document.getElementsByTagName("script")[0];

  s.parentNode.insertBefore(hm, s);

})();







function Toggle(id) {

  var imid = 'i' + id;

  var dd = document.getElementById(id);

  var im = document.getElementById(imid);



  if (dd.style.display == 'none') {

    dd.style.display = '';

    dd.style.visibility = 'visible';

    im.src = 'images/minus.gif';

  }

  // Collapse the branch if it is visible

  else {

    dd.style.display = 'none';

    im.src = 'images/plus.gif';

  }

}





</script>



<script type="text/javascript">



  var _gaq = _gaq || [];

  _gaq.push(['_setAccount', 'UA-16360355-14']);

  _gaq.push(['_trackPageview']);



  (function() {

    var ga = document.createElement('script'); ga.type = 'text/javascript'; ga.async = true;

    ga.src = ('https:' == document.location.protocol ? 'https://ssl' : 'http://www') + '.google-analytics.com/ga.js';

    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(ga, s);

  })();





function counter(obj)

{



var ID=obj.name;

var xmlhttp;

if (window.XMLHttpRequest)

  {// code for IE7+, Firefox, Chrome, Opera, Safari

  xmlhttp=new XMLHttpRequest();

  }

else

  {// code for IE6, IE5

  xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");

  }

xmlhttp.onreadystatechange=function()

  {

  if (xmlhttp.readyState==4 &amp;&amp; xmlhttp.status==200)

    {

    document.getElementById("myDiv").innerHTML=xmlhttp.responseText;

    }

  }

xmlhttp.open("POST","counter.jsp",true);

xmlhttp.setRequestHeader("Content-type","application/x-www-form-urlencoded");

xmlhttp.send("URLID="+ID+"");

}

</script>



</head>



<body>







<div width:100%="" align="center">

<table width="100%" cellspacing="0" border="0">

  <tbody>

	<tr>

    <td>

    <div>

    <table width="100%" cellspacing="1" cellpadding="0" border="0" align="center">

      <tbody><tr scope="col" bgcolor="#4584C1">

        <td colspan="8" height="90"><div id="Layer1" style="position: absolute; width: 300px; height: 25px; z-index: 1; left: 686px; top: 7px;">

	       <table height="100%" width="100%" cellspacing="0" cellpadding="0" border="0">

	            <tbody><tr valign="middle" align="left">

				  <td><img src="images/E-phon.gif" height="15" width="15">&nbsp;</td>

	              <td width="30%"> <a href="http://www.lib.ecnu.edu.cn/help/info.php" target="_blank" class="daohang2">总咨询台</a></td>

				  <td><img src="images/E-FAQ.gif" height="15" width="15">&nbsp;</td>

	              <td width="30%"> <a href="http://202.120.82.59/kb/index.php?CategoryID=2" target="_blank" class="daohang2">常见问题</a></td>

				  <td><img src="images/E-home.gif" height="15" width="15">&nbsp;</td>

	              <td width="40%" valign="middle"> <a href="http://www.lib.ecnu.edu.cn/" target="_blank" class="daohang2">网站首页</a></td>

	            </tr>

	       	</tbody></table>

        </div>

          <div id="Layer3" background="images/news-logo.gif" style="position:absolute; width:600px; height:68px; z-index:3; left: 25px; top: 9px;">

            <table height="70" width="100%" cellspacing="0" cellpadding="0" border="0">

              <tbody><tr>

                <td><span class="biaoti2"><img src="images/logo.jpg" height="60" width="330"></span> <font face="华文行楷" size="6px" color="#FFFFFF">&nbsp;&nbsp;电子资源导航</font></td>

              </tr>

            </tbody></table>

		  </div>

		  <div id="Layer2" style="position: absolute; width: 300px; height: 32px; z-index: 2; left: 670px; top: 58px;">

			  <table height="20" width="300" cellspacing="0" cellpadding="0" border="0">

			    <tbody><tr align="center">

			      <td width="50%" background="images/button01.gif"><span><a href="http://www.lib.ecnu.edu.cn/help/off_campus.php" target="_blank" class="daohang1">校外访问说明</a></span></td>

			      <td width="50%" background="images/button01.gif"><a href="http://www.lib.ecnu.edu.cn/about/bylaw/e_rule.php" target="_blank" class="daohang1">版权公告</a></td>

			    </tr>

			  </tbody></table>

		 </div>

		</td>

      </tr>



    <tr bgcolor="#003366" align="center">

	        <td height="25" width="110" bgcolor="#003366"><span><a href="http://202.120.82.33/news/?cat=5" target="_blank" class="daohang2">试用数据库</a></span></td>

	        <td width="130"><span><a href="http://202.120.82.36/webaccess/redirect.php?url=http://ccc.calis.edu.cn" target="_blank" class="daohang2">外文期刊网</a></span></td>

	        <td width="110"><span><a href="http://202.120.82.33/info/" target="_blank" class="daohang2">数据库简介</a></span></td>

	        <td width="110"><span><a href="http://www.lib.ecnu.edu.cn/help/j_kernal.php" target="_blank" class="daohang2">核心期刊指南</a></span></td>

			<td width="130"><span><a href="http://researchpro.lib.ecnu.edu.cn/iii/mfrpro/loadSearchPage.do?searchpage=simple&amp;searchtype=simple&amp;language=chx&amp;passthrough=false&amp;accountid=ecnu&amp;accountpassword=ecnu&amp;searchterm=" target="_blank" class="daohang2">跨库检索</a></span></td>

	        <td width="110"><a href="http://www.lib.ecnu.edu.cn/help/bib_tool/noteexpress.php" target="_blank" class="daohang2">文献管理软件</a></td>

			<td width="110"><span><a href="https://docs.ecnu.edu.cn/vpn/install/index.html" target="_blank" class="daohang2">校外访问登录</a></span></td>

	        <td width="120"><span><a href="http://202.120.82.17:8080/iptest" target="_blank" class="daohang2">IP地址测试</a></span></td>

	  </tr>

</tbody></table>



</div>



     <!--========================== 主区 ================================= -->









<div align="left">

  <!--检索部分-->

</div>

<p align="left">

</p>



<div align="left">

  <table width="100%" border="0">

    <tbody>

    <tr>

	  <td scope="col" height="20" align="left">

	  <span class="searchtext"> <a href="index.jsp">数据库首页</a>/按数据库收录文献类型浏览</span>

	</td>

	</tr>

	  <tr>

		<td><hr class="default" size="1" noshade="noshade"></td>

	</tr>





      <!--按照类型排序查找-->



     <tr height="15">

        <td scope="col" height="15" align="left">

            <table width="100%" border="0">

		        <tbody><tr>





	                             <td>

						           <b><span class="stytle12"><a href="typeindex.jsp?typeid=1">

						           期刊</a></span></b>

								</td>







	                             <td>

						           <b><span class="stytle12"><a href="typeindex.jsp?typeid=2">

						           图书</a></span></b>

								</td>







	                             <td>

						           <b><span class="stytle12"><a href="typeindex.jsp?typeid=3">

						           学位论文</a></span></b>

								</td>







	                             <td>

						           <b><span class="stytle12"><a href="typeindex.jsp?typeid=4">

						           会议论文</a></span></b>

								</td>







	                             <td>

						           <b><span class="stytle12"><a href="typeindex.jsp?typeid=5">

						           报纸</a></span></b>

								</td>







	                             <td>

						           <b><span class="stytle12"><a href="typeindex.jsp?typeid=6">

						           参考工具</a></span></b>

								</td>







	                             <td>

						           <b><span class="stytle12"><a href="typeindex.jsp?typeid=7">

						           古籍</a></span></b>

								</td>







	                             <td>

						           <b><span class="stytle12"><a href="typeindex.jsp?typeid=8">

						           多媒体</a></span></b>

								</td>







	                             <td>

						           <b><span class="stytle12"><a href="typeindex.jsp?typeid=9">

						           文摘索引</a></span></b>

								</td>







	                             <td>

						           <b><span class="stytle12"><a href="typeindex.jsp?typeid=10">

						           目录索引</a></span></b>

								</td>







	                             <td>

						           <b><span class="stytle12"><a href="typeindex.jsp?typeid=11">

						           检索平台</a></span></b>

								</td>







	                             <td>

						           <b><span class="stytle12"><a href="typeindex.jsp?typeid=12">

						           商业信息</a></span></b>

								</td>



						    </tr>

						    <tr>







	                             <td>

						           <b><span class="stytle12"><a href="typeindex.jsp?typeid=13">

						           百科全书</a></span></b>

								</td>







	                             <td>

						           <b><span class="stytle12"><a href="typeindex.jsp?typeid=14">

						           报告</a></span></b>

								</td>







	                             <td>

						           <b><span class="stytle12"><a href="typeindex.jsp?typeid=15">

						           标准</a></span></b>

								</td>







	                             <td>

						           <b><span class="stytle12"><a href="typeindex.jsp?typeid=16">

						           参考资料</a></span></b>

								</td>







	                             <td>

						           <b><span class="stytle12"><a href="typeindex.jsp?typeid=17">

						           传记</a></span></b>

								</td>







	                             <td>

						           <b><span class="stytle12"><a href="typeindex.jsp?typeid=18">

						           档案</a></span></b>

								</td>







	                             <td>

						           <b><span class="stytle12"><a href="typeindex.jsp?typeid=19">

						           法律法规</a></span></b>

								</td>







	                             <td>

						           <b><span class="stytle12"><a href="typeindex.jsp?typeid=20">

						           化学反应</a></span></b>

								</td>







	                             <td>

						           <b><span class="stytle12"><a href="typeindex.jsp?typeid=21">

						           化学物质</a></span></b>

								</td>







	                             <td>

						           <b><span class="stytle12"><a href="typeindex.jsp?typeid=22">

						           科技成果</a></span></b>

								</td>







	                             <td>

						           <b><span class="stytle12"><a href="typeindex.jsp?typeid=23">

						           名录</a></span></b>

								</td>







	                             <td>

						           <b><span class="stytle12"><a href="typeindex.jsp?typeid=24">

						           年鉴</a></span></b>

								</td>



						    </tr>

						    <tr>







	                             <td>

						           <b><span class="stytle12"><a href="typeindex.jsp?typeid=25">

						           书评</a></span></b>

								</td>







	                             <td>

						           <b><span class="stytle12"><a href="typeindex.jsp?typeid=26">

						           统计汇编</a></span></b>

								</td>







	                             <td>

						           <b><span class="stytle12"><a href="typeindex.jsp?typeid=27">

						           新闻</a></span></b>

								</td>







	                             <td>

						           <b><span class="stytle12"><a href="typeindex.jsp?typeid=28">

						           学术搜索引擎</a></span></b>

								</td>







	                             <td>

						           <b><span class="stytle12"><a href="typeindex.jsp?typeid=29">

						           政府出版物</a></span></b>

								</td>







	                             <td>

						           <b><span class="stytle12"><a href="typeindex.jsp?typeid=30">

						           专利</a></span></b>

								</td>







					<td></td>

		      </tr>

           </tbody></table>

        </td>

	   </tr>





	 <tr>

		<td><hr class="default" size="1" noshade="noshade"></td>

	</tr>

  </tbody>

  </table>



</div>





<table width="100%">

	 <tbody><tr width="100%" class="searchtext">

	       <td height="15" width="50%">数据库名称</td>

	       <td height="15" width="20%">类型</td>

	       <td height="15" width="20%">分类</td>

	       <td height="15" width="10%">语种</td>

	 </tr>









     <tr>

 <td height="30">

            <table>

            <tbody>





								           <tr>

											<td>

												<span class="stytle12"><a onclick="Toggle('1012')"><img style="cursor: hand" id="i1012" src="images/plus.gif" border="0" align="bottom"></a>&nbsp;<a href="http://202.120.82.131/Dlib" name="12" onclick="return counter(this)" target="_blank">Apabi电子图书</a></span>

											</td>

								           </tr>



            </tbody>

            </table>



        </td>





        <td height="30">



         <span class="stytle12"><a href="typeindex.jsp?typeid=2">图书</a></span>



      </td>





       <td height="30">



	        <span class="stytle12"><a href="Categindex.jsp?subjectid=0">综合</a></span>



      </td>





         <td height="30">



           <span class="stytle12"><a href="alphabetindex.jsp?alph=ch">中文</a></span>



       </td>

     </tr>



     <!-- ========================== div展开=================================== -->



        <tr bgcolor="#EAEAEA">

        <td colspan="4" align="left">



		   <div id="1012" style="display:none;">



	         <table height="50" width="100%" cellspacing="0" cellpadding="0" border="0">



		           	<tbody><tr><td align="left"><span class="stytle10">|-&nbsp;别称:&nbsp;阿帕比电子图书;阿帕比数字图书;方正电子图书&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span></td></tr>



		           	<tr><td align="left"><span class="stytle10">



		           		 |-<a href="http://202.120.82.33/info/apabiebook.html" target="_blank">简介</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;





								          |- <a href="http://202.120.82.33/info/wp-content/uploads/2013/05/Apabi电子图书使用指南.pdf" target="_blank">使用指南</a> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;



						  </span></td>

		        		  <td align="right"><span class="stytle10">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;联系人:&nbsp;<a class="label" href="mailto:libmaster@library.ecnu.edu.cn">蒋萍</a>

		        		  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span></td>



		         </tr>



	         </tbody></table>

	        </div>

        </td>

      </tr>







     <tr>

 <td height="30">

            <table>

            <tbody>





								           <tr>

											<td>

												<span class="stytle12"><a onclick="Toggle('1025')"><img style="cursor: hand" id="i1025" src="images/plus.gif" border="0" align="bottom"></a>&nbsp;<a href="http://www.cadal.zju.edu.cn/IndexSearch.action" name="25" onclick="return counter(this)" target="_blank">CADAL百万册电子书</a></span>

											</td>

								           </tr>



            </tbody>

            </table>



        </td>





        <td height="30">



         <span class="stytle12"><a href="typeindex.jsp?typeid=1">期刊</a></span>



         <span class="stytle12"><a href="typeindex.jsp?typeid=2">图书</a></span>



         <span class="stytle12"><a href="typeindex.jsp?typeid=7">古籍</a></span>



      </td>





       <td height="30">



	        <span class="stytle12"><a href="Categindex.jsp?subjectid=0">综合</a></span>



      </td>





         <td height="30">



           <span class="stytle12"><a href="alphabetindex.jsp?alph=ch">中文</a></span>



       </td>

     </tr>



     <!-- ========================== div展开=================================== -->



        <tr bgcolor="#EAEAEA">

        <td colspan="4" align="left">



		   <div id="1025" style="display:none;">



	         <table height="50" width="100%" cellspacing="0" cellpadding="0" border="0">



		           	<tbody><tr><td align="left"><span class="stytle10">|-&nbsp;别称:&nbsp;中美百万册电子图书&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span></td></tr>



		           	<tr><td align="left"><span class="stytle10">



		           		 |-<a href="http://202.120.82.33/info/cadal.html" target="_blank">简介</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;





						  </span></td>

		        		  <td align="right"><span class="stytle10">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;联系人:&nbsp;<a class="label" href="mailto:libmaster@library.ecnu.edu.cn">王新霞</a>

		        		  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span></td>



		         </tr>



	         </tbody></table>

	        </div>

        </td>

      </tr>







     <tr>

 <td height="30">

            <table>

            <tbody>





								           <tr>

											<td>

												<span class="stytle12"><a onclick="Toggle('1026')"><img style="cursor: hand" id="i1026" src="images/plus.gif" border="0" align="bottom"></a>&nbsp;<a href="http://reserve.calis.edu.cn/dlib/Default2.asp?lang=g" name="26" onclick="return counter(this)" target="_blank">Calis高校教学参考书全文数据库</a></span>

											</td>

								           </tr>



            </tbody>

            </table>



        </td>





        <td height="30">



         <span class="stytle12"><a href="typeindex.jsp?typeid=2">图书</a></span>



      </td>





       <td height="30">



	        <span class="stytle12"><a href="Categindex.jsp?subjectid=0">综合</a></span>



      </td>





         <td height="30">



           <span class="stytle12"><a href="alphabetindex.jsp?alph=ch">中文</a></span>



       </td>

     </tr>



     <!-- ========================== div展开=================================== -->



        <tr bgcolor="#EAEAEA">

        <td colspan="4" align="left">



		   <div id="1026" style="display:none;">



	         <table height="50" width="100%" cellspacing="0" cellpadding="0" border="0">







		           	<tbody><tr><td align="left"><span class="stytle10">



		           		 |-<a href="http://202.120.82.33/info/calisjiaocan.html" target="_blank">简介</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;





						  </span></td>

		        		  <td align="right"><span class="stytle10">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;联系人:&nbsp;<a class="label" href="mailto:libmaster@library.ecnu.edu.cn">李硕</a>

		        		  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span></td>



		         </tr>



	         </tbody></table>

	        </div>

        </td>

      </tr>







     <tr>

 <td height="30">

            <table>

            <tbody>





								           <tr>

											<td>

												<span class="stytle12"><a onclick="Toggle('1030')"><img style="cursor: hand" id="i1030" src="images/plus.gif" border="0" align="bottom"></a>&nbsp;<a href="http://ebooks.cambridge.org" name="30" onclick="return counter(this)" target="_blank">Cambridge Books online</a></span>

											</td>

								           </tr>



            </tbody>

            </table>



        </td>





        <td height="30">



         <span class="stytle12"><a href="typeindex.jsp?typeid=2">图书</a></span>



      </td>





       <td height="30">



	        <span class="stytle12"><a href="Categindex.jsp?subjectid=0">综合</a></span>



      </td>





         <td height="30">



           <span class="stytle12"><a href="alphabetindex.jsp?alph=eg">西文</a></span>



       </td>

     </tr>



     <!-- ========================== div展开=================================== -->



        <tr bgcolor="#EAEAEA">

        <td colspan="4" align="left">



		   <div id="1030" style="display:none;">



	         <table height="50" width="100%" cellspacing="0" cellpadding="0" border="0">



		           	<tbody><tr><td align="left"><span class="stytle10">|-&nbsp;别称:&nbsp;剑桥电子图书&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span></td></tr>



		           	<tr><td align="left"><span class="stytle10">

		           	|-&nbsp;收录年限：&nbsp;1950-2009&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

		           		 |-<a href="http://202.120.82.33/info/cambridgebook.html" target="_blank">简介</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;





								          |- <a href="http://202.120.82.33/info/wp-content/uploads/2012/05/CambridgeBooksonline.pdf" target="_blank">使用指南</a> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;



						  </span></td>

		        		  <td align="right"><span class="stytle10">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;联系人:&nbsp;<a class="label" href="mailto:libmaster@library.ecnu.edu.cn">熊泽泉</a>

		        		  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span></td>



		         </tr>



	         </tbody></table>

	        </div>

        </td>

      </tr>







     <tr>

 <td height="30">

            <table>

            <tbody>





								           <tr>

											<td>

												<span class="stytle12"><a onclick="Toggle('1042')"><img style="cursor: hand" id="i1042" src="images/plus.gif" border="0" align="bottom"></a>&nbsp;<a href="http://search.ebscohost.com/login.aspx?profile=ehost&amp;defaultdb=nlebk" name="42" onclick="return counter(this)" target="_blank">eBook Collection (EBSCOhost)</a></span>

											</td>

								           </tr>



            </tbody>

            </table>



        </td>





        <td height="30">



         <span class="stytle12"><a href="typeindex.jsp?typeid=2">图书</a></span>



      </td>





       <td height="30">



	        <span class="stytle12"><a href="Categindex.jsp?subjectid=0">综合</a></span>



      </td>





         <td height="30">



           <span class="stytle12"><a href="alphabetindex.jsp?alph=eg">西文</a></span>



       </td>

     </tr>



     <!-- ========================== div展开=================================== -->



        <tr bgcolor="#EAEAEA">

        <td colspan="4" align="left">



		   <div id="1042" style="display:none;">



	         <table height="50" width="100%" cellspacing="0" cellpadding="0" border="0">



		           	<tbody><tr><td align="left"><span class="stytle10">|-&nbsp;别称:&nbsp;Netlibrary eBooks&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span></td></tr>



		           	<tr><td align="left"><span class="stytle10">

		           	|-&nbsp;收录年限：&nbsp;1975-&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

		           		 |-<a href="http://202.120.82.33/info/nelibrarybook.html" target="_blank">简介</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;





						  </span></td>

		        		  <td align="right"><span class="stytle10">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;联系人:&nbsp;<a class="label" href="mailto:libmaster@library.ecnu.edu.cn">仇玉芹</a>

		        		  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span></td>



		         </tr>



	         </tbody></table>

	        </div>

        </td>

      </tr>







     <tr>

 <td height="30">

            <table>

            <tbody>





								<tr>

								  <td>

									<table>

								     <tbody>

								      <tr>

								      <td class="std"><a onclick="Toggle('1107')"><img style="cursor: hand" id="i1107" src="images/plus.gif" border="0" align="bottom"></a>&nbsp;<font class="stytle12" color="#000000">Royal Society of Chemistry(英国皇家化学学会, RSC)</font></td>

								      </tr>



								             <tr>

								             	<td><span class="stytle10">&nbsp;&nbsp;<a href="http://pubs.rsc.org" name="107" onclick="return counter(this)" target="_blank">国际站点</a>&nbsp;</span></td>

								             </tr>





								             <tr>

								             	<td><span class="stytle10">&nbsp;&nbsp;<a href="http://rsc.calis.edu.cn" name="108" onclick="return counter(this)" target="_blank">calis镜像站点</a>&nbsp;</span></td>

								             </tr>





								     </tbody>

								  </table>

								            </td>

								           </tr>



            </tbody>

            </table>



        </td>





        <td height="30">



         <span class="stytle12"><a href="typeindex.jsp?typeid=1">期刊</a></span>



         <span class="stytle12"><a href="typeindex.jsp?typeid=2">图书</a></span>



      </td>





       <td height="30">



	        <span class="stytle12"><a href="Categindex.jsp?subjectid=0">化学</a></span>



      </td>





         <td height="30">



           <span class="stytle12"><a href="alphabetindex.jsp?alph=eg">西文</a></span>



       </td>

     </tr>



     <!-- ========================== div展开=================================== -->



        <tr bgcolor="#EAEAEA">

        <td colspan="4" align="left">



		   <div id="1107" style="display:none;">



	         <table height="50" width="100%" cellspacing="0" cellpadding="0" border="0">



		           	<tbody><tr><td align="left"><span class="stytle10">|-&nbsp;别称:&nbsp;RSC;英国皇家化学学会电子期刊&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span></td></tr>



		           	<tr><td align="left"><span class="stytle10">

		           	|-&nbsp;收录年限：&nbsp;1997-&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

		           		 |-<a href="http://202.120.82.33/info/rsc.html" target="_blank">简介</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;





								          |- <a href="http://202.120.82.33/info/wp-content/uploads/2012/05/rsc.pdf" target="_blank">使用指南</a> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;



						  </span></td>

		        		  <td align="right"><span class="stytle10">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;联系人:&nbsp;<a class="label" href="mailto:libmaster@library.ecnu.edu.cn">赵建庆</a>

		        		  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span></td>



		         </tr>



	         </tbody></table>

	        </div>

        </td>

      </tr>







     <tr>

 <td height="30">

            <table>

            <tbody>





								           <tr>

											<td>

												<span class="stytle12"><a onclick="Toggle('1120')"><img style="cursor: hand" id="i1120" src="images/plus.gif" border="0" align="bottom"></a>&nbsp;<a href="http://www.oecd-ilibrary.org" name="120" onclick="return counter(this)" target="_blank">SourceOECD</a></span>

											</td>

								           </tr>



            </tbody>

            </table>



        </td>





        <td height="30">



         <span class="stytle12"><a href="typeindex.jsp?typeid=1">期刊</a></span>



         <span class="stytle12"><a href="typeindex.jsp?typeid=2">图书</a></span>



         <span class="stytle12"><a href="typeindex.jsp?typeid=14">报告</a></span>



         <span class="stytle12"><a href="typeindex.jsp?typeid=26">统计汇编</a></span>



      </td>





       <td height="30">



	        <span class="stytle12"><a href="Categindex.jsp?subjectid=0">经济</a></span>



      </td>





         <td height="30">



           <span class="stytle12"><a href="alphabetindex.jsp?alph=eg">西文</a></span>



       </td>

     </tr>



     <!-- ========================== div展开=================================== -->



        <tr bgcolor="#EAEAEA">

        <td colspan="4" align="left">



		   <div id="1120" style="display:none;">



	         <table height="50" width="100%" cellspacing="0" cellpadding="0" border="0">



		           	<tbody><tr><td align="left"><span class="stytle10">|-&nbsp;别称:&nbsp;经济合作发展组织数据库&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span></td></tr>



		           	<tr><td align="left"><span class="stytle10">

		           	|-&nbsp;收录年限：&nbsp;1998-&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

		           		 |-<a href="http://202.120.82.33/info/soecd.html" target="_blank">简介</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;





								          |- <a href="http://202.120.82.33/info/wp-content/uploads/2012/06/SourceOECD.pdf" target="_blank">使用指南</a> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;



						  </span></td>

		        		  <td align="right"><span class="stytle10">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;联系人:&nbsp;<a class="label" href="mailto:libmaster@library.ecnu.edu.cn">杨莉</a>

		        		  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span></td>



		         </tr>



	         </tbody></table>

	        </div>

        </td>

      </tr>







     <tr>

 <td height="30">

            <table>

            <tbody>





								           <tr>

											<td>

												<span class="stytle12"><a onclick="Toggle('1124')"><img style="cursor: hand" id="i1124" src="images/plus.gif" border="0" align="bottom"></a>&nbsp;<a href="http://link.springer.com" name="245" onclick="return counter(this)" target="_blank">SpringerLink Books</a></span>

											</td>

								           </tr>



            </tbody>

            </table>



        </td>





        <td height="30">



         <span class="stytle12"><a href="typeindex.jsp?typeid=2">图书</a></span>



      </td>





       <td height="30">



	        <span class="stytle12"><a href="Categindex.jsp?subjectid=0">综合</a></span>



      </td>





         <td height="30">



           <span class="stytle12"><a href="alphabetindex.jsp?alph=eg">西文</a></span>



       </td>

     </tr>



     <!-- ========================== div展开=================================== -->



        <tr bgcolor="#EAEAEA">

        <td colspan="4" align="left">



		   <div id="1124" style="display:none;">



	         <table height="50" width="100%" cellspacing="0" cellpadding="0" border="0">



		           	<tbody><tr><td align="left"><span class="stytle10">|-&nbsp;别称:&nbsp;斯普林格电子书&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span></td></tr>



		           	<tr><td align="left"><span class="stytle10">

		           	|-&nbsp;收录年限：&nbsp;图书全文:2005-;丛书全文:1997-&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

		           		 |-<a href="http://202.120.82.33/info/springerb.html" target="_blank">简介</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;





								          |- <a href="http://202.120.82.33/info/wp-content/uploads/2012/05/SpringerLinkBook.pdf" target="_blank">使用指南</a> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;



						  </span></td>

		        		  <td align="right"><span class="stytle10">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;联系人:&nbsp;<a class="label" href="mailto:libmaster@library.ecnu.edu.cn">宋振世</a>

		        		  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span></td>



		         </tr>



	         </tbody></table>

	        </div>

        </td>

      </tr>







     <tr>

 <td height="30">

            <table>

            <tbody>





								           <tr>

											<td>

												<span class="stytle12"><a onclick="Toggle('1206')"><img style="cursor: hand" id="i1206" src="images/plus.gif" border="0" align="bottom"></a>&nbsp;<a href="http://www.bj.cxstar.cn/BOOKCD/format/release/aspx/182f8d810000800bd3.aspx?&amp;pinst=18c4c1a6004ae50bd3" name="206" onclick="return counter(this)" target="_blank">畅想之星多媒体资源</a></span>

											</td>

								           </tr>



            </tbody>

            </table>



        </td>





        <td height="30">



         <span class="stytle12"><a href="typeindex.jsp?typeid=2">图书</a></span>



         <span class="stytle12"><a href="typeindex.jsp?typeid=8">多媒体</a></span>



      </td>





       <td height="30">



	        <span class="stytle12"><a href="Categindex.jsp?subjectid=0">综合</a></span>



      </td>





         <td height="30">



           <span class="stytle12"><a href="alphabetindex.jsp?alph=ch">中文</a></span>



       </td>

     </tr>



     <!-- ========================== div展开=================================== -->



        <tr bgcolor="#EAEAEA">

        <td colspan="4" align="left">



		   <div id="1206" style="display:none;">



	         <table height="50" width="100%" cellspacing="0" cellpadding="0" border="0">



		           	<tbody><tr><td align="left"><span class="stytle10">|-&nbsp;别称:&nbsp;华东师范大学非书资源管理平台&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span></td></tr>



		           	<tr><td align="left"><span class="stytle10">



		           		 |-<a href="http://202.120.82.33/info/changxiang.html" target="_blank">简介</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;





						  </span></td>

		        		  <td align="right"><span class="stytle10">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;联系人:&nbsp;<a class="label" href="mailto:libmaster@library.ecnu.edu.cn">郑伟</a>

		        		  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span></td>



		         </tr>



	         </tbody></table>

	        </div>

        </td>

      </tr>







     <tr>

 <td height="30">

            <table>

            <tbody>





								<tr>

								  <td>

									<table>

								     <tbody>

								      <tr>

								      <td class="std"><a onclick="Toggle('1140')"><img style="cursor: hand" id="i1140" src="images/plus.gif" border="0" align="bottom"></a>&nbsp;<font class="stytle12" color="#000000">超星数字图书馆 (新平台近140万册)</font></td>

								      </tr>



								             <tr>

								             	<td><span class="stytle10">&nbsp;&nbsp;<a href="http://www.sslibrary.com/ssreader/download" name="325" onclick="return counter(this)" target="_blank">移动端下载</a>&nbsp;</span></td>

								             </tr>





								             <tr>

								             	<td><span class="stytle10">&nbsp;&nbsp;<a href="http://www.sslibrary.com" name="140" onclick="return counter(this)" target="_blank">主站</a>&nbsp;</span></td>

								             </tr>





								     </tbody>

								  </table>

								            </td>

								           </tr>



            </tbody>

            </table>



        </td>





        <td height="30">



         <span class="stytle12"><a href="typeindex.jsp?typeid=2">图书</a></span>



      </td>





       <td height="30">



	        <span class="stytle12"><a href="Categindex.jsp?subjectid=0">综合</a></span>



      </td>





         <td height="30">



           <span class="stytle12"><a href="alphabetindex.jsp?alph=ch">中文</a></span>



       </td>

     </tr>



     <!-- ========================== div展开=================================== -->



        <tr bgcolor="#EAEAEA">

        <td colspan="4" align="left">



		   <div id="1140" style="display:none;">



	         <table height="50" width="100%" cellspacing="0" cellpadding="0" border="0">







		           	<tbody><tr><td align="left"><span class="stytle10">



		           		 |-<a href="http://202.120.82.33/info/chaoxing.html" target="_blank">简介</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;





								          |- <a href="http://202.120.82.33/info/wp-content/uploads/2013/05/超星数字图书馆使用指南.pdf" target="_blank">使用指南</a> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;



						  </span></td>

		        		  <td align="right"><span class="stytle10">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;联系人:&nbsp;<a class="label" href="mailto:libmaster@library.ecnu.edu.cn">蒋萍</a>

		        		  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span></td>



		         </tr>



	         </tbody></table>

	        </div>

        </td>

      </tr>







     <tr>

 <td height="30">

            <table>

            <tbody>





								           <tr>

											<td>

												<span class="stytle12"><a onclick="Toggle('1267')"><img style="cursor: hand" id="i1267" src="images/plus.gif" border="0" align="bottom"></a>&nbsp;<a href="http://www.degruyter.com/browse?type_0=books" name="318" onclick="return counter(this)" target="_blank">德古意特出版社电子书</a></span>

											</td>

								           </tr>



            </tbody>

            </table>



        </td>





        <td height="30">



         <span class="stytle12"><a href="typeindex.jsp?typeid=2">图书</a></span>



         <span class="stytle12"><a href="typeindex.jsp?typeid=17">传记</a></span>



      </td>





       <td height="30">



	        <span class="stytle12"><a href="Categindex.jsp?subjectid=0">区域研究</a></span>



	        <span class="stytle12"><a href="Categindex.jsp?subjectid=0">综合</a></span>



      </td>





         <td height="30">



           <span class="stytle12"><a href="alphabetindex.jsp?alph=eg">西文</a></span>



       </td>

     </tr>



     <!-- ========================== div展开=================================== -->



        <tr bgcolor="#EAEAEA">

        <td colspan="4" align="left">



		   <div id="1267" style="display:none;">



	         <table height="50" width="100%" cellspacing="0" cellpadding="0" border="0">







		           	<tbody><tr><td align="left"><span class="stytle10">

		           	|-&nbsp;收录年限：&nbsp;1874-2017&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

		           		 |-<a href="http://202.120.82.33/info/德古意特出版社图书.html" target="_blank">简介</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;





						  </span></td>

		        		  <td align="right"><span class="stytle10">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;联系人:&nbsp;<a class="label" href="mailto:libmaster@library.ecnu.edu.cn">蒋萍</a>

		        		  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span></td>



		         </tr>



	         </tbody></table>

	        </div>

        </td>

      </tr>







     <tr>

 <td height="30">

            <table>

            <tbody>





								           <tr>

											<td>

												<span class="stytle12"><a onclick="Toggle('1141')"><img style="cursor: hand" id="i1141" src="images/plus.gif" border="0" align="bottom"></a>&nbsp;<a href="http://edu.duxiu.com" name="141" onclick="return counter(this)" target="_blank">读秀学术搜索</a></span>

											</td>

								           </tr>



            </tbody>

            </table>



        </td>





        <td height="30">



         <span class="stytle12"><a href="typeindex.jsp?typeid=2">图书</a></span>



         <span class="stytle12"><a href="typeindex.jsp?typeid=28">学术搜索引擎</a></span>



      </td>





       <td height="30">



	        <span class="stytle12"><a href="Categindex.jsp?subjectid=0">综合</a></span>



      </td>





         <td height="30">



           <span class="stytle12"><a href="alphabetindex.jsp?alph=ch">中文</a></span>



       </td>

     </tr>



     <!-- ========================== div展开=================================== -->



        <tr bgcolor="#EAEAEA">

        <td colspan="4" align="left">



		   <div id="1141" style="display:none;">



	         <table height="50" width="100%" cellspacing="0" cellpadding="0" border="0">







		           	<tbody><tr><td align="left"><span class="stytle10">



		           		 |-<a href="http://202.120.82.33/info/duxiu.html" target="_blank">简介</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;





								          |- <a href="http://202.120.82.33/info/wp-content/uploads/2013/05/读秀学术搜索使用指南.pdf" target="_blank">使用指南</a> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;



						  </span></td>

		        		  <td align="right"><span class="stytle10">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;联系人:&nbsp;<a class="label" href="mailto:libmaster@library.ecnu.edu.cn">蒋萍</a>

		        		  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span></td>



		         </tr>



	         </tbody></table>

	        </div>

        </td>

      </tr>







     <tr>

 <td height="30">

            <table>

            <tbody>





								           <tr>

											<td>

												<span class="stytle12"><a onclick="Toggle('1253')"><img style="cursor: hand" id="i1253" src="images/plus.gif" border="0" align="bottom"></a>&nbsp;<a href="http://www.degruyter.com/search?authorCount=5&amp;f_0=language&amp;pageSize=100&amp;publisher_0=HUP&amp;q_0=ENGL&amp;searchTitles=true&amp;sort=date" name="300" onclick="return counter(this)" target="_blank">哈佛大学出版社电子图书</a></span>

											</td>

								           </tr>



            </tbody>

            </table>



        </td>





        <td height="30">



         <span class="stytle12"><a href="typeindex.jsp?typeid=2">图书</a></span>



      </td>





       <td height="30">



	        <span class="stytle12"><a href="Categindex.jsp?subjectid=0">文科综合</a></span>



      </td>





         <td height="30">



           <span class="stytle12"><a href="alphabetindex.jsp?alph=eg">西文</a></span>



       </td>

     </tr>



     <!-- ========================== div展开=================================== -->



        <tr bgcolor="#EAEAEA">

        <td colspan="4" align="left">



		   <div id="1253" style="display:none;">



	         <table height="50" width="100%" cellspacing="0" cellpadding="0" border="0">



		           	<tbody><tr><td align="left"><span class="stytle10">|-&nbsp;别称:&nbsp;哈佛大学出版社回溯图书&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span></td></tr>



		           	<tr><td align="left"><span class="stytle10">

		           	|-&nbsp;收录年限：&nbsp;1913-2006&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;

		           		 |-<a href="http://202.120.82.33/info/哈佛大学出版社电子图书.html" target="_blank">简介</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;





						  </span></td>

		        		  <td align="right"><span class="stytle10">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;联系人:&nbsp;<a class="label" href="mailto:libmaster@library.ecnu.edu.cn">蒋萍</a>

		        		  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span></td>



		         </tr>



	         </tbody></table>

	        </div>

        </td>

      </tr>







     <tr>

 <td height="30">

            <table>

            <tbody>





								           <tr>

											<td>

												<span class="stytle12"><a onclick="Toggle('1158')"><img style="cursor: hand" id="i1158" src="images/plus.gif" border="0" align="bottom"></a>&nbsp;<a href="http://202.120.82.27:8080/CADAL/Index.action" name="158" onclick="return counter(this)" target="_blank">华东师范大学图书馆全文电子书库</a></span>

											</td>

								           </tr>



            </tbody>

            </table>



        </td>





        <td height="30">



         <span class="stytle12"><a href="typeindex.jsp?typeid=1">期刊</a></span>



         <span class="stytle12"><a href="typeindex.jsp?typeid=2">图书</a></span>



         <span class="stytle12"><a href="typeindex.jsp?typeid=7">古籍</a></span>



      </td>





       <td height="30">



	        <span class="stytle12"><a href="Categindex.jsp?subjectid=0">综合</a></span>



      </td>





         <td height="30">



           <span class="stytle12"><a href="alphabetindex.jsp?alph=ch">中文</a></span>



       </td>

     </tr>



     <!-- ========================== div展开=================================== -->



        <tr bgcolor="#EAEAEA">

        <td colspan="4" align="left">



		   <div id="1158" style="display:none;">



	         <table height="50" width="100%" cellspacing="0" cellpadding="0" border="0">



		           	<tbody><tr><td align="left"><span class="stytle10">|-&nbsp;别称:&nbsp;华东师大民国电子书刊库&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span></td></tr>



		           	<tr><td align="left"><span class="stytle10">



		           		 |-<a href="http://202.120.82.33/info/hsdmgbook.html" target="_blank">简介</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;





								          |- <a href="http://202.120.82.33/info/wp-content/uploads/2012/05/minguodianzishu.pdf" target="_blank">使用指南</a> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;



						  </span></td>

		        		  <td align="right"><span class="stytle10">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;联系人:&nbsp;<a class="label" href="mailto:libmaster@library.ecnu.edu.cn">李硕</a>

		        		  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span></td>



		         </tr>



	         </tbody></table>

	        </div>

        </td>

      </tr>







     <tr>

 <td height="30">

            <table>

            <tbody>





								           <tr>

											<td>

												<span class="stytle12"><a onclick="Toggle('1259')"><img style="cursor: hand" id="i1259" src="images/plus.gif" border="0" align="bottom"></a>&nbsp;<a href="http://hdsfdx.chineseall.cn" name="306" onclick="return counter(this)" target="_blank">书香校园互联网数字图书馆</a></span>

											</td>

								           </tr>



            </tbody>

            </table>



        </td>





        <td height="30">



         <span class="stytle12"><a href="typeindex.jsp?typeid=2">图书</a></span>



      </td>





       <td height="30">



	        <span class="stytle12"><a href="Categindex.jsp?subjectid=0">综合</a></span>



      </td>





         <td height="30">



           <span class="stytle12"><a href="alphabetindex.jsp?alph=ch">中文</a></span>



       </td>

     </tr>



     <!-- ========================== div展开=================================== -->



        <tr bgcolor="#EAEAEA">

        <td colspan="4" align="left">



		   <div id="1259" style="display:none;">



	         <table height="50" width="100%" cellspacing="0" cellpadding="0" border="0">



		           	<tbody><tr><td align="left"><span class="stytle10">|-&nbsp;别称:&nbsp;书香校园电子书&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span></td></tr>



		           	<tr><td align="left"><span class="stytle10">



		           		 |-<a href="http://202.120.82.33/info/书香校园电子书.html" target="_blank">简介</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;





						  </span></td>

		        		  <td align="right"><span class="stytle10">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;联系人:&nbsp;<a class="label" href="mailto:libmaster@library.ecnu.edu.cn">蒋萍</a>

		        		  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span></td>



		         </tr>



	         </tbody></table>

	        </div>

        </td>

      </tr>







     <tr>

 <td height="30">

            <table>

            <tbody>





								           <tr>

											<td>

												<span class="stytle12"><a onclick="Toggle('1292')"><img style="cursor: hand" id="i1292" src="images/plus.gif" border="0" align="bottom"></a>&nbsp;<a href="http://lib.jmu.edu.cn/departments2/magazine/philosophyol/index.htm" name="350" onclick="return counter(this)" target="_blank">四库全书</a></span>

											</td>

								           </tr>



            </tbody>

            </table>



        </td>





        <td height="30">



         <span class="stytle12"><a href="typeindex.jsp?typeid=2">图书</a></span>



      </td>





       <td height="30">



	        <span class="stytle12"><a href="Categindex.jsp?subjectid=0">古籍</a></span>



      </td>





         <td height="30">



           <span class="stytle12"><a href="alphabetindex.jsp?alph=ch">中文</a></span>



       </td>

     </tr>



     <!-- ========================== div展开=================================== -->



        <tr bgcolor="#EAEAEA">

        <td colspan="4" align="left">



		   <div id="1292" style="display:none;">



	         <table height="50" width="100%" cellspacing="0" cellpadding="0" border="0">







		           	<tbody><tr><td align="left"><span class="stytle10">



		           		 |-<a href="http://202.120.82.33/info/skqs.html" target="_blank">简介</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;





						  </span></td>

		        		  <td align="right"><span class="stytle10">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;联系人:&nbsp;<a class="label" href="mailto:libmaster@library.ecnu.edu.cn"></a>

		        		  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span></td>



		         </tr>



	         </tbody></table>

	        </div>

        </td>

      </tr>







     <tr>

 <td height="30">

            <table>

            <tbody>





								           <tr>

											<td>

												<span class="stytle12"><a onclick="Toggle('1216')"><img style="cursor: hand" id="i1216" src="images/plus.gif" border="0" align="bottom"></a>&nbsp;<a href="http://library.xhestore.com" name="227" onclick="return counter(this)" target="_blank">新华e店</a></span>

											</td>

								           </tr>



            </tbody>

            </table>



        </td>





        <td height="30">



         <span class="stytle12"><a href="typeindex.jsp?typeid=2">图书</a></span>



      </td>





       <td height="30">



	        <span class="stytle12"><a href="Categindex.jsp?subjectid=0">综合</a></span>



      </td>





         <td height="30">



           <span class="stytle12"><a href="alphabetindex.jsp?alph=ch">中文</a></span>



       </td>

     </tr>



     <!-- ========================== div展开=================================== -->



        <tr bgcolor="#EAEAEA">

        <td colspan="4" align="left">



		   <div id="1216" style="display:none;">



	         <table height="50" width="100%" cellspacing="0" cellpadding="0" border="0">







		           	<tbody><tr><td align="left"><span class="stytle10">



		           		 |-<a href="http://202.120.82.33/info/xinhuaedian.html" target="_blank">简介</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;





						  </span></td>

		        		  <td align="right"><span class="stytle10">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;联系人:&nbsp;<a class="label" href="mailto:libmaster@library.ecnu.edu.cn">蒋萍</a>

		        		  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span></td>



		         </tr>



	         </tbody></table>

	        </div>

        </td>

      </tr>







     <tr>

 <td height="30">

            <table>

            <tbody>





								           <tr>

											<td>

												<span class="stytle12"><a onclick="Toggle('1264')"><img style="cursor: hand" id="i1264" src="images/plus.gif" border="0" align="bottom"></a>&nbsp;<a href="http://read.ccpph.com.cn" name="314" onclick="return counter(this)" target="_blank">中国共产党思想理论资源数据库</a></span>

											</td>

								           </tr>



            </tbody>

            </table>



        </td>





        <td height="30">



         <span class="stytle12"><a href="typeindex.jsp?typeid=2">图书</a></span>



      </td>





       <td height="30">



	        <span class="stytle12"><a href="Categindex.jsp?subjectid=0">文科综合</a></span>



	        <span class="stytle12"><a href="Categindex.jsp?subjectid=0">法律/政治</a></span>



      </td>





         <td height="30">



           <span class="stytle12"><a href="alphabetindex.jsp?alph=ch">中文</a>&nbsp;<a href="alphabetindex.jsp?alph=eg">西文</a></span>



       </td>

     </tr>



     <!-- ========================== div展开=================================== -->



        <tr bgcolor="#EAEAEA">

        <td colspan="4" align="left">



		   <div id="1264" style="display:none;">



	         <table height="50" width="100%" cellspacing="0" cellpadding="0" border="0">



		           	<tbody><tr><td align="left"><span class="stytle10">|-&nbsp;别称:&nbsp;ccpph,党政图书馆,中国理论网金典数据库&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span></td></tr>



		           	<tr><td align="left"><span class="stytle10">



		           		 |-<a href="http://202.120.82.33/info/sixianglilunziyuan.html" target="_blank">简介</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;





						  </span></td>

		        		  <td align="right"><span class="stytle10">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;联系人:&nbsp;<a class="label" href="mailto:libmaster@library.ecnu.edu.cn">赵建庆</a>

		        		  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span></td>



		         </tr>



	         </tbody></table>

	        </div>

        </td>

      </tr>







     <tr>

 <td height="30">

            <table>

            <tbody>





								           <tr>

											<td>

												<span class="stytle12"><a onclick="Toggle('1189')"><img style="cursor: hand" id="i1189" src="images/plus.gif" border="0" align="bottom"></a>&nbsp;<a href="http://202.120.82.49/tpi_1/sysasp/include/index.asp" name="189" onclick="return counter(this)" target="_blank">中国年谱数据库</a></span>

											</td>

								           </tr>



            </tbody>

            </table>



        </td>





        <td height="30">



         <span class="stytle12"><a href="typeindex.jsp?typeid=2">图书</a></span>



         <span class="stytle12"><a href="typeindex.jsp?typeid=6">参考工具</a></span>



         <span class="stytle12"><a href="typeindex.jsp?typeid=8">多媒体</a></span>



      </td>





       <td height="30">



	        <span class="stytle12"><a href="Categindex.jsp?subjectid=0">文科综合</a></span>



      </td>





         <td height="30">



           <span class="stytle12"><a href="alphabetindex.jsp?alph=ch">中文</a></span>



       </td>

     </tr>



     <!-- ========================== div展开=================================== -->



        <tr bgcolor="#EAEAEA">

        <td colspan="4" align="left">



		   <div id="1189" style="display:none;">



	         <table height="50" width="100%" cellspacing="0" cellpadding="0" border="0">



		           	<tbody><tr><td align="left"><span class="stytle10">|-&nbsp;别称:&nbsp;年谱数据库;谱主图片数据库;谱主影音数据库;谱主论著数据库;谱主数据库&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </span></td></tr>



		           	<tr><td align="left"><span class="stytle10">



		           		 |-<a href="http://202.120.82.33/info/nianpu.html" target="_blank">简介</a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;





						  </span></td>

		        		  <td align="right"><span class="stytle10">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;联系人:&nbsp;<a class="label" href="mailto:libmaster@library.ecnu.edu.cn">方方</a>

		        		  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</span></td>



		         </tr>



	         </tbody></table>

	        </div>

        </td>

      </tr>







  </tbody></table>





<table>

 <tbody><tr height="100"><td></td></tr>

</tbody></table>



<p align="center"><span class="style23"><span class="style24">Copyright@ 2011&nbsp;<a href="http://www.lib.ecnu.edu.cn/" target="_blank">华东师范大学图书馆 </a>

<br> <br>



</span></span></p>

















</td></tr></tbody></table></div></body></html>"""
selector=etree.HTML(file)

titles=selector.xpath('/html/body/div/table/tbody/tr/td/table[1]/tbody/tr[2]/td[1]/table/tbody/tr/td/span/a/text()')
s = titles[0].decode('gbk')
print s.encode('utf-8')







