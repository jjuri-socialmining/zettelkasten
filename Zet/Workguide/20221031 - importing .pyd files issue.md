---
title: 20221031 - importing .pyd files issue
created: 2022-Oct-31
tags:
  - 'issue/done'
project: lynx
date:
  - start: 2022-10-31
  - end: 2022-10-31
  - due: 2022-10-31
publish: False
---
up:: [[Issues list]]

source:: [[20221031 - importing .pyd files issue email]]

- [[221031102441 - The pyd is API wrapped in DLL]]
- [[221031103328 - The hsc api build machine is setup to compile with Visual Studio Express 2013]]
- Brad switching to MingW64 to setup a environment to build API.
- [[221031104409 - The newer versions of MSYS2 don't support Olympus.pyd]].

Solution: Using absolute path instead relative path to append PATH.
```
Using this:         sys.path.append(os.path.abspath("./cache/api/por/1.12.1388"))
Instead of this:    sys.path.append("./cache/api/por/1.12.1388")
```