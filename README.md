# dd-export-alerts
## Purpose
This basic script will either dump all the monitor definitions from your account or update an existing monitor defintion from a dumped configuration file.   This is meant to help maintain the lifecycle of the Dataodg monitors outside of the tool.    This script comes with no support or warranties.   

## Use
The tool has the following command line options.   By using these command line options you can either dump all the monitor configurations to seperate files in the current working directory or update an existing monintor with a JSON monitor defintion.    You have the option of supplying the Datadog App and API key on the command line or as variables in the scirpt.    The values provided at the commmand line have the high precedence over the supplied variables. 

```
usage: dd-alert-manage.py [-h] [-d | -s SEND] [-a APIKEY] [-p APPKEY]

Simple script that will either dump all the Datadog monitor configuration or
import a single one

optional arguments:
  -h, --help            show this help message and exit
  -d, --dump            Dump all the monitor configurations to current working
                        directory
  -s SEND, --send SEND  Import a single moniitor configuration by filename
  -a APIKEY, --apikey APIKEY
                        The Datadog API key
  -p APPKEY, --appkey APPKEY
                        The Datadog App key
```   

## Upadtes
This is the intial version of this script.   I will happily take suggestions or PR updates.   


