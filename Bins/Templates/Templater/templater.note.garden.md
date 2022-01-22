<%* 
  let title = tp.file.title;
  if (title.startsWith("Untitled")) {
  	title = await tp.system.prompt("Input title of note");
    await tp.file.rename(title);
  }

  note_type = await tp.system.suggester(["concept", "fact", "think", "place", "nation", "linking", "how to", "funny"], ["permanent/concept", "permanent/fact", "permanent/think", "permanent/place", "permanent/nation", "permanent/linking", "permanent/howto", 'funny']);

   await tp.file.move("/Zet/Garden/" + title);
   
  tR += "---"
%>
title: <%* tR += title %>
UID: <% tp.date.now("YYMMDDHHmmss") %>
created: <% tp.date.now("DD-MMM-YYYY") %>
tags:
  - 'created/<% tp.date.now("YYYY/MMM/DD") %>'
  - 'garden'
  - '<%* tR += note_type %>'
aliases:
  - 
publish: False
---
# <%* tR += title %>

## Notes:
<% tp.file.cursor() %>

## Ideas & thoughts:


