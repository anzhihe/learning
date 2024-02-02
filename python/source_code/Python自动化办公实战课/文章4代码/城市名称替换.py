# 保存映射关系的函数,函数的主要功能是通过字典实现的
def replace_city(city_name):
    return {
        "GUANGDONG":"广东省",
        "HEBEI":"河北省",
        "HUNAN":"湖南省",
        "HANGZHOU":"杭州市"
    }[city_name]

# 根据映射关系实现批量循环
def replace_multi(my_citys, replaced_string):
    for pinyin_city in my_citys:
        replaced_string = replaced_string.replace(
            pinyin_city,replace_city(pinyin_city))
    return replaced_string
    
# 哪些城市要替换
citys = ("GUANGDONG", "HUNAN")

# 需要替换的字符串
string1 = """
GUANGDONG，简称“粤”，中华人民共和国省级行政区，省会广州。
因古地名广信之东，故名“GUANGDONG”。位于南岭以南，南海之滨，
与香港、澳门、广西、HUNAN、江西及福建接壤，与海南隔海相望。"""

string2 = replace_multi(citys, string1)
print(string2)

{"abc":123, "aaa":456}["abc"]