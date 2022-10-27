---
title: How to start spica5 simulator
created: 2022-Oct-11
tags:
  - 'permanent/howto'
publish: True
---
up:: [[hsc Simulator|Simulator.py]]

### Notes:
localhost: 127.0.0.1
default port: 60009

```
python3 -m pip install zmq
python3 -m pip install twisted
```

[[Cygwin]], python3

```bash
export HSC_DIR=/cygdrive/c/Users/dutran/projects/hsc/
export PYTHONPATH=${HSC_DIR}/spica5/tools/simulators:${HSC_DIR}/spica5/tools/simulators/spica5:${HSC_DIR}/spica5/tools/simulators/spica5/impl
python3 ${HSC_DIR}/spica5/tools/simulators/spica5/simulator.py
```

```log
$ python3 ${HSC_DIR}/simulators/spica5/simulator.py
Exception in thread Thread-2:
Traceback (most recent call last):
  File "/usr/lib/python3.9/threading.py", line 973, in _bootstrap_inner
    self.run()
  File "/usr/lib/python3.9/threading.py", line 910, in run
    self._target(*self._args, **self._kwargs)
  File "/cygdrive/c/Users/dutran/projects/hsc/simulators/spica5/impl/spica5_impl.py", line 245, in _start_zmq
    import zmq
ModuleNotFoundError: No module named 'zmq'
Creating local XMLRPC server on http://127.0.0.1:60009
```




