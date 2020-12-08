# RepoKaKaoAlarmBot

깃허벨 대표 레포지토리입니다

깃허벨 텔레그램 레포지토리 주소\
https://github.com/margarets-kim/telegram_githubell

깃허벨 웹사이트 레포지토리 주소\
https://github.com/margarets-kim/RKAB_web

## 깃허벨 매뉴얼

1. 플랫폼 선택하기
   카카오톡과 텔레그램 중 원하는 플랫폼을 선택하세요 \
   텔레그램은 선톡 기능이 존재하지만 많은 사람들이 사용하진 않습니다 \
   카카오톡은 누구나 사용하는 대중적인 메신저지만 선톡 기능이 존재하지 않아 수동으로 확인해야합니다.

2. 웹사이트에서 원하는 깃허브 레포지토리 등록하기

   [깃허벨 사이트](https://githubell.netlify.app)에 접속하세요
   ![첫번째 사진](./markdown_img/web-main.png)
   자신이 이용하는 플랫폼을 선택하세요

   ### 카카오 버전

   ![카카오](./markdown_img/web_k_0.png)

   ### 텔레그램 버전

   ![텔레그램](./markdown_img/web_t_1.png)

3. 깃허브 레포지토리 주소를 입력하세요

   ![카카오](./markdown_img/web_k_1.png)
   https://github.com/owner/repo 형식으로 레포지토리 주소를 입력하세요
   ![카카오](./markdown_img/web_k_2_error.png)
   올바른 주소 URL형식만 입력받을 수 있습니다

4. 플랫폼 안내 양식에 맞춰 진행하실경우 마지막으로 QR코드가 생성됩니다
   ![카카오](./markdown_img/web_k_4.png)
5. 카카오톡은 @깃허벨 채널을 먼저 추가해주세요
   ![카카오](./markdown_img/kakao_channel.png)
6. 채팅하기를 누른 후 `관심 레포 추가` 버튼을 눌러서 QR코드를 촬영해주세요(모바일 환경)
   ![카카오](./markdown_img/kakao_chat_qrread.png)
   QR코드가 성공적으로 인식 될 경우 등록되었다는 메세지를 받게됩니다
7. 등록한 레포지토리는 `레포 상태 확인`을 통해 해당 레포지토리 업데이트 내역을 확인할 수 있습니다
   ![카카오](./markdown_img/kakao_chat_choose.png)
   처음에 등록한 별명을 순서대로 보여주며 `입략하기`를 통해 해당 레포지토리의 Index 번호를 입력하세요
   ![카카오](./markdown_img/kakao_chat_no_check.png)
   호출된 레포지토리의 상태를 알려줍니다
   ![카카오](./markdown_img/kakao_chat_check.png)
8. 텔레그램은 [@githubell_bot]('https://t.me/githubell_bot')을 추가해주세요
   ![텔레그램](./markdown_img/telegram_intro.png)
9. 외부 Qr code 인식 어플 (일반 카메라도 가능)을 통해 QR코드를 인식 시켜주세요
   ![텔레그램](./markdown_img/telegram_chat_branch.png)
   ![텔레그램](./markdown_img/telegram_chat_alias.png)
   카카오톡과는 달리 채팅 안에서 브랜치 선택과 별명 짓기가 이루어집니다
   ![텔레그램](./markdown_img/telegram_chat_send.png)
10. 텔레그램은 레포지토리의 변화를 감지하고 먼저 메세지를 보내주는 기능이 제공됩니다
    ![텔레그램](./markdown_img/telegram_chat_push.png)
11. 좋아하는 플랫폼이나 원하는 기능에 맞춰 플랫폼을 선택하고 등록해보세요 :)

## 실행 스크립트

### Step 1. 가상환경 생성하기

### `python -m venv {가상환경 이름}`

해당 명령어를 통해 현재 위치한 경로에 파이썬 가상환경을 생성할 수 있습니다\
해당 프로젝트의 파이썬 버전은 3.8입니다!

### mac/Linux 가상 환경 실행 명령어

### `source {가상환경이름}/bin/activate {가상환경이름}`

### window 가상 환경 실행 명령어

### `source {가상환경이름}/Script/activate {가상환경이름}`

### 가상 환경 종료 명령어

### `deactivate`

### Step 2. pip install

### `pip install -r requirments.txt`

가상환경을 실행한 후 해당 명령어를 통해 패키지 파일을 모두 설치하세요

### Step 3. 서버 실행하기

### `python manage.py runserver`

해당 명령어를 통해 서버를 구동할 수 있습니다!

## 기술스택

### Server-side

- Django
- MySql

### Client-side

- React
- Bootstrap

### Tools

- Webpack
- Babel
- pip
- Postman

### Kakao i Open Builder Api 관리 및 Web Front-End 구축

김민주 / 임유빈

### Git hub Api 및 DB 관리

최성훈 / 이광열

## BACK-END SERVER - Django

Django는 파이썬 기반이기 때문에 다양하고 강력한 라이브러리가 많습니다 또한 비교적 쉽고 간결하므로
개발시간 단축 효과를 줍니다. BACK-END 서버를 구현을 할때, 가장 많이 쓰는 스프링의 경우 여러가지 설정 및
프로그램 구조를 이해하는데 시간이 오래걸리지만 Django는 간단하게 BACK-END 서버 구축을 도와줍니다. 그렇기 때문에
Django를 BACK-END로 정하였습니다.

## HOST SERVER - PythonAnywhere

PythonAnywhere는 Django를 운영하는데 가장 효율적으로 서비스를 제공하여 줍니다.
몇번의 조작으로 서버 구성을 해줄 뿐 아니라 여러가지 방면에서 개발자를 위한 편리한 서비스를 제공하여 줍니다

## BACK-END 관련 소스코드 구조(2020.12.07 기준)

````.
.RepoKakaoAlarmBot
├── README.md
├── cron.py
├── api
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   └── githubApi.py
│   └── models.py
│   └── tests.py
│   └── urls.py
│   └── views.py
├── manage.py
└── static
    └── admin
        ├── css
        ├── fonts
        ├── img
        └── js```
````

# BACK-END API

이 API는 POST 및 GET 요청을 사용 하여 통신하고 HTTP 응답 코드 를 사용 하여 상태 및 오류를 표시합니다. 모든 응답은 표준 JSON으로 제공됩니다.
모든 요청에는 content-typeof 가 포함됩니다 application/json 되어야하며 본문은 유효한 JSON이어야합니다.

## 응답 코드

### 응답 코드

```
200: 성공
404: 잘못된 요청이거나 실패
```

### 에러 메시지 예시

```json
{
  "code": 404,
  "message": "브랜치명은 비어 있으면 안됩니다."
}
```

## 회원가입

**요청:**

```json
POST http://margarets.pythonanywhere.com/api/

Request body:
{
    "id":"shchoi",
    "fav_repository":"https://github.com/margarets-kim/RepoKaKaoAlarmBot",
    "nick_name":"csh",
    "type":"kakao",
    "branch":"main"
}
```

**성공시:**

```json
{
  "code": 200,
  "message": "정상적으로 api 호출 완료"
}
```

**실패시:**

```json
{
  "code": "404",
  "message": "브랜치명은 비어 있으면 안됩니다."
}
```

## 깃 레파지토리 변경 이력 요청

**요청:**

```json
GET "http://margarets.pythonanywhere.com/api/?id=tjdgns461&fav_repository=https://github.com/margarets-kim/RepoKaKaoAlarmBot&nick_name=뚱이&type=kakao&branch=main"
```

| 파라미터         |                의미                 |
| ---------------- | :---------------------------------: |
| `id`             |       등록된 유저 아이디 정보       |
| `fav_repository` | 등록된 유저가 관심등록한 레파지토리 |
| `nick_name`      |        유저가 등록한 닉네임         |
| `type`           |              sns 타입               |
| `branch`         |     관심 레파지토리의 브랜치명      |

**성공시:**

```json
HTTP/1.1 200
Server: margarets.pythonanywhere.com
Content-Type: application/json

[
    {
        "sha": "c6e1c072d558fcd0efed8ea6fc575349143e1b44",
        "node_id": "MDY6Q29tbWl0MzA1OTA5OTI3OmM2ZTFjMDcyZDU1OGZjZDBlZmVkOGVhNmZjNTc1MzQ5MTQzZTFiNDQ=",
        "commit": {
            "author": {
                "name": "GwangYeol Lee",
                "email": "gwangyeal@gmail.com",
                "date": "2020-12-05T19:51:55Z"
            },
            "committer": {
                "name": "GwangYeol Lee",
                "email": "gwangyeal@gmail.com",
                "date": "2020-12-05T19:51:55Z"
            },
            "message": "paramsModified",
            "tree": {
                "sha": "ef0be0db8fdd14e34770866e72da21bfd1eb15c1",
                "url": "https://api.github.com/repos/margarets-kim/RepoKaKaoAlarmBot/git/trees/ef0be0db8fdd14e34770866e72da21bfd1eb15c1"
            },
            "url": "https://api.github.com/repos/margarets-kim/RepoKaKaoAlarmBot/git/commits/c6e1c072d558fcd0efed8ea6fc575349143e1b44",
            "comment_count": 0,
            "verification": {
                "verified": false,
                "reason": "unsigned",
                "signature": null,
                "payload": null
            }
        },
        "url": "https://api.github.com/repos/margarets-kim/RepoKaKaoAlarmBot/commits/c6e1c072d558fcd0efed8ea6fc575349143e1b44",
        "html_url": "https://github.com/margarets-kim/RepoKaKaoAlarmBot/commit/c6e1c072d558fcd0efed8ea6fc575349143e1b44",
        "comments_url": "https://api.github.com/repos/margarets-kim/RepoKaKaoAlarmBot/commits/c6e1c072d558fcd0efed8ea6fc575349143e1b44/comments",
        "author": {
            "login": "prglee6274",
            "id": 48249600,
            "node_id": "MDQ6VXNlcjQ4MjQ5NjAw",
            "avatar_url": "https://avatars2.githubusercontent.com/u/48249600?v=4",
            "gravatar_id": "",
            "url": "https://api.github.com/users/prglee6274",
            "html_url": "https://github.com/prglee6274",
            "followers_url": "https://api.github.com/users/prglee6274/followers",
            "following_url": "https://api.github.com/users/prglee6274/following{/other_user}",
            "gists_url": "https://api.github.com/users/prglee6274/gists{/gist_id}",
            "starred_url": "https://api.github.com/users/prglee6274/starred{/owner}{/repo}",
            "subscriptions_url": "https://api.github.com/users/prglee6274/subscriptions",
            "organizations_url": "https://api.github.com/users/prglee6274/orgs",
            "repos_url": "https://api.github.com/users/prglee6274/repos",
            "events_url": "https://api.github.com/users/prglee6274/events{/privacy}",
            "received_events_url": "https://api.github.com/users/prglee6274/received_events",
            "type": "User",
            "site_admin": false
        },
        "committer": {
            "login": "prglee6274",
            "id": 48249600,
            "node_id": "MDQ6VXNlcjQ4MjQ5NjAw",
            "avatar_url": "https://avatars2.githubusercontent.com/u/48249600?v=4",
            "gravatar_id": "",
            "url": "https://api.github.com/users/prglee6274",
            "html_url": "https://github.com/prglee6274",
            "followers_url": "https://api.github.com/users/prglee6274/followers",
            "following_url": "https://api.github.com/users/prglee6274/following{/other_user}",
            "gists_url": "https://api.github.com/users/prglee6274/gists{/gist_id}",
            "starred_url": "https://api.github.com/users/prglee6274/starred{/owner}{/repo}",
            "subscriptions_url": "https://api.github.com/users/prglee6274/subscriptions",
            "organizations_url": "https://api.github.com/users/prglee6274/orgs",
            "repos_url": "https://api.github.com/users/prglee6274/repos",
            "events_url": "https://api.github.com/users/prglee6274/events{/privacy}",
            "received_events_url": "https://api.github.com/users/prglee6274/received_events",
            "type": "User",
            "site_admin": false
        },
        "parents": [
            {
                "sha": "b76df6ff6c4d83a18417fab23a34a2d2fd4cf958",
                "url": "https://api.github.com/repos/margarets-kim/RepoKaKaoAlarmBot/commits/b76df6ff6c4d83a18417fab23a34a2d2fd4cf958",
                "html_url": "https://github.com/margarets-kim/RepoKaKaoAlarmBot/commit/b76df6ff6c4d83a18417fab23a34a2d2fd4cf958"
            }
        ]
    }]
```

**실패시:**

```json
{
  "code": "404",
  "message": "깃 허브 API 호출시 문제가 발생 하였습니다."
}
```

## 유저 새 레포지토리 등록 요청

유저가 서버에 새 레포지토리를 등록하는 요청입니다

```json
POST "http://margarets.pythonanywhere.com/api/"
```

| 파라미터         |                의미                 |
| ---------------- | :---------------------------------: |
| `id`             |       등록된 유저 아이디 정보       |
| `fav_repository` | 등록된 유저가 관심등록한 레파지토리 |
| `nick_name`      |        유저가 등록한 닉네임         |
| `type`           |              sns 타입               |
| `branch`         |     관심 레파지토리의 브랜치명      |

**성공시:**

```json
HTTP/1.1 200
Server: margarets.pythonanywhere.com
Content-Type: application/json
{
    "정상적으로 api 호출 완료"
}
```

**실패시:**

```json
HTTP/1.1 404
Server: margarets.pythonanywhere.com
Content-Type: application/json
{
    "정상적이지 않은 {변수 이름} 입니다"
}
```

## 유저기 요청한 닉네임 레포지토리의 실제 레포지토리 정보 요청

유저가 저장한 별명 레포지토리의 실제 정보를 가져오는 요청입니다.\
새로운 정보가 갱신되었는지 확인하기 전에 먼저 실행되는 api 요청함수입니다

**요청:**

```json
GET "http://margarets.pythonanywhere.com/api/git/?id={id}&&nick_name={nick_name}}"
```

| 파라미터    |          의미           |
| ----------- | :---------------------: |
| `id`        | 등록된 유저 아이디 정보 |
| `nick_name` |  유저가 등록한 닉네임   |

**성공시:**

```json
HTTP/1.1 200
Server: margarets.pythonanywhere.com
Content-Type: application/json
{
    "repoUrl": "https://github.com/margarets-kim/telegram_githubell",
    "repoBranch": "main"
}
```

**실패시:**

```json
HTTP/1.1 200
Server: margarets.pythonanywhere.com
Content-Type: application/json
{
    "repoUrl": [], //빈 배열 리턴
    "repoBranch": []
}
}
```

## 유저 레포지토리 저장 정보 요청

변경사항이 있는지 앞서 실제 레포지토리의 정보를 들고온 후 기존 DB와 비교 요청을 하는 api 요청 함수입니다

**요청:**

```json
GET "http://margarets.pythonanywhere.com/api/?{Params}"
```

| 파라미터         |                의미                 |
| ---------------- | :---------------------------------: |
| `id`             |       등록된 유저 아이디 정보       |
| `fav_repository` | 등록된 유저가 관심등록한 레파지토리 |
| `nick_name`      |        유저가 등록한 닉네임         |
| `type`           |              sns 타입               |
| `branch`         |     관심 레파지토리의 브랜치명      |

# DATABASE MODEL - MYSQL

MySQL은 가장 널리 사용되고 있는 관계형 데이터베이스 관리 시스템(RDBMS: Relational DBMS)입니다.
MySQL은 오픈 소스이며, 다중 사용자와 다중 스레드를 지원합니다.
또한, C언어, C++, JAVA, PHP 등 여러 프로그래밍 언어를 위한 다양한 API를 제공하고 있습니다.
MySQL은 유닉스, 리눅스, 윈도우 등 다양한 운영체제에서 사용할 수 있으며, 특히 PHP와 함께 웹 개발에 자주 사용됩니다.
MySQL은 오픈 소스 라이센스를 따르기는 하지만, 상업적으로 사용할 때는 상업 라이센스를 구입해야만 합니다.

MySQL이 가지는 장점은 다음과 같습니다.

1. 오픈 소스 라이센스를 따르기 때문에 무료로 사용할 수 있습니다.

2. 다양한 운영체제에서 사용할 수 있으며, 여러 가지의 프로그래밍 언어를 지원합니다.

3. 크기가 큰 데이터 집합도 아주 빠르고 효과적으로 처리할 수 있습니다.

4. 널리 알려진 표준 SQL 형식을 사용합니다.

5. MySQL 응용 프로그램을 사용자의 용도에 맞게 수정할 수 있습니다.

## Project - ERD

![erd.jpg](./erd.JPG)

# BACK-END 배치 프로그램

## 프로그램 개요

30분 주기로 배치 프로그램을 실행합니다. 레파지토리 테이블에서 등록된 레파지토리를 가지고 와서
헤당 레파지토리의 변경 이력을 깃 API로 조회 합니다. 만약 변경 이력이 존재 한다면 해당 레파지토리에 관심을 가지고 있는
유저들에게 변경 되었다는 알림을 보냅니다(현재는 텔레그램 서비스만 정상적으로 작동중 입니다.)

```
def batch():
    print("깃 허브쪽 배치 프로그램이 돌고 있습니다.")  # 배치 프로그램이 돌고 있다는 로그남김 log
    try:
        conn = None
        conn = MySQLdb.connect(user='root', password='1234', db='open_source', charset='utf8')
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

                sql = "SELECT b.id,b.nick_name,b.type,a.git_api_address,a.fav_repository,b.user_get_date FROM repository a
                LEFT JOIN user b ON a.fav_repository = b.fav_repository WHERE a.fav_repository=%s";
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
                        content = requests.get(url,headers={'Authorization':'token 6f6d00c786cd3662b25716bf6c6fb6a2084f401d'},
                        params={'sha':branch,'since':timestampStr})
                        jsonObject = json.loads(content.content)
                        telegram(j[0],j[1],j[4],j[5],dataList[1],jsonObject,conn) # 이 부분 수정 필요
        conn.commit()
    except Exception as e:
        raise Exception('GITHUB API 호출할때 문제가 생겼습니다.')
    finally:
        if conn != None:
            conn.close()

```
