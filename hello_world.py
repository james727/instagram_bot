import praw
import instagram_converter
from prawoauth2 import PrawOAuth2Mini
key = "dFh4UjkvhdQIGw"
secret = "0FS1_D2242Y-cdC2EiEZdTjZ6u4"
token = "54589065-hluT2YOUajr1nTPdDokqFOGL_1g"
refresh = "54589065-hvu78d_mz4VDyGMLRTNIveSoP2k"
user_agent = ('instareposter 1.0')
r = praw.Reddit(user_agent = user_agent)
scopes = ['identity', 'read', 'submit']
oauth_helper = PrawOAuth2Mini(r, app_key = key, app_secret = secret,
                                access_token = token, refresh_token = refresh, scopes=scopes)
oauth_helper.refresh()
subreddit = r.get_subreddit("InstaRepostBot")
already_done = []

def bot_response(submission, new_url):
    head = "Hi! I'm InstaRepostBot. I take instagram links and re-upload them to streamable or imgur. Your new link is below \n\n"
    mid = new_url
    tail = "\n\nI'm only running for a short trial period, pm me feedback if you like the bot and want it to keep running!"
    submission.add_comment(head+mid+tail)


for submission in subreddit.get_new(limit = 20):
    post_id = submission.id
    url = submission.url
    domain = url.split('//')[1].split('/')[0]
    if 'instagram' in domain.split('.') and post_id not in already_done:
        new_url = instagram_converter.convert_instagram(url)
        if new_url!= None:
            bot_response(submission, new_url)
            already_done.append(post_id)
