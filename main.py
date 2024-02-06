from flask import Flask, request, jsonify
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app)

names = {"silas": {"age": 45, "gender": 'male'},
         "opa": {"age": 56, "class": 'upper'}
         }

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help='Name is required', required=True)
video_put_args.add_argument("views", type=int, help='Views is required', required=True)
video_put_args.add_argument("likes", type=int, help='Likes is required', required=True)

class Helloworld(Resource):
    def get(self, name):
        if name in names:
            return names[name]
        else:
            return "put a valid name"
        
    def put(self, video_id):
        args = video_put_args.parse_args()
        # print(args)
        return {video_id: args}

api.add_resource(Helloworld, "/<int:video_id>")

if __name__ == "__main__":
    app.run(debug=True, port=8090)