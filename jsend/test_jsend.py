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
import json
# from  .jsend import RSuccess, RFail, RError
from .jsend import *

def test_jsend():
    rs = RSuccess()
    rf = RFail()
    rr = RError()
    lst = [rs] + [rf] + [rr]

    assert rs.status == 'success'
    assert rf.status == 'fail'
    assert rr.status == 'error'
    assert rs.message == ''
    assert rf.message == ''
    assert rr.message is not None

    # check code initial
    assert rs.code == 0 and rf.code == 0

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

    # test data part
    for i in lst:
        try:
            i.data = 'This is data'
        except Exception as e:
            print(e)
            assert False

    # test RError's code part
    try:
        rr.code = 404
    except Exception as e:
        print(e)
        assert False


    # test code part
    for i in lst:
        try:
            i.code = 200
        except Exception as e:
            print(e)
            assert False


    # test message part
    for i in lst:
        try:
            msg = 'This a test message'
            i.message = msg
            assert i.message == msg
        except Exception as e:
            print(e)
            assert False



    #     try:
    #         i.data = 'abc'
    #     except AttributeError as e:
    #         assert e
    #     else:
    #         assert False

    # try:
    #     rr.code = 'code'
    # except AttributeError as e:
    #     assert e
    # else:
    #     assert False


def test_jsend_parse():
    rs = RSuccess()
    rf = RFail()
    re = RError()
    s_rs = json.dumps(rs)
    s_rf = json.dumps(rf)
    s_re = json.dumps(re)

    rs.data = { k : v for (k, v) in zip(['a', 'b', 'c'], [3, 4, 5])}
    rs_json = json.dumps(rs)
    assert jsend_parse(rs_json) == rs

    rf.data = { k : v for (k, v) in zip(['a', 'b', 'c'], [3, 4, 5])}
    rf_json = json.dumps(rf)
    assert jsend_parse(rf_json) == rf

    re.data = { k : v for (k, v) in zip(['a', 'b', 'c'], [3, 4, 5])}
    re_json = json.dumps(re)
    assert jsend_parse(re_json) == re

    ## put some malformed jsend-str
    # rs
    mal_rs = rs
    mal_rs['status'] = 'what-status'
    mal_rs_json = json.dumps(mal_rs)
    assert jsend_parse(mal_rs_json) == mal_rs_json
    mal_rs.pop('status')
    mal_rs_json = json.dumps(mal_rs)
    assert jsend_parse(mal_rs_json) == mal_rs_json

    # rf
    mal_rf = rf
    mal_rf['status'] = 'what-status'
    mal_rf_json = json.dumps(mal_rf)
    assert jsend_parse(mal_rf_json) == mal_rf_json
    mal_rf.pop('status')
    mal_rf_json = json.dumps(mal_rf)
    assert jsend_parse(mal_rf_json) == mal_rf_json

    # re
    mal_re = re
    mal_re['status'] = 'what-status'
    mal_re_json = json.dumps(mal_re)
    assert jsend_parse(mal_re_json) == mal_re_json
    mal_re.pop('status')
    mal_re_json = json.dumps(mal_re)
    assert jsend_parse(mal_re_json) == mal_re_json

    # clearly not jsend format str
    strs = ['{wo}', 'aowfa', '{"b" : c}', '{"data" : {"a" : "ok" }}']
    for k in strs:
        assert jsend_parse(k) == k


if __name__ == '__main__':
    test_jsend()
    test_jsend_parse()
