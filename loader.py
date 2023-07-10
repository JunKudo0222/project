import instaloader

    #インスタグラムにログイン
    loader = instaloader.Instaloader()
    loader.login(INSTAGRAM_ID, INSTAGRAM_PASSWORD)

    #指定したIDのprofileオブジェクトを作成
    profile = instaloader.Profile.from_username(loader.context, id)#id:フォロワーを取得したいアカウントのユーザーID

    #指定したIDのフォロワーを全件取得
    followers = profile.get_followers()

    #ユーザーIDを出力する
    for follower in followers:
        print(follower.username)

