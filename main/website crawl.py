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