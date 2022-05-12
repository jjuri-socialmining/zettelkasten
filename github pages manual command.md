```
git branch -f gh-pages

git checkout gh-pages

git reset --hard origin/master

git add -A .

git commit -a -m 'gh-pages update'

git push origin gh-pages --force

git checkout master
```