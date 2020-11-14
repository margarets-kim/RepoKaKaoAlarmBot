import MySQLdb
from api.githubApi import getRepositoryInfo

def batch():
    print("깃 허브쪽 배치 프로그램이 돌고 있습니다.")  # 배치 프로그램이 돌고 있다는 로그남김 log
    try:
        conn = None
        conn = MySQLdb.connect(user='margarets', password='db20192808', db='margarets$repoalarm', charset='utf8')
        curs = conn.cursor()

        sql = "SELECT GIT_API_ADDRESS,FAV_REPOSITORY,GIT_UPDATED_AT FROM REPOSITORY;"
        curs.execute(sql)
        result = curs.fetchall()

        sql = "SELECT DATE_FORMAT(NOW(),'%Y%m%d%H%i%s');"
        curs.execute(sql)
        time = curs.fetchall()

        for i in result:
            dataList = getRepositoryInfo(i[0], 1)
            if dataList[0] == 404:
                raise Exception('GITHUB API 호출할때 문제가 생겼습니다.')
            if dataList[1] != i[2]:  # dataList[1]은 깃 업데이트날, i[2]은 db상 저장된 깃 업데이트날
                sql = "UPDATE REPOSITORY SET GIT_UPDATED_AT=%s,UPDATED_AT=%s WHERE FAV_REPOSITORY = %s"
                curs.execute(sql, (dataList[1], time, i[1]))

                sql = "SELECT b.id,b.nick_name FROM repository a LEFT JOIN user b ON a.fav_repository = b.fav_repository WHERE a.fav_repository=%s";
                curs.execute(sql, [i[1]])

                result = curs.fetchall()
                for j in result:
                    print(j[0], j[1])

        conn.commit()
    except Exception as e:
        raise Exception('GITHUB API 호출할때 문제가 생겼습니다.')
    finally:
        if conn != None:
            conn.close()