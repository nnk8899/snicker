import datetime
from flask import Flask
from flask_restful import reqparse, abort, Api, Resource



app = Flask(__name__)
api = Api(app)

IPs = {
	'10.10.50.30': '2018-08-02 00:00:00',
	'10.10.50.27': '2018-08-02 00:00:00',
	'10.10.50.28': '2018-08-02 00:00:00',
	'127.0.0.1': '2018-08-02 00:00:00'
	}


def abort_if_ips_doesnt_exist(ip_id):
    if ip_id not in IPs:
        abort(404, message="IP {} doesn't exist".format(ip_id))


parser = reqparse.RequestParser()
parser.add_argument('update_timestamp')


class IP(Resource):
    def get(self, ip_id):
        abort_if_ips_doesnt_exist(ip_id)
        return IPs[ip_id]

    def delete(self, ip_id):
        abort_if_ips_doesnt_exist(ip_id)
        del IPs[ip_id]
        return '', 204

    def put(self, ip_id):
        args = parser.parse_args()
        print(args)
        newtime = args['update_timestamp']
        print(newtime)
        IPs[ip_id] = newtime
        return newtime, 201


# IPList
# shows a list of all ips, and check the heartbeat
class IPList(Resource):
    def get(self):
        return IPs


class Alarm(Resource):
    def put(self, ip_id):
        newtime = datetime.datetime.now()
        fp = open("alarm.log", "at")
        fp.write(ip_id + " 10 mins not move detected at %s\n" % newtime)
        fp.close()
        import pyttsx3
        import win32com
        speaker = pyttsx3.init()
        u = '欧巴~有人需要士力架!'
        speaker.say(u)
        speaker.runAndWait()
        IPs[ip_id] = str(newtime)
        return ip_id, 201


#
# Actually setup the Api resource routing here
#
api.add_resource(IPList, '/ips')
api.add_resource(IP, '/ips/<ip_id>')
api.add_resource(Alarm, '/alarm/<ip_id>')

if __name__ == '__main__':
    app.run(debug=True)
