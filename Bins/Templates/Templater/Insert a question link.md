<%* 
  title = tp.date.now("❓YYMMDD-HHmm");
  if (tp.file.exists(title) == false) {
    (await tp.file.create_new("", title)).basename;
  }
%>
[[<%* tR += title %>]]