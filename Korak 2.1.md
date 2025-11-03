## 🏷️ Tagovi
#python #video-tutorijal' > "🎬 Python Decoratori Tutorijal.md"

### **2.3 U LOGSEQ-U:**
1. Otvorite LogSeq
    
2. Automatski se otvara dnevna nota
    
3. Napišite:
    

- [[Python Decoratori Tutorijal]] 📹
    
    - URL::
        
    - Trajanje::
        
    - Datum:: {{date:YYYY-MM-DD}}
-  Ključni koncepti:
    
    - [[Python Decoratori]]
        
    - [[Python Funkcije]]
        
- Bitne ideje:
    
    - Decoratori modifikuju funkcije
        
    - Koriste @sintaksu
- Primer koda:
@decorator
def my_function():
    pass
    
- Tagovi: #python #video-tutorijal

---

## 🎯 **KORAK 3: KREIRANJE KONCEPT NOTA**

### **3.1 U OBSIDIAN-U:**
```bash
# Kreirajte koncept notu
echo '# 📚 Python Decoratori

## 🎯 Definicija
Funkcije koje modifikuju ponašanje drugih funkcija.

## 💡 Suština
- Wrapper funkcije
- Ne menja originalni kod
- Koristi @sintaksu

## 🔧 Kako Se Koristi
```python
def my_decorator(func):
    def wrapper():
        print("Pre funkcije")
        func()
        print("Posle funkcije")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

