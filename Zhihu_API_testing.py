from zhihu_oauth import ZhihuClient
from zhihu_oauth.exception import NeedCaptchaException

client = ZhihuClient()

# 用户登录，如不需要验证码直接登录，若需要验证码则使用验证码登录
try:
    client.login('hzhangal0330@gmail.com', 'zhm940330')
except NeedCaptchaException:
    # 保存验证码并提示输入，重新登录
    with open('a.gif', 'wb') as f:
        f.write(client.get_captcha())
    captcha = input('please input captcha:')
    client.login('hzhangal0330@gmail.com', 'zhm940330', captcha)

me = client.from_url('https://www.zhihu.com/people/SONG-OF-SIREN')

print('name', me.name)
print('headline', me.headline)
print('description', me.description)

print('following topic count', me.following_topic_count)
print('following people count', me.following_topic_count)
print('followers count', me.follower_count)

print('voteup count', me.voteup_count)
print('get thanks count', me.thanked_count)

print('answered question', me.answer_count)
print('question asked', me.question_count)
print('collection count', me.collection_count)
print('article count', me.articles_count)
print('following column count', me.following_column_count)

print('testing')
print(me.followers)

for _, answer in zip(range(5), me.answers.order_by('votenum')):
    print(answer.question.title, answer.voteup_count)

# for _, follower in zip(range(20), me.followers):
#     print(follower.name, follower.voteup_count)
#     for _, answer in zip(range(3), follower.answers.order_by('votenum')):
#         print(answer.question.title, answer.voteup_count)
