from config import logger
from flask import Flask,request,jsonify
from flask_restful import Resource, Api
# The data to log
text = 'Hello, world!'

# Writes the log entry
logger.log_text(text)
print('Logged: {}'.format(text))

app = Flask(__name__)
api = Api(app)

class ApiController(Resource):
    
    
    @app.route('/hello', methods=['GET'])
    def get_hello():
        logger.log_text("SimpleApi: Inside HelloWorld method")
        print('SimpleApi: p {}'.format("Inside HelloWorld method"))
        return {'hello': 'world'}
    
    @app.route('/tasks', methods=['GET'])
    def get_task():
        tasks =  [
            {
                'id': 1,
                'title': u'Learn Python',
                'description': u'Flask Gunicorn WSGI', 
                'done': True
            },
            {
                'id': 2,
                'title': u'Learn Key skills',
                'description': u'Docker OpenApi Swagger', 
                'done': False
            }
        ]
        logger.log_text("SimpleApi: Inside tasks method")
        print('SimpleApi: p {}'.format("Inside tasks method"))
        return jsonify(tasks)
    
    @app.route("/square", methods=['GET', 'POST'])
    def get_square(): 
        logger.log_text("SimpleApi: Inside square method")
        print('SimpleApi: p {}'.format("Inside tasks method"))
        number = request.args.get('number')
        return jsonify({'square': int(number)**2}) 
    
    @app.route('/saymyname', methods=['POST'])
    def postYourName():
        content = request.json
        name = content['name']
        logger.log_text("SimpleApi: Inside postYourName method, your name :"+name)
        print('SimpleApi: p {}'.format("Inside postYourName method, your name :"+name))
        return "Hi  %s !" %name

#api.add_resource(ApiController, '/hello', endpoint = 'hello')
#api.add_resource(ApiController, '/tasks', endpoint = 'tasks')

    

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='8082')
