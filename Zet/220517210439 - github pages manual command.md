---
title: github pages manual command
UID: 220517210439
created: 17-May-2022
tags:
  - 'created/2022/May/17'
  - 'seeding'
  - 'permanent/fact'
aliases: '220517210439'
publish: False
---
## Notes:
Command để publish trong action ghpages trên [[github]]

```
git branch -f gh-pages

git checkout gh-pages

git reset --hard origin/master

git add -A .

git commit -a -m 'gh-pages update'

git push origin gh-pages --force

git checkout master
```

