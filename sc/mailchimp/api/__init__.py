# -*- coding: utf-8 -*-
# Cleber J Santos <cleber@simplesconsultoria.com.br>

import urllib
import urllib2
import re
from StringIO import StringIO
import errorcodes
import os

try:
    import json
except ImportError:
    try:
        import simplejson as json
    except ImportError:
        raise ImportError("Please install the simplejson package, easy_install simplejson")

class MailChimpError(Exception):
    msg = None
    code = None
    errorcodes = errorcodes.responses

    def __init__(self, code=code,msg=msg):
        self.msg = msg
        self.code = code

    def __call__(self):
        try:
            errormsg = ', '.join(self.errorcodes[int(self.code)])
        except KeyError, e:
            errormsg = self.msg
        except ValueError, e:
            errormsg = self.msg

        return {'status':self.code or 000,'msg':'Message: %s - %s' %(self.code,errormsg)}

class MailChimp(object):
    """
    MailChimp API Version 1.3
    http://apidocs.mailchimp.com/1.3/
    """

    apikey = None #myKeyFromMailChimpApi - Info: https://us2.admin.mailchimp.com/account/api/
    ssl = True # If True use https protocol else use http protocol
    debug_mode = False #Debug mode off is default
    user_agent = "sc.mailchimp.api"
    errorcodes = errorcodes.responses
    headers = {}
    api_version = '1.3'

    def __init__(self, apikey=apikey, ssl=ssl,debug_mode=debug_mode):
        try:
            self.dc = apikey.rsplit('-', 1)[-1]
        except AttributeError, e:
            merror = MailChimpError(e['code'],e['error'])
            return merror()

        self.apikey = apikey
        self.tableerrors = self.errorcodes
        self.err = None
        self.debug_mode = debug_mode
        if ssl:
            self.protocol = 'https'
        else:
            self.protocol = 'http'

        self.urlbase = "%s://%s.api.mailchimp.com/%s/" % (self.protocol, self.dc, self.api_version)

    def __call__(self, **kwargs):
        if self.apikey:
            kwargs['apikey'] = self.apikey

        if "user-agent" not in self.headers:
            self.headers['user-agent'] = self.user_agent

        data = urllib.urlencode(kwargs)
        urlfull = self.urlbase + '?' + data

        if self.debug_mode:
           print 'URL:', self.urlbase
           print 'URL Full:', urlfull
           print 'POST data:', data
           print 'API Version:', self.api_version
           print 'API Key:', self.apikey
           print 'User Agent:', self.user_agent
           print 'Headers:', self.headers

        req = urllib2.Request(urlfull,headers=self.headers or {})

        try:
            handle = urllib2.urlopen(req)
        except urllib2.HTTPError, e:
            if (e.code == 304):
                return []
            else:
               self.err = e.code
        except urllib2.URLError, e:
            if hasattr(e, 'reason'):
                self.err = {'code':000,'error':'We failed to reach a server. Reason: %s' % str(e.reason)}
            elif hasattr(e, 'code'):
                self.err = e.code

        if self.err is None:
            if handle.code == 200 and handle.msg.lower() == 'ok':
                status = 200

            resp = handle.read()
            io = StringIO(resp)
            jsReturned = json.load(io)

            if 'error' in jsReturned:
                merror = MailChimpError(jsReturned['code'],jsReturned['error']) 
                return merror()
            else:
                try:
                    jsReturned['status'] = status
                except TypeError, e:
                    pass
        else:
            if self.err.has_key('error'):
                jsReturned = MailChimpError(self.err['code'],self.err['error'])()
            else:
                jsReturned =  MailChimpError(self.err['code'])()

        return jsReturned
