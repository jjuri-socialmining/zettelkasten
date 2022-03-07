## List from tags
With certain tags
%%
```dataview
LIST
FROM #permanent/fact and #created/2021/Aug  
```
%%


Without certain tags
%%
```dataview
LIST
FROM #permanent/people
```
%%

Liệt kê các page có nhắc tới 1 page xác định
```dataview
LIST
FROM [[~Lịch Sử Việt Nam]]
```

Liệt kê các page được nhắc đến trong một page xác định
```dataview
LIST
FROM outgoing([[~Lịch Sử Việt Nam]])
```

Liệt kê các page có tag `#permanent/people` và có birth giá trị trong YAML fronmatter
```dataview
LIST
FROM #permanent/people 
WHERE birth
```

