<%* 
  let title = tp.file.title;
  if (title.startsWith("Untitled")) {
  	title = await tp.system.prompt("Input title of note");
    await tp.file.rename(title);
  }

  note_type = await tp.system.suggester(["book📚", "website"], ["source/book", "source/website"]);
	
  let sub_dir = ""
  if (note_type == "source/book") {
    sub_dir = "/Reference_Box/Books/"
  }
  else if (note_type == "source/website") {
    sub_dir = "/Reference_Box/Websites/"
  }

  await tp.file.move(sub_dir + title);
  tR += "---"
%>
title: '<%* tR += title %>'
UID: <% tp.date.now("YYMMDDHHmmss") %>
tags:
  - 'created/<% tp.date.now("YYYY/MMM/DD") %>'
  - '<%* tR += note_type %>'
---
# <%* tR += title %>

## Notes:
<% tp.file.cursor() %>
