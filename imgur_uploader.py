from imgurpython import ImgurClient
client_id = '82c51ca2f32f6d6'
client_secret = '077827772b09216439f16463a4fc84128ffd82f5'
client = ImgurClient(client_id, client_secret)

def upload_image(image_path, title, description):
    album = None
    config = {
		'album': album,
		'name':  title,
		'title': title,
		'description': description
	}
    image = client.upload_from_path(image_path, config=config, anon=False)
    return image
