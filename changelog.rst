version 0.4.0 2012-07-16 released
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
    fix: add setter for data(RSuccess, RFail, RError), 
         add setter for code(RError)

version 0.2.4 2011-11-19 released

version 0.2.2 2011-11-18 released
