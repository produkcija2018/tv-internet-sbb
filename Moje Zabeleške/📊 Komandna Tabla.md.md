# 📊 Komandna Tabla

## 📅 Današnji Zadaci
```dataview
TASK FROM "Daily Notes"
WHERE !completed AND contains(file.name, date(today))
GROUP BY file.link
```

## 🔄 Aktivni Projekti
```dataview
TABLE file.mtime AS "Poslednja izmena"
FROM ""
WHERE contains(file.name, "📋") OR contains(file.name, "Projekat")
SORT file.mtime DESC
```

## 🏷️ Nedavne Note po Kategorijama
```dataview
TABLE file.ctime AS "Kreirano"
FROM ""
WHERE file.ctime >= date(today) - dur(7 days)
SORT file.ctime DESC
LIMIT 10
```

## 📈 Statistika
```dataview
LIST "Ukupno nota: " + length(rows)
FROM ""
WHERE file.name != this.file.name
```