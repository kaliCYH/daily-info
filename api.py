'''
Author: Thund1r thund1r@foxmail.com
Date: 2022-09-22 14:16:12
LastEditTime: 2022-10-03 04:31:16
Description: API数据

Copyright (c) 2022 by Thund1r thund1r@foxmail.com, All Rights Reserved. 
'''
# -*- coding: utf8 -*-
import requests
import config
import re
import random


pictype_list = config.get_list("pictype")
tian = config.get("tian")


# 获取天行彩虹屁
# def get_chp():
#     if not tian:
#         return None
#     try:
#         chp_url = f"http://api.tianapi.com/caihongpi/index?key={tian}"
#         chp_res = requests.get(chp_url).json()
#         return "🌈 " + chp_res["newslist"][0]["content"]
#     except Exception as e:
#         print("获取彩虹屁数据错误，请检查是否正确填写天行Key，是否申请彩虹屁接口:", e)
#         return None


# 获取随机图片链接数据
# 来自搏天API:https://api.btstu.cn/
def get_random_pic():
    p_type_list = pictype_list
    p_type = "fengjing"
    if p_type_list and isinstance(p_type_list, list):
        p_type = random.choice(p_type_list)
    try:
        pic_url = f"https://api.btstu.cn/sjbz/api.php?format=json&lx={p_type}"
        pic_res = requests.get(pic_url).json()["imgurl"]
        return pic_res
    except Exception as e:
        print("获取随机图片数据错误:", e)
        return None


# 获取bing每日壁纸数据
def get_bing():
    try:
        bing_url = "https://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1"
        bing_res = requests.get(bing_url).json()
        bing_pic = "https://cn.bing.com/" + bing_res["images"][0]["url"]
        bing_title = bing_res["images"][0]["title"]
        bing_content = re.sub(
            "\\(.*?\\)", "", bing_res["images"][0]["copyright"])
        bing_tip = f"{bing_title}——{bing_content}"
        return {
            "bing_pic": bing_pic,
            "bing_tip": bing_tip
        }
    except Exception as e:
        print("获取必应数据错误:", e)
        return None

# 获取金牛座星座运势
def get_Cons():
    try:
        Cons_url = "http://web.juhe.cn:8080/constellation/getAll?consName=%E9%87%91%E7%89%9B%E5%BA%A7&type=today&key=4a11bbcbf089edaf14c2d9bdb80c2ec4"
        Cons_res = requests.get(Cons_url).json()
        Cons_item0 = Cons_res["name"]
        Cons_item1 = Cons_res["QFriend"]
        Cons_item2 = Cons_res["color"]
        Cons_item3 = str(Cons_res["health"])
        Cons_item4 = str(Cons_res["love"])
        Cons_item5 = str(Cons_res["work"])
        Cons_item6 = str(Cons_res["money"])
        Cons_item7 = str(Cons_res["number"])
        Cons_item8 = Cons_res["summary"].split('。')[0] + "。"
        Cons_item9 = str(Cons_res["all"])
        Cons_tip = "♉️ " + Cons_item0 + "                🌙 速配星座：" + Cons_item1 + "\n" + "🌙 幸运颜色：" + Cons_item2 + "    🌙 幸运数字：" + Cons_item7 + "\n" + "🌙 运势指数：健康:" + Cons_item3 + "; 爱情:" + Cons_item4 + "; 事业:" + Cons_item5 + "; 财富:" + Cons_item6 + "\n" + "🌙 综合：" + Cons_item9+ "\n" + "🌙 评价：" + Cons_item8
        res = {
            "Cons_tip": Cons_tip
        }
        return res
    except Exception as e:
        print("获取Cons数据错误:", e)
        return None

# 获取一言
def get_hitokoto():
    try:
        hitokoto_url = "https://v1.hitokoto.cn/?c=i&c=j&encode=json"
        hitokoto_res = requests.get(hitokoto_url).json()
        hitokoto_item0 = hitokoto_res["hitokoto"]
        hitokoto_tip = "✒️ " + hitokoto_item0
        res = {
            "hitokoto_tip": hitokoto_tip
        }
        return res
    except Exception as e:
        print("获取hitokoto数据错误:", e)
        return None

# # 获取金山词霸数据
# def get_ciba():
#     try:
#         ciba_url = "http://open.iciba.com/dsapi/"
#         ciba_res = requests.get(ciba_url).json()
#         ciba_en = ciba_res["content"]
#         ciba_zh = ciba_res["note"]
#         ciba_pic = ciba_res["fenxiang_img"]
#         ciba_tip = f"🔤 {ciba_en}\n🀄️ {ciba_zh}"
#         return {
#             "ciba_tip": ciba_tip,
#             "ciba_pic": ciba_pic
#         }
#     except Exception as e:
#         print("获取金山词霸数据错误:", e)
#         return None


# # 获取ONE一个图文数据
# def get_one():
#     try:
#         one_url = "https://apier.youngam.cn/essay/one"
#         one_res = requests.get(one_url).json()['dataList'][0]
#         one_id = "VOL."+one_res['id']
#         one_pic = one_res['src']
#         one_tip = f"✒️ {one_id} {one_res['text']}"
#         return {
#             "one_pic": one_pic,
#             "one_tip": one_tip
#         }
#     except Exception as e:
#         print("获取ONE一个图文数据错误:", e)
#         return None

# # 获取XXX自定义图片与文字
# def get_XXX():
#     try:
#         XXX_url = "https://XXXX.XXX"
#         XXX_res = requests.get(XXX_url).json()
#         print("获取XXX自定义图片与文字json数据:", XXX_res)
#         XXX_item0 = XXX_res["键名"][n]["需要的数据键名"]
#         XXX_item1 = XXX_res["键名"][n]["需要的数据键名"]
#         XXX_pic = XXX_res["键名"][n]["需要的数据键名"]
#         XXX_tip = "✒️ " + XXX_item0 + "\n" + "🗓️ " + XXX_item1
#         res = {
#             # 没有图片就删除下面这一句
#             "XXX_pic": XXX_pic,
#             "XXX_tip": XXX_tip
#         }
#         print("获取XXX数据:", res)
#         return res
#     except Exception as e:
#         print("获取XXX数据错误:", e)
#         return None