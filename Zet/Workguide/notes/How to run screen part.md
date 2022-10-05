---
title: How to run screen part
created: 2022-Jul-18
tags:
  - 'permanent/howto'
---

Modify the api version to test: `users\lynx\api.py`, the api file will be fetched in `users\lynx\cache\api\lynx_800\<version>` automatically

```python
# Fetch the LYNX API
api_version = "1.0.1.1151"
load_api(LYNX, api_version=api_version, api_type="nightly")
```

How to run:
Use gitbash
```shell
cd users/lynx
# "C:\Python\Python36-32\python" test_screening.py
"C:\Users\hcmswlab\AppData\Local\Programs\Python\Python310\python" test_screening.py
```

Note:
Modify the version of CTC/CPL fw in `users\lynx\test_screening.py` file to pass the test codition.

```python
cpl_fw_ver = [0, 12, 0, 2345]
ctc_fw_ver = [0, 14, 0, 431]
```



