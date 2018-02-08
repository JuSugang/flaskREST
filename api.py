from flask import Flask, jsonify, request
from flask_restful import reqparse, abort, Api, Resource
from flask_sqlalchemy import SQLAlchemy
import time
import datetime
import os
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://localhost/restdatabase'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

api = Api(app)
db = SQLAlchemy(app)


from models import *

# shows a single todo item and lets you delete a todo item
class Particle(Resource):
    def get(self, frame_id):
        query=Result.query.get(frame_id)
        js=''
        js+='"{'
        js+=' "timestamp" : " '+query.timestamp+' ", '
        js+=' "particles" : " '+query.particles+' " '
        js+='}"'
        return js

    def delete(self, frame_id):
        abort_if_todo_doesnt_exist(frame_id)
        del TODOS[todo_id]
        return '', 204

    def put(self, frame_id):
        args = parser.parse_args()
        TODOS[todo_id] = task
        return task, 201

# shows a list of all todos, and lets you POST to add new tasks
class ParticleList(Resource):
    def get(self):
    	query=Result.query.all()
    	js='"{'
    	for i in query:
    		js+=str(i.id)+':'
    		js+='{'
    		js+=' "timestamp" : " '+i.timestamp+' ", '
    		js+=' "particles" : " '+i.particles+' " '
    		js+='}'

    	js=js[:-1]
    	js+='}"'

        print("js : "+js)
    	return js

    def post(self):
        ts = time.time()
        timeStamp = datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
        particlesStr = request.form["particles"]
        print("ourtime: ",ts,particlesStr)
        result = Result(
            timestamp=timeStamp,
            particles=particlesStr
            )
        db.session.add(result)
        db.session.commit()
        return timeStamp, 201

api.add_resource(ParticleList, '/particles')
api.add_resource(Particle, '/particles/<frame_id>')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)