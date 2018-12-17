import requests
from lxml import etree
import pymysql
import re

conn = pymysql.connect(host="66.42.65.73", user="root", password="zhouqian",database="test", charset="utf8")
cursor = conn.cursor()

keyWords = u'数据分析师'
shenzhen = '040000'

r = requests.get('https://search.51job.com/list/'+ shenzhen +',000000,0000,00,9,99,'+ keyWords +',2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=')
r.encoding = 'gbk'
htm = r.text
html = etree.HTML(htm)
page_num = re.search('\d+',html.xpath('//*[@id="resultList"]/div[55]/div/div/div/span[1]')[0].text,flags=0).group()


for i in range(1,int(page_num)+1):
    r = requests.get('https://search.51job.com/list/'+ shenzhen +',000000,0000,00,9,99,'+ keyWords +',2,'+ str(i) +'.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=')
    r.encoding = 'gbk'
    htm = r.text
    html = etree.HTML(htm)
    data_detailed = html.xpath('//*[@id="resultList"]/div/p/span/a/@href')
    data_job = html.xpath('//*[@id="resultList"]/div/p/span/a')
    data_company = html.xpath('//*[@id="resultList"]/div/span[1]/a')
    data_address = html.xpath('//*[@id="resultList"]/div/span[2]')
    data_salary = html.xpath('//*[@id="resultList"]/div/span[3]')
    for i in range(len(data_job)):
        print(data_job[i].text.strip() + ",", data_company[i].text.strip() + ",", data_address[i+1].text, data_salary[i+1].text)
        sql = "INSERT INTO python(detailed, job, company, address, salary)values('%s','%s','%s','%s','%s')"%(data_detailed[i], data_job[i].text.strip(), data_company[i].text.strip(), data_address[i+1].text, data_salary[i+1].text)
        cursor.execute(sql)
        conn.commit()

conn.close()
