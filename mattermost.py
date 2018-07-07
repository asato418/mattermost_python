"""
mattermostdriver 用サンプルコード

"""
"""
driverの読み込み
"""
from mattermostdriver import Driver

"""
環境依存の接続文字列の定義
"""
foo = Driver({
    'url': 'mattermost.take.fujitsu.local',
    'login_id': 'asato',
    'password': 'xxxxxxxx',
    'token': 'oafkropjifnefgfy8twwahm7oy',
    'scheme': 'http',
    'port': 80,
    'basepath': '/api/v4',
    'verify': True
})

"""
設定した内容でログイン
"""
foo.login()

"""
channel_idの取得(辞書形式で価をとってきて [id] を拾ってる
"""
channel_id = foo.channels.get_channel_by_name_and_team_name('asato', 'test')['id']

"""
試しに、users.get_user_by_usernameでとってきた文字列を、create_post関数でmattermost自体に書き込んでみる

"""
message='user_information(asato) is'+str(foo.users.get_user_by_username('asato'))

foo.api['posts'].create_post(options={
    'channel_id': channel_id, 
    'message': message
    })

"""
もう一つ試しに、emojiのリストを mattermostに書き込んでみる
"""

message='Current emoji_list is '+ str(foo.emoji.get_emoji_list())

foo.api['posts'].create_post(options={
    'channel_id': channel_id, 
    'message': message
    })

"""
team所属のchannelのリストを簡単に出したかったんだけど、チャンネルIDをとってきてString配列にして渡さないとうまく動かない？何か間違ってる？？
"""
team_dict=foo.teams.get_team_by_name('asato')
team_id=team_dict['id']
channel_ids=[]
channel_ids.append(channel_id)
channel_id = foo.channels.get_channel_by_name_and_team_name('asato', 'test2')['id']
channel_ids.append(channel_id)

"""  結果をいちいち出すとうっとうしいので一旦コメント
print(foo.channels.get_list_of_channels_by_ids(team_id, channel_ids))
"""

channel_id = foo.channels.get_channel_by_name_and_team_name('asato', 'test2')['id']
"""  結果をいちいち出すとうっとうしいので一旦コメント
print(foo.posts.get_posts_for_channel(channel_id))
"""

"""
チャネルのポストをとってきて、posts部分だけ print
"""
print(foo.posts.get_posts_for_channel(channel_id)["order"])


