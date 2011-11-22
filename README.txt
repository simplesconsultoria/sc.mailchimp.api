.. contents:: Table of Contents
   :depth: 2

sc.mailchimp.api
*******************************************************************

Overview
--------

Python wrapper for the MailChimp API


Requirements
------------

    - Python >= 2.4 (http://python.org/download/)
    - simplejson >= 2.2.1 (http://pypi.python.org/pypi/simplejson)


Installation
------------

To enable this product,on a buildout based installation:

    1. Edit your buildout.cfg and add ``sc.mailchimp.api``
       to the list of eggs to install ::

        [buildout]
        ...
        eggs = 
            sc.mailchimp.api

After updating the configuration you need to run the ''bin/buildout'',
which will take care of updating your system.


Usage
-----

* Parameters

 * apikey (Your MailChimp API key eg.: 11f4654fg78g546g76876gsddsf657d3ffb-us2)
 * debug_mode (Is optional, True or False. False is default)
 * ssl (Is optional, True or False for used https protocol. True is default)


* Parameters for classe instance

 * method (More info in http://apidocs.mailchimp.com/1.3. eg.: getAccountDetails)
 * output (Output Formats for Serialized calls. json is default. eg.: json, php,xml or lolcode)
 * Others parameters (Each method requires a certain parameter, the information in the API eg.:
    mc(method='listMemberInfo',id='List X', email_address='cleber@simplesconsultoria.com').


>>> from sc.mailchimp.api import MailChimp
>>> mc = MailChimp(apikey='11f4654fg78g546g76876gsddsf657d3ffb-us2',debug_mode=True)
>>> inst = mc(method='getAccountDetails',output='json')
>>> inst


Sponsoring
----------

    * Development of this product was sponsored by:
        
        * `Simples Consultoria  <http://www.simplesconsultoria.com.br/>`_.


Credits
-------

    * Cleber J Santos (cleber at simplesconsultoria dot com dot br) - 
      Idea and implementation.
