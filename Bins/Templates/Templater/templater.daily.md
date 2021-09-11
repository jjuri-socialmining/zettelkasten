<%*
  let title = tp.file.title;
  
  if (title.startsWith("Untitled")) {
    title = tp.date.now("📝YYMMDD");
	if (tp.file.exists(title)) {
      await tp.system.prompt("!!! The file name" + title + " is exist");
	  return;
    }
	else {
	  await tp.file.rename(title);
	}
  }

  note_type = await tp.system.suggester(["Routine", "Private"], ["#daily/routine", "#daily/private"]);
  
  await tp.file.move("/Spaces/Daily/Journal/" + title);
  tR += "---"
%>
title: <%* tR += title %>
UID: <% tp.date.now("YYMMDDHHmmss") %>
created: <% tp.date.now("YYYY/MMM/DD") %>
tags:
  - '#created/<% tp.date.now("YYYY/MMM/DD") %>'
  - '#📅'
  - '<%* tR += note_type %>'
---
<% "[[" + tp.date.yesterday("📝YYMMDD") + "|Yesterday]] -> Today -> [[" + tp.date.tomorrow("📝YYMMDD")  + "|Tomorrow]]" %>
# <% tp.date.now("dddd, MMM D, YYYY") %>

## Notes:
<% tp.file.cursor() %>
