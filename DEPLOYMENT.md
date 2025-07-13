# 🚀 Guide de Déploiement - Portfolio NJIOTCHO JUNIOR

## 📋 Prérequis
- Compte GitHub
- Compte Vercel (gratuit)
- Compte Render ou Railway (gratuit)

## 🎯 Plan de Déploiement

### 1. **Backend Flask (API) - Render/Railway**

#### Option A : Render (Recommandé)
1. **Créer un compte Render** : https://render.com
2. **Connecter votre repo GitHub**
3. **Créer un nouveau Web Service**
4. **Configuration** :
   - **Build Command** : `pip install -r requirements.txt`
   - **Start Command** : `gunicorn app:app`
   - **Environment Variables** :
     ```
     FLASK_ENV=production
     SECRET_KEY=votre_cle_secrete_ici
     MAIL_SERVER=smtp.gmail.com
     MAIL_PORT=587
     MAIL_USE_TLS=True
     MAIL_USERNAME=juniornjiotcho@gmail.com
     MAIL_PASSWORD=votre_mot_de_passe_application
     ```

#### Option B : Railway
1. **Créer un compte Railway** : https://railway.app
2. **Connecter votre repo GitHub**
3. **Déployer automatiquement**

### 2. **Frontend React - Vercel**

1. **Créer un compte Vercel** : https://vercel.com
2. **Connecter votre repo GitHub**
3. **Configuration automatique** :
   - Framework Preset : Create React App
   - Build Command : `npm run build`
   - Output Directory : `build`
   - Install Command : `npm install`

## 🔧 Configuration Post-Déploiement

### 1. **Mettre à jour les URLs CORS**
Dans le backend déployé, mettre à jour les URLs autorisées :
```python
CORS(app, origins=[
    'https://votre-frontend.vercel.app',
    'http://localhost:3000'  # Pour le développement
])
```

### 2. **Mettre à jour l'URL de l'API dans le frontend**
Dans `frontend/src/hooks/useApi.js`, remplacer :
```javascript
const API_BASE_URL = 'http://localhost:5000';
```
Par :
```javascript
const API_BASE_URL = 'https://votre-backend.render.com';
```

### 3. **Configurer l'email**
1. **Gmail** : Activer l'authentification à 2 facteurs
2. **Créer un mot de passe d'application**
3. **Utiliser ce mot de passe dans les variables d'environnement**

## 📁 Structure des Fichiers de Déploiement

```
mon_portfolio/
├── app.py                 # Backend Flask
├── requirements.txt       # Dépendances Python
├── Procfile              # Configuration Heroku/Render
├── runtime.txt           # Version Python
├── env.example           # Variables d'environnement
├── frontend/
│   ├── package.json      # Dépendances React
│   ├── vercel.json       # Configuration Vercel
│   └── public/           # Assets statiques
└── static/               # Images et uploads
```

## 🔒 Sécurité

### Variables d'Environnement à Configurer
- `SECRET_KEY` : Clé secrète pour Flask
- `MAIL_PASSWORD` : Mot de passe d'application Gmail
- `FLASK_ENV` : `production` en production

### CORS Configuration
Autoriser seulement les domaines de votre frontend déployé.

## 🚀 Commandes de Déploiement

### Backend (Local Test)
```bash
# Installer les dépendances
pip install -r requirements.txt

# Tester localement
python app.py
```

### Frontend (Local Test)
```bash
cd frontend
npm install
npm start
```

### Build Frontend
```bash
cd frontend
npm run build
```

## 📊 Monitoring

### Backend
- **Render Dashboard** : Monitoring automatique
- **Logs** : Accessibles via le dashboard
- **Health Check** : `/api/health`

### Frontend
- **Vercel Analytics** : Performance et erreurs
- **Build Logs** : Accessibles via le dashboard

## 🔄 Mise à Jour

### Backend
1. Pousser les changements sur GitHub
2. Déploiement automatique sur Render/Railway

### Frontend
1. Pousser les changements sur GitHub
2. Déploiement automatique sur Vercel

## 🆘 Dépannage

### Erreurs Courantes
1. **CORS** : Vérifier les URLs autorisées
2. **Email** : Vérifier les credentials Gmail
3. **Build** : Vérifier les dépendances

### Logs
- **Backend** : Dashboard Render/Railway
- **Frontend** : Dashboard Vercel

## 📞 Support
- **Documentation Render** : https://render.com/docs
- **Documentation Vercel** : https://vercel.com/docs
- **Documentation Flask** : https://flask.palletsprojects.com 