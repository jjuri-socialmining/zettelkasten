---
title: 🛠️210829-Làm templater routine
tags:
  - '#created/2021/Aug/29'
  - 'tasks/done'
is_done: True
---

## Notes:
Làm cái note templater routine, cuối ngày sẽ prom và nhập tất cả thông tin lịch trình sinh hoạt hằng ngày. Cuối ngày bật lên và nhập vào thui

## Result
Đã làm được, nhưng có vẻ không thể stick được với nó, không có nhiều ý nghĩa lắm

```
<%* 
  let title = tp.file.title;
  if (title.startsWith("Untitled")) {
  	title = await tp.system.prompt("Input title of note");
  }
  await tp.file.rename(title);
  note_type = await tp.system.suggester(["book📚", "article📰", "film🎞️", "video🎞️"], ["source/book", "source/article", "source/film", "source/video"]);

  tR += "---"
%>
title: '<%* tR += title %>'
UID: <% tp.date.now("YYMMDDHHmmss") %>
tags:
  - 'created/<% tp.date.now("YYYY/MMM/DD") %>'
  - '<%* tR += note_type %>'
---


<% tp.file.cursor() %>

```