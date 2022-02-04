from flask import Flask, jsonify, request
from healthcheck import HealthCheck, EnvironmentDump


app = Flask(__name__)

health = HealthCheck()
# add your own check function to the healthcheck


def check_available():
    return True, "ok"


health.add_check(check_available)

app.add_url_rule("/healthcheck", "healthcheck", view_func=health.run)


@app.route('/', methods=['GET'])
def helloworld():
    if(request.method == 'GET'):
        data = {"data": "Hello World"}
        return jsonify(data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5003)
    app.run(debug=True)
