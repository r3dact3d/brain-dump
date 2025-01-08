---
type: people-note
description: This is my people template
foam_template:
  filepath: 'People/$FOAM_TITLE.md'
---

# $FOAM_TITLE

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
