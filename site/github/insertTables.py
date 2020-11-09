import pymysql, sys, os, traceback
sys.path.append(os.path.dirname(os.path.dirname(__file__)) + "\github")
import githubApi

def insertUser(id, fav_repository,nick_name):
    try:
        conn = None
        if len(id) == 0 :
            raise Exception('아이디는 비어 있으면 안됩니다.')
        if len(fav_repository) == 0 :
            raise Exception('관심 레파지토리는 비어 있으면 안됩니다.')
        if len(nick_name) == 0 :
            raise Exception('별명은 비어 있으면 안됩니다.')
        conn = pymysql.connect(user='root', password='1234', db='open_source', charset='utf8')
        curs = conn.cursor()

        sql = "SELECT DATE_FORMAT(NOW(),'%Y%m%d%H%i%s');"
        curs.execute(sql)
        result = curs.fetchall()

        code = githubApi.getRepositoryInfo(fav_repository,0); #url parser를 통해 git api 주소를 가지고 온다.
        if code[0] == 404 :
            raise Exception('GITHUB API 호출할때 문제가 생겼습니다.')

        git_create_at = code[0]
        git_updated_at = code[1]
        git_api_address = code[2]

        sql = "INSERT INTO REPOSITORY (fav_repository,git_api_address,git_created_at,git_updated_at,created_at,updated_at) " \
              "VALUES (%s,%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE UPDATED_AT = %s"
        curs.execute(sql, (fav_repository, git_api_address, git_create_at, git_updated_at, result,result,result))

        sql = "INSERT INTO USER (id,fav_repository,nick_name,created_at,updated_at) VALUES (%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE UPDATED_AT = %s"
        curs.execute(sql, (id, fav_repository, nick_name, result, result, result))

        conn.commit()

    except Exception as e:
        if conn != None :
            conn.rollback()
        print('예외가 발생했습니다.', e)
        traceback.print_exc()
    finally :
        if conn != None :
            conn.close()

#insertUser('tjdgns461', 'https://github.com/realsuperman/spring-project','별이')
#insertUser('tjdgns462', 'https://github.com/realsuperman/spring-project','달이')
#insertUser('tjdgns462', 'https://github.com/realsuperman/SSU-Competition','햇님')
#insertUser('seonghun7304', 'https://github.com/realsuperman/spring-project','쿵이')
#insertUser('tjdgns463', 'https://github.com/realsuperman/SSU-Competition','콩이')
#insertUser('tjdgns464', 'https://github.com/realsuperman/spring-project','캉이')