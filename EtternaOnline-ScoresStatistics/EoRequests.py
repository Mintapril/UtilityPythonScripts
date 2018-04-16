import re
import requests
import os
from threading import Thread
import rmodule
import time
import json

def get_user_details(n, x, save_json):
    headers = {
    'X-Requested-With': 'XMLHttpRequest',
    'Content-Length': '2947',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache'}
    while x >= 0:
        x = x - 1
        data = {'columns[0][data]': 'songname',
        'columns[0][name]': '', 
        'columns[0][searchable]': 'true',
        'columns[0][orderable]': 'true',
        'columns[0][search][value]': '',
        'columns[0][search][regex]': 'false',
        'columns[1][data]': 'user_chart_rate_rate',
        'columns[1][name]': '',
        'columns[1][searchable]': 'true',
        'columns[1][orderable]': 'true', 
        'columns[1][search][value]': '',
        'columns[1][search][regex]': 'false',
        'columns[2][data]': 'Overall',
        'columns[2][name]': '',
        'columns[2][searchable]': 'true',
        'columns[2][orderable]': 'true',
        'columns[2][search][value]': '',
        'columns[2][search][regex]': 'false',
        'columns[3][data]': 'wifescore',
        'columns[3][name]': '',
        'columns[3][searchable]': 'true',
        'columns[3][orderable]': 'true',
        'columns[3][search][value]': '',
        'columns[3][search][regex]': 'false',
        'columns[4][data]': 'datetime',
        'columns[4][name]': '',
        'columns[4][searchable]': 'true',
        'columns[4][orderable]': 'true',
        'columns[4][search][value]': '',
        'columns[4][search][regex]': 'false',
        'columns[5][data]': 'stream',
        'columns[5][name]': '',
        'columns[5][searchable]': 'true',
        'columns[5][orderable]': 'true',
        'columns[5][search][value]': '',
        'columns[5][search][regex]': 'false',
        'columns[6][data]': 'jumpstream',
        'columns[6][name]': '',
        'columns[6][searchable]': 'true',
        'columns[6][orderable]': 'true',
        'columns[6][search][value]': '',
        'columns[6][search][regex]': 'false',
        'columns[7][data]': 'handstream',
        'columns[7][name]': '',
        'columns[7][searchable]': 'true',
        'columns[7][orderable]': 'true',
        'columns[7][search][value]': '',
        'columns[7][search][regex]': 'false',
        'columns[8][data]': 'stamina',
        'columns[8][name]': '',
        'columns[8][searchable]': 'true',
        'columns[8][orderable]': 'true',
        'columns[8][search][value]': '',
        'columns[8][search][regex]': 'false',
        'columns[9][data]': 'jackspeed',
        'columns[9][name]': '',
        'columns[9][searchable]': 'true',
        'columns[9][orderable]': 'true',
        'columns[9][search][value]': '',
        'columns[9][search][regex]': 'false',
        'columns[10][data]': 'chordjack',
        'columns[10][name]': '',
        'columns[10][searchable]': 'true',
        'columns[10][orderable]': 'true',
        'columns[10][search][value]': '',
        'columns[10][search][regex]': 'false',
        'columns[11][data]': 'technical',
        'columns[11][name]': '',
        'columns[11][searchable]': 'true',
        'columns[11][orderable]': 'true',
        'columns[11][search][value]': '',
        'columns[11][search][regex]': 'false',
        'columns[12][data]': 'nocc',
        'columns[12][name]': '',
        'columns[12][searchable]': 'true',
        'columns[12][orderable]': 'true',
        'columns[12][search][value]': '',
        'columns[12][search][regex]': 'false',
        'order[0][column]': '4',
        'order[0][dir]': 'desc',
        'draw': "1",
        'start': '0',
        'length': '999999',
        'search[value]': '', 
        'search[regex]': 'false',
        'userid': n}
        n = n + 1
        url = "https://etternaonline.com/score/userScores"
        r = requests.post(url, headers=headers, data=data)
        r.close()
        r = r.json()
        get_user_details_2(r, n, save_json)

def get_user_details_2(r, user_id, save_json):
    records_total = r["recordsTotal"]
    n = 0
    if records_total == 0:
        pass
    else:
        user_details = r["data"]
        songs_scores = {}
        for i in list(range(int(records_total))):
            per_user_name = user_details[i]
            song_name_o = per_user_name["songname"]
            song_name = song_name_re.search(song_name_o)
            if song_name is None:
                continue
            song_name = song_name.group(0)
            song_key = song_name.replace('<a href="https://etternaonline.com/song/view/', "").replace('">', "")
            song_name = song_name_o.replace(song_name, "").replace("</a>", "")
            wife = per_user_name["wifescore"]
            wife = wife.strip("%")
            per_user_name = per_user_name["Overall"]
            per_user_name = per_user_name.replace('<a href="', '').replace('</a>', "")
            user_url = user_url_re.search(per_user_name)
            
            if user_url is None or wife == "0":
                n = n + 1
                continue
            user_url = user_url.group(0)
            if n == i:
                user_name, user_rating, ratings = rmodule.get_user(user_url)
            overall_rating = per_user_name.replace(user_url, "").replace('">', "")
            overall_rating = overall_rating.replace("</a>","")
            if song_name + "  view/" + song_key in songs_scores:
                if songs_scores[song_name + "  view/" + song_key][0] > overall_rating:
                    continue
            songs_scores[song_name + "  view/" + song_key] = [overall_rating, wife]
            user_songs_scores[user_name] = [user_rating, ratings, songs_scores]
        json_file = json.dumps(user_songs_scores)
        if save_json == True:
            with open(os.path.join("scores", "scores.json"), "w", encoding="utf_8") as _json:
                _json.write(json_file)
    try:
        if user_name in tmp:
            pass
        else:
            print("User '" + user_name + "' statistics completed.")
        tmp.append(user_name)
    except UnboundLocalError:
        pass


def search():
    what = input("想查询谁呢(´・ω・｀) （大小写敏感） (键入statistic进入统计歌曲模式)\n")
    if what == "statistic":
        print("---------------------------")
        statistic()
    jud = input("想查询总分还是单曲分数呢(｀・ω・´) （rate或songs） \n")
    if jud == "rate":
        try:
            print("Overall Rating: " + user_songs_scores[what][0])
            print(user_songs_scores[what][1])
        except KeyError:
            print("查无此人，请检查拼写")
    if jud == "songs":
        try:
            with open(what + "_scores.txt", "w", encoding="utf-8") as scores_:
                for song in user_songs_scores[what][2]:
                    print(song, "Wife:" + user_songs_scores[what][2][song][1] + "%", user_songs_scores[what][2][song][0])
                    scores_.write(song + "  Wife:" + user_songs_scores[what][2][song][1] + "%" + "  " + user_songs_scores[what][2][song][0] + "\n")
        except KeyError:
            print("查无此人，请检查拼写")
    search()


def statistic():
    dict_statistic = {}
    n = 1
    b = len(user_songs_scores)
    p = thread_n / len(user_songs_scores)
    for user in user_songs_scores:
        user_rating = user_songs_scores[user][0]
        for song in user_songs_scores[user][2]:
            song_rating = user_songs_scores[user][2][song][0]
            wife = float(user_songs_scores[user][2][song][1])
            if  user_rating == "Unranked":
                continue
            a = 30 - (float(song_rating) * (30 / float(user_rating))) + offset            
            if a > 0:
                if wife > 97.5:
                    if a > 10:
                        continue
                    a = a * (2 * p)
                if wife < 77:
                    continue
                a = a * (1.5 * p)
            if a < 0:
                if wife > 97.5:
                    if a < -10:
                        continue  
                    a = a * (2 * p)
                if wife < 77:
                    continue
                a = a * (1.5 * p)

            if song in dict_statistic:
                dict_statistic[song][user] = a
            else:
                dict_statistic[song] = {user:a}
        
        print("Calculating......  ", str(round(100 * (n * (1 / b)), 2)) + "%", end='\r')
        n = n + 1
    print("")
    dict_statistic_2 = {}
    dict_statistic_3 = {}
    n = 1
    b = len(dict_statistic)
    for song in dict_statistic:
        if len(dict_statistic[song]) <= min_scores: 
            n = n + 1
            print("Processing......  ", str(round(100 * (n * (1 / b)), 2)) + "%", end='\r')
            continue
        for user in dict_statistic[song]:
            if song in dict_statistic_2:
                dict_statistic_2[song][user] = dict_statistic[song][user]
            else:
                dict_statistic_2[song] = {user:dict_statistic[song][user]}
                
            dict_statistic_3[song] = round(sum(dict_statistic_2[song].values()), 7)
        print("Processing......  ", str(round(100 * (n * (1 / b)), 2)) + "%", end='\r')
        n = n + 1
    print("")

    _soeted = sorted(dict_statistic_3.items(), key = lambda dict_statistic_3 : dict_statistic_3[1])
    n = 0
 
    with open("statistic.txt", "w", encoding="utf-8") as statistic_:
        for song in _soeted:
            song = str(song)
            statistic_.write(song.strip("('").strip(")").replace("'", "") + "\n")
    print("---------------------------")
    fuck(dict_statistic_2)

def fuck(dict_statistic_2):
    what = input("可以输入歌曲名+ view/xxxxx(请查看生成的statistic.txt文件)来查询每首歌曲相对每一位玩家的难度，键入back返回(｀・ω・´) \n")
    if what == "back":
        search()
    print("---------------------------")
    try:
        b = dict_statistic_2[what]
        for bb in b:
            b[bb] = b[bb] * 13
        _soeted = sorted(b.items(), key = lambda b : b[1])
        with open(str(what).replace("/", " ") + "_scores.txt" ,"w", encoding="utf-8") as song_scores:
            for a in _soeted:
                print(a)
                song_scores.write(str(a).strip("(").strip(")") + "\n")
    except KeyError:
        print("找不到歌曲，请检查拼写")
    print("---------------------------")

    fuck(dict_statistic_2)

def run():
    global offset, thread_n, min_scores
    try:
        with open('settings.ini', "r", errors="ignore") as setting:
            for line in setting:
                if "MIN_SCORES_COUNT" in line:
                    min_scores = int(line.replace("MIN_SCORES_COUNT = ", "").strip())
                if "OFFSET" in line:
                    offset = float(line.replace("OFFSET = ", "").strip())
                if "THREAD" in line:
                    thread_n = int(line.replace("THREAD = ", "").strip())
                if "SAVE_JSON = True" in line:
                    save_json = True
                else:
                    save_json = False
            
    except FileNotFoundError:
        print("请不要删除配置文件，蟹蟹")
        print("已重置为默认值")
        with open('settings.ini', "w", encoding="utf-8") as setting:
            settings = "//每首歌排行榜最少要有的玩家数量。若玩家数量少于该值，歌曲将被忽略\nMIN_SCORES_COUNT = 8\n//分数计算的偏移值，若无问题不建议修改\nOFFSET = -2.53\n//线程数，不要修改\nTHREAD = 16\n//是否保存json文件\nSAVE_JSON = False"
            setting.write(settings)

        min_scores = 8    #######每首歌排行榜最少要有的玩家的数量
        offset = -2.53    #######分数计算偏移值，不建议修改
        thread_n = 16     ##########线程数，不要修改
        save_json = True  #####是否保存json文件
        time.sleep(1)

    userid = input("(｀・ω・´)累计注册过的人数，截至本程序完成时为2480 \n")
    input("(´・ω・｀)准备好了嘛，预计等待时间10分钟。准备好请回车")
    print("(´・ω・｀)开始统计，请稍等")
    if save_json == True:
        os.makedirs("scores", exist_ok=True)
    global user_songs_scores, all_user, tmp, song_name_re, user_url_re
    user_songs_scores = {}
    all_user = {}
    tmp = []
    song_name_re = re.compile('<a href="https://etternaonline.com/song/view/\d{1,6}">')
    user_url_re = re.compile('https://etternaonline\.com/score/view/\w{40,50}')

    userid = int(userid)
    userid_t = userid % thread_n
    if userid_t == 0:
        userid_t = (userid // thread_n)
    else:
        userid_t = (userid // thread_n) + 1
    print("loop count=" + str(userid_t))

    t1 = Thread(target=get_user_details, args=[1, userid_t, save_json])
    t2 = Thread(target=get_user_details, args=[userid_t + 1, userid_t, save_json])
    t3 = Thread(target=get_user_details, args=[(2 * userid_t) + 1, userid_t, save_json])
    t4 = Thread(target=get_user_details, args=[(3 * userid_t) + 1, userid_t, save_json])
    t5 = Thread(target=get_user_details, args=[(4 * userid_t) + 1, userid_t, save_json])
    t6 = Thread(target=get_user_details, args=[(5 * userid_t) + 1, userid_t, save_json])
    t7 = Thread(target=get_user_details, args=[(6 * userid_t) + 1, userid_t, save_json])
    t8 = Thread(target=get_user_details, args=[(7 * userid_t) + 1, userid_t, save_json])
    t9 = Thread(target=get_user_details, args=[(8 * userid_t) + 1, userid_t, save_json])
    t10 = Thread(target=get_user_details, args=[(9 * userid_t) + 1, userid_t, save_json])
    t11 = Thread(target=get_user_details, args=[(10 * userid_t) + 1, userid_t, save_json])
    t12 = Thread(target=get_user_details, args=[(11 * userid_t) + 1, userid_t, save_json])
    t13 = Thread(target=get_user_details, args=[(12 * userid_t) + 1, userid_t, save_json])
    t14 = Thread(target=get_user_details, args=[(13 * userid_t) + 1, userid_t, save_json])
    t15 = Thread(target=get_user_details, args=[(14 * userid_t) + 1, userid_t, save_json])
    t16 = Thread(target=get_user_details, args=[(15 * userid_t) + 1, userid_t, save_json])


    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t6.start()
    t7.start()
    t8.start()
    t9.start()
    t10.start()
    t11.start()
    t12.start()
    t13.start()
    t14.start()
    t15.start()
    t16.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()
    t7.join()
    t8.join()
    t9.join()
    t10.join()
    t11.join()
    t12.join()
    t13.join()
    t14.join()
    t15.join()
    t16.join()
    search()

if __name__ == '__main__':
    run()


