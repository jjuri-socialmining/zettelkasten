---
title: Gatsby website generator
UID: 210909222917
tags:
  - '#created/2021/Sep/09'
  - '#seed🥜'
  - '#permanent/concept'
aliases:
  - 
---
# Gatsby website generator

## Notes:
[[Tạo website từ markdown]]
https://www.gatsbyjs.com/docs/quick-start/

Gatsby là một công cụ/thư viện của [[Nodejs]], để tải Gatsby ta dùng [[Node package manager|npm]]

Install nodejs, npm:
- npm viết tắt của [[Node package manager]]
- [[npm tích hợp sẵn trong gói cài của Nodejs]]

### Tạo server local
Khi run cmd `npm init gatsby` hiện lỗi
```
F:\Dung>npm init gatsby
Error: EPERM: operation not permitted, mkdir 'C:\Users\Ngoc'
command not found: create-gatsby
```

solve theo link https://github.com/facebook/create-react-app/issues/9091
```
Try installing it globally first, using the command  
npm install -g create-react-app

And then, you can create your app using the command,  
npx create-react-app <Name of your app>
```
![[setup_server_nodejs_20210909230735.png]]

sau khi start 
```
Compiled successfully!

You can now view gatsby in the browser.

  Local:            http://localhost:3000
  On Your Network:  http://192.168.1.10:3000

```
### Generate website from markdown
https://www.digitalocean.com/community/tutorials/how-to-generate-pages-from-markdown-in-gatsby
```
npm install gatsby-source-filesystem gatsby-transformer-remark
```

## Ideas & thoughts:

## Questions:


## Tham khảo:
```dataview
list
from [[Gatsby website generator]]
sort file.name asc
```