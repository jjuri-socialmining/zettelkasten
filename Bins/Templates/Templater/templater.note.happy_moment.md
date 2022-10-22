<%* 
  let title1 = tp.file.title;
  if (title1.startsWith("Untitled")) {
  	title1 = await tp.system.prompt("Input title of note");

  }
  let date2 = tp.date.now("YYMMDDHHmmss")
  let title = "🙂 " + date2 + " - " + title1
  await tp.file.rename(title);
  

await tp.file.move("/Zet/Thinking/" + title);

  tR += "---"
%>
title: <%* tR += title1 %>
UID: <% date2 %>
created: <% tp.date.now("DD-MMM-YYYY") %>
tags:
  - 'created/<% tp.date.now("YYYY/MMM/DD") %>'
  - 'evergreen'
  - 'permanent/think/happymoment'
publish: False
---
up:: [[Những niềm vui giản dị]]
## Notes:
<% tp.file.cursor() %>
