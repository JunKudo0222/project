
import requests
import json
import sys

# Your Account info
def get_user_info():
    return {
            "username": "shimaumaen",
            "password": "Iojk3231"
            }

# HTTP Headers to login
def login_http_headers():
    ua = "".join(["Mozilla/5.0 (Windows NT 6.1; WOW64) ",
                  "AppleWebKit/537.36 (KHTML, like Gecko) ",
                  "Chrome/56.0.2924.87 Safari/537.36"])
    return {
            "user-agent": ua,
            "referer":"https://www.instagram.com/",
            "x-csrftoken":"null",
            "cookie":"sessionid=null; csrftoken=null"
            }

# login session
def logined_session():
    session = requests.Session()
    login_headers = login_http_headers()
    user_info = get_user_info()
    login_url = "https://www.instagram.com/accounts/login/ajax/"
    session.post(login_url, data=user_info, headers=login_headers)
    return session

# a fetch (max 3000 followers)
def fetch_followers(session, user_id, query_hash, after=None):
    variables = {
        "id": user_id,
        "first": 3000,
    }
    if after:
        variables["after"] = after

    followers_url = "".join(["https://www.instagram.com/graphql/query/?",
                             "query_hash=" + query_hash + "&",
                             "variables=" + json.dumps(variables)])
    # HTTP Request
    followers = session.get(followers_url)
    dic = json.loads(followers.text)
    print(dic)

    sys.exit()
    edge_followed_by = dic["data"]["user"]["edge_followed_by"]

    count = edge_followed_by["count"] # number of followers
    after = edge_followed_by["page_info"]["end_cursor"] # next pagination
    has_next = edge_followed_by["page_info"]["has_next_page"]
    return {
            "count": count,
            "after": after,
            "has_next":  has_next,
            "followers": edge_followed_by["edges"]
            }

def fetch_all_followers(session, user_id, query_hash):
    after     = None # pagination
    followers = []  

    while(True):
        fetched_followers = fetch_followers(session, user_id, query_hash, after)
        followers += fetched_followers["followers"]

        if fetched_followers["has_next"]:
            after = fetched_followers["after"]
        else:
            return {
                    "count": fetched_followers["count"],
                    "followers": followers
                    }

def main(user_id, query_hash):
    session = logined_session()
    return fetch_all_followers(session, user_id, query_hash)

if __name__ == '__main__':
    user_id  = "54263450419" # user id to search 
    query_hash = "d4d88dc1500312af6f937f7b804c68c3" # your query id
    main(user_id, query_hash)
