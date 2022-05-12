## Example 1
%%
```dataview
TABLE birth, death, yearold
FROM #permanent/people
```
%%

## Example 2
%%
```dataview
TABLE birth
FROM #permanent/people
Where birth = date(0900-10-11)
```
%%
##  Peoples with birthday 1000 from now
%%
```dataview
TABLE birth, death, yearold
FROM #permanent/people
Where birth < date(today) - dur(1000 years)
```
%%

tag people with YAML death
%%
```dataview
TABLE birth
FROM #permanent/people 
WHERE death
```
%%

list path files
```dataview
TABLE file.path
FROM #permanent/people 
sort decs
```