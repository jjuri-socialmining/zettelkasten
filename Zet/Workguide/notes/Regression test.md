# Regression test

## Regression team
- [[Regression repo]]

How to read and analyze regression results
- https://sw.inphi-corp.local/bookstack/books/regression/page/how-to-read-and-analyze-regression-results

### Regression labs

```
CTCB-CTCB
user: sjclab-007248
pass: Test@inphi
```
![lab7248.png](images/lab7248.PNG)

## Check regression issue

[[Get log api from regression test]]

python Tasks when regression run??
![](2022-01-18-11-04-22.png)

## Connect olympus

```python
def connect(
    protocol=None,
    mb=None,
    edc_id=None,
    api=None,
    ip=None,
    port=None,
    target=None,
    target_type=None,
    upper_die=0,
):
    """
    Connects to a target and returns a reference to that target. Will only connect once. Target is saved
    globally so you can use register read/write methods at any point after the connect without saving a
    reference.
    """
    global g_connectors

    upper_die = 0
    if target is not None and isinstance(target, lazy_mod.targets.HscTarget):
        # use stuff from the target class directly
        edc_id = target.edc_id
        protocol = target.protocol
        api = target.api
        ip = target.ip
        port = target.port
        upper_die = target.upper_die
        mb = target.mb
        target_type = target.target_type

    if edc_id in g_connectors:
        print("Already connected to target at edc_id {:#x}".format(edc_id))
        return g_connectors[edc_id]
    else:
        protocol = protocol.strip().lower()
        if protocol == "xmlrpc":
            connector = _xmlrpc(edc_id, api, ip, port, upper_die, mb)
        elif protocol == "olympus":
            connector = _olympus(edc_id, api, mb, target_type)
        # elif protocol == "simulator":
        #     connector = _simulator(edc_id, api, *args, **kwargs)
        # elif protocol == "ate":
        #     connector = _ate(edc_id, api, *args, **kwargs)
        else:
            raise ValueError("Protocol '{}' unknown".format(protocol))

        connector.protocol = protocol
        # this connector is not known, try to use it!
        data = connector.read(connector.die, 0x1E0003)
        if data in (0xBADA, 0xFFFF, 0x0):
            print("WARNING: Reg access probably failed in a weird way; device id reading back bogus value")
            print("data = 0x%04x" % (data))

        g_connectors[edc_id] = connector

        return connector
```