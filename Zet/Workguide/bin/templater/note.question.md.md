<%*
  let title = tp.file.title;
  if (title.startsWith("Untitled")) {
    await tp.file.rename(title);
  }

  await tp.file.move("/inbox/questions/" + title + "❓");
  tR += "---"
%>
title: <%* tR += title %>
UID: <% tp.date.now("YYMMDDHHmmss") %>
created: <% tp.date.now("DD-MMM-YYYY") %>
tags:
  - 'created/<% tp.date.now("YYYY/MM/DD") %>'
  - 'question/todo'
---
<% tp.file.cursor() %>