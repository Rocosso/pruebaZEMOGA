
@app.route('/ping') #APIrest Working with Json
def ping():
    return jsonify({'message':'received package!'})

@app.route('/profileTw') #APIrest Working with Json from a pyfile
def get_profileTw():
    return jsonify(profileTw)

@app.route('/profileTw', methods=['POST']) #APIrest Working with Json to a console
def add_profileTw():
    new_profile = [
    {"name" : "juan", "experience" : "best personality", "image" : "profile twitter Juan's image" }
]
    profileTw.append(new_profile)
    return jsonify({"profile":  profileTw})



from ProfileTwitter import profileTw
profileTw = [
    { "name" : "luis","experience" : "better programmer today", "image" : "profile twitter image" }
]