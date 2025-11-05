# Kreiraj osnovnu web strukturu
mkdir -p web-content
cd web-content

# Kreiraj glavni HTML fajl
cat > index.html << 'EOF'
<!DOCTYPE html>
<html lang="sr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>TV & Internet Paketi</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body { font-family: Arial, sans-serif; line-height: 1.6; background: #f4f4f4; }
        .container { max-width: 1200px; margin: 0 auto; padding: 20px; }
        header { background: #2c3e50; color: white; padding: 1rem; text-align: center; }
        .package { background: white; margin: 20px 0; padding: 20px; border-radius: 8px; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
        .contact { background: #3498db; color: white; padding: 20px; border-radius: 8px; text-align: center; }
        h1 { margin-bottom: 1rem; }
        h2 { color: #2c3e50; margin-bottom: 1rem; }
        .price { color: #e74c3c; font-weight: bold; font-size: 1.2em; }
    </style>
</head>
<body>
    <header>
        <h1>📺🌐 TV & Internet Paketi</h1>
        <p>Najbolje ponude za vaš dom</p>
    </header>

    <div class="container">
        <div class="package">
            <h2>📺 TV Paketi</h2>
            <p><strong>Osnovni paket:</strong> 200+ kanala <span class="price">1.990 RSD/mesec</span></p>
            <p><strong>Sportski paket:</strong> +50 sportskih kanala <span class="price">2.490 RSD/mesec</span></p>
            <p><strong>Premium paket:</strong> Svi kanali + filmovi <span class="price">2.990 RSD/mesec</span></p>
        </div>

        <div class="package">
            <h2>🌐 Internet Paketi</h2>
            <p><strong>100 Mbps:</strong> Idealno za porodicu <span class="price">1.490 RSD/mesec</span></p>
            <p><strong>300 Mbps:</strong> Za zahtevnije korisnike <span class="price">2.290 RSD/mesec</span></p>
            <p><strong>1 Gbps:</strong> Najbrza opcija <span class="price">3.490 RSD/mesec</span></p>
        </div>

        <div class="contact">
            <h2>📞 Kontaktirajte nas!</h2>
            <p>Telefon: <strong>011/123-456</strong></p>
            <p>Email: <strong>info@tv-internet.rs</strong></p>
            <p>Telegram bot: <strong>@tv_internet_helper_bot</strong> (uskoro)</p>
            <p>Radno vreme: 08:00 - 20:00</p>
        </div>
    </div>
</body>
</html>
EOF

# Vrati se u glavni folder
cd ..