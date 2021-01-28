from bs4 import BeautifulSoup
import sqlite3
import urllib.request
import urllib.error
import re
# url = "https://www.zhipin.com/beijing/"
# headers = {
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
#                   "(KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.50"
# }
# req = urllib.request.Request(url=url, headers=headers)
# response = urllib.request.urlopen(req)
# print(response.read().decode("utf-8"))
def main():
    baseurl = "https://www.zhipin.com/c101010100-p100101/"
    # data_list = get_data(baseurl)
    # save_path = ".\\职位信息"
# 伪装请求，目前会出现"code":37,"message":"您的访问行为异常.","zpData":
    ask_url(baseurl)
def ask_url(url):
    head = {#camouflage
        'accept': '*/*',
        'accept - encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'x-requested-with': 'XMLHttpRequest',
        # 'referer':'https://www.zhipin.com/web/geek/recommend?random=1611842001907',
        # 'cookies':'_bl_uid=3nktzemI887f9L4z71mF4dIum33z; lastCity=101010100; __zp_seo_uuid__=9a8636c4-028c-47ec-a8f8-c9324d6a8b50; __g=-; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1611639562,1611749108,1611836630,1611836634; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1611841970; wt2=TGY01o3Vgho2iYBh; __l=r=https://www.baidu.com/link?url=t9xx_VPBgykKzL8pR9Vd_OHqEmpmYV6lIb02JiUeD0jfOD9n9J-sumltGrY8r29D&wd=&eqid=f3a014b200048277000000056012accd&l=/www.zhipin.com/web/geek/recommend?random=1611842001907&s=3&g=&friend_source=0&s=3&friend_source=0; __zp_stoken__=19babaTdWAjB9dy8GY3ABeygHJ20/Vk4fAnhJfHU9ARYsIy92IF1REBVoN2pqBXA6BRxKLiAGSB19DBckBAVpOnNiGksjagdrGnAGOS8KVGxLEFlJTThFGQl+OHElCFRNA01AFzt9Rxt8BQlHeg==; __c=1611836629; __a=21756992.1598267270.1611749108.1611836629.105.14.34.34',
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.50',

    }
    request = urllib.request.Request(url=url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    print(html)
def get_data():
    data_list = [ ]
    for i in range(0,2):
        url = baseurl + "?page=2&ka=page-"+str(i)
        html = ask_url(url)
        soup = BeautifulSoup(html, "html.parse")
        for item in soup.find_all('div', class_="job-primary"):#获取职位列表
            data = []   #保存职位信息
            item = str(item)
            link = re.findall(pattern, item)[0]#获取职位列表里的单个职位
            print(item)
    return data_list
# 保存数据
# def save_data(savepath):
#     print("...")
if __name__ == "__main__":
    main()
    # init_db("movetest.db")
# # 公司名字正则
# findcompanyname = re.compile(r'')
# # 月薪正则
# findsalary = re.compile()
# # technology request
# findtechnologyrequest = re.compile()
# # 工作地点正则
# findworkposition = re.compile()
# # 描述正则
# finddescription = re.compile()
def init_db(dbpath):
    sql = '''
        create table jobtq(
        id integer primary key autoincrement,
        findcompanyname text,
        findsalary text,
        findtechnologyrequest text,
        findworkposition text,
        finddescription text,
        )
    '''
    conn = sqlite3.connect(dbpath)
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit()
    conn.close()