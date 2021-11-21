<%* 
  let title = tp.file.title;
  if (title.startsWith("Untitled")) {
  	title = await tp.system.prompt("Input title of note");
    await tp.file.rename(title);
  }

  note_type = "writing/" + tp.date.now("YYYY/MMM/DD")
  await tp.file.move("/Zet/Writing/" + title);
  tR += "---"
%>
title: <%* tR += title %>
UID: <% tp.date.now("YYMMDDHHmmss") %>
created: <% tp.date.now("DD-MMM-YYYY") %>
tags:
  - 'created/<% tp.date.now("YYYY/MMM/DD") %>'
  - 'forest'
  - '<%* tR += note_type %>'
publish: True
---
# <%* tR += title %>

## Notes:
<% tp.file.cursor() %>

## Ref
