# ** -- coding: utf-8 -- **
#!/usr/bin/env python
#
#Copyright (c) 2011 darkdarkfruit <darkdarkfruit@gmail.com>
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in
#all copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#THE SOFTWARE.
#

'''
compatable with jsend:
http://labs.omniti.com/labs/jsend

shortely:
=================================================================
A basic JSend-compliant response is as simple as this:
{{{
{
    status : "success",
    data : {
        "post" : { "id" : 1, "title" : "A blog post", "body" : "Some useful content" }
     }
}
}}}

When setting up a JSON API, you'll have all kinds of different types of calls and responses.
JSend separates responses into some basic types, and defines required and optional keys for each type:

| ''Type'' | ''Description''                                        | ''Required Keys'' | ''Optional Keys'' |
|----------+--------------------------------------------------------+-------------------+-------------------|
| success  | All went well, and (usually) some data was returned.   | status, data      |                   |
|          |                                                        |                   |                   |
| fail     | There was a problem with the data submitted,           | status, data      |                   |
|          | or some pre-condition of the API call wasn't satisfied |                   |                   |
|          |                                                        |                   |                   |
| error    | An error occurred in processing the request,           | status, message   | code, data        |
|          | i.e. an exception was thrown                           |                   |                   |

=================================================================


changelog: (2012-07-26)
In pracmatical usage, a key "message" for all responese is very convenient for development.
So add 'message' key to "Optional Keys" for type(success, fail)


| ''Type'' | ''Description''                                        | ''Required Keys''  | ''Optional Keys'' |
|----------+--------------------------------------------------------+--------------------+-------------------|
| success  | All went well, and (usually) some data was returned.   | status, code, data | message           |
|          |                                                        |                    |                   |
| fail     | There was a problem with the data submitted,           | status, code, data | message           |
|          | or some pre-condition of the API call wasn't satisfied |                    |                   |
|          |                                                        |                    |                   |
| error    | An error occurred in processing the request,           | status, message    | code, data        |
|          | i.e. an exception was thrown                           |                    |                   |





changelog: (2012-07-16)
In pracmatical usage, code representing status is very important, so add 'code' key to "Required Keys"


| ''Type'' | ''Description''                                        | ''Required Keys''  | ''Optional Keys'' |
|----------+--------------------------------------------------------+--------------------+-------------------|
| success  | All went well, and (usually) some data was returned.   | status, code, data |                   |
|          |                                                        |                    |                   |
| fail     | There was a problem with the data submitted,           | status, code, data |                   |
|          | or some pre-condition of the API call wasn't satisfied |                    |                   |
|          |                                                        |                    |                   |
| error    | An error occurred in processing the request,           | status, message    | code, data        |
|          | i.e. an exception was thrown                           |                    |                   |






this module include 3 classes:
==============================
RSuccess --> Result Success
RFail    --> Result Fail
RError   --> Result Error
==============================


'''

__all__ = ['RSuccess', 'RFail', 'RError', 'jsend_parse']

import json



class RSuccess(dict):
    """
    client successfully get the data from server.
    rs_success, result_success
    """

    def __init__(self, status='success', code=0, data={}, message='successful'):
        """init jsend structure representing: "SUCCESS"
        """
        super(RSuccess, self).__init__()
        self['status'] = status
        self['code'] = code
        self['data'] = data
        self['message'] = message # optional


    @property
    def status(self):
        """get status

        Arguments:
        - `self`:
        """
        return self['status']


    @property
    def code(self):
        """get code

        Arguments:
        - `self`:
        """
        return self['code']


    @code.setter
    def code(self, code):
        """ set code

        Arguments:
        - 'self':
        - 'code' : set code
        """
        self['code'] = code


    @property
    def data(self):
        """get data

        Arguments:
        - `self`:
        """
        return self['data']


    @data.setter
    def data(self, data):
        """ set data

        Arguments:
        - 'self':
        - 'data' : set data
        """
        self['data'] = data



    @property
    def message(self):
        """get message

        Arguments:
        - `self`:
        """
        return self['message']


    @message.setter
    def message(self, message):
        """ set message

        Arguments:
        - 'self':
        - 'message' : set message
        """
        self['message'] = message



class RFail(dict):
    """
    client can't get data from server. (Server is alright)
    rs_fail, result_fail
    """

    def __init__(self, status='fail', code=-1, data={}, message='failed'):
        """init jsend structure representing: "FAIL"
        """
        super(RFail, self).__init__()
        self['status'] = status
        self['code'] = code
        self['data'] = data
        self['message'] = message # optional


    @property
    def status(self):
        """get status

        Arguments:
        - `self`:
        """
        return self['status']


    @property
    def code(self):
        """get code

        Arguments:
        - `self`:
        """
        return self['code']


    @code.setter
    def code(self, code):
        """ set code

        Arguments:
        - 'self':
        - 'code' : set code
        """
        self['code'] = code


    @property
    def data(self):
        """get data

        Arguments:
        - `self`:
        """
        return self['data']


    @data.setter
    def data(self, data):
        """ set data

        Arguments:
        - 'self':
        - 'data' : set data
        """
        self['data'] = data



    @property
    def message(self):
        """get message

        Arguments:
        - `self`:
        """
        return self['message']


    @message.setter
    def message(self, message):
        """ set message

        Arguments:
        - 'self':
        - 'message' : set message
        """
        self['message'] = message



class RError(dict):
    """
    client can't get data from server.
    Processing is normal, but error occurs(often, it's due to server error)

    rs_fail, result_fail
    """
    def __init__(self, status='error', code=-2, data={}, message='error'):
        """init jsend structure representing: "ERROR"
        """
        super(RError, self).__init__()
        self['status'] = status
        self['code'] = code
        self['data'] = data
        self['message'] = message # optional


    @property
    def status(self):
        """get status

        Arguments:
        - `self`:
        """
        return self['status']


    @property
    def message(self):
        """get message

        Arguments:
        - `self`:
        """
        return self['message']

    @message.setter
    def message(self, msg):
        """ set error message

        Arguments:
        - 'self':
        - 'msg' : set the message
        """
        self['message'] = msg


    @property
    def code(self):
        """get code

        Arguments:
        - `self`:
        """
        return self['code']


    @code.setter
    def code(self, code):
        """get code

        Arguments:
        - `self`:
        """
        self['code'] = code


    @property
    def data(self):
        """get data

        Arguments:
        - `self`:
        """
        return self['data']


    @data.setter
    def data(self, data):
        """ set data

        Arguments:
        - 'self':
        - 'date' : set data
        """
        self['data'] = data




def jsend_parse(json_str):
    """
    parse @a_dict_json_format and return an RSuccess instance.
    if ok:
        return a parsed dict
    else:
        return @json_str        # unchanged

    Arguments:
    - `self`:
    - `json_str`:
    """
    # 1. it must be able to loads to json
    try:
        d = json.loads(json_str)
    except Exception as e:
        print('Error: Could not json.loads @json_str: %s. @json_str should be in json format. \nException is: %s' % (json_str, e))
        return json_str

    _j = None
    if not d.has_key('status') or d['status'] not in ['success', 'fail', 'error']:
        print('Error: Valid jsend format should have key: "status"\n. And the value of :"status" should be one of "success", "fail" or "error"')
        return json_str

    status = d['status']

    r = None
    if status == 'success':     # should be RSuccess
        r = RSuccess(**d)
    elif status == 'fail' :     # should be RFail
        r = RFail(**d)
    else:                       # should be RError
        r = RError(**d)

    return r
