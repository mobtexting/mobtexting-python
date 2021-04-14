# python plugin for mobtexting

This package makes it easy to send [Mobtexting notifications](https://mobtexting.com).

## Installation

You can install the package via pip :

``` bash
pip instal 
 l git+git://github.com/mobtexting/mobtexting-python.git --user
```

## Send SMS Usage

```python
from mobtexting.client import Client

access_token = 'xxxxxxxxxxxxxxxxxx'

client = Client(access_token)

response = client.send(
    to="1234567890",
    _from="MobTxt",
    body="Hello from Python!",
    service="P"
)

print response.json()
```
##Voice
### Voice Click2call
```python
from mobtexting.voice import Voice
# enter the following details
access_token = 'XXXXXXXXXXXXX'
bridge="DID Number"
_from="number with country code"
to="Phone number with Country Code / IVR flow to which call has to connect"

voice = Voice(access_token)
response=voice.c2c( bridge, _from,  to)
print(response.json())
```
### Voice  Call Logs Report
```python
start_date="mm/dd/yyyy"
end_date="mm/dd/yyyy"
response=voice.call_logs(start_date,end_date)
print(response.json())
```

### Voice  Call Recording Report
```python
start_date="mm/dd/yyyy"
end_date="mm/dd/yyyy"
response=voice.recordings(start_date,end_date)
print(response.json())
```
visit [documentation](https://portal.mobtexting.com/docs/v2/verify "documentation") for a list of all parameters


## Verify Usage
```python
from mobtexting.verify import Verify

access_token = 'xxxxxxxxxxxxxxxxxx'

verify = Verify(access_token)
```
### Send

```python
response = verify.send(
    to="1234567890",
)

print response.json()
```
#### With optional paramaters
```python
response = verify.send(
    to="1234567890",
    data = {
        'length': 4,
        'timeout': 600
    }
)

print response.json()
```
visit [documentation](https://portal.mobtexting.com/docs/v2/verify "documentation") for a list of all parameters

### Check

```python
response = verify.check(
    id='b51be650-fdb2-4633-b101-d450e8d9ec64', # id received while sending
    token='123456' # token entered by user
)

print response.json()
```

### Cancel
```python
response = verify.cancel(
    id='4e28e081-2900-4523-aed6-a21eb39c2ae6' # id received while sending
)

print response.json()
```

