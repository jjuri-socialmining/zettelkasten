<%* 
  let title = tp.file.title;
  if (title.startsWith("Untitled")) {
  	title = await tp.system.prompt("Input title of note");

  }
  let date = tp.date.now("YYMMDD - ")
  let date2 = tp.date.now("YYMMDDHHmmss")
  title = date + title
  await tp.file.rename(title);
  note_process = await tp.system.suggester(["🥜Seed", "🌱Seeding", "🌲Evergreen", "🏡Garden"], ["seed", "seeding","evergreen", "garden"]);

  note_type = await tp.system.suggester(["concept", "fact", "think", "place", "nation", "linking", "how to", "funny"], ["permanent/concept", "permanent/fact", "permanent/think", "permanent/place", "permanent/nation", "permanent/linking", "permanent/howto", 'funny']);

  if (note_type == "permanent/think") {
    title = "❕ " + title;
    await tp.file.rename(title);
	await tp.file.move("/Zet/Thinking/" + title);
  }
  else {
    await tp.file.move("/Zet/" + title);
  }

  tR += "---"
%>
title: <%* tR += title %>
UID: <% date2 %>
created: <% tp.date.now("DD-MMM-YYYY") %>
tags:
  - 'created/<% tp.date.now("YYYY/MMM/DD") %>'
  - '<%* tR += note_process %>'
  - '<%* tR += note_type %>'
publish: False
---
## Notes:
<% tp.file.cursor() %>

## Source:


