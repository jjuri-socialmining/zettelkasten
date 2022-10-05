---
title: How to check a branch has been merged into other
tags:
  - 'permanent/howto'
---
[[Git command]]

`git branch --merged master` lists branches merged into _master_

`git branch --merged` lists branches merged into _HEAD_ (i.e. tip of current branch)

`git branch --no-merged` lists branches that have not been merged

