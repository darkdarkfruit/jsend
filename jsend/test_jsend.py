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
jsend test
==========
You should have py.test installed first.
pip install -U pytest

Then, run
>> py.test  test_jsend.py



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

When setting up a JSON API, you'll have all kinds of different types of calls and responses.  JSend separates responses into some basic types, and defines required and optional keys for each type:

||''Type''||''Description''||''Required Keys''||''Optional Keys''||
||success ||All went well, and (usually) some data was returned.||status, data||||
||fail    ||There was a problem with the data submitted, or some pre-condition of the API call wasn't satisfied||status, data||||
||error   ||An error occurred in processing the request, i.e. an exception was thrown||status, message||code, data||
=================================================================

this module include 3 classes:
==============================
RSuccess --> Result Success
RFail    --> Result Fail
RError   --> Result Error
==============================

test_jsend.py
'''

from  jsend import RSuccess, RFail, RError

def test_jsend():
    rs = RSuccess()
    rf = RFail()
    rr = RError()
    lst = [rs] + [rf] + [rr]

    assert rs.status == 'success'
    assert rf.status == 'fail'
    assert rr.status == 'error'
    assert rr.message is not None

    for i in lst:
        i.data['hello'] = 'hello'
        assert i.data['hello'] == 'hello'

    rr.message = 'server error'
    assert rr.message == 'server error'

    rr.code['stack'] = 'stack info...'
    assert rr.code['stack'] == 'stack info...'

    
    # test property. can read, but can not write
    for i in lst:
        try:
            i.status = 'abc'
        except AttributeError as e:
            assert e
        else:
            assert False

        try:
            i.data = 'abc'
        except AttributeError as e:
            assert e
        else:
            assert False

    try:
        rr.code = 'code'
    except AttributeError as e:
        assert e
    else:
        assert False
    
