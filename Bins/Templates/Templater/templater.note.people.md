<%* 
  let title = tp.file.title;
  if (title.startsWith("Untitled")) {
  	title = await tp.system.prompt("Input title of note");
    await tp.file.rename(title);
  }

  note_type = "permanent/people"
  await tp.file.move("/Zet/People/" + title);
  birth = "birth: "
  death = "death: "
  alias_txt = ""
   
  tR += "---"
%>
title: <%* tR += title %>
UID: <% tp.date.now("YYMMDDHHmmss") %>
tags:
  - '#created/<% tp.date.now("YYYY/MMM/DD") %>'
  - '#seed🥜'
  - '<%* tR += note_type %>'
<%* tR += birth %>
<%* tR += death %>
aliases:
  - <%* tR += alias_txt %>
publish: False
---
# <%* tR += title %>

## Notes:

