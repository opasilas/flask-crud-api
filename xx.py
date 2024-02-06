@app.route("/get-user/<user_id>")
def get_user(user_id):
    user_data = {
        "id": user_id,
        'name': 'opasilas',
        'sport': 'basketball',
        'food': 'amala'
    }

    # query parameter

    extra = request.args.get("extra")

    if extra:
        user_data['extra'] = extra
    else:
        pass

    return jsonify(user_data), 200

# @app.route("/create-user/<user-id>", methods= ['POST'])
# def create_user(user_id):