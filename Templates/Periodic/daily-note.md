---
periodic: daily
---
# <% tp.file.title %>

**Prev Day:** **[[<% tp.date.now("YYYY-MM-DD", -1, tp.file.title, "[daily-note-]YYYY-MM-DD") %>]]**  
**Next Day:** **[[<% tp.date.now("YYYY-MM-DD", +1, tp.file.title, "[daily-note-]YYYY-MM-DD") %>]]**  
**Week:** **[[<% tp.date.now("gggg-ww", 0, tp.file.title, "[weekly-note-]gggg-ww" %>]]**  
___
## Quiet time
#### Inspiration 📜
<% tp.web.daily_quote() %>
#### Blessings 🌟
**What am I grateful for today?**  
- <% tp.file.cursor() %>
#### This Week's Rep

```dataview
task 
from "Journal/<% tp.date.now(gggg-ww, 0, tp.file.title, [weekly-note-]gggg-ww) %>"
```


___
## Field Notes 📝
- 

___
## Daily Inventory

- **Accomplishments**: What did you achieve today?
- **Challenges**: What challenges did you face?
- **Learnings**: What did you learn today?
- **Plans**: What do you plan to do tomorrow? 

___
## Notes Created Today
```dataview
list 
where file.cday = date("<% tp.file.title %>") and file.name != "<% tp.file.title %>"
sort file.ctime desc
```
