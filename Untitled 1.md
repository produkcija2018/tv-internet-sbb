cd web-content

# Kreiraj profesionalni sajt sa custom domenom
cat > index.html << 'EOF'
<!DOCTYPE html>
<html lang="sr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TVInternet.rs - Najbolji TV i Internet Paketi</title>
    <meta name="description" content="Besplatna instalacija TV i internet paketa. Preko 200 kanala, brzine do 1Gbps. Najpovoljnije cene u Srbiji.">
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: 'Arial', sans-serif; line-height: 1.6; background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: #333; min-height: 100vh; }
        .container { max-width: 1200px; margin: 0 auto; padding: 20px; }
        
        header { 
            background: rgba(255, 255, 255, 0.95); 
            padding: 2rem; 
            text-align: center; 
            border-radius: 15px; 
            box-shadow: 0 8px 25px rgba(0,0,0,0.1); 
            margin-bottom: 2rem; 
            border: 3px solid #3498db;
        }
        
        .package { 
            background: white; 
            margin: 20px 0; 
            padding: 30px; 
            border-radius: 15px; 
            box-shadow: 0 6px 15px rgba(0,0,0,0.1); 
            transition: all 0.3s ease; 
            border-left: 5px solid #3498db;
        }
        
        .package:hover { 
            transform: translateY(-10px) scale(1.02); 
            box-shadow: 0 12px 25px rgba(0,0,0,0.15);
        }
        
        .contact { 
            background: #2c3e50; 
            color: white; 
            padding: 40px; 
            border-radius: 15px; 
            text-align: center; 
            margin-top: 3rem;
            box-shadow: 0 8px 25px rgba(0,0,0,0.2);
        }
        
        h1 { 
            color: #2c3e50; 
            margin-bottom: 0.5rem; 
            font-size: 3rem; 
            text-shadow: 2px 2px 4px rgba(0,0,0,0.1);
        }
        
        h2 { 
            color: #3498db; 
            margin-bottom: 1rem; 
            font-size: 2rem; 
            border-bottom: 2px solid #3498db;
            padding-bottom: 0.5rem;
        }
        
        .price { 
            color: #e74c3c; 
            font-weight: bold; 
            font-size: 1.8em; 
            background: #f8f9fa;
            padding: 10px 20px;
            border-radius: 25px;
            display: inline-block;
            margin: 15px 0;
        }
        
        .features { 
            list-style: none; 
            padding: 0; 
            margin: 20px 0;
        }
        
        .features li { 
            padding: 12px 0; 
            border-bottom: 1px solid #ecf0f1; 
            font-size: 1.1em;
        }
        
        .features li:before { 
            content: "✅ "; 
            color: #27ae60; 
            font-weight: bold; 
            margin-right: 10px;
        }
        
        .btn { 
            display: inline-block; 
            background: linear-gradient(45deg, #3498db, #2980b9); 
            color: white; 
            padding: 15px 35px; 
            border-radius: 50px; 
            text-decoration: none; 
            font-weight: bold; 
            margin-top: 20px; 
            transition: all 0.3s ease;
            font-size: 1.1em;
            box-shadow: 0 4px 15px rgba(52, 152, 219, 0.3);
        }
        
        .btn:hover { 
            background: linear-gradient(45deg, #2980b9, #3498db);
            transform: translateY(-3px);
            box-shadow: 0 6px 20px rgba(52, 152, 219, 0.4);
        }
        
        .packages-grid { 
            display: grid; 
            grid-template-columns: repeat(auto-fit, minmax(350px, 1fr)); 
            gap: 30px; 
            margin: 40px 0;
        }
        
        .badge {
            background: #e74c3c;
            color: white;
            padding: 5px 15px;
            border-radius: 20px;
            font-size: 0.8em;
            margin-left: 10px;
            vertical-align: super;
        }
        
        .telegram-widget {
            background: #0088cc;
            color: white;
            padding: 20px;
            border-radius: 10px;
            margin: 20px 0;
            text-align: center;
        }
        
        @media (max-width: 768px) { 
            .packages-grid { grid-template-columns: 1fr; }
            h1 { font-size: 2rem; }
            .package { padding: 20px; }
        }
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>📺🌐 TVInternet.rs</h1>
            <p style="font-size: 1.3em; color: #7f8c8d;">Najpovoljniji TV i internet paketi u Srbiji</p>
            <p style="margin-top: 10px; font-size: 1.1em;">🎯 Besplatna instalacija • 📞 24/7 podrška • 💰 Najniže cene</p>
        </header>

        <div class="telegram-widget">
            <h3>💬 Brza poruka preko Telegrama</h3>
            <p>Klikni dugme ispod za direktan kontakt:</p>
            <a href="https://t.me/tv_internet_helper_bot" class="btn" style="background: linear-gradient(45deg, #0088cc, #006699);">📱 Pošalji poruku na Telegram</a>
        </div>

        <div class="packages-grid">
            <div class="package">
                <h2>📺 Osnovni TV Paket <span class="badge">POPULARNO</span></h2>
                <p>Savršen za celu porodicu - preko 200 kanala u HD kvalitetu</p>
                <ul class="features">
                    <li><strong>200+ kanala</strong> - svežanj najboljih programa</li>
                    <li><strong>HD kvalitet</strong> - kristalno jasna slika</li>
                    <li><strong>15 sportskih kanala</strong> - uživajte u utakmicama</li>
                    <li><strong>10 filmskih kanala</strong> - najnoviji filmovi i serije</li>
                    <li><strong>5 dečjih kanala</strong> - zabava za najmlađe</li>
                    <li><strong>Besplatna instalacija</strong> - montiramo za 24h</li>
                </ul>
                <div class="price">1.990 RSD/mesec</div>
                <a href="https://t.me/tv_internet_helper_bot?text=Želim+Osnovni+TV+Paket" class="btn">📞 Poruči TV Paket</a>
            </div>

            <div class="package">
                <h2>🌐 Internet 300 Mbps <span class="badge">NAJČEŠĆE</span></h2>
                <p>Savršena brzina za rad od kuće, gaming i streaming</p>
                <ul class="features">
                    <li><strong>300 Mbps brzina</strong> - bez zastoja i seckanja</li>
                    <li><strong>Neograničen protok</strong> - surfujte bez brige</li>
                    <li><strong>Bez ugovorne obaveze</strong> - sloboda otkaza</li>
                    <li><strong>WiFi ruter u paketu</strong> - besplatno</li>
                    <li><strong>24/7 tehnička podrška</strong> - uvek tu za vas</li>
                    <li><strong>Instalacija za 24h</strong> - brzo i profesionalno</li>
                </ul>
                <div class="price">2.290 RSD/mesec</div>
                <a href="https://t.me/tv_internet_helper_bot?text=Želim+Internet+300+Mbps" class="btn">📞 Poruči Internet</a>
            </div>

            <div class="package">
                <h2>🔥 Kombinovani Paket <span class="badge">USTEDA 30%</span></h2>
                <p>TV + Internet - sve u jednom, platite manje!</p>
                <ul class="features">
                    <li><strong>TV 200+ kanala</strong> - potpuni TV paket</li>
                    <li><strong>Internet 300 Mbps</strong> - brzi internet</li>
                    <li><strong>Ušteda 30%</strong> - u odnosu na odvojene pakete</li>
                    <li><strong>Premium podrška</strong> - prioritetna usluga</li>
                    <li><strong>Besplatna instalacija</strong> - uključujući WiFi ruter</li>
                    <li><strong>Prvi mesec 50% popusta</strong> - probajte povoljno</li>
                </ul>
                <div class="price">2.990 RSD/mesec</div>
                <a href="https://t.me/tv_internet_helper_bot?text=Želim+Kombinovani+Paket" class="btn">📞 Poruči Kombinovano</a>
            </div>
        </div>

        <div class="contact" id="contact">
            <h2>📞 Kontaktirajte nas!</h2>
            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 20px; margin-top: 20px;">
                <div>
                    <h3>📱 Telefon</h3>
                    <p><strong>011/123-456</strong></p>
                    <p>Radno vreme: 08-20h</p>
                </div>
                <div>
                    <h3>📧 Email</h3>
                    <p><strong>info@tvinternet.rs</strong></p>
                    <p>Odgovor u roku od 2h</p>
                </div>
                <div>
                    <h3>📍 Adresa</h3>
                    <p><strong>Beograd, Srbija</strong></p>
                    <p>Besplatna instalacija na teritoriji grada</p>
                </div>
                <div>
                    <h3>💬 Telegram Bot</h3>
                    <p><strong>@tv_internet_helper_bot</strong></p>
                    <p>24/7 automatski odgovori</p>
                </div>
            </div>
            
            <div style="margin-top: 30px; padding: 20px; background: rgba(255,255,255,0.1); border-radius: 10px;">
                <h3>🚀 Brza narudžbina preko Telegram bota:</h3>
                <a href="https://t.me/tv_internet_helper_bot" class="btn" style="background: linear-gradient(45deg, #0088cc, #006699); margin: 10px;">
                    🤖 Otvori Telegram Bota
                </a>
                <p style="margin-top: 10px; font-size: 0.9em;">Klikni gore da direktno pošalješ poruku našem botu!</p>
            </div>
        </div>

        <footer style="text-align: center; margin-top: 40px; padding: 20px; color: white; opacity: 0.8;">
            <p>© 2024 TVInternet.rs - Sva prava zadržana. | Napredni AI sistem za automatsku komunikaciju</p>
        </footer>
    </div>

    <script>
        // Jednostavni tracker za klikove
        document.querySelectorAll('.btn').forEach(btn => {
            btn.addEventListener('click', function() {
                // Možeš da dodaš Google Analytics ili drugi tracker ovde
                console.log('Kliknuto na:', this.textContent);
            });
        });
        
        // Animacija za pakete kada udju u viewport
        const observerOptions = {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        };
        
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.style.opacity = '1';
                    entry.target.style.transform = 'translateY(0)';
                }
            });
        }, observerOptions);
        
        // Inicijalno sakrij i pripremi pakete za animaciju
        document.querySelectorAll('.package').forEach(pkg => {
            pkg.style.opacity = '0';
            pkg.style.transform = 'translateY(30px)';
            pkg.style.transition = 'all 0.6s ease';
            observer.observe(pkg);
        });
    </script>
</body>
</html>
EOF