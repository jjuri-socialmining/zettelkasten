<%*
  let title = tp.file.title;
  
  if (title.startsWith("Untitled")) {
    title = tp.date.now("📝YYMMDD");
    await tp.file.rename(title);
  }

  note_type = await tp.system.suggester(["Routine", "Private"], ["#daily/routine", "#daily/private"]);
  
  await tp.file.move("/Spaces/Daily/" + title);
  tR += "---"
%>
title: <%* tR += title %>
UID: <% tp.date.now("YYMMDDHHmmss") %>
tags:
  - '#created/<% tp.date.now("YYYY/MMM/DD") %>'
  - '<%* tR += note_type %>'
---
# <%* tR += title %>

## Notes:
<% tp.file.cursor() %>

## Tham khảo:
```dataview
list
from [[<%* tR += title %>]]
sort file.name asc
```