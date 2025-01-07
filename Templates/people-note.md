---
name: <% tp.file.title %>
role: 
team: 
company:
location: 
entity:
  - person
meetings: 
created: <% tp.file.creation_date() %>
modified: <% tp.file.last_modified_date() %>
---
# <% tp.file.title %>
## Details
- **Preferred Pronouns:** 
- **Interests:** 
- **Pets:** 

```dataview
table rows.Details as "Mentions"
from !"Templates"
where contains(log, "<% tp.file.title %>")
flatten log as Details
where contains(Details, "<% tp.file.title %>")
group by file.link as Note
sort rows.file.day desc
```
___
### Tasks
```dataview
task
where contains(text, "<% tp.file.title %>")
```

---
## Meetings
```dataview
list
from "Meetings"
where contains(participants, "<% tp.file.title %>")
sort file.cdate desc, file.ctime desc
```