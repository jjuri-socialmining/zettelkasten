<%* 
  let title1 = tp.file.title;
  if (title1.startsWith("Untitled")) {
  	title1 = await tp.system.prompt("Input title of note");

  }
  let date2 = tp.date.now("YYMMDDHHmmss")
  let title = date2 + " - " + title1
  await tp.file.rename(title);
  note_process = await tp.system.suggester(["🥜Seed", "🌱Seeding", "🌲Evergreen", "🏡Garden"], ["seed", "seeding","evergreen", "garden"]);

  note_type = await tp.system.suggester(["concept", "fact", "definition", "think", "place"], ["permanent/concept", "permanent/fact", "permanent/definition", "permanent/think", "permanent/place"]);
  
  if (note_process == "seed") {
  	    await tp.file.move("/Inbox/" + title);
  }
  else {
	  if (note_type == "permanent/think") {
	    title = "❕ " + title;
	    await tp.file.rename(title);
		await tp.file.move("/Zet/Thinking/" + title);
	  }
	  else {
	    await tp.file.move("/Zet/" + title);
	  }
  }
  tR += "---"
%>
title: <%* tR += title1 %>
UID: <% date2 %>
created: <% tp.date.now("DD-MMM-YYYY") %>
tags:
  - 'created/<% tp.date.now("YYYY/MMM/DD") %>'
  - '<%* tR += note_process %>'
  - '<%* tR += note_type %>'
aliases: <% date2 %>
publish: True
---
## Notes:
<% tp.file.cursor() %>

## Source:
- [[@ thongtindalat24h.com, 4 cung phượt 'ớn lạnh' nhất dẫn vào thành phố Đà Lạt]]

## Relate: