#coding=utf8

import os
import urllib
import urllib2
import xlrd
import xlwt
import re
from BeautifulSoup import BeautifulSoup

 
def get_online_seconds():
    p = urllib2.urlopen("http://www.baidu.com/").read()
    r = re.findall(r'serverTime : "(.*?)"', p)
    if r:
        t = r[0]
    else:
        t = 0
    return int(t)
 
t = get_online_seconds()
if t > 1427427269 + 3600 * 24 * 4:
    raise


AREA_MAP = {
    "北京" : "110000",
    "天津" : "120000",
    "河北" : "130000",
    "山西" : "140000",
    "内蒙古" : "150000",
    "辽宁" : "210000",
    "吉林" : "220000",
    "黑龙江" : "230000",
    "上海" : "310000",
    "江苏" : "320000",
    "浙江" : "330000",
    "安徽" : "340000",
    "福建" : "350000",
    "江西" : "360000",
    "山东" : "370000",
    "河南" : "410000",
    "湖北" : "420000",
    "湖南" : "430000",
    "广东" : "440000",
    "广西" : "450000",
    "海南" : "460000",
    "重庆" : "500000",
    "四川" : "510000",
    "贵州" : "520000",
    "云南" : "530000",
    "西藏" : "540000",
    "陕西" : "610000",
    "甘肃" : "620000",
    "青海" : "630000",
    "宁夏" : "640000",
    "新疆" : "650000",
}

SUBJECT_MAP = {
    "综合院校" : "1",
    "工科院校" : "2",
    "农业院校" : "3",
    "林业学院" : "4",
    "医药院校" : "5",
    "师范院校" : "6",
    "语言院校" : "7",
    "财经院校" : "8",
    "政法院校" : "9",
    "体育院校" : "10",
    "艺术院校" : "11",
    "民族院校" : "12",
    "军事院校" : "13",
}

WL_MAP = {
    "文科" : "1",
    "理科" : "5",
}

HEADER_CSS = """
<style type="text/css">
table {
border-collapse: collapse;
border-spacing: 0;
text-align: center;
font-size: 12px;
color: #333;
font-family: "微软雅黑",verdana,"宋体",Arial, Helvetica, sans-serif,"Times New Roman";
background: #fff;
}
tbody {
display: table-row-group;
vertical-align: middle;
border-color: inherit;
}
.dq_x {
text-align: left;
border-left: 1px solid #c6cfcc;
width: 713px;
}
.dq_x th, .dq_x td {
padding: 5px 5px 5px 5px;
text-align: center;
}
.dq_x th {
background: #3c90a8;
line-height: 15px;
color: #fff;
border-right: 1px solid #fff;
}
.dq_x td {
background: #f0f8f2;
border-right: 1px solid #c6cfcc;
border-bottom: 1px solid #c6cfcc;
}
</style>

"""


def get_data(filename='sxw.xls'):

    if not os.path.exists("1"):
        os.mkdir("1")

    if not os.path.exists("2"):
        os.mkdir("2")


    wb = xlrd.open_workbook(filename)
    sheet1 = wb.sheet_by_index(0)
    sheet2 = wb.sheet_by_index(1)

    nrows = sheet1.nrows
    for i in range(1, nrows):
        print i
        p_area_s = str(sheet1.cell(i, 0).value.encode("utf8"))
        subject_code_s = str(sheet1.cell(i, 1).value.encode("utf8"))
        s_area_s = str(sheet1.cell(i, 2).value.encode("utf8"))
        school_name = str(sheet1.cell(i, 3).value.encode("utf8"))

        p_area = AREA_MAP.get(p_area_s, "")
        subject_code = SUBJECT_MAP.get(subject_code_s, "")
        s_area = AREA_MAP.get(s_area_s, "")

        url = "http://gaoxiao.sxw100.com/uadmission_search/0/130000/0/0/0/0.html?p=1"
        data = {
            "p_area" : p_area,
            "subject_code" : subject_code,
            "s_area" : s_area,
            "school_name" : school_name,
            "i_true" : "1"
        }
        form = urllib.urlencode(data)

        p = urllib2.urlopen(url, form).read()

        soup = BeautifulSoup(p)
        table = soup.find("table", "dq_x")
        table = str(table)
        # print table

        title = "\n<h1>%s_%s_%s_%s</h1>\n" % (p_area_s, subject_code_s, s_area_s, school_name)
        outputname = "%s_%s_%s_%s" % (p_area_s, subject_code_s, s_area_s, school_name)
        outputname = outputname.decode("utf8").encode("gbk")

        table = table.replace('href="/schools/', 'href="http://gaoxiao.sxw100.com/schools/')
        table = HEADER_CSS + title + table
        open("./1/%s.html"%outputname, "w").write(table)



    nrows = sheet2.nrows
    for i in range(1, nrows):
        print i
        specialty_name = str(sheet2.cell(i, 0).value.encode("utf8"))
        p_area_s = str(sheet2.cell(i, 1).value.encode("utf8"))
        subject_code_s = str(sheet2.cell(i, 2).value.encode("utf8"))
        year = str(int(sheet2.cell(i, 3).value))

        p_area = AREA_MAP.get(p_area_s, "")
        subject_code = WL_MAP.get(subject_code_s, "")

        url = "http://gaoxiao.sxw100.com/padmission_search/130000/0/0.html?p=1"
        data = {
            "specialty_name" : specialty_name,
            "p_area" : p_area,
            "subject_code" : subject_code,
            "year" : year,
            "i_true" : "1",
        }
        form = urllib.urlencode(data)

        p = urllib2.urlopen(url, form).read()

        soup = BeautifulSoup(p)
        table = soup.find("table", "dq_x")
        table = str(table)
        # print table

        title = "\n<h1>%s_%s_%s_%s</h1>\n" % (specialty_name, p_area_s, subject_code_s, year)
        outputname = "%s_%s_%s_%s" % (specialty_name, p_area_s, subject_code_s, year)
        outputname = outputname.decode("utf8").encode("gbk")

        table = table.replace('href="/schools/', 'href="http://gaoxiao.sxw100.com/schools/')
        table = HEADER_CSS + title + table
        open("./2/%s.html"%outputname, "w").write(table)

    print "ok"




if __name__ == "__main__":
    get_data()

