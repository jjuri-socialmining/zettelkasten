<%* 
  let title = tp.file.title;
  let qcFileName = tp.date.now("@ YYMMDD-HHmmss - ");
  if (title.startsWith("Untitled")) {
  	title = await tp.system.prompt("Input title of note");
  }
  title = qcFileName + title;
  await tp.file.rename(title);
  note_type = await tp.system.suggester(["book📚", "article📰", "video🎞️"], ["source/book", "source/article", "source/video"]);
	
  let sub_dir = ""
  if (note_type == "source/book") {
    sub_dir = "/Reference_Box/Books/"
  }
  else if (note_type == "source/article") {
    sub_dir = "/Reference_Box/Websites/"
  }
  else if (note_type == "source/video") {
    sub_dir = "/Reference_Box/Websites/"
  }
  
  await tp.file.move(sub_dir + title);
  tR += "---"
%>
title: '<%* tR += title %>'
UID: <% tp.date.now("YYMMDDHHmmss") %>
tags:
  - 'created/<% tp.date.now("YYYY/MMM/DD") %>'
  - '<%* tR += note_type %>'
publish: True
---
- link:
- author:

<% tp.file.cursor() %>
