#  What is it?

  A python jsend module with simplication and modification attached.


#  Note:
  python version: >=3.5

  (For python2.7 version, use jsend_version < 0.9, eg: https://github.com/darkdarkfruit/jsend/releases/tag/v_0.7.1)


# JSEND MODIFIED DRAFT


    ## Original jsend link:
    [https://labs.omniti.com/labs/jsend](https://labs.omniti.com/labs/jsend)


    ## What's modified:
    ### Fields:


    |--------+--------+----------+----------+-------------------------------------------------------|
    | Field  | type   | Required | Optional | Meaning                                               |
    |--------+--------+----------+----------+-------------------------------------------------------|
    | status | string | * (S/F)  |          | Is the response successful?                           |
    | code   | any    |          | *        | CODE for application logic(Normally it is an integer) |
    | data   | any    |          | *        | Data(payload) of the response                         |
    | desc   | any    |          | *        | Description: normally it's a helping infomation       |
    | meta   | any    |          | *        | eg: servers/ips chain in distributed env.             |
    |        |        |          |          |                                                       |
    |--------+--------+----------+----------+-------------------------------------------------------|

* Field:status is always in state: "S" or "F"(represents "Successful", "Failed"), no 3th state.
    * original states: ('success', 'fail', 'error')
        It's too much pain to distinguish fail or error, so 2 states("S", "F") are enough.

* (-) Removed original "message" field, as it is vague. (A whole message? A helping text?)

* (+) Add field:desc to describe this message. (The field is optional)

* (+) Add field:meta to add some meta infomation. (eg: network chain, node name, proxy info, ...)





#  Install:
  pip install python-jsend or (pip3 install python-jsend)
  Or
  download the tarbal, decompress it, then run "python setup.py install"

#  Test:
      > pip3 install pytest
      > whereis pytest
      > pytest: /usr/local/bin/pytest
      > pytest --version
      > This is pytest version 3.3.2, imported from /usr/local/lib/python3.6/site-packages/pytest.py
      >
      > pytest jsend/

*  Very simple: only need to use 1 class and 2 functions.
  * 1 class:     Message
  * 2 functions: make_successful_message, make_failed_message


*  Usage: (sample)

  
    Python 3.6.2 (default, Aug 10 2017, 10:07:10) 
    Type 'copyright', 'credits' or 'license' for more information
    IPython 6.1.0 -- An enhanced Interactive Python. Type '?' for help.
    
    In [1]: import jsend
       ...: 
    
    In [2]: jsend.__version__
       ...: 
    Out[2]: '0.9'
    
    In [3]: msg = jsend.make_successful_message(code=0, data={'payload' : 'yes'})
       ...: 
    
    In [4]: msg
    Out[4]: 
    {'code': 0,
     'data': {'payload': 'yes'},
     'desc': None,
     'meta': None,
     'status': 'S'}
    
    In [5]: msg.dumps()
    Out[5]: '{"status": "S", "code": 0, "data": {"payload": "yes"}, "desc": null, "meta": null}'
    
    In [6]: msg.dumps(skip_none=True)
    Out[6]: '{"status": "S", "code": 0, "data": {"payload": "yes"}}'
    
    In [7]: msg_failed = jsend.make_failed_message()
       ...: 
    
    In [8]: msg_failed
    Out[8]: {'code': None, 'data': None, 'desc': None, 'meta': None, 'status': 'F'}
    
    In [9]: msg_failed.dumps()
    Out[9]: '{"status": "F", "code": null, "data": null, "desc": null, "meta": null}'
    
    In [10]: msg_failed.dumps(skip_none=True)
    Out[10]: '{"status": "F"}'
    
    In [11]: msg_loaded = jsend.Message.loads(msg.dumps())
        ...: 
    
    In [12]: msg_loaded
    Out[12]: 
    {'code': 0,
     'data': {'payload': 'yes'},
     'desc': None,
     'meta': None,
     'status': 'S'}
    
    In [13]: msg_loaded.data = 0
    
    In [14]: msg_loaded = jsend.Message.loads(msg.dumps())
        ...: 
    
    In [15]: msg_loaded
    Out[15]: 
    {'code': 0,
     'data': {'payload': 'yes'},
     'desc': None,
     'meta': None,
     'status': 'S'}
    
    In [16]: msg_loaded.dumps()
    Out[16]: '{"status": "S", "code": 0, "data": {"payload": "yes"}, "desc": null, "meta": null}'
    
    In [17]: msg_loaded.dumps(skip_none=True)
    Out[17]: '{"status": "S", "code": 0, "data": {"payload": "yes"}}'
    
    In [18]: 
