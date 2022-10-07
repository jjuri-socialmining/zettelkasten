---
title: Obsidian Task Manager plugin
UID: 220917153918
created: 17-Sep-2022
tags:
  - 'created/2022/Sep/17'
  - 'permanent/concept'
publish: False
---
up::[[Obsidian]], [[Obsidian Plugins]]

Task Manager plugin là plugin sử dụng checkbox của markdown để phát hiện tasks. Plugin này hỗ trợ thêm một số cú pháp như cho `due date`, `repeat`,...

Một ví dụ mẫu cho task của plugin này:
%%
- [ ] Some thing todo 🛫 2022-09-17 📅 2022-09-18 🔁 every day 
%%

Sample query
%%
```tasks
not done
```
%%


Find in specific tags
```tasks
not done
tags include task
```

Find in specific folder
```tasks
not done
path includes Spaces/Projects
```

### Reference:
https://obsidian-tasks-group.github.io/obsidian-tasks/quick-reference/