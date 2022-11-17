<%* 
  let title = tp.file.title;
  let date2 = tp.date.now("YYMMDDHHmmss")
  if (title.startsWith("Untitled")) {
  	title = await tp.system.prompt("Input title of note");
    await tp.file.rename(title);
  }

   await tp.file.move("/notes/concept/" + title);

  tR += "---"
%>
title: <%* tR += title %>
UID: <% date2 %>
created: <% tp.date.now("DD-MMM-YYYY") %>
tags:
  - 'created/<% tp.date.now("YYYY/MMM/DD") %>'
  - 'permanent/concept'
aliases:
  -
publish: False
---

<% tp.file.cursor() %>



