from rest_framework.views import exception_handler
from rest_framework.exceptions import ValidationError




def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if isinstance(exc, ValidationError):
        response.data['code'] = response.status_code
        response.data['data'] = []
        if isinstance(response.data, dict):
            response.data['message'] = list(dict(response.data).values())[0][0]

            for key in dict(response.data).keys():

                if key not in ['code', 'data', 'message']:
                    response.data.pop(key)

        else:
            response.data['message'] = '输入有误'

        return response

    if response is not None:
        response.data.clear()
        response.data['code'] = response.status_code
        response.data['data'] = []

        if response.status_code == 404:
            try:
                response.data['message'] = response.data.pop('detail')
                response.data['message'] = "未找到"
            except KeyError:
                response.data['message'] = "未找到"

        if response.status_code == 400:

            response.data['message'] = '输入错误'

        elif response.status_code == 401:
            response.data['message'] = '未认证'

        elif response.status_code >= 500:
            response.data['message'] = "服务器错误"

        elif response.status_code == 403:
            response.data['message'] = "权限不允许"

        elif response.status_code == 405:
            response.data['message'] = '请求不允许'
        else:
            response.data['message'] = '未知错误'
    return response
