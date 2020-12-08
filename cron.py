import MySQLdb,threading,time,requests,json
from api.githubApi import getRepositoryInfo
from datetime import datetime, timedelta

def batch():
    print("깃 허브쪽 배치 프로그램이 돌고 있습니다.")  # 배치 프로그램이 돌고 있다는 로그남김 log
    try:
        conn = None
        conn = MySQLdb.connect(user='margarets', password='db20192808', db='margarets$repoalarm',host='margarets.mysql.pythonanywhere-services.com', charset='utf8')
        #conn = MySQLdb.connect(user='root', password='1234', db='open_source', charset='utf8')
        curs = conn.cursor()

        sql = "SELECT GIT_API_ADDRESS,FAV_REPOSITORY,GIT_UPDATED_AT FROM repository;"
        curs.execute(sql)
        result = curs.fetchall()

        sql = "SELECT DATE_FORMAT(NOW(),'%Y%m%d%H%i%s');"
        curs.execute(sql)
        time = curs.fetchall()

        for i in result:
            dataList = getRepositoryInfo(i[0], None , 1)
            if dataList[0] == 404:
                raise Exception('GITHUB API 호출할때 문제가 생겼습니다.')
            if dataList[1] != i[2]:  # dataList[1]은 깃 업데이트날, i[2]은 db상 저장된 깃 업데이트날

                sql = "UPDATE repository SET GIT_UPDATED_AT=%s,UPDATED_AT=%s WHERE FAV_REPOSITORY = %s"
                curs.execute(sql, (dataList[1], time, i[1]))

                sql = "SELECT b.id,b.nick_name,b.type,a.git_api_address,a.fav_repository,b.user_get_date FROM repository a LEFT JOIN user b ON a.fav_repository = b.fav_repository WHERE a.fav_repository=%s";
                curs.execute(sql, [i[1]])

                result2 = curs.fetchall()
                for j in result2:
                    str = j[3]
                    index = str.find('branches')
                    url = str[:index]+"commits"
                    branch = str[str.find('branches/'):]
                    branch = branch[branch.find('/'):].replace('/','')

                    if j[2] == 'kakao' :
                        print("카카오를 할 것")
                    else : # 나머지 케이스는 텔레그램
                        date = datetime.strptime(i[2], '%Y-%m-%dT%H:%M:%SZ') + timedelta(seconds=+1)
                        timestampStr = date.strftime("%Y-%m-%dT%H:%M:%SZ")
                        content = requests.get(url,headers={'Authorization':'token 6f6d00c786cd3662b25716bf6c6fb6a2084f401d'},params={'sha':branch,'since':timestampStr})
                        jsonObject = json.loads(content.content)
                        telegram(j[0],j[1],j[4],j[5],dataList[1],jsonObject,conn) # 이 부분 수정 필요
        conn.commit()
    except Exception as e:
        raise Exception('GITHUB API 호출할때 문제가 생겼습니다.')
    finally:
        if conn != None:
            conn.close()

def telegram(id,nick_name,fav_repository,user_date,updated_date,json,conn) : # 데이터 업데이트를 한다. 텔레그램의 경우 그리고 api를 쏜다.
    output_dict = None;
    curs = conn.cursor()

    if json!=[] :
        date = datetime.strptime(user_date, '%Y-%m-%dT%H:%M:%SZ') + timedelta(seconds=+0)
        timestampStr = date.strftime("%Y-%m-%dT%H:%M:%SZ")
        json = [json for json in json if json['commit']['committer']['date'] > timestampStr]


        sql = "UPDATE user SET user_get_date=%s,updated_at=(SELECT DATE_FORMAT(NOW(),'%%Y%%m%%d%%H%%i%%s')) WHERE id = %s AND type='telegram' AND fav_repository=%s"
        curs.execute(sql,(updated_date,id,fav_repository))
    print(json)
    
   # date = json[0].get("commit").get("committer").get("date")
   # name = json[0].get("commit").get("committer").get("name")
   # email = json[0].get("commit").get("committer").get("email")
   # msg = json[0].get("commit").get("message")
    #url = "https://api.telegram.org/bot${telegramBotToken}/sendMessage?chat_id=${telegramChatId}&text=${text}"
    url = "https://api.telegram.org/bot1498546920:AAFFE6PJlfZjFvWS51fvwDElA0ay6k96QEI/sendMessage?chat_id=1100956819&text=%EB%A0%88%ED%8F%AC%EC%A7%80%ED%86%A0%EB%A6%AC%EA%B0%80%20%EC%97%85%EB%8D%B0%EC%9D%B4%ED%8A%B8%EB%90%90%EC%96%B4!%0A%EC%9D%B4%EB%A6%84%20%3A%20%EB%B3%84%EB%AA%85%EB%B3%84%EB%AA%85%20(%EC%A7%84%EC%A7%9C%EC%9D%B4%EB%A6%84)%0A%EB%B8%8C%EB%9E%9C%EC%B9%98%20%3A%20%EB%B8%8C%EB%9E%9C%EC%B9%98%EC%9D%B4%EB%A6%84%0A--%EC%BB%A4%EB%B0%8B%EC%9D%B4%EB%A0%A5--%0A%EB%82%A0%EC%A7%9C%20%3A%202020-11-11T11%3A11%3A11Z%0A%EC%9D%B4%EB%A6%84%20%3A%20%ED%99%8D%EA%B8%B8%EB%8F%99%0A%EC%9D%B4%EB%A9%94%EC%9D%BC%20%3A%20min01134%40naver.com%0A%EC%BB%A4%EB%B0%8B%20%EB%A9%94%EC%84%B8%EC%A7%80%20%3A%20%EC%BB%A4%EB%B0%8B%EB%A9%94%EC%84%B8%EC%A7%80%EC%BB%A4%EB%B0%8B%0A%EC%A3%BC%EC%86%8C%20%3A%20https%3A%2F%2Fgithub.com%2Fmargarets-kim%2FRKAB_web%2Fcommit%2Ff2eba1d9660d73da4865e222a9b687fe35e0fde4"

    res = requests.get(url)

while True:    # while에 True를 지정하면 무한 루프
    batch()
    time.sleep(30)
