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
  await tp.file.move("/Spaces/Daily/Journal/" + title);
  tR += "---"
%>
title: <%* tR += title %>
UID: <% tp.date.now("YYMMDDHHmmss") %>
created: <% tp.date.now("DD-MMM-YYYY") %>
tags:
  - 'created/<% tp.date.now("YYYY/MMM/DD") %>'
  - 'daily/journal'
---
<% "[[" + tp.date.yesterday("📝YY-MM-DD") + "|<- Yesterday]] | [[" + tp.date.tomorrow("📝YY-MM-DD")  + "|Tomorrow ->]]" %>
# <% tp.date.now("dddd, MMM D, YYYY") %>

## Notes:
<% tp.file.cursor() %>

