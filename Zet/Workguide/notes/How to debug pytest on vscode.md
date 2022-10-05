# How to debug pytest on vscode

Regression test of hsc is using python 2.7 on mingwin
install python 2.7, usually on `C:\Python27`
add this to windows path environment

![this](2021-10-05-21-21-41.png)
![](2021-10-05-21-22-56.png)
## Setup
- Install vscode [Python extension pack](https://marketplace.visualstudio.com/items?itemName=donjayamanne.python-extension-pack) for vs code

```
pytest --pyargs tests/anlt
```

See more:
- https://code.visualstudio.com/docs/python/testing
- https://dzone.com/articles/vs-code-setup-for-python-development-and-testing