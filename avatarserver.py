from flask import Flask, send_file, jsonify
import urllib.request
import requests
import random
import json

import os
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 1

avatar_dir = "avatars" # no slash
avatar2_dir = "bancho" # no slash

# create avatars directory if it does not exist
if not os.path.exists(avatar_dir):
	os.makedirs(avatar_dir)
	
@app.route("/status")
def serverStatus():
	return jsonify({
		"response" : 200,
		"status" : 1
	})

@app.route("/<int:uid>")
def serveAvatar(uid):
	# Check if avatar exists
	if os.path.isfile("{}/{}.png".format(avatar_dir, uid)):
		avatarid = uid
	else:
		avatarid = -1

	# Serve actual avatar or default one
	return send_file("{}/{}.png".format(avatar_dir, avatarid))


@app.route("/bancho/id/<int:uid>")
def serveAvatar2(uid):
	# Check if avatar exists
	if os.path.isfile("{}/{}.png".format(avatar2_dir, uid)):
		avatarid = uid
	else:
		urllib.request.urlretrieve(f"https://a.ppy.sh/{uid}", f"bancho/{uid}.png")
		avatarid = uid

	# Serve actual avatar or default one
	return send_file("{}/{}.png".format(avatar2_dir, avatarid))


@app.route("/bancho/u/<string:uid>")
def serveAvatar3(uid):
	key = random.choice(api)
	reqjson = requests.get(url=f"https://osu.ppy.sh/api/get_user?k={key}&u={uid}").json()
	uid = reqjson[0]['user_id']
	# Check if avatar exists
	if os.path.isfile("{}/{}.png".format(avatar2_dir, uid)):
		avatarid = uid
	else:
		urllib.request.urlretrieve(f"https://a.ppy.sh/{uid}", f"bancho/{uid}.png")
		avatarid = uid

	# Serve actual avatar or default one
	return send_file("{}/{}.png".format(avatar2_dir, avatarid))


@app.errorhandler(404)
def page_not_found(error):
    return send_file("{}/-1.png".format(avatar_dir))

	
# Run the server
app.run(host="0.0.0.0", port=5000)
