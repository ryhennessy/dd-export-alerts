#!/usr/bin/python

from datadog import initialize, api
import json
import argparse
import os

######################################################################
# Define the App and the API key below or you will need to supply it 
# them as CLI options.
#####################################################################

APIKEY=""
APPKEY="" 


def validate_key (default_key, key):
   if default_key == "" and key == None: 
         print ("Please provide a valide Datadog App and API key either on the command line or as constants in the script")
         exit ()
   elif default_key != "" and key == None:
         return default_key
   else:
         return key

def dump_all_monitors ():
     print ("Dumping the monitor list from Datadog")
     monitors = api.Monitor.get_all()

     #Dump Monitor Definitions each in their own file
     for  monitor in monitors:
        filename = monitor['name'].replace("/", "-")
        filename = filename + ".json"
        fp = open(filename, "w")
        fp.write(json.dumps(monitor, indent=4))
        fp.close()

def import_monitor (filename):
    if os.path.exists(filename):
       print ("Importing into Datadog the monitor: ", filename)
       fp = open(filename, 'r')
       data = json.load(fp)
       fp.close()
       api.Monitor.update(data['id'], query=data['query'], name=data['name'], message=data['message'], options=data['options'], tags=data['tags'])
    else:
       print ("Unable able to open file: ", filename)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Simple script that will either dump all the Datadog monitor configuration or import a single one")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-d", "--dump", action="store_true", help="Dump all the monitor configurations to current working directory")
    group.add_argument("-s", "--send", action="store", help="Import a single moniitor configuration by filename")
    parser.add_argument("-a", "--apikey", action="store", help="The Datadog API key")
    parser.add_argument("-p", "--appkey", action="store", help="The Datadog App key")
    args = parser.parse_args()


    #######Build the initial connection to Datadog with correct API and APP keys 
    ###### Validate which key value is valid. (CLI Argument or Constant Above.  Default: CLI KEY) 
    options={}
    options.update({'app_key': validate_key(APPKEY, args.appkey)})
    options.update({'api_key': validate_key(APIKEY, args.apikey)})
    initialize(**options)

    if args.dump:
       dump_all_monitors()
    elif args.send != None:
       import_monitor(args.send)
    else:
       print ("Please provide either an import or dump command")

