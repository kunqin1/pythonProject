import hashlib
import hmac
import json
import random
import string
import time

# 随机生成字符串重新组装成新的字符串
import requests


def make(rule, n):
    """
    :param rule: 随机数的组成规则
    :param n: 生成随机数的长度
    :return: 返回生成的随机数
    """
    # rule = string.ascii_letters + string.digits 字母加数字的格式
    ran_str = ''.join(random.sample(rule, n))
    print(ran_str)
    return ran_str


# def MakeRN():
#     """
#     :生成0-9范围内的随机数
#     :return: 生成的随机数
#     """
#     RN = random.randint(0, 9)
#     return RN
#
#
# def MakeRNumber(x, y):
#     """
#     :生成在一定范围内的随机数字
#     :param x: 开始的数字，包括
#     :param y: 结束的范围，不包括
#     :return: 生成的随机数
#     """
#     RN = random.randint(x, y)
#     return RN
#
#
# def MakeRS():
#     """
#     :从a-z里面随机产生一个字母
#     :return:
#     """
#     Str = string.ascii_lowercase
#     RS = random.choice(Str)
#     return RS
#
#
# def MakeStr():
#     """
#     # 生成规律的随机字符串
#     :return:
#     """
#     nonceStr = str(MakeRN()) + str(MakeRS()) + str(MakeRN()) + str(MakeRS()) + str(MakeRN()) + str(MakeRS()) + str(
#         MakeRN()) + str(MakeRN()) + '-' + str(
#         MakeRN()) + str(
#         MakeRN()) + str(MakeRS()) + str(MakeRN()) + '-' + str(MakeRN()) + str(MakeRN()) + str(MakeRN()) + str(
#         MakeRN()) + '-' + str(MakeRS()) + str(MakeRN()) + str(MakeRS()) + str(
#         MakeRN()) + '-' + str(MakeRN()) + str(MakeRN()) + str(MakeRS()) + str(MakeRN()) + str(MakeRN()) + str(
#         MakeRN()) + str(MakeRN()) + str(MakeRS()) + str(MakeRS()) + str(
#         MakeRN()) + str(MakeRS()) + str(MakeRS())
#     print(nonceStr)
#     return nonceStr


class InterfaceSign:

    def getStringA(self, content):
        """
        按照参数名ASCII码从小到大排序
        :param content:
        :return:
        """
        data = []
        StringA = ''
        # for key1 in content: 对性能有较大的消耗
        # 获取字典里面的值
        for key1, value in content.items():
            # 将字典转化为key=value形式
            Str = str(key1) + '=' + str(value)
            data.append(Str)
        # 将list按照key从小到大进行排序,sort默认升序
        data.sort()
        nums = 0
        # print(data)
        for i in data:
            max_nums = len(data)
            nums = nums + 1
            # 如果是最后一位就不要带上&
            # 拼接字符串
            if nums == max_nums:
                StringA += str(i)
            else:
                StringA += str(i) + '&'
        # print(StringA)
        return StringA

    # 处理生成签名和组装post请求参数
    def GetStringSignTemp(self, interfaceKey, content):
        """
        :param interfaceKey: 接口的密匙
        :param content: 接口的参数
        :return: 返回加密的参数
        """
        StringA = self.getStringA(content)
        StringSignTemp = StringA + "&" + "key=" + interfaceKey
        # print(StringSignTemp)
        interfaceKey = interfaceKey.encode('utf-8')
        StringSignTemp = StringSignTemp.encode('utf-8')
        # .hexdigest 加密后为字符串类型
        interfaceSign = hmac.new(interfaceKey, StringSignTemp, digestmod=hashlib.sha256).hexdigest().upper()
        content['sign'] = interfaceSign
        # print(content)
        # content['timestamp'] = int(time.time())
        # 将数据转化为json格式
        data = json.dumps(content, ensure_ascii=False)
        return data

    # 组装GET\PUT请求参数
    def GetURL(self, interfaceKey, content):
        data = self.GetStringSignTemp(interfaceKey, content)
        params = self.getStringA(json.loads(data))
        # print(params)
        return params


sign = InterfaceSign()
