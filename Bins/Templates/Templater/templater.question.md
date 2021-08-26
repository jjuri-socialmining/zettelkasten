<%*
  title = tp.date.now("❓YYMMDD-HHmm")

  if (title.startsWith("Untitled")) {
    await tp.file.rename(title);
  }

  await tp.file.move("/Spaces/Daily/" + title);
  tR += "---"
%>
title: <%* tR += title %>
UID: <% tp.date.now("YYMMDDHHmmss") %>
tags:
  - '#created/<% tp.date.now("YYYY/MM/DD") %>'
  - '#question❓'
---
# <%* tR += title %>

## Cards content:

<% tp.file.cursor() %>

## Tham khảo:
```dataview
list
from [[<%* tR += title %>]]
sort file.name asc
```