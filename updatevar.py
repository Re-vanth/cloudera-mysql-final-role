import yaml
from yaml import load, dump

prop_file_name = 'properties.yml'
var_file_name = './group_vars/all.yml'
hosts_file = 'hosts'

def readproperties():
    with open(prop_file_name) as f:
        data = yaml.load(f, Loader=yaml.Loader)
    return data

def updatehosts(data):
    f= open(hosts_file,"w+")
    for key,val in data["hosts"].items():
        f.write("[%s]\n" %key)
        f.write("%s\n" %val)
    f.close()

def updatevars(data):
    with open(var_file_name, "w") as f:
        f.write("---\n")
        for key,val in data["variables"].items():
            if(key=="kdc_admin_user"):
                f.write("%s:" %key)
                f.write('"%s"\n' %val)
            else:
                f.write("%s:" %key)
                f.write(" %s\n" %val)

        f.close 

properties = readproperties()
updatehosts(properties)
updatevars(properties)
