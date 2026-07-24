import json, os, urllib.request
from django.conf import settings
class ZabbixAPIClient:
    def __init__(self, url=None, user=None, password=None):
        self.url = url or os.getenv('ZABBIX_URL', settings.ZABBIX_URL)
        self.user = user or os.getenv('ZABBIX_USER', settings.ZABBIX_USER)
        self.password = password or os.getenv('ZABBIX_PASSWORD', settings.ZABBIX_PASSWORD)
        self.auth = None
    def call(self, method, params=None, auth=None):
        data={'jsonrpc':'2.0','method':method,'params':params or {},'id':1}
        token = self.auth if auth is None else auth
        if token: data['auth']=token
        req=urllib.request.Request(self.url, data=json.dumps(data).encode(), headers={'Content-Type':'application/json'})
        with urllib.request.urlopen(req, timeout=10) as resp:
            payload=json.loads(resp.read().decode())
        if 'error' in payload: raise RuntimeError(payload['error'])
        return payload.get('result')
    def api_version(self): return self.call('apiinfo.version', auth=False)
    def login(self):
        self.auth = self.call('user.login', {'username':self.user,'password':self.password}, auth=False); return self.auth
    def validate_connection(self): return {'version': self.api_version(), 'logged': bool(self.login())}
    def list_hosts(self):
        if not self.auth: self.login()
        return self.call('host.get', {'output':['hostid','host','name','status']})
    def list_problems(self):
        if not self.auth: self.login()
        return self.call('problem.get', {'output':'extend', 'recent':'true'})
    def list_triggers(self):
        if not self.auth: self.login()
        return self.call('trigger.get', {'output':['triggerid','description','priority','value']})
    def list_items(self):
        if not self.auth: self.login()
        return self.call('item.get', {'output':['itemid','name','key_','value_type','status'], 'limit': 200})
    def validate_lab_task(self, task_code):
        if task_code == 'problems_ativos': return len(self.list_problems()) > 0
        if task_code == 'hosts_cadastrados': return len(self.list_hosts()) > 0
        return False
