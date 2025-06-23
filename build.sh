#!/bin/bash
# Build-Script für Render.com Deployment

# 1. React-Frontend bauen
cd frontend_react
npm install
npm run build
cd ..

# 2. (Optional) Python-Abhängigkeiten installieren
pip install -r requirements.txt

# 3. Fertig! Flask nutzt das gebaute Frontend automatisch
