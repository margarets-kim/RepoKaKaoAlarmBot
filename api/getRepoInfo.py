import httplib2, json, requests
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

class GetInfo (APIView) : 
    def getRepoInfo (self, request) :
        fav_repository = request.Get.get('fav_repository', '')

        branch_lists = []
        res_json = {}

        index = fav_repository.find('github')
        url = fav_repository[index:]
        index = url.find("/")
        url_repos = "https://api.github.com/repos"+url[index:]
        url_branches = "https://api.github.com/repos"+url[index:]+"/branches"

        content_repos = requests.get(url_repos, headers={'Authorization': 'token 2a19d3dda9e148fd04518bb6d9a61fb8bed6899f'})
        jsonObject_repos = json.loads(content_repos.content)

        avatar_url = jsonObject_repos.get("owner").get("avatar_url")
        name = jsonObject_repos.get("name")
        created_at = jsonObject_repos.get("created_at")
        updated_at = jsonObject_repos.get("updated_at")
        stargazers_count = jsonObject_repos.get("stargazers_count")
        forks = jsonObject_repos.get("forks")

        content_branches = requests.get(url_branches, headers={'Authorization': 'token 2a19d3dda9e148fd04518bb6d9a61fb8bed6899f'})
        jsonObject_branches = json.loads(content_branches.content)
        json_size = len(jsonObject_branches)

        for i in range(1, int(json_size)+1):
            print(i)
            branch_lists.append(jsonObject_branches[i-1].get("name"))

        res_json = {
            "avatar_url : " + avatar_url, 
            "name : " + name, 
            "created_at : " + created_at, 
            "updated_at : " + updated_at, 
            "stargazers_count : " + str(stargazers_count), 
            "forks : " + str(forks),
            "branch_lists : " + str(branch_lists)
            }

        return JsonResponse(res_json, status = 200)