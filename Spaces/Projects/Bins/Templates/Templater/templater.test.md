<%* if (tp.date.now("M-D") == 1-1 ) { tR += "New year" } %>
<%* if (tp.date.now("ddd") == "Sun" ) { %>
[[<% tp.date.now("YYYY-MM-DD", -6) %>|Mon]]
[[<% tp.date.now("YYYY-MM-DD", -5) %>|Tue]]
[[<% tp.date.now("YYYY-MM-DD", -4) %>|Wed]]
[[<% tp.date.now("YYYY-MM-DD", -3) %>|Thu]]
[[<% tp.date.now("YYYY-MM-DD", -2) %>|Fri]]
[[<% tp.date.now("YYYY-MM-DD", -1) %>|Sat]]
<%* } %>
