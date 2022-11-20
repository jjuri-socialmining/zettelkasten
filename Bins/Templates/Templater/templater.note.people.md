<%* 
  let title = tp.file.title;
  if (title.startsWith("Untitled")) {
  	title = await tp.system.prompt("Input title of note");
    await tp.file.rename(title);
  }

  note_type = "permanent/people"
  await tp.file.move("/Zet/People/" + title);
  birth = "birth:"
  death = "death:"
  tR += "---"
%>
title: <%* tR += title %>
UID: <% tp.date.now("YYMMDDHHmmss") %>
tags:
  - 'created/<% tp.date.now("YYYY/MMM/DD") %>'
  - '<%* tR += note_type %>'
<%* tR += birth %>
<%* tR += death %>
fc-calendar: Gregorian Calendar
fc-date:
  year:
  month:
  day:
fc-category: Birthday
fc-display-name:  Birthday of <%* tR += title %>
publish: False
---
up:: [[People MOC]],

## Notes:
<% tp.file.cursor() %>
