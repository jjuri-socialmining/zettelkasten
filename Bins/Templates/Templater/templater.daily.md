<%*
  let title = tp.file.title;
  
  if (title.startsWith("Untitled")) {
    title = tp.date.now("YYYY-MM-DD");
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
gotobed:
wakeup:
exersice:
reading:
summary: TBD
location: TBD
---
up:: [[Daily notes]]

<% "[[" + tp.date.yesterday("YYYY-MM-DD") + "|<- Yesterday]] | " + tp.date.now("ddd") + " | [[" + tp.date.tomorrow("YYYY-MM-DD")  + "|Tomorrow ->]]" %>

## Notes:
- [[5 bucket list đáng làm nhất hiện tại]]
- Điều gì làm mình vui trong ngày? -> [[Những niềm vui giản dị]]

<% tp.file.cursor() %>

![[Tasks list]]

<%* if (tp.date.now("ddd") == "Sun" ) { %>
## Weekly review:
- [[<% tp.date.now("YYYY-MM-DD", -6) %>|Mon]]
- [[<% tp.date.now("YYYY-MM-DD", -5) %>|Tue]]
- [[<% tp.date.now("YYYY-MM-DD", -4) %>|Wed]]
- [[<% tp.date.now("YYYY-MM-DD", -3) %>|Thu]]
- [[<% tp.date.now("YYYY-MM-DD", -5) %>]]
- [[<% tp.date.now("YYYY-MM-DD", -1) %>|Sat]]
<%* } %>