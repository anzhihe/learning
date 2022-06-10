class YearConverters():
    regex = '\d{4}'


    def to_python(self, value):
        '''
        这函数返回的值最终会传到视图
        :param value:
        :return:
        '''
        return int(value)

    # 用来反向解析
    def to_url(self, value):
        return str(value)
