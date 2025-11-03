### **Kreirajte: "🔗 Centralni Hub.md"**
# 🔗 Centralni Hub

Ova nota služi kao **centralna tačka** za sve ostale note.

## 🗂️ Kategorije Sadržaja

### 🎓 Tutorijali i Vodiči
```dataview
LIST FROM ""
WHERE contains(file.name, "Faza") OR contains(file.name, "Tutorijal")
SORT file.name ASC
```

### 🔧 Alati i Tehnologije
```dataview
LIST FROM ""
WHERE contains(file.name, "Git") OR contains(file.name, "Termux") OR contains(file.name, "Android")
SORT file.name ASC
```

### 📊 Produktivnost
```dataview
LIST FROM ""
WHERE contains(file.name, "Izveštaj") OR contains(file.name, "Kanban") OR contains(file.name, "Dataview")
SORT file.name ASC
```

### 🎨 Template-i
```dataview
LIST FROM "Templates"
SORT file.name ASC
```

## 🔄 Automatski Linkovi
```dataview
LIST FROM ""
WHERE file.name != this.file.name
AND !contains(file.name, "Templates/")
SORT file.ctime DESC
LIMIT 20
```
