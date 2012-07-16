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

changelog: (2012-07-16)
in pracmatical usage, code representing status is very import, so add 'code' key to "Required Keys"


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

__all__ = ['RSuccess', 'RFail', 'RError']



class RSuccess(dict):
    """
    client successfully get the data from server.
    rs_success, result_success
    """
    
    def __init__(self, ):
        """init
        """
        super(RSuccess, self).__init__()
        self['status'] = 'success'
        self['code'] = 0
        self['data'] = {}

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
        """ set error message
        
        Arguments:
        - 'self':
        - 'msg' : set the message
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
        """ set error message
        
        Arguments:
        - 'self':
        - 'msg' : set the message
        """
        self['data'] = data
        



class RFail(dict):
    """
    client can't get data from server. (Server is alright)
    rs_fail, result_fail
    """
    
    def __init__(self, ):
        """init
        """
        super(RFail, self).__init__()
        self['status'] = 'fail'
        self['code'] = 0
        self['data'] = {}

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
        """ set error message
        
        Arguments:
        - 'self':
        - 'msg' : set the message
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
        """ set error message
        
        Arguments:
        - 'self':
        - 'msg' : set the message
        """
        self['data'] = data




class RError(dict):
    """
    client can't get data from server. 
    Processing is normal, but error occurs(often, it's due to server error)

    rs_fail, result_fail
    """
    
    def __init__(self, ):
        """init
        """
        super(RError, self).__init__()        
        self['status'] = 'error'
        self['message'] = 'error occurs during processing'
        self['code'] = {} #optional
        self['data'] = {} #optional

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
        """ set error message
        
        Arguments:
        - 'self':
        - 'msg' : set the message
        """
        self['data'] = data
