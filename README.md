# pyoauth4twitter 1.0

Provide a convenient way of obtaining access tokens &amp; authorizing HTTP requests

You need to provide some information before demo get ready to work.

Go to [My applications](https://dev.twitter.com/apps), select one application (if you don't have one, you should [create one](https://dev.twitter.com/apps/new)).

All information that might required is in application's "Details" page, including:

* Consumer key
* Consumer secret
* Callback URL
* Access token (optional)
* Access token secret (optional)

(Note that you might not have access token and access token sercet, it is OK except that you cannot skip the first step in demo, for the purpose of generating them)

make a copy of 'config-example.py', rename it to 'config.py'

`cp config-example.py config.py`

Edit config.py , fill in fields as needed

Your demo are ready now ! 

`python deom.py`

Our demo has two parts, both of which can be skipped. 

1. For the first part, it will attempt to obtain an access token 

2. For the second part, query profile of user @twitter and output it to stdout

Read demo.py and you can easily figure out how to use our oauth lib!
