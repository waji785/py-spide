from bs4 import BeautifulSoup
import sqlite3
import urllib.request
import urllib.error
import re
import xlwt
def main():
    baseurl = 'https://www.liepin.com/zhaopin/?sfrom=click-pc_homepage-centre_searchbox-search_new&dqs=010&key=JAVA'
    datalist = getdata(baseurl)
    savepath = ".\\职位信息"
    print(datalist)
    # 伪装请求
def askurl(url):
    # 请求头
    head = {
        'accept': '*/*',
        'accept - encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'x-requested-with': 'XMLHttpRequest',
        'referer':'https://www.liepin.com/zhaopin/?sfrom=click-pc_homepage-centre_searchbox-search_new&dqs=010&key=JAVA',
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.50',

    }
    #构造request
    request = urllib.request.Request(url=url, headers=head)
    html = ""
    try:
    #构造response
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
def getdata(baseurl):
    data = [ ]
    for i in range(0,1):
        url = baseurl + "?page=2&ka=page-"+str(i)
        html = askurl(url)
        soup = BeautifulSoup(html, "html.parser")
        print(html)
        # 获取职位列表
        for item in soup.find_all('div', class_="job-content"):
            # 保存职位信息
            data = []
            item = str(item)
            # 添加公司名字，月薪，技能要求，工作地点，职位描述到列表
            companyname = re.findall(findcompanyname, item)[0]
            data.append(companyname)
            salary = re.findall(findsalary, item)[0]
            data.append(salary)
            workposition = re.findall(findworkposition, item)[0]
            data.append(workposition)
    return data
# 保存数据到excel
def savedata(datalist,savepath):
    print("...")
    book = xlwt.Workbook(encodeing="utf-8",style_copression=0)
    sheet = book.add_sheet('职位表单',cell_overwrite_ok=True)
    #定义列
    col = ("公司名字")
    for i in range(0,5):
        sheet.write(0,i,col[i])
    for i in range(0,):
        dta = datalist[i]
        for j in range(0,5):
            sheet.write(i+1,j,data[j])
    book.save(savepath)
if __name__ == "__main__":
    main()
    print("....")
    # init_db("movetest.db")
# 公司名字正则
findcompanyname = re.compile(r'<p class="companyy-name">(.*?)<span>')
# 月薪正则
findsalary = re.compile(r'<span class="text-warning">(.*?)<span>')
# 工作地点正则
findworkposition = re.compile(r'<span class="area">(.*?)<span>')
# 描述正则
# finddescription = re.compile()
# # def init_db(dbpath):
#     sql = '''
#         create table jobtq(
#         id integer primary key autoincrement,
#         findcompanyname text,
#         findsalary text,
#         findtechnologyrequest text,
#         findworkposition text,
#         finddescription text,
#         )
#     '''
#     conn = sqlite3.connect(dbpath)
#     cursor = conn.cursor()
#     cursor.execute(sql)
#     conn.commit()
#     conn.close()