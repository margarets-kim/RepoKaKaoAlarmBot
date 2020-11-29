import MySQLdb
from rest_framework.views import APIView
from rest_framework.response import Response
from . import githubApi
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json, requests
from datetime import datetime, timedelta

class UserView(APIView):
    def post(self, request):
        id = request.POST.get('id','')
        fav_repository = request.POST.get('fav_repository','')
        nick_name = request.POST.get('nick_name', '')
        type = request.POST.get('type', '')
        branch = request.POST.get('branch', '')
        try:
            conn = None
            if len(id) == 0:
                raise Exception('아이디는 비어 있으면 안됩니다.')
            if len(fav_repository) == 0:
                raise Exception('관심 레파지토리는 비어 있으면 안됩니다.')
            if len(nick_name) == 0:
                raise Exception('별명은 비어 있으면 안됩니다.')
            if len(type) == 0:
                raise Exception('타입은 비어 있으면 안됩니다.')
            if len(branch) == 0:
                raise Exception('브랜치명은 비어 있으면 안됩니다.')
            conn = MySQLdb.connect(user='margarets', password='db20192808', db='margarets$repoalarm',host='margarets.mysql.pythonanywhere-services.com',charset='utf8')
            #conn = MySQLdb.connect(user='root', password='1234', db='open_source', charset='utf8')
            curs = conn.cursor()

            sql = "SELECT DATE_FORMAT(NOW(),'%Y%m%d%H%i%s');"
            curs.execute(sql)
            result = curs.fetchall()

            code = githubApi.getRepositoryInfo(fav_repository, branch ,0);  # url parser를 통해 git api 주소를 가지고 온다.
            if code[0] == 404:
                raise Exception('정상적이지 않은 레파지토리명 입니다')
            git_create_at = code[0]
            git_updated_at = code[1]
            git_api_address = code[2]
            fav_repository = fav_repository+"/branches/"+branch
            sql = "INSERT INTO repository (fav_repository,git_api_address,git_created_at,git_updated_at,created_at,updated_at) " \
                  "VALUES (%s,%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE UPDATED_AT = %s"
            curs.execute(sql, (fav_repository, git_api_address, git_create_at, git_updated_at, result, result, result))

            sql = "INSERT INTO user (id,fav_repository,nick_name,type,created_at,updated_at) VALUES (%s,%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE UPDATED_AT = %s,NICK_NAME=%s,TYPE=%s"
            curs.execute(sql, (id, fav_repository, nick_name, type, result, result, result,nick_name,type))

            conn.commit()
            return Response("정상적으로 api 호출 완료", status=200)
        except Exception as e:
            if conn != None:
                conn.rollback()
            return Response(str(e), status=404)
        finally:
            if conn != None:
                conn.close()

    def get(self,request):
        id = request.GET.get('id','')
        fav_repository = request.GET.get('fav_repository','')
        nick_name = request.GET.get('nick_name', '')
        type = request.GET.get('type', '')
        branch = request.GET.get('branch', '')

        try:
            if len(id) == 0:
                raise Exception('아이디는 비어 있으면 안됩니다.')
            if len(fav_repository) == 0:
                raise Exception('관심 레파지토리는 비어 있으면 안됩니다.')
            if len(nick_name) == 0:
                raise Exception('별명은 비어 있으면 안됩니다.')
            if len(type) == 0:
                raise Exception('타입은 비어 있으면 안됩니다.')
            if len(branch) == 0:
                raise Exception('브랜치명은 비어 있으면 안됩니다.')
            json = batch(id,fav_repository,nick_name,type,branch)
            return Response(json, status=200)
        except Exception as e:
            return Response("error", status=404)

def batch(id,fav_repository,nick_name,type,branch):
    try:
        conn = None
        fav_repository = fav_repository + "/branches/" + branch
        conn = MySQLdb.connect(user='margarets', password='db20192808', db='margarets$repoalarm',host='margarets.mysql.pythonanywhere-services.com', charset='utf8')
        #conn = MySQLdb.connect(user='root', password='1234', db='open_source', charset='utf8')
        curs = conn.cursor()
        sql = "SELECT a.git_api_address,a.fav_repository,a.git_updated_at FROM repository a inner join user b on a.fav_repository = b.fav_repository WHERE b.id=%s AND b.type=%s AND b.fav_repository=%s";
        curs.execute(sql, (id,type,fav_repository))
        result = curs.fetchall()

        sql = "SELECT DATE_FORMAT(NOW(),'%Y%m%d%H%i%s');"
        curs.execute(sql)
        time = curs.fetchall()

        for i in result:
            dataList = githubApi.getRepositoryInfo(i[0], None , 1)
            if dataList[0] == 404:
                raise Exception('GITHUB API 호출할때 문제가 생겼습니다.')
            sql = "SELECT b.id,b.nick_name,b.type,a.git_api_address,a.fav_repository FROM repository a inner join user b on a.fav_repository = b.fav_repository WHERE b.id=%s AND b.type=%s AND b.fav_repository=%s";
            curs.execute(sql, (id,type,fav_repository))
            result = curs.fetchall()
            for j in result:
                str = j[3]
                index = str.find('branches')
                url = str[:index]+"commits"
                branch = str[str.find('branches/'):]
                branch = branch[branch.find('/'):].replace('/','')

                date = datetime.strptime(i[2], '%Y-%m-%dT%H:%M:%SZ') + timedelta(seconds=+1)
                timestampStr = date.strftime("%Y-%m-%dT%H:%M:%SZ")
                content = requests.get(url,headers={'Authorization':'token 6f6d00c786cd3662b25716bf6c6fb6a2084f401d'},params={'sha':branch,'since':timestampStr})
                jsonObject = json.loads(content.content)
                return jsonObject
                #telegram(j[0],j[1],j[4],jsonObject) # 이 부분 수정 필요
    except Exception as e:
        print(e)
        raise Exception('GITHUB API 호출할때 문제가 생겼습니다.')
    finally:
        if conn != None:
            conn.close()

class GetRepoInfo (APIView) :
    def get (self, request) :
        try :
            id = request.query_params.get('id', '')
            repo = request.query_params.get('repo', '')

            fav_repository = 'https://github.com/' + id + '/' + repo

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
            owner = jsonObject_repos.get("owner").get("login")

            content_branches = requests.get(url_branches, headers={'Authorization': 'token 6f6d00c786cd3662b25716bf6c6fb6a2084f401d'})
            jsonObject_branches = json.loads(content_branches.content)
            json_size = len(jsonObject_branches)

            for i in range(1, int(json_size)+1):
                branch_lists.append(jsonObject_branches[i-1].get("name"))

            context = {"avatar_url" : avatar_url, "name" : name, "created_at" : created_at, "updated_at" : updated_at, "stargazers_count" : stargazers_count,  "forks" : forks, "branch_lists" : branch_lists, "owner" : owner}

            return Response(context, status=200)    

        except Exception as e:
            return Response(str(e), status=404)  

def sendList (kakao_id) :
    try : 
        repoList = []

        conn = None
        conn = MySQLdb.connect(user='margarets', password='db20192808', db='margarets$repoalarm',host='margarets.mysql.pythonanywhere-services.com', charset='utf8')
        #conn = MySQLdb.connect(user='root', password='@dbclfr0506', db='open_source',host='localhost', charset='utf8')
        curs = conn.cursor()

        sql = 'SELECT nick_name FROM user WHERE id = %s;'
        curs.execute(sql, [kakao_id])
        result = curs.fetchall()

        for i in result :
            repoList.append(i[0])

        return repoList
    except Exception as e :
        return print(str(e))

def returnGit (id, nick_name) :
    try : 
        repoList = []

        conn = None
        conn = MySQLdb.connect(user='margarets', password='db20192808', db='margarets$repoalarm',host='margarets.mysql.pythonanywhere-services.com', charset='utf8')
        #conn = MySQLdb.connect(user='root', password='@dbclfr0506', db='open_source',host='localhost', charset='utf8')
        curs = conn.cursor()

        sql = 'SELECT fav_repository, type FROM user WHERE id = %s and nick_name = %s;'
        curs.execute(sql, (id, nick_name))
        result = curs.fetchall()

        fav_repository = result[0][0]
        #branch = result[0][1]
        branch='main'

        return fav_repository, branch
    except Exception as e :
        return print(str(e))

def insertDb (id, fav_repository, type, nick_name, branch) :
    try:
        conn = None
        if len(id) == 0:
            raise Exception('아이디는 비어 있으면 안됩니다.')
        if len(fav_repository) == 0:
            raise Exception('관심 레파지토리는 비어 있으면 안됩니다.')
        if len(nick_name) == 0:
            raise Exception('별명은 비어 있으면 안됩니다.')
        if len(type) == 0:
            raise Exception('타입은 비어 있으면 안됩니다.')
        if len(branch) == 0:
            raise Exception('브랜치명은 비어 있으면 안됩니다.')
        conn = MySQLdb.connect(user='margarets', password='db20192808', db='margarets$repoalarm',host='margarets.mysql.pythonanywhere-services.com',charset='utf8')
        #conn = MySQLdb.connect(user='root', password='1234', db='open_source', charset='utf8')
        curs = conn.cursor()

        sql = "SELECT DATE_FORMAT(NOW(),'%Y%m%d%H%i%s');"
        curs.execute(sql)
        result = curs.fetchall()

        code = githubApi.getRepositoryInfo(fav_repository, branch ,0);  # url parser를 통해 git api 주소를 가지고 온다.
        if code[0] == 404:
            raise Exception('정상적이지 않은 레파지토리명 입니다')
        git_create_at = code[0]
        git_updated_at = code[1]
        git_api_address = code[2]
        fav_repository = fav_repository+"/branches/"+branch
        sql = "INSERT INTO repository (fav_repository,git_api_address,git_created_at,git_updated_at,created_at,updated_at) " \
            "VALUES (%s,%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE UPDATED_AT = %s"
        curs.execute(sql, (fav_repository, git_api_address, git_create_at, git_updated_at, result, result, result))

        sql = "INSERT INTO user (id,fav_repository,nick_name,type,created_at,updated_at) VALUES (%s,%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE UPDATED_AT = %s,NICK_NAME=%s,TYPE=%s"
        curs.execute(sql, (id, fav_repository, nick_name, type, result, result, result,nick_name,type))

        conn.commit()
        return print("github API 호출 성공")
    except Exception as e:
        if conn != None:
            conn.rollback()
        return print(str(e))
    finally:
        if conn != None:
            conn.close()

##########################################################################################kakao

@csrf_exempt
def barcode(request):
    answer = ((request.body).decode('utf-8'))
    return_json_str=json.loads(answer)
    return_str_skill=return_json_str['action']['name']
    return_str_git=return_json_str['action']['detailParams']['barcode']['value']
    return_str_id=return_json_str['userRequest']['user']['properties']['plusfriendUserKey']
    return_str_alias="첫번째레포"
    return_str_git_barcodeData=json.loads(return_str_git)
    return_str_branch="main"

    insertDb(return_str_id,return_str_git_barcodeData.get("barcodeData"),"kakao",return_str_alias,return_str_branch)
    
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

@csrf_exempt
def repoList(request):
    answer = ((request.body).decode('utf-8'))
    return_json_str=json.loads(answer)
    return_str_skill=return_json_str['action']['name']
    return_str_id=return_json_str['userRequest']['user']['properties']['plusfriendUserKey']

    repoList_arr=sendList(return_str_id)
    return_str_repoList="등록하신 레포 목록입니다.\n"

    for i in range(0,len(repoList_arr),1):
        return_str_repoList=return_str_repoList+str(i+1)+". "+repoList_arr[i]
        if(i<len(repoList_arr)-1):
            return_str_repoList+="\n"

    if return_str_skill == '레포리스트':
        return JsonResponse({
            'version': "2.0",
            'template': {
                'outputs': [{
                    'simpleText': {
                        'text': f"{return_str_repoList}"
                    }
                }],
                'quickReplies':[{
                    'label': '입력하기',
                    'action': 'message',
                }]
            }
        })

@csrf_exempt
def repoStatus(request):
    answer = ((request.body).decode('utf-8'))
    return_json_str=json.loads(answer)
    return_str_skill=return_json_str['action']['name']
    return_str_id=return_json_str['userRequest']['user']['properties']['plusfriendUserKey']
    repoList_arr=sendList(return_str_id)
    
    #return_str_repoAlias=int(return_json_str['action']['detailParams']['repoAlias']['value'])
    return_str_repoAlias=1
    return_str_git_url, return_str_git_branch = returnGit(return_str_id,repoList_arr[return_str_repoAlias-1])

    res=batch(return_str_id, return_str_git_url, repoList_arr[return_str_repoAlias-1], 'kakao', return_str_git_branch)
    print(res)

    if return_str_skill == '레포상태':
        return JsonResponse({
            'version': "2.0",
            'template': {
                'outputs': [{
                    'simpleText': {
                        'text': f"{res}"
                    }
                }],
            }
        })