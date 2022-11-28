---
title: How to add requirements.txt in python project
UID: 221125231547
created: 25-Nov-2022
tags:
  - 'created/2022/Nov/25'
  - 'howto'
aliases:
  - requirements
  - install packages in requirements.txt file
publish: False
---
## Notes:
Command sẽ giúp list các [[python package]] cần để run một python project nhất định nào đó.

```shell
pip install pipreqs
pipreqs /path/to/project
```

Để install các package trong file `requirements.txt`, thêm option `-r`
```
pip install -r requirements.txt
```