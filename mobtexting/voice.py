import requests


class Voice:
    api_endpoint = 'https://portal.mobtexting.com/api/v2/'

    def __init__(self, access_token):
        self.access_token = access_token
        self.headers = {
            'Accept': 'application/json',
            'Authorization': access_token
        }

    def c2c(self, bridge, _from, to, data={}):
        url = self.api_endpoint + 'voice/c2c?access_token=' + self.access_token + '&bridge=' + bridge + '&from=' + _from + '&to=' + to
        r = requests.get(url, headers=self.headers, data=data)
        return r

    def c2c_post(self, bridge, _from, to, data={}):
        url = self.api_endpoint + 'voice/c2c?access_token=' + self.access_token + '&bridge=' + bridge + '&from=' + _from + '&to=' + to
        r = requests.post(url, headers=self.headers, data=data)
        return r

    def call_logs(self, start_date, end_date):
        url = self.api_endpoint + 'voice/calls?access_token=' + self.access_token + '&datetime[end_at]=' + start_date + '-' + end_date
        response = requests.get(url, headers=self.headers)
        return response

    def recordings(self, start_date, end_date):
        url = self.api_endpoint + 'voice/calls?access_token=' + self.access_token + '&datetime[r.created_at]=' + start_date + '+' + end_date
        response = requests.get(url, self.headers)
        return response
