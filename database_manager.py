# database_manager.py
import sqlite3
import datetime
from datetime import datetime

class DatabaseManager:
    def __init__(self, db_path="sbb_leads.db"):
        self.db_path = db_path
        self.init_db()
    
    def init_db(self):
        """Proširena inicijalizacija baze - dodaje nove tabele ako ne postoje"""
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        
        # Tabela za statistiku (dodajemo ako ne postoji)
        c.execute('''
            CREATE TABLE IF NOT EXISTS bot_stats (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT UNIQUE,
                messages_processed INTEGER DEFAULT 0,
                new_leads INTEGER DEFAULT 0
            )
        ''')
        
        conn.commit()
        conn.close()
        print("✅ Database Manager initialized successfully")
    
    def get_daily_stats(self):
        """Dobijanje dnevne statistike"""
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        
        today = datetime.now().strftime("%Y-%m-%d")
        c.execute('SELECT * FROM bot_stats WHERE date = ?', (today,))
        result = c.fetchone()
        
        conn.close()
        
        if result:
            return {
                'date': result[1],
                'messages_processed': result[2],
                'new_leads': result[3]
            }
        else:
            return {
                'date': today,
                'messages_processed': 0,
                'new_leads': 0
            }
    
    def get_lead_stats(self):
        """Detaljna statistika leadova"""
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        
        c.execute('SELECT COUNT(*) FROM leads WHERE status = "new"')
        new_leads = c.fetchone()[0]
        
        c.execute('SELECT COUNT(*) FROM leads WHERE status = "contacted"')
        contacted = c.fetchone()[0]
        
        c.execute('SELECT COUNT(*) FROM leads')
        total = c.fetchone()[0]
        
        conn.close()
        
        return {
            'new_leads': new_leads,
            'contacted_leads': contacted,
            'total_leads': total
        }

# Test
if __name__ == "__main__":
    db = DatabaseManager()
    print("📊 Database Manager Test:")
    print("Daily Stats:", db.get_daily_stats())
    print("Lead Stats:", db.get_lead_stats())
