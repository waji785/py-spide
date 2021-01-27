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
#request
    ask_url(baseurl)
def ask_url(url):
    head = {#camouflage
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.50"
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
pattern = re.compile(r'<a href="(.*?)">')
def get_data():
    data_list = [ ]
    for i in range(0,10):
        url = baseurl + str(i*25)
        html = ask_url(url)
        soup = BeautifulSoup(html, "html.parse")
        for item in soup.find_all("div", class_="item"):
            data = []
            item = str(item)
            link = re.findall(pattern, item)
            print(link)
    return data_list
# save data
# def save_data(savepath):
#     print("...")
if __name__ == "__main__":
    main()
# company name
findcompanyname = re.compile()
# monthly salary
findsalary = re.compile()
# technology request
findtechnologyrequest = re.compile()
# work position
findworkposition = re.compile()
# description
finddescription = re.compile()
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