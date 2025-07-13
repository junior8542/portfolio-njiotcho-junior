#!/bin/bash

echo "🚀 Script de Déploiement - Portfolio NJIOTCHO JUNIOR"
echo "=================================================="

# Couleurs pour les messages
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Fonction pour afficher les messages
print_status() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Vérifier si Git est installé
if ! command -v git &> /dev/null; then
    print_error "Git n'est pas installé. Veuillez l'installer d'abord."
    exit 1
fi

# Vérifier si le repo est un repo Git
if [ ! -d ".git" ]; then
    print_warning "Ce dossier n'est pas un repo Git. Initialisation..."
    git init
    git add .
    git commit -m "Initial commit - Portfolio NJIOTCHO JUNIOR"
fi

print_status "Configuration du déploiement..."

# Créer .gitignore si il n'existe pas
if [ ! -f ".gitignore" ]; then
    print_status "Création du fichier .gitignore..."
    cat > .gitignore << EOF
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/
env.bak/
venv.bak/

# Flask
instance/
.webassets-cache

# React
frontend/node_modules/
frontend/.pnp
frontend/.pnp.js
frontend/coverage/
frontend/build/
frontend/.DS_Store
frontend/.env.local
frontend/.env.development.local
frontend/.env.test.local
frontend/.env.production.local
frontend/npm-debug.log*
frontend/yarn-debug.log*
frontend/yarn-error.log*

# IDE
.vscode/
.idea/
*.swp
*.swo

# OS
.DS_Store
Thumbs.db

# Logs
*.log

# Environment variables
.env
.env.local
.env.production
EOF
fi

# Vérifier les fichiers de déploiement
print_status "Vérification des fichiers de déploiement..."

required_files=("app.py" "requirements.txt" "Procfile" "runtime.txt" "frontend/package.json" "frontend/vercel.json")

for file in "${required_files[@]}"; do
    if [ -f "$file" ]; then
        print_status "✅ $file trouvé"
    else
        print_error "❌ $file manquant"
        exit 1
    fi
done

# Build du frontend
print_status "Build du frontend React..."
cd frontend

if [ ! -d "node_modules" ]; then
    print_status "Installation des dépendances React..."
    npm install
fi

print_status "Build de l'application React..."
npm run build

if [ $? -eq 0 ]; then
    print_status "✅ Build React réussi"
else
    print_error "❌ Erreur lors du build React"
    exit 1
fi

cd ..

# Commit et push des changements
print_status "Préparation du déploiement..."

# Ajouter tous les fichiers
git add .

# Commit
git commit -m "🚀 Préparation déploiement - $(date)"

print_status "✅ Fichiers préparés pour le déploiement"
echo ""
echo "🎯 Étapes suivantes :"
echo ""
echo "1. 🌐 BACKEND (Render/Railway) :"
echo "   - Aller sur https://render.com ou https://railway.app"
echo "   - Connecter votre repo GitHub"
echo "   - Créer un nouveau Web Service"
echo "   - Build Command: pip install -r requirements.txt"
echo "   - Start Command: gunicorn app:app"
echo ""
echo "2. ⚛️  FRONTEND (Vercel) :"
echo "   - Aller sur https://vercel.com"
echo "   - Connecter votre repo GitHub"
echo "   - Déployer automatiquement"
echo ""
echo "3. 🔧 POST-DÉPLOIEMENT :"
echo "   - Mettre à jour l'URL de l'API dans frontend/src/hooks/useApi.js"
echo "   - Configurer les variables d'environnement"
echo "   - Tester les fonctionnalités"
echo ""
echo "📚 Consultez DEPLOYMENT.md pour plus de détails"
echo ""
print_status "🚀 Prêt pour le déploiement !" 