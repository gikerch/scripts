#coding: utf-8
import time
start = time.clock()
import requests
import re
from bs4 import BeautifulSoup
import datetime
import xlwt
from xlwt import Formula
from selenium import webdriver


wb = xlwt.Workbook(encoding = 'gbk')
day = str(datetime.date.today())[2:]
ws1 = wb.add_sheet(u'京东显示器%s' %day,cell_overwrite_ok = True)
style0 = xlwt.easyxf('font:name SimSun,bold on;align:vert centre, horiz center',num_format_str='#,##0.00')
style1 = xlwt.easyxf('font:name SimSun,bold on',num_format_str='#,##0.00') 

#首行标题#
ws1.write(0, 0,u'今日排名',style0)
ws1.write(0, 1,u'品牌',style0)
ws1.write(0, 2,u'型号',style0)
ws1.write(0, 3,u'面板',style0)
ws1.write(0, 4,u'今日价格',style0)
ws1.write(0, 5,u'商品id',style0)
ws1.write(0, 6,u'链接',style0)
ws1.write(0, 7,u'品名',style0)
# ws1.write(0, 7,u'剩余可投金额',style0)
# ws1.write(0,8,u'还款方式',style0)
for t in range(0,7):
    ws1.col(t).width = 5000
ws1.col(7).width = 16000

##获取ip地址
#url_orgin = 'http://www.youdaili.net/Daili/guonei'
#content = requests.get(url_orgin)
#doc = H.document_fromstring(content.text)
#link= doc.xpath('//ul[@class="newslist_line"]/li[1]/a[1]') 
#url= link[0].get('href')

#Ip_content = requests.get(url)
#doc2 = H.document_fromstring(Ip_content.text)
#page_num= doc2.xpath('//ul[@class="pagelist"]/li[1]/a/text()')[0].encode('utf-8') 
#page_nums = re.findall(r'\d+', page_num)

#for i in range(1,2):

    #if i == 1:
        #Url = url
    #else:
        #Url = url[:-5]+'_%s.html' %i

    #html = requests.get(Url).text
    #res = re.findall(r'\d+\.\d+\.\d+\.\d+\:\d+', html)

##选取可用ip
#for i in range(len(res)):
    #t  = random.randint(1,len(res))
    #proxy_select = res[t]  
    #proxies = {       
             #"http": "http://%s"%(proxy_select),
             #"https": "http://%s"%(proxy_select),}    
    #url ='http://p.3.cn/prices/get?skuid=J_1492986'
    #try:
        #content =requests.get(url,proxies=proxies,timeout = 10) 
        #if content.status_code==200:
            #break
    #except:
        #pass

name = []
skuid = []
link = []
price = []
brand = []
model = []
version = []

# headers = {"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
#            "Accept-Encoding": "gzip, deflate, sdch",
#            "Accept-Language": "zh-CN,zh;q=0.8",
#            "Cache-Control": "max-age=0",
#            "Connection": "keep-alive",
#            # "Cookie":"_jrda=1; 3AB9D23F7A4B3C9B=QHIXKHAQB4IYWJAVYJSO2AHJTT37TCP7M327DN5LZKMTF7H4XKIMFEAP2ULKWFIJYJQUZEVOHV2ZSW4VQLDIHMYAPQ; TrackID=1QqZ14C9GyvWHoI2NUypVN2vyyP1oD218mI3PyEuFPPUWEAsA1qVlX_fLlsI1uQgPUtsIC55A_HjBgMiIQAsFQvMhwdBqJGSb6YMl4zSUDrQ; pinId=RuY2_h-xqMgyIVQ1is9ieg; ceshi3.com=5tG7U9bPccjjVQy1kjQRMNXvWSy8r2HlWnqDcjKTFz8; unpl=V2_ZzNtbRFSShR8XUVVLxkIUWJXFV5KBUYTfQoSV3IQX1cwBEJUclRCFXIURldnGFQUZAAZXEpcQxZFCHZXchBYAWcCGllyBBNNIEwHDCRSBUE3XHxcFVUWF3RaTwEoSVoAYwtBDkZUFBYhW0IAKElVVTUFR21yVEMldQl2V3odWgJiABBYRWdzEkU4dlx8Gl0NYDMTbUNnAUEpDUFTcxtfSGQCFltFUkAXcA92VUsa; CCC_SE=ADC_AlO9GA0RKLlXWNdo6NBz9MkDQ5xO%2f%2bkAD%2fNUd1JM50yZz5c%2b%2f%2f%2bpbpnl096lFY3hquvT%2f05kSDPIh5uWP6Wy%2feyDXEVpIP5z751kK28UPKBXTQ66QAQ3i6faPkiRmqaZiFb6sodQB%2fAS7%2fcAzWKneB7NkWUdebUu%2fNtn6wAe0K%2flw6XdhUPbbV4eRF1aiIZWhHlyxYGMiUKrbGSJ3cupXJVSJqeoZugGAOG7U30iiiwlH9o50Ncurwx3SAlfOMsDVx6F2iJtcDKOhc0S9%2fM5nyo1nt5tmcu48a%2f2FMBfUg98Zr4KDtfoIOU9Pana9d5v5Sk8tkH8UJF17TiAJHWHOPjREGHJBZOttfgIkcLCfZTxOd6lYWB8VUa5POb5cjRNV8WAaJBjBHGvPtdAaErR2WYlW5e5luuQVZiXweE1M6P329LcSzMOixnomgpWDXd10FzuqDeVEZ7lj0%2fPBHgwjWvBwDXG1u8GZq3wRu4IEA0f2%2fPWym2ojWvpLj63YVFmsWu7JXHU%2fsGDCNbmatgqisMBpWj41UjzYuDQw%2bz6YuRnsRk3Y5%2f7ipPS6aEX3BKF; __jdv=122270672|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_2147a1c95ed749618e1000c17c8dd864|1481373940602; ipLoc-djd=1-72-4137-0; ipLocation=%u5317%u4EAC; areaId=1; listck=7cec6238c39cadf48d251cf92a33237b; __jda=122270672.2057642346.1461226371.1481292033.1481373916.18; __jdb=122270672.10.2057642346|18.1481373916; __jdc=122270672; __jdu=2057642346",
#            "Cookie": "__jdv=122270672|direct|-|none|-|1482473808062; ipLoc-djd=1-72-4137-0; ipLocation=%u5317%u4EAC; areaId=1; listck=57668111b1988e034958c688def7d88a; __jda=122270672.1482473808057209630078.1482473808.1482473808.1482473808.1; __jdb=122270672.27.1482473808057209630078|1.1482473808; __jdc=122270672; __jdu=1482473808057209630078",
#            "Host": "list.jd.com",
#            "Upgrade-Insecure-Requests":'1',
#            "User-Agent":"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36"}

def get_cookies(url,cookies_list):
    
    dirver = webdriver.PhantomJS()
    
    # 添加cookies
    for cookie in cookies_list:
        dirver.add_cookie({k: cookie[k] for k in (
        'name', 'value', 'domain', 'path', 'expiry') if k in cookie})

    # 访问页面获取当前页面cookie
    dirver.get(url)


    new_cookies_list = dirver.get_cookies()

    cookie_dict =  {}
    for cookie in new_cookies_list:
        if cookie.has_key('name') and cookie.has_key('value'):
            cookie_dict[cookie['name']] = cookie['value']
    return cookie_dict, new_cookies_list
    
def get_page(url,cookie):

    headers ={"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
           "Connection": "keep-alive",
           "Cookie":cookie,
           "Host": "list.jd.com",
           "Referer":"https://list.jd.com/list.html?cat=670,677,688&page=6&trans=1&JL=6_0_0",
           "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36"}
    timeout = 5
    r = requests.get(url, headers=headers,timeout=timeout)
    return r.text

def deal_cookies(cookies_dict):
  #   cookie = ''
  #   for k,v in cookies_dict.items():
        # cookie += k+'='+v+';'
    cookie = 'areaId=1;ipLoc-djd=1-72-4137-0;__jdv=122270672|direct|-|none|-|1483069224412;listck=da8774e\
    d50745801d0edf9326efe3d71;__jda=122270672.14830692244021170427418.1483069224.1483069224.1483069224.1;\
    __jdc=122270672;__jdb=122270672.1.14830692244021170427418|1.1483069224;__jdu=14830692244021170427418'
    return cookie

def get_cookie_1230():
    # 获取首页cookie
    cookies1,cookies_list1 = get_cookies('https://list.jd.com/list.html?cat=670,677,688',[])
    # print cookies1,cookies_list1
    # 获取第五cookie
    cookies5,cookies_list5 = get_cookies('https://list.jd.com/list.html?cat=670,677,688&page=5&trans=1&JL=6_0_0',cookies_list1)
    # print cookies5,cookies_list5
    # 获取第6页cookie
    cookies6,cookies_list6 =  get_cookies('https://list.jd.com/list.html?cat=670,677,688&page=6&trans=1&JL=6_0_0',cookies_list5)
    # print cookies6, cookies_list6

    cookies = ''
    for k,v in cookies6.items():
        cookies += k+'='+v+';'
    cookies = cookies[:-1]
    return cookies
cookies = get_cookie_1230()

# s = requests.Session()
headers ={"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
           "Connection": "keep-alive",
           # "Cookie":"_jrda=1; 3AB9D23F7A4B3C9B=QHIXKHAQB4IYWJAVYJSO2AHJTT37TCP7M327DN5LZKMTF7H4XKIMFEAP2ULKWFIJYJQUZEVOHV2ZSW4VQLDIHMYAPQ; TrackID=1QqZ14C9GyvWHoI2NUypVN2vyyP1oD218mI3PyEuFPPUWEAsA1qVlX_fLlsI1uQgPUtsIC55A_HjBgMiIQAsFQvMhwdBqJGSb6YMl4zSUDrQ; pinId=RuY2_h-xqMgyIVQ1is9ieg; ceshi3.com=5tG7U9bPccjjVQy1kjQRMNXvWSy8r2HlWnqDcjKTFz8; unpl=V2_ZzNtbRFSShR8XUVVLxkIUWJXFV5KBUYTfQoSV3IQX1cwBEJUclRCFXIURldnGFQUZAAZXEpcQxZFCHZXchBYAWcCGllyBBNNIEwHDCRSBUE3XHxcFVUWF3RaTwEoSVoAYwtBDkZUFBYhW0IAKElVVTUFR21yVEMldQl2V3odWgJiABBYRWdzEkU4dlx8Gl0NYDMTbUNnAUEpDUFTcxtfSGQCFltFUkAXcA92VUsa; CCC_SE=ADC_AlO9GA0RKLlXWNdo6NBz9MkDQ5xO%2f%2bkAD%2fNUd1JM50yZz5c%2b%2f%2f%2bpbpnl096lFY3hquvT%2f05kSDPIh5uWP6Wy%2feyDXEVpIP5z751kK28UPKBXTQ66QAQ3i6faPkiRmqaZiFb6sodQB%2fAS7%2fcAzWKneB7NkWUdebUu%2fNtn6wAe0K%2flw6XdhUPbbV4eRF1aiIZWhHlyxYGMiUKrbGSJ3cupXJVSJqeoZugGAOG7U30iiiwlH9o50Ncurwx3SAlfOMsDVx6F2iJtcDKOhc0S9%2fM5nyo1nt5tmcu48a%2f2FMBfUg98Zr4KDtfoIOU9Pana9d5v5Sk8tkH8UJF17TiAJHWHOPjREGHJBZOttfgIkcLCfZTxOd6lYWB8VUa5POb5cjRNV8WAaJBjBHGvPtdAaErR2WYlW5e5luuQVZiXweE1M6P329LcSzMOixnomgpWDXd10FzuqDeVEZ7lj0%2fPBHgwjWvBwDXG1u8GZq3wRu4IEA0f2%2fPWym2ojWvpLj63YVFmsWu7JXHU%2fsGDCNbmatgqisMBpWj41UjzYuDQw%2bz6YuRnsRk3Y5%2f7ipPS6aEX3BKF; __jdv=122270672|baidu-pinzhuan|t_288551095_baidupinzhuan|cpc|0f3d30c8dba7459bb52f2eb5eba8ac7d_0_2147a1c95ed749618e1000c17c8dd864|1481373940602; ipLoc-djd=1-72-4137-0; ipLocation=%u5317%u4EAC; areaId=1; listck=7cec6238c39cadf48d251cf92a33237b; __jda=122270672.2057642346.1461226371.1481292033.1481373916.18; __jdb=122270672.10.2057642346|18.1481373916; __jdc=122270672; __jdu=2057642346",
           "Cookie": cookies,
           "Host": "list.jd.com",
           "Referer":"https://list.jd.com/list.html?cat=670,677,688&page=5&trans=1&JL=6_0_0",
           "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36"}

for p in range(1,21):
# for p in range(1,2):
    req = requests.get('https://list.jd.com/list.html?cat=670,677,688&page=%s&trans=1&JL=6_0_0&ms=5#J_main'%p, headers=headers)
    print req.cookies    
    soup = BeautifulSoup(req.text, "html.parser")
    items = soup.findAll(attrs={"class":"gl-item"})
    for i in range(len(items)):
        name.append(items[i].find(attrs={"class":"p-name"}).em.text.strip())
        print items[i].find(attrs={"class":"p-name"}).em.text.strip()
        id_num = items[i].a.get('href')[14:][:-5]
        print id_num
        skuid.append(id_num)
        link.append("http://item.jd.com/%s.html"%id_num)
        
        
# proxiess = [{'http': u'http://118.194.197.186:8080', 'https': u'http://118.194.197.186:8080'}]
##选取可用ip  {'http': u'http://58.253.238.242:80', 'https': u'http://58.253.238.242:80'}

# for t in range(0,len(proxiess)):
#     proxies = proxiess[t]
#     print proxies
#     priceTest = []
#     ss = time.clock()
#     for i in range(4):
#         for pp in range(0,10):
#             try:
#                 ppp = requests.get('http://p.3.cn/prices/get?older=J_'+skuid[i],proxies=proxies)
#                 if ppp.json()[0].has_key('p'):
#                     priceTest.append(ppp.json()[0]['p'])
#                     break
#             except:
#                 pass
#     sss = time.clock()
#     if len(priceTest) == 0:
#         pass
#     else:
#         if priceTest[0] == priceTest[1]:
#             pass
#         else:
#             if sss-ss<5:
#                 break
#
#
# print u'ip测试结束'
# print 'the ip:%s'% proxies
# try:
#     for i in range(len(skuid)):
#         #for i in range(1,200):  #测试用
#         for pp in range(1,100):
#             try:
#                 ppp = requests.get('http://p.3.cn/prices/get?older=J_'+skuid[i],proxies=proxies)
#                 time.sleep(1.3)
#                 if ppp.json()[0].has_key('p'):
#                     break
#             except:
#                 pass
#         price.append(ppp.json()[0]['p'])
# except:
#     for i in range(len(skuid)):
#         price.append(0)
#         print i
for i in range(len(skuid)):
    price.append(0)
    print i
    
for iname in name:
    if u"飞利浦" in iname:
        version.append(re.compile(r'PLS|IPS|TN|VA|MVA|ADS').findall(iname[12:]))
    else:
        version.append(re.compile(r'PLS|IPS|TN|VA|MVA|ADS').findall(iname))
    iname = ' '.join(iname.split())
    
    if u'） ' in iname[:20]:
        brand.append(iname.split(u'）')[0]+u'）')
        model.append(iname.split(u'）')[1].strip().split(' ')[0])
    elif u'）' in iname[:20]:
        brand.append(iname.split(u'）')[0]+u'）')
        model.append(iname.split(u'）')[1].strip().split(' ')[0])
    else:
        try:
            model.append(iname.split(' ')[1])
            brand.append(iname.split(' ')[0])          
        except:
            brand.append(iname[0:10])
            model.append('')


#'品牌'型号',参数','价格''商品id','链接',
n = 0
for m in range(len(name)):
    ws1.write(n+1,0,int(n+1),style1)
    ws1.write(n+1,1,brand[m],style1)
    ws1.write(n+1,2,model[m],style1)
    ws1.write(n+1,3,version[m],style1)
    ws1.write(n+1,4,price[m],style1)
    ws1.write(n+1,5,skuid[m],style1)
    b = '"%s"'%link[m]
    ws1.write(n+1,6,Formula('HYPERLINK(%s;"link")' %b))
    ws1.write(n+1,7,name[m],style1)
#       ws1.write(n+1,7,invest_amount[m],style1)
#       ws1.write(n+1,8,repayment[m],style1)
    n+=1

print n


wb.save(u'JD显示器数据.xls') 
#wb.save(u'D:\历史数据\JD显示器\JD显示器%s.xls'%(datetime.datetime.strftime(datetime.datetime.now(),"%y-%m-%d")))

print 'well done!'


end = time.clock()
print u'程序运行耗时:',end-start
