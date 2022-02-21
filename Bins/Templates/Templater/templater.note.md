<%* 
  let title1 = tp.file.title;
  if (title1.startsWith("Untitled")) {
  	title1 = await tp.system.prompt("Input title of note");

  }
  let date2 = tp.date.now("YYMMDDHHmmss")
  let title = date2 + " - " + title1
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
title: <%* tR += title1 %>
UID: <% date2 %>
created: <% tp.date.now("DD-MMM-YYYY") %>
noteid:
tags:
  - 'created/<% tp.date.now("YYYY/MMM/DD") %>'
  - '<%* tR += note_process %>'
  - '<%* tR += note_type %>'
publish: True
---
## Notes:
<% tp.file.cursor() %>

## Source:
- [[@ nghiencuulichsu.com, Hàm Nghi Một nhà ái quốc, một nghệ sĩ đa tài]]




