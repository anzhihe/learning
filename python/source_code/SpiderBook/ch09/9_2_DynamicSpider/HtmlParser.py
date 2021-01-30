#coding:utf-8
import codecs
import json
import re
from DynamicSpider.DataOutput import DataOutput
from DynamicSpider.HtmlDownloader import HtmlDownloader


class HtmlParser(object):

    def parser_url(self,page_url,response):
        pattern = re.compile(r'(http://movie.mtime.com/(\d+)/)')
        urls = pattern.findall(response)
        if urls!=None :
            # 将urls进行去重
            return list(set(urls))
        else:
            return None




    def parser_json(self,page_url,response):
        '''
        解析响应
        :param response:
        :return:
        '''
        #将=和；之间的内容提取出来
        # print page_url
        pattern = re.compile(r'=(.*?);')
        result = pattern.findall(response)[0]
        if result!=None:
            #json模块加载字符串
            value = json.loads(result)
            try:
                isRelease = value.get('value').get('isRelease')
            except Exception,e:
                print e
                return None
            if isRelease:
                if value.get('value').get('hotValue')==None:
                    return self._parser_release(page_url,value)
                else:
                    return self._parser_no_release(page_url,value,isRelease=2)
            else:
                return self._parser_no_release(page_url,value)



    def _parser_release(self,page_url,value):
        '''
        解析已经上映的影片
        var result_201611132231493282 = { "value":{"isRelease":true,"movieRating":{"MovieId":108737,"RatingFinal"
        :7.7,"RDirectorFinal":7.7,"ROtherFinal":7,"RPictureFinal":8.4,"RShowFinal":10,"RStoryFinal":7.3,"RTotalFinal"
        :10,"Usercount":4067,"AttitudeCount":4300,"UserId":0,"EnterTime":0,"JustTotal":0,"RatingCount":0,"TitleCn"
        :"","TitleEn":"","Year":"","IP":0},"movieTitle":"奇异博士","tweetId":0,"userLastComment":"","userLastCommentUrl"
        :"","releaseType":1,"boxOffice":{"Rank":1,"TotalBoxOffice":"5.66","TotalBoxOfficeUnit":"亿","TodayBoxOffice"
        :"4776.8","TodayBoxOfficeUnit":"万","ShowDays":10,"EndDate":"2016-11-13 22:00","FirstDayBoxOffice":"8146
        .21","FirstDayBoxOfficeUnit":"万"}},"error":null};var movieOverviewRatingResult=result_201611132231493282

        :param page_url:电影链接
        :param value:json数据
        :return:

        '''
        try:
            isRelease = 1
            movieRating = value.get('value').get('movieRating')
            boxOffice = value.get('value').get('boxOffice')
            movieTitle = value.get('value').get('movieTitle')

            RPictureFinal = movieRating.get('RPictureFinal')
            RStoryFinal = movieRating.get('RStoryFinal')
            RDirectorFinal = movieRating.get('RDirectorFinal')
            ROtherFinal = movieRating.get('ROtherFinal')
            RatingFinal = movieRating.get('RatingFinal')

            MovieId =  movieRating.get('MovieId')
            Usercount = movieRating.get('Usercount')
            AttitudeCount =  movieRating.get('AttitudeCount')

            TotalBoxOffice =  boxOffice.get('TotalBoxOffice')
            TotalBoxOfficeUnit =  boxOffice.get('TotalBoxOfficeUnit')
            TodayBoxOffice =  boxOffice.get('TodayBoxOffice')
            TodayBoxOfficeUnit =  boxOffice.get('TodayBoxOfficeUnit')

            ShowDays = boxOffice.get('ShowDays')
            try:
                Rank = boxOffice.get('Rank')
            except Exception,e:
                Rank=0
            #将提取其中的内容进行返回
            return (MovieId,movieTitle,RatingFinal,
                    ROtherFinal,RPictureFinal,RDirectorFinal,
                    RStoryFinal,Usercount,AttitudeCount,
                    TotalBoxOffice+TotalBoxOfficeUnit,
                    TodayBoxOffice+TodayBoxOfficeUnit,
                    Rank,ShowDays,isRelease )
        except Exception,e:
            print e,page_url,value
            return None

    def _parser_no_release(self,page_url,value,isRelease = 0):
        '''
        var result_201611141343063282 = { "value":{"isRelease":false,"movieRating":
        {"MovieId":236608,"RatingFinal":-1,"RDirectorFinal":0,"ROtherFinal":0,
        "RPictureFinal":0,"RShowFinal":0,"RStoryFinal":0,"RTotalFinal":0,
        "Usercount":5,"AttitudeCount":19,"UserId":0,"EnterTime":0,
        "JustTotal":0,"RatingCount":0,"TitleCn":"","TitleEn":"","Year":"",
        "IP":0},"movieTitle":"江南灵异录之白云桥","tweetId":0,
        "userLastComment":"","userLastCommentUrl":"","releaseType":2,
        "hotValue":{"MovieId":236608,"Ranking":53,"Changing":4,
        "YesterdayRanking":57}},"error":null};
        var movieOverviewRatingResult=result_201611141343063282;
        :param page_url:
        :param value:
        :return:
        '''
        try:
            movieRating = value.get('value').get('movieRating')
            movieTitle = value.get('value').get('movieTitle')

            RPictureFinal = movieRating.get('RPictureFinal')
            RStoryFinal = movieRating.get('RStoryFinal')
            RDirectorFinal = movieRating.get('RDirectorFinal')
            ROtherFinal = movieRating.get('ROtherFinal')
            RatingFinal = movieRating.get('RatingFinal')

            MovieId =  movieRating.get('MovieId')
            Usercount = movieRating.get('Usercount')
            AttitudeCount =  movieRating.get('AttitudeCount')
            try:
                Rank = value.get('value').get('hotValue').get('Ranking')
            except Exception,e:
                Rank = 0
            return (MovieId,movieTitle,RatingFinal,
                    ROtherFinal,RPictureFinal,RDirectorFinal,
                    RStoryFinal, Usercount,AttitudeCount,u'无',
                    u'无',Rank,0,isRelease )
        except Exception,e:
            print e,page_url,value
            return None


if __name__=='__main__':
    downloader = HtmlDownloader()
    output = DataOutput()
    content = downloader.download('http://theater.mtime.com/China_Beijing/')
    HtmlParser().parser_url('',content)
#     content = downloader.download('http://service.library.mtime.com/Movie.api?Ajax_CallBack=true&Ajax_CallBackType=Mtime.Library.Services&Ajax_CallBackMethod=GetMovieOverviewRating&Ajax_CrossDomain=1&Ajax_RequestUrl=http%3A%2F%2Fmovie.mtime.com%2F108737%2F&t=201611132231493282&Ajax_CallBackArgument0=108737')
#     # print content
#     data =  HtmlParser().parser_json(content)
#     output.store_data(data)
#     output.output_end()
# #
