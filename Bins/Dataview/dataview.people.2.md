```dataview
TABLE file.ctime as created 
FROM "" 
WHERE date(now) - file.ctime <= dur(1 days) 
SORT file.ctime desc 
```
