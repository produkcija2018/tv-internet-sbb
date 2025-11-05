import os
import time
import subprocess
import sqlite3
from datetime import datetime

class ProjectManager:
    def __init__(self):
        self.processes = {}
        
    def start_bot(self):
        """Pokreće Telegram bota"""
        try:
            print("🤖 Pokrećem Telegram bota...")
            process = subprocess.Popen(['python3', 'smart_bot.py'], 
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE)
            self.processes['bot'] = process
            print("✅ Bot pokrenut!")
            return True
        except Exception as e:
            print(f"❌ Greška pri pokretanju bota: {e}")
            return False
            
    def start_web_server(self):
        """Pokreće web server"""
        try:
            print("🌐 Pokrećem web server...")
            os.chdir('web-content')
            process = subprocess.Popen(['python3', '-m', 'http.server', '8000'],
                                    stdout=subprocess.PIPE,
                                    stderr=subprocess.PIPE)
            self.processes['web'] = process
            os.chdir('..')
            print("✅ Web server pokrenut na portu 8000!")
            return True
        except Exception as e:
            print(f"❌ Greška pri pokretanju web servera: {e}")
            return False
            
    def check_leads(self):
        """Proverava nove leads iz baze"""
        try:
            conn = sqlite3.connect('leads.db')
            c = conn.cursor()
            c.execute("SELECT COUNT(*) FROM leads WHERE status='new'")
            new_leads = c.fetchone()[0]
            conn.close()
            
            if new_leads > 0:
                print(f"🎯 Ima {new_leads} novih leadova!")
            return new_leads
        except:
            return 0
            
    def show_stats(self):
        """Prikazuje statistiku projekta"""
        print("\n" + "="*50)
        print("📊 TVINTERNET.RS - STATISTIKA PROJEKTA")
        print("="*50)
        
        # Proveri leads
        leads_count = self.check_leads()
        print(f"🎯 Novi leadovi: {leads_count}")
        
        # Proveri da li procesi rade
        bot_status = "🟢 AKTIVAN" if self.processes.get('bot') and self.processes['bot'].poll() is None else "🔴 NEAKTIVAN"
        web_status = "🟢 AKTIVAN" if self.processes.get('web') and self.processes['web'].poll() is None else "🔴 NEAKTIVAN"
        
        print(f"🤖 Telegram bot: {bot_status}")
        print(f"🌐 Web server: {web_status}")
        print(f"⏰ Vreme: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("="*50)
        
    def run(self):
        """Glavna petlja projekta"""
        print("🚀 POKRECEM TVINTERNET.RS SISTEM...")
        
        # Pokreni komponente
        self.start_bot()
        self.start_web_server()
        
        # Glavna petlja
        try:
            while True:
                self.show_stats()
                time.sleep(60)  # Proveri svakih 60 sekundi
                
        except KeyboardInterrupt:
            print("\n🛑 Zaustavljam sistem...")
            for name, process in self.processes.items():
                if process and process.poll() is None:
                    process.terminate()
            print("✅ Sistem zaustavljen!")

if __name__ == '__main__':
    manager = ProjectManager()
    manager.run()
