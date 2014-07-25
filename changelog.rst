version 0.7.1 released at 2014-07-25

====================================
changelog:
    fix a minor pychecker warning(Local variable (_j) not used)




version 0.7.0 released at 2014-07-13
====================================
changelog:
    fixed critical bug: new dict instance not dict reference.
    eg:
        # return a new dict instance(not reference) of dict(data)
        self['data'] = dict(data) if isinstance(data, dict) else data




version 0.6.0 released at 2014-07-12
====================================
changelog:
    make RSuccess, RFail, RError take default parameters in __init__ method.


version 0.5.1 released at 2012-08-09.
====================================
changelog:
    add a function parse_jsend(jsend_str)
        return a jsend object if @jsend_str is a valid jsend-json str else return original @jsend_str


version 0.5.0 2012-07-26 released
====================================
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







version 0.4.0 2012-07-16 released
====================================
    fix: in pracmatical usage, code representing status is very
    import, so add 'code' key to "Required Keys" for "type" of
    "success", "fail". See the table below


| ''Type'' | ''Description''                                        | ''Required Keys''  | ''Optional Keys'' |
|----------+--------------------------------------------------------+--------------------+-------------------|
| success  | All went well, and (usually) some data was returned.   | status, code, data |                   |
|          |                                                        |                    |                   |
| fail     | There was a problem with the data submitted,           | status, code, data |                   |
|          | or some pre-condition of the API call wasn't satisfied |                    |                   |
|          |                                                        |                    |                   |
| error    | An error occurred in processing the request,           | status, message    | code, data        |
|          | i.e. an exception was thrown                           |                    |                   |



version 0.3.0 2012-06-13 released
====================================
    fix: add setter for data(RSuccess, RFail, RError),
         add setter for code(RError)

version 0.2.4 2011-11-19 released
====================================

version 0.2.2 2011-11-18 released
====================================
