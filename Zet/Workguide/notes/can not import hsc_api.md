# can not import hsc_api
tags: #issue

```
ImportError: DLL load failed while importing
```
![](images/2022-01-17-17-42-03.png)
          

The Python3.10 versions and environments are exactly the same. In fact, we tested on 2 extra PCs (without running tests, just importing the API) to verify and it worked on one but not on the other. At the end, we were able to import the APIs on 2 setups, and failed on 2 setups.

Do you know if there is an extra dependency that must be installed in order to import Python3.10 compiled dll/pyd files?

## Relate:
- [[python]]
- [[swig]]
