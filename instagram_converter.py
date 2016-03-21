import instagram_test
import streamable_test
import imgur_uploader
import os

#url = "https://www.instagram.com/p/BDHle7CxhwM/?taken-by=nba&hl=en"

def convert_instagram(url):
    if instagram_test.link_type(url)=="media":
        media_type, url =  instagram_test.parse_instagram_url(url)
        path = instagram_test.download_media(media_type, url)
    else:
        path = None
    if path == None:
        return None
    if media_type == "photo":
        image = imgur_uploader.upload_image(path, "", "")
        base = "http://imgur.com/"
        os.remove(path)
        return base + image['id']
    elif media_type == "video":
        video_info = streamable_test.upload_file(path)
        base = "https://streamable.com/"
        os.remove(path)
        return base + video_info['shortcode']

#print convert_instagram(url)
