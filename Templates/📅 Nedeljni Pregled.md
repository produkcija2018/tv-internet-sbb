# 📅 Nedeljni Pregled - <% tp.date.now("YYYY-[W]WW") %>

## 🎯 Ciljevi za Nedelju
- 

## 📊 Prošla Nedelja u Reviji
- **Postignuća:**
- **Izazovi:**
- **Naučene Lekcije:**

## 📝 Aktivnosti po Danima
- **Ponedeljak:**
- **Utorak:**
- **Sreda:**
- **Četvrtak:**
- **Petak:**
- **Subota:**
- **Nedelja:**

## ✅ Završeni Zadaci
```dataview
TASK FROM "Daily Notes"
WHERE completed AND file.ctime >= date(today) - dur(7 days)
GROUP BY file.link
```

## 🔄 Aktivni Projekti
```dataview
TABLE file.mtime AS "Poslednja Izmena"
FROM ""
WHERE contains(file.name, "📋") OR contains(file.name, "Projekat")
AND file.ctime >= date(today) - dur(7 days)
SORT file.mtime DESC
```

## 📈 Metrike i Statistika
- **Ukupno nota kreirano ove nedelje:** ```dataview LIST WHERE file.ctime >= date(today) - dur(7 days) AND file.name != this.file.name ```
- **Procenat završenih zadataka:** (možete dodati ručno)

## 🎯 Fokus za Sledeću Nedelju
- 

## 🔗 Povezano
<< [[<% tp.date.now("YYYY-[W]WW", -7) %>|↞ Prošla Nedelja]] | [[<% tp.date.now("YYYY-[W]WW", 7) %>|Sledeća Nedelja ↠]] >>

---
*Automatski generisano*
