import MySQLdb
from rest_framework.views import APIView
from rest_framework.response import Response
from . import githubApi
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json, requests

class UserView(APIView):
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
                conn.close()

@csrf_exempt
def barcode(request):
    answer = ((request.body).decode('utf-8'))
    return_json_str=json.loads(answer)
    return_str_skill=return_json_str['action']['name']
    return_str_git=return_json_str['action']['detailParams']['barcode']['value']
    return_str_id=return_json_str['userRequest']['user']['properties']['plusfriendUserKey']
    return_str_alias="두번째레포"
    return_str_git_barcodeData=json.loads(return_str_git)


    data = {'fav_repository':return_str_git_barcodeData.get("barcodeData"),'nick_name':return_str_alias,'id':return_str_id}
    #devData(data)
    
    if return_str_skill == '바코드':
        return JsonResponse({
            'version': "2.0",
            'template': {
                'outputs': [{
                    'simpleText': {
                        'text': f"[{return_str_alias}] 등록 완료!"
                    }
                }],
            }
        })
def devData(data):
    print(1)
    res=requests.post('http://margarets.pythonanywhere.com/api/', data=data)
    print(2)
    print(res.status_code)

class GetInfo (APIView) : 
    def get (self, request) :
        fav_repository = request.get.get('fav_repository', '')

        branch_lists = []

        index = fav_repository.find('github')
        url = fav_repository[index:]
        index = url.find("/")
        url_repos = "https://api.github.com/repos"+url[index:]
        url_branches = "https://api.github.com/repos"+url[index:]+"/branches"

        content_repos = requests.get(url_repos, headers={'Authorization': 'token 6f6d00c786cd3662b25716bf6c6fb6a2084f401d'})
        jsonObject_repos = json.loads(content_repos.content)

        avatar_url = jsonObject_repos.get("owner").get("avatar_url")
        name = jsonObject_repos.get("name")
        created_at = jsonObject_repos.get("created_at")
        updated_at = jsonObject_repos.get("updated_at")
        stargazers_count = jsonObject_repos.get("stargazers_count")
        forks = jsonObject_repos.get("forks")

        content_branches = requests.get(url_branches, headers={'Authorization': 'token 6f6d00c786cd3662b25716bf6c6fb6a2084f401d'})
        jsonObject_branches = json.loads(content_branches.content)
        json_size = len(jsonObject_branches)

        for i in range(1, int(json_size)+1):
            branch_lists.append(jsonObject_branches[i-1].get("name"))

        return Response({
            "avatar_url" : avatar_url, 
            "name" : name, 
            "created_at" : created_at, 
            "updated_at" : updated_at, 
            "stargazers_count" : stargazers_count, 
            "forks" : forks,
            "branch_lists" : branch_lists
            }, status = 200)        
