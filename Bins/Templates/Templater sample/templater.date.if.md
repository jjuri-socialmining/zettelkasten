<%* if (tp.date.now("M-D") == 1-1 ) { tR += "New year" } %>
<%* if (tp.date.now("ddd") == "Sun" ) { %>
[[<% tp.date.now("YYYY-MM-DD", -1) %>]]
[[<% tp.date.now("YYYY-MM-DD", -2) %>]]
[[<% tp.date.now("YYYY-MM-DD", -3) %>]]
[[<% tp.date.now("YYYY-MM-DD", -4) %>]]
[[<% tp.date.now("YYYY-MM-DD", -5) %>]]
[[<% tp.date.now("YYYY-MM-DD", -6) %>]]
<%* } %>
