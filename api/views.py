import MySQLdb
#from rest_framework.views import APIView
#from rest_framework.response import Response
from . import githubApi
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json, requests

""" class UserView(APIView):
    def post(self, request):
        id = request.POST.get('id','')
        fav_repository = request.POST.get('fav_repository','')
        nick_name = request.POST.get('nick_name', '')
        try:
            conn = None
            if len(id) == 0:
                raise Exception('아이디는 비어 있으면 안됩니다.')
            if len(fav_repository) == 0:
                raise Exception('관심 레파지토리는 비어 있으면 안됩니다.')
            if len(nick_name) == 0:
                raise Exception('별명은 비어 있으면 안됩니다.')
            conn = MySQLdb.connect(user='margarets', password='db20192808', db='margarets$repoalarm',host='margarets.mysql.pythonanywhere-services.com',charset='utf8')
            curs = conn.cursor()

            sql = "SELECT DATE_FORMAT(NOW(),'%Y%m%d%H%i%s');"
            curs.execute(sql)
            result = curs.fetchall()

            code = githubApi.getRepositoryInfo(fav_repository, 0);  # url parser를 통해 git api 주소를 가지고 온다.
            if code[0] == 404:
                raise Exception('정상적이지 않은 레파지토리명 입니다')
            git_create_at = code[0]
            git_updated_at = code[1]
            git_api_address = code[2]

            sql = "INSERT INTO repository (fav_repository,git_api_address,git_created_at,git_updated_at,created_at,updated_at) " \
                  "VALUES (%s,%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE UPDATED_AT = %s"
            curs.execute(sql, (fav_repository, git_api_address, git_create_at, git_updated_at, result, result, result))

            sql = "INSERT INTO user (id,fav_repository,nick_name,created_at,updated_at) VALUES (%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE UPDATED_AT = %s,NICK_NAME=%s"
            curs.execute(sql, (id, fav_repository, nick_name, result, result, result,nick_name))

            conn.commit()
            return Response("정상적으로 api 호출 완료", status=200)
        except Exception as e:
            if conn != None:
                conn.rollback()
            return Response(str(e), status=404)
        finally:
            if conn != None:
                conn.close() """


def test(id, fav_repository, nick_name):
    try:
        conn = None
        if len(id) == 0:
            raise Exception('아이디는 비어 있으면 안됩니다.')
        if len(fav_repository) == 0:
            raise Exception('관심 레파지토리는 비어 있으면 안됩니다.')
        if len(nick_name) == 0:
            raise Exception('별명은 비어 있으면 안됩니다.')
        conn = MySQLdb.connect(user='margarets', password='db20192808', db='margarets$repoalarm',host='margarets.mysql.pythonanywhere-services.com', charset='utf8')
        #conn = MySQLdb.connect(user='root', password='@dbclfr0506', db='open_source',host='localhost', charset='utf8')
        curs = conn.cursor()

        sql = "SELECT DATE_FORMAT(NOW(),'%Y%m%d%H%i%s');"
        curs.execute(sql)
        result = curs.fetchall()

        code = githubApi.getRepositoryInfo(fav_repository, 0)  # url parser를 통해 git api 주소를 가지고 온다.
        if code[0] == 404:
            raise Exception('정상적이지 않은 레파지토리명 입니다')
        git_create_at = code[0]
        git_updated_at = code[1]
        git_api_address = code[2]

        sql = "INSERT INTO repository (fav_repository,git_api_address,git_created_at,git_updated_at,created_at,updated_at) " \
                "VALUES (%s,%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE UPDATED_AT = %s"
        curs.execute(sql, (fav_repository, git_api_address, git_create_at, git_updated_at, result, result, result))

        sql = "INSERT INTO user (id,fav_repository,nick_name,created_at,updated_at) VALUES (%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE UPDATED_AT = %s,NICK_NAME=%s"
        curs.execute(sql, (id, fav_repository, nick_name, result, result, result,nick_name))

        conn.commit()
        #return Response("정상적으로 api 호출 완료", status=200)
        print("정상적으로 api 호출 완료")
    except Exception as e:
        if conn != None:
            conn.rollback()
        #return Response(str(e), status=404)
        print(str(e))
    finally:
        if conn != None:
            conn.close()

@csrf_exempt
def barcode(request):
    answer = ((request.body).decode('utf-8'))
    return_json_str=json.loads(answer)
    return_str=return_json_str['action']['name']
    return_str_git=return_json_str['action']['detailParams']['barcode']['value']
    return_str_id=return_json_str['userRequest']['user']['properties']['plusfriendUserKey']
    return_str_alias="첫번째 레포다"
    #return_str_alias=return_json_str['action']['detailParams']['barcode']['value']

    if return_str == '바코드':
        #test(return_str_id,return_str_git['barcodeData'],return_str_alias)
        print(return_str_git['barcodeData'])
        #print(return_str_id)
        #print(return_str_alias)
        return JsonResponse({
            'version': "2.0",
            'template': {
                'outputs': [{
                    'simpleText': {
                        'text': "qr코드 전송이 완료되었습니다."
                    }
                }],
            }
        })