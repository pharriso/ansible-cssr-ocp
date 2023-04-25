import json
file = open('/etc/128technology/local.init', 'r')
data = json.load(file)
data['cpuProperties']['cores'] = 2
file = open('/etc/128technology/local.init', 'w')
json.dump(data, file, indent=4)
file.close()
