#coding=utf-8
__author__ = 'L'

import Spider_getAllCity
import spider_AQIHistory
import spider_getAQI

import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

if __name__ == '__main__':

    FileName = 'cityurl.txt'
    # if not os.path.exists(SiteFileName):  # 无关平台。 创建区域文件夹
    # os.mkdir(SiteFileName)

    citylist = Spider_getAllCity.get_CityUrl(FileName)  #  得到该区域记录的城市与相应地址。

    for i in citylist:
        city_name = i[0]
        city_url = i[1]
        print "wating...  " + city_url + '\n'    # 加 \n 是一个好西瓜。

        file = open('url.txt', 'a')
        mlist = spider_AQIHistory.getPerMonthURL(city_url)  #  输入 城市分页面的，得到该城市每个月份的文件名与URL
        for j in mlist:
            filename = j[0] + '.txt'
            historyurl = j[1]
            file.write(filename + "  " + historyurl + '\n')
            print 'saving ...  ' + str(filename) + '... \n'     # 编码方式。
            spider_getAQI.save_FomartAQI(str(filename), historyurl)  #  这个加了str的方式在windows下错误，在linux正确，去掉在windows正确，在linux不正确。
            # print "爬虫充电中...."
        file.close()


        # file.write(monthlist)
