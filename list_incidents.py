#!/usr/bin/env python
#
# Copyright (c) 2016, PagerDuty, Inc. <info@pagerduty.com>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of PagerDuty Inc nor the
#       names of its contributors may be used to endorse or promote products
#       derived from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL PAGERDUTY INC BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import requests
import json

# Update to match your API key
API_KEY = '<Enter the API key>'

# Update to match your chosen parameters
SINCE = ''
UNTIL = ''
DATE_RANGE = ''
STATUSES = ['triggered']
INCIDENT_KEY = ''
SERVICE_IDS = []
TEAM_IDS = ['']
USER_IDS = []
URGENCIES = []
TIME_ZONE = 'UTC'
SORT_BY = []
INCLUDE = []
inc = []
CONTENT = "."

# Update to match your email address
EMAIL = ''

# Update to match your chosen parameters for the incident

TYPE = 'incident'
SUMMARY = '.'
STATUS = 'acknowledged'
ESCALATION_LEVEL = 1
ASSIGNED_TO_USER = ''
ESCALATION_POLICY = ''

def list_incidents():

    url = 'https://api.pagerduty.com/incidents'
    headers = {
        'Accept': 'application/vnd.pagerduty+json;version=2',
        'Authorization': 'Token token={token}'.format(token=API_KEY)
    }
    payload = {
        'since': SINCE,
        'until': UNTIL,
        'date_range': DATE_RANGE,
        'statuses[]': STATUSES,
        'incident_key': INCIDENT_KEY,
        'service_ids[]': SERVICE_IDS,
        'team_ids[]': TEAM_IDS,
        'user_ids[]': USER_IDS,
        'urgencies[]': URGENCIES,
        'time_zone': TIME_ZONE,
        'sort_by[]': SORT_BY,
        'include[]': INCLUDE
    }
    r = requests.get(url, headers=headers, params=payload)
    print('Status Code: {code}'.format(code=r.status_code))
    out = r.json()
    print(len(out['incidents']))
    for i in range(len(out['incidents'])):
        if len(out['incidents']) > 0:
            print(out['incidents'][i])
            update_incident(out['incidents'][i]['id'])



def update_incident(incident_update):
    url = 'https://api.pagerduty.com/incidents/{id}'.format(id=incident_update)
    headers = {
        'Accept': 'application/vnd.pagerduty+json;version=2',
        'Authorization': 'Token token={token}'.format(token=API_KEY),
        'Content-type': 'application/json',
        'From': EMAIL
    }
    payload = {
        'incident': {
            'type': TYPE,
            'summary': SUMMARY,
            'status': STATUS,
            'escalation_level': ESCALATION_LEVEL,
            'assigned_to_user': ASSIGNED_TO_USER,
            'escalation_policy': ESCALATION_POLICY
        }
    }
    r = requests.put(url, headers=headers, data=json.dumps(payload))
    print('Status Code: {code}'.format(code=r.status_code))
    print(r.json())


if __name__ == '__main__':
    list_incidents()

