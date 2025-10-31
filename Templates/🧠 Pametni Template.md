# {{title}}

## Kontekst
<%* 
// Automatski generiše timestamp
const date = tp.date.now("YYYY-MM-DD HH:mm");
-%>

**Kreirano:** <% date %>

## Sadržaj


## Povezano sa
<%*
// Automatski dodaje link ka Home ako postoji
const homeNote = tp.file.find_tfile("🏠 Home");
if (homeNote) {
    tR += "[[🏠 Home]] | ";
}
tR += "[[Druga Tema]]";
-%>

## Status
- 💡 Ideja
- 📝 U pisanju  
- ✅ Završeno

## Tags
#<% tp.file.folder() %>

---
*Kreirano pomoću Templatera*
