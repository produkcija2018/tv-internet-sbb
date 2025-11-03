**Kreirajmo:** "📑 Indeks Mape Znanja.md"

# 📑 Indeks Mape Znanja

## Sve Note Mape Znanja
```dataview
LIST FROM ""
WHERE contains(file.name, "Mapa") OR contains(file.name, "Setup") OR contains(file.tags, "mapa-znanja")
SORT file.name ASC
```

## Note po Fazama
```dataview
TABLE file.ctime AS "Kreirano"
FROM ""
WHERE file.folder = "Faza 1" OR file.folder = "Faza 2" OR file.folder = "Faza 3"
SORT file.ctime DESC
```

## Nedavno Ažurirano
```dataview
TABLE file.mtime AS "Poslednja Izmena"
FROM ""
WHERE file.mtime >= date(today) - dur(7 days)
SORT file.mtime DESC
LIMIT 10
```