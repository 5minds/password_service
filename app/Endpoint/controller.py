from Service import WiFiPasswords as Service1
from Service import Passwords as Service2

def get_resources(api):
    api.add_resource(Service1.WiFiPasswords, '/passwords/wifi')
    api.add_resource(Service2.Passwords, '/passwords')
    return api
