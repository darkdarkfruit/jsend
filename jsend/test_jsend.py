# ** -- coding: utf-8 -- **
# !/usr/bin/env python
#
# Copyright (c) 2011 darkdarkfruit <darkdarkfruit@gmail.com>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
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
import json
# from  .jsend import RSuccess, RFail, RError
from .jsend import *


def test_jsend():
    msg = make_successful_message()
    msg.status = STATUS_SUCCESSFUL
    msg.code = 100
    msg.data = {'hey': 'you, world, successful'}
    msg.desc = 'aloha'
    assert msg.is_successful()
    assert not msg.is_failed()
    assert msg.code == 100
    msg.code = 200
    assert msg.code == 200
    desc = 'desc changed'
    msg.desc = desc
    assert msg.desc == desc
    data = {'hey': 'what'}
    msg.data = data
    assert msg.data == data
    msg.status = STATUS_FAILED
    assert msg.status == STATUS_FAILED

    msg.status = STATUS_SUCCESSFUL
    msg.status = 'Any other status'
    assert msg.status == STATUS_SUCCESSFUL  # not change when setting invalid status

    code = 0
    data = {'body': 'way to go'}
    desc = 'description: test message'
    meta = ['127.0.0.1', 'google.com']
    d = {
        'status': 'S',
        'code': code,
        'data': data,
        'desc': desc,
        'meta': meta
    }
    msg = Message.load_from_dict(d)
    assert not msg.is_failed()
    assert msg.is_successful()
    assert msg.code == code
    assert msg.data == data
    assert msg.desc == desc
    assert msg.meta == meta

    msg = Message.loads(json.dumps(d))
    assert not msg.is_failed()
    assert msg.is_successful()
    assert msg.code == code
    assert msg.data == data
    assert msg.desc == desc
    assert msg.meta == meta
    d = msg.as_dict()
    for k, v in d.items():
        assert v == getattr(msg, k)
        assert v == msg[k]

    msg2 = Message.loads(msg.dumps())
    assert sorted([k, v] for k, v in msg.items()) == sorted([k, v] for k, v in msg2.items())

    msg2 = Message.loads(msg.dumps(skip_none=True))
    assert sorted([k, v] for k, v in msg.items()) == sorted([k, v] for k, v in msg2.items())
    assert 'code' in msg2
    msg2.code = None
    msg2.data = None
    msg2.desc = None
    msg2.meta =  None

    d3 = json.loads(msg2.dumps(skip_none=True))
    assert not 'code' in d3
    assert not 'data' in d3
    assert not 'desc' in d3
    assert not 'meta' in d3

    msg = make_successful_message(0, {'hello': 'world'}, 'description', 'meta')
    assert msg.is_successful()
    assert msg.code == 0

    msg = make_failed_message(0, {'hello': 'world'}, 'description', 'meta')
    assert msg.is_failed()
    assert msg.code == 0


if __name__ == '__main__':
    test_jsend()
