<%*
  let title = tp.file.title;
  
  if (title.startsWith("Untitled")) {
    title = tp.date.now("📝YY-MM-DD");
	if (tp.file.exists(title)) {
      await tp.system.prompt("!!! The file name" + title + " is exist");
	  return;
    }
	else {
	  await tp.file.rename(title);
	}
  }
  await tp.file.move("/Spaces/Daily/" + title);
  tR += "---"
%>
title: <%* tR += title %>
UID: <% tp.date.now("YYMMDDHHmmss") %>
created: <% tp.date.now("DD-MMM-YYYY") %>
tags:
  - 'created/<% tp.date.now("YYYY/MMM/DD") %>'
  - 'daily/private'
summary: TBD
location: TBD
---
up:: [[Daily notes]]

<% "[[" + tp.date.yesterday("📝YY-MM-DD") + "|<- Yesterday]] | [[" + tp.date.tomorrow("📝YY-MM-DD")  + "|Tomorrow ->]]" %>
# <% tp.date.now("dddd, MMM D, YYYY") %>

## Notes:
<% tp.file.cursor() %>

Điều gì làm mình vui trong ngày? -> [[Những niềm vui giản dị]]


<%* if (tp.date.now("ddd") == "Sun" ) { %>
## Weekly review:
[[<% tp.date.now("📝YY-MM-DD", -6) %>|Mon]]
[[<% tp.date.now("📝YY-MM-DD", -5) %>|Tue]]
[[<% tp.date.now("📝YY-MM-DD", -4) %>|Wed]]
[[<% tp.date.now("📝YY-MM-DD", -3) %>|Thu]]
[[<% tp.date.now("📝YY-MM-DD", -2) %>|Fri]]
[[<% tp.date.now("📝YY-MM-DD", -1) %>|Sat]]
<%* } %>