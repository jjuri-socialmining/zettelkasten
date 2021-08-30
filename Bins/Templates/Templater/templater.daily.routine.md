<%*
  let title = tp.file.title;
  
  if (title.startsWith("Untitled")) {
    title = tp.date.now("⏰YYMMDD");
	if (tp.file.exists(title)) {
      await tp.system.prompt("!!! The file name" + title + " is exist");
	  return;
    }
	else {
	  await tp.file.rename(title);
	}
  }

  exercise_type = ''
  wakeup = await tp.system.prompt("Dậy lúc mấy giờ? HH:mm");
  sleep = await tp.system.prompt("Ngủ lúc mấy giờ? HH:mm");
  drink = await tp.system.prompt("Uống đủ nước không?");
  exercise_min = await tp.system.prompt("Thể dục bao nhiêu phút?");
  if (exercise_min > 0) {
    exercise_type = await tp.system.suggester(["🏃‍♂️Chạy bộ", "💗Tabata", "Nhảy dây"], ["Running", "Tabata", "Rope Jump"]);

  }

  await tp.file.move("/Spaces/Daily/Routine/" + title);
  tR += "---"
%>
title: <%* tR += title %>
UID: <% tp.date.now("YYMMDDHHmmss") %>
tags:
  - '#created/<% tp.date.now("YYYY/MMM/DD") %>'
  - '#daily/routine⏰'
wakeup: <%* tR += wakeup %>
sleep: <%* tR += sleep %>
drink: <%* tR += drink %>
---
