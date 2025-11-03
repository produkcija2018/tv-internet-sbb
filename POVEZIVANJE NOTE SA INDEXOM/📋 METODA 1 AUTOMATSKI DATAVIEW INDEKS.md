### **Kreirajte notu: "📑 Indeks Svih Nota.md"**
markdown

# 📑 Indeks Svih Nota

## 📝 Sve Note u Vault-u (Abecedno)
```dataview
TABLE file.ctime AS "Kreirano"
FROM ""
WHERE file.name != this.file.name
SORT file.name ASC
```
------------------------------
## 🏷️ Note po Tagovima
```dataview
TABLE file.ctime AS "Kreirano"
FROM ""
WHERE file.tags
GROUP BY file.tags
SORT file.tags ASC
```
## 📂 Note po Folderima
```dataview
TABLE length(rows.file.link) AS "Broj Nota"
WHERE file.folder
GROUP BY file.folder
SORT length(rows.file.link) DESC
```
## 🎯 Nepovezane Note (Siročad)
```dataview
LIST FROM ""
WHERE length(file.inlinks) = 0 AND length(file.outlinks) = 0
AND file.name != this.file.name
AND file.name != "🏠 Home.md"
AND file.name != "🧭 Kompletni Tutorijal Setup-a.md"
SORT file.name ASC
```
## 🔄 Nedavno Ažurirano
```dataview
TABLE file.mtime AS "Poslednja Izmena"
FROM ""
WHERE file.mtime >= date(today) - dur(7 days)
SORT file.mtime DESC
LIMIT 15
```
