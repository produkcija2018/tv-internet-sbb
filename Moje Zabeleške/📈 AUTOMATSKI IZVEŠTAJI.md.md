# 📈 Automatski Izveštaji

## 📅 Nedeljni Pregled Aktivnosti
```dataview
TABLE WITHOUT ID
 file.day as Datum,
 choice(rows.T.text != "", "✅", "❌") as "Dnevna Nota",
 length(rows.T.task) as "Zadaci"
FROM "Daily Notes"
FLATTEN file.tasks as T
WHERE file.day >= date(today) - dur(7 days)
GROUP BY file.day
SORT file.day DESC
```

## 🏷️ Najčešći Tagovi
```dataview
LIST FROM ""
WHERE file.ctime >= date(today) - dur(30 days)
FLATTEN file.tags as tag
GROUP BY tag
SORT length(rows) DESC
LIMIT 10
```

## 🔗 Najpovezanije Note
```dataview
LIST FROM ""
WHERE length(file.inlinks) > 5 OR length(file.outlinks) > 5
SORT length(file.inlinks) + length(file.outlinks) DESC
LIMIT 15
```

## 📊 Produktivnost po Danima
```dataview
TABLE WITHOUT ID
 file.day as Dan,
 length(rows.T.text) as "Ukupno Zadataka",
 length(filter(rows.T.text, (t) => t.completed)) as "Završeni",
 round(length(filter(rows.T.text, (t) => t.completed)) / length(rows.T.text) * 100) + "%" as "Uspešnost"
FROM "Daily Notes"
FLATTEN file.tasks as T
WHERE file.day >= date(today) - dur(14 days)
GROUP BY file.day
SORT file.day DESC
```

## 📈 Statistika Vault-a
```dataview
LIST "Ukupno nota: " + length(rows.file.link)
LIST "Nota kreirano ove nedelje: " + length(rows.file.link)
FROM ""
WHERE file.ctime >= date(today) - dur(7 days)
```

## 📈 Statistika Vault-a
```dataview
LIST "Ukupno nota: " + length(rows.file.link)
LIST "Nota kreirano ove nedelje: " + length(rows.file.link)
FROM ""
WHERE file.ctime >= date(today) - dur(7 days)
```
*Automatski generisano - ažurira se u realnom vremenu*