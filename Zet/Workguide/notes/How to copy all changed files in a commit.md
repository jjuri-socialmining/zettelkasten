---
title: How to copy all changed files in a commit
created: 2022-Jul-04
tags:
  - 'permanent/howto'
---
```
cp $(git diff --name-only HEAD^) build-output
```


```shell
git diff --name-only HEAD~ HEAD | zip patched.zip -@
```
```
./git-cp.sh  6b3a7284b9d4f6f741eae821c317940e13724321 ab571943d61fa8ba45df43347eb808eb644b9c59 'C:/change/'
```

```shell
git checkout <SHA of old commit>
git diff --name-only <SHA of old commit> <SHA of newer commit> | xargs git checkout-index -f --prefix='C:\changes\'
```
```
git diff --name-only 6b3a7284b9d4f6f741eae821c317940e13724321 73e16fe852c7270b50a86fc841de952760f899fe | xargs git checkout-index -f --prefix='C:\changes'
```
# Explanation

`git checkout <SHA of old commit>` will cause the following `git checkout-index` to copy files out of the old commit.

`git diff --name-only <SHA of old commit> <SHA of newer commit>` will return a list of all files that have been changed between the old and the newer commit.

`xargs git checkout-index -f --prefix='C:\changes\'` will take all the files returned by the first command (by using a pipe) and will use each line as an argument for the following `git checkout-index` command.

Source:
- https://stackoverflow.com/questions/49845109/copy-differing-files-between-two-commits-to-a-specific-folder-using-git