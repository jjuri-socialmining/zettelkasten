<%* 
  let title = tp.file.title;
  if (title.startsWith("Untitled")) {
  	title = await tp.system.prompt("Input title of note");
    await tp.file.rename(title);
  }

  note_process = await tp.system.suggester(["🥜Seed", "🌱Seeding", "🌲Evergreen", "🏡Garden"], ["#seed🥜", "#seeding🌱","#evergreen🌲", "#garden🏡"]);

  note_type = await tp.system.suggester(["concept", "fact", "people 🤵", "think", "place", "nation"], ["#permanent/concept", "#permanent/fact", "#permanent/people", "#permanent/think", "#permanent/place", "#permanent/nation"]);
  
  if (note_type == "#permanent/think") {
    title = "❕ " + title;
    await tp.file.rename(title);
	await tp.file.move("/Zet/Thinking/" + title);
  }
  else if (note_type == "#permanent/people"){
    await tp.file.move("/Zet/People/" + title);
  }
  else {
    await tp.file.move("/Zet/" + title);
  }

  alias_txt = ''
  if (note_type == "#permanent/concept") {
    alias_txt = title
  }
   
  tR += "---"
%>
title: <%* tR += title %>
UID: <% tp.date.now("YYMMDDHHmmss") %>
tags:
  - '#created/<% tp.date.now("YYYY/MM/DD") %>'
  - '<%* tR += note_process %>'
  - '<%* tR += note_type %>'
aliases:
  - <%* tR += alias_txt %>
---
# <%* tR += title %>

## Notes:
<% tp.file.cursor() %>

## Ideas & thoughts:

## Questions:


## Tham khảo:
```dataview
list
from [[<%* tR += title %>]]
sort file.name asc
```