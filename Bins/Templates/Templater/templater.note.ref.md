<%* 
  let title = tp.file.title;
  if (title.startsWith("Untitled")) {
  	title = await tp.system.prompt("Input title of note");
    await tp.file.rename(title);
  }

  note_type = await tp.system.suggester(["book📚", "website"], ["#source/book", "#source/website"]);
  
  sub_dir = ""
  if (note_type == "#source/book") {
    sub_dir = "Books/"
  }
  else if (note_type == "#source/website") {
    sub_dir = "Websites/"
  }
  
  await tp.file.move("/Reference_Box/" + sub_dir + title);
   
  tR += "---"
%>
title: <%* tR += title %>
UID: <% tp.date.now("YYMMDDHHmmss") %>
tags:
  - '#created/<% tp.date.now("YYYY/MM/DD") %>'
  - '<%* tR += note_process %>'
  - '<%* tR += note_type %>'
aliases:
  - 
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