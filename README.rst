What is it?
============
a python jsend module.
compatable with jsend: http://labs.omniti.com/labs/jsend


Shortely: (borrowed from http://labs.omniti.com/labs/jsend)
=================================================================
"""
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

"""

This module includes 3 classes:
==============================
RSuccess --> Result Success

RFail    --> Result Fail

RError   --> Result Error


