# Copyright 2020 Adobe
# All Rights Reserved.

# NOTICE: Adobe permits you to use, modify, and distribute this file in
# accordance with the terms of the Adobe license agreement accompanying
# it.
# A splunk plugin developed for sending alerts from Splunk
# to a webhook endpoint with customer payload
# Developed by:
#     Ankit Tyagi
#     SRE - Adobe
#################################################################

# Meta
# File location on Splunk: $SPLUNK_HOME$/etc/apps/customWebhook_app/bin/customWebhook.py
#

from __future__ import print_function
from future import standard_library
standard_library.install_aliases()
import sys, json
import requests

def process_args(*args):
    return json.dumps(args)

def send_alert_data(*args):
    args = json.loads(process_args(*args))
    for config in args:
      if 'headers' in config:
        headers = config.get('headers')
        headers = headers.replace("'", '"')
        headers = json.loads(headers)

      if 'payload' in config:
        data = config.get('payload')
        data = data.replace("'", '"')

      if 'base_url' in config:
        url = config.get('base_url')

      if 'alert_source' in config:
          alert_source = config.get('alert_source')
          data = json.loads(data)
          data['alert_source'] = alert_source
          data = json.dumps(data)
    try:
        alert_source = alert_source.encode('utf-8')
        res = requests.post(url=url, data=data, headers=headers)
        print("Server response: %s" % json.dumps(res.json()), file=sys.stderr)
        return 200 <= res.status_code < 300
    except requests.exceptions.RequestException as e:
        print("ERROR Error sending message: %s" % e, file=sys.stderr)
        return False

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--execute":
        payload = json.loads(sys.stdin.read())
        if not send_alert_data(payload.get('configuration')):
            print("Failed trying to send alert notification", file=sys.stderr)
            sys.exit(2)
        else:
            print("INFO alert notification successfully sent", file=sys.stderr)
    else:
        print("FATAL Unsupported execution mode (expected --execute flag)", file=sys.stderr)
        sys.exit(1)
