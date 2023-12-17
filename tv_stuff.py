from conf import *
from pyvizio import Vizio

TV = Vizio(ip=IP, 
           auth_token=AUTH_CODE, 
           name=DEVICE_NAME, 
           device_type=DEVICE_TYPE,
           device_id="your device id"
        )

# pyvizio --ip=IP:PORT  --device_type="your device type" --auth="your tv auth code"
