JSEND MODIFIED DRAFT
=====================

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


