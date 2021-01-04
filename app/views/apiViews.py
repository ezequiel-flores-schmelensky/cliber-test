# coding=utf-8
from run import app
from flask import request, jsonify, json
from ..models.user import User

"""" API Rest """

#@app.route('/api/user', methods=['POST'])
#def user():
#    response = {"name":"test"}
#    return jsonify(response), 200


#@app.route('/api/user/<id>', methods=['GET', 'DELETE', 'PATCH'])
#def user_id(id):
#    response = {"name":"test"}
#    #response = TagController().crud_id(request, id)
#    return jsonify(response), 200


@app.route('/api/user/<int:page>/profiles', methods=['GET'])
def user_list(page=1):
    try:
        query = request.args
        per_page = 25
        username = ""
        order = "id"
        if "pagination" in query:
            per_page = int(query["pagination"])

        if "username" in query:
            username = query["username"]

        if "order_by" in query:
            order = query["order_by"]

        users = User.query.filter(
            User.username.like("%"+ username +"%")
        ).order_by(order).paginate(page, per_page=per_page)
    except Exception:
        #flash("No users in the database.")
        users = None
        return jsonify(users), 400
        
    response = {}
    response['has_prev'] = users.has_prev
    response['has_next'] = users.has_next
    response['prev_num'] = users.prev_num
    response['next_num'] = users.next_num
    response['users'] = [ {"id":user.id, "username":user.username, "image_url":user.image_url, "type":user.type, "link":user.link} for user in users.items]

    return jsonify(response), 200