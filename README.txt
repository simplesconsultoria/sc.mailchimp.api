Introduction
============

Python wrapper for the MailChimp API

Usage
-----

- Parameters

 * apikey (Your MailChimp API key eg.: 11f4654fg78g546g76876gsddsf657d3ffb-us2)
 * debug_mode (Is optional, True or False. False is default)
 * ssl (Is optional, True or False for used https protocol. True is default)

- Parameters for classe instance

 * method (More info in http://apidocs.mailchimp.com/1.3. eg.: getAccountDetails)
 * output (Output Formats for Serialized calls. json is default. eg.: json, php,xml or lolcode)
 * Others parameters (Each method requires a certain parameter, the information in the API eg.: mc(method='listMemberInfo',id='List X', email_address='cleber@simplesconsultoria.com.

>>> from sc.mailchimp.api import MailChimp
>>> mc = MailChimp(apikey='11f4654fg78g546g76876gsddsf657d3ffb-us2',debug_mode=True)
>>> inst = mc(method='getAccountDetails',output='json')
>>> inst
