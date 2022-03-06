<%*
  let title = tp.file.title;
  
  if (title.startsWith("Untitled")) {
    title = tp.date.now("YYMMDD - Journal");
	if (tp.file.exists(title)) {
      await tp.system.prompt("!!! The file name" + title + " is exist");
	  return;
    }
	else {
	  await tp.file.rename(title);
	}
  }
  await tp.file.move("/Spaces/Journal/" + title);
  tR += "---"
%>
title: <%* tR += title %>
UID: <% tp.date.now("YYMMDDHHmmss") %>
created: <% tp.date.now("DD-MMM-YYYY") %>
tags:
  - 'created/<% tp.date.now("YYYY/MMM/DD") %>'
  - 'daily/journal'
---
# <%* tR += title %>

## Notes:
<% tp.file.cursor() %>

