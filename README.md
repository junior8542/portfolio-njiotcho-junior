# Portfolio Personnel - NJIOTCHO JUNIOR

## 🚀 Description

Portfolio professionnel moderne développé avec **React** (frontend) et **Flask** (backend API). Ce projet présente mes compétences en développement web, mes réalisations et mon expérience professionnelle.

## ✨ Fonctionnalités

### Frontend React
- **Design moderne et responsive** avec animations fluides
- **Navigation intuitive** avec React Router
- **Pages dynamiques** : Accueil, À propos, Projets, Contact
- **Marquee animé** sur toutes les pages
- **Intégration API** avec hooks personnalisés
- **Gestion d'état** avec React Hooks
- **Animations CSS** et transitions fluides

### Backend Flask API
- **API REST** complète avec endpoints JSON
- **CORS configuré** pour le frontend React
- **Gestion des emails** avec Flask-Mail
- **Validation des données** côté serveur
- **Gestion d'erreurs** robuste
- **Documentation des endpoints** intégrée

## 🛠️ Technologies Utilisées

### Frontend
- **React 18** - Framework JavaScript
- **React Router** - Navigation
- **CSS3** - Styles et animations
- **FontAwesome** - Icônes
- **Responsive Design** - Mobile-first

### Backend
- **Flask** - Framework Python
- **Flask-CORS** - Gestion CORS
- **Flask-Mail** - Envoi d'emails
- **JSON** - Format de données

## 📁 Structure du Projet

```
mon_portfolio/
├── app.py                 # Backend Flask API
├── requirements.txt       # Dépendances Python
├── README.md             # Documentation
└── frontend/             # Application React
    ├── public/
    │   └── images/       # Images statiques
    ├── src/
    │   ├── components/   # Composants React
    │   ├── pages/        # Pages de l'application
    │   ├── hooks/        # Hooks personnalisés
    │   ├── services/     # Services API
    │   └── styles/       # Fichiers CSS
    └── package.json      # Dépendances Node.js
```

## 🚀 Installation et Démarrage

### Prérequis
- Python 3.8+
- Node.js 16+
- npm ou yarn

### Backend Flask

1. **Installer les dépendances Python :**
```bash
pip install -r requirements.txt
```

2. **Démarrer le serveur Flask :**
```bash
python app.py
```

Le backend sera accessible sur `http://localhost:5000`

### Frontend React

1. **Naviguer vers le dossier frontend :**
```bash
cd frontend
```

2. **Installer les dépendances :**
```bash
npm install
```

3. **Démarrer l'application React :**
```bash
npm start
```

Le frontend sera accessible sur `http://localhost:3000`

## 📚 API Endpoints

### Endpoints Disponibles

| Méthode | Endpoint | Description |
|---------|----------|-------------|
| GET | `/api/health` | Vérification de santé de l'API |
| GET | `/api/profile` | Informations du profil |
| GET | `/api/about` | Informations à propos |
| GET | `/api/projects` | Tous les projets |
| GET | `/api/projects/<id>` | Projet spécifique |
| GET | `/api/projects/featured` | Projets mis en avant |
| POST | `/api/contact` | Envoyer un message |
| GET | `/api/skills` | Compétences |
| GET | `/api/experience` | Expérience professionnelle |
| GET | `/api/education` | Formation |

### Exemple d'utilisation

```javascript
// Récupérer le profil
const response = await fetch('http://localhost:5000/api/profile');
const profile = await response.json();

// Envoyer un message de contact
const contactData = {
  name: 'John Doe',
  email: 'john@example.com',
  subject: 'Collaboration',
  message: 'Bonjour, je souhaite collaborer...'
};

const response = await fetch('http://localhost:5000/api/contact', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify(contactData)
});
```

## 🎨 Fonctionnalités du Design

### Animations
- **Fade In** - Apparition progressive des éléments
- **Slide In** - Glissement depuis les côtés
- **Scale** - Effets de zoom au survol
- **Gradient Animations** - Dégradés animés

### Responsive Design
- **Mobile-first** - Optimisé pour mobile
- **Tablet** - Adaptation pour tablettes
- **Desktop** - Interface complète pour desktop

### Couleurs et Thème
- **Palette moderne** - Bleus, violets, gris
- **Gradients** - Dégradés élégants
- **Contraste** - Lisibilité optimale

## 📱 Pages Disponibles

### 🏠 Accueil
- Présentation personnelle
- Projets mis en avant
- Statistiques rapides
- Call-to-action

### 👤 À propos
- Description détaillée
- Compétences techniques
- Expérience professionnelle
- Formation

### 💻 Projets
- Galerie de projets
- Filtres par technologie
- Détails des projets
- Liens vers GitHub/Demo

### 📧 Contact
- Formulaire de contact
- Informations de contact
- Liens sociaux
- Envoi d'email

## 🔧 Configuration

### Variables d'environnement

Pour le backend Flask, configurez dans `app.py` :

```python
# Configuration email
app.config['MAIL_USERNAME'] = 'votre-email@gmail.com'
app.config['MAIL_PASSWORD'] = 'votre-mot-de-passe-app'

# Clé secrète
app.secret_key = 'votre-cle-secrete'
```

### Personnalisation

1. **Modifier les données** dans `app.py` (section `portfolio_data`)
2. **Changer les images** dans `frontend/public/images/`
3. **Ajuster les couleurs** dans les fichiers CSS
4. **Modifier les animations** selon vos préférences

## 🚀 Déploiement

### Backend (Heroku, Railway, etc.)
```bash
# Créer un Procfile
echo "web: python app.py" > Procfile

# Déployer
git push heroku main
```

### Frontend (Vercel, Netlify, etc.)
```bash
# Build de production
npm run build

# Déployer le dossier build
```

## 📊 Projets Inclus

1. **Plateforme de gestion des élections présidentielles** - Flask, PostgreSQL
2. **Robot Suiveur** - Arduino, Proteus
3. **Design Photoshop** - Logo PmExchange
4. **PmExchange** - Plateforme d'échange de biens et services
5. **Serveur ZIMBRA** - Déploiement serveur de messagerie

## 🤝 Contribution

Les contributions sont les bienvenues ! Pour contribuer :

1. Fork le projet
2. Créer une branche feature (`git checkout -b feature/AmazingFeature`)
3. Commit les changements (`git commit -m 'Add AmazingFeature'`)
4. Push vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrir une Pull Request

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

## 📞 Contact

- **Email** : juniornjiotcho@gmail.com
- **Téléphone** : +237 680 640 264
- **Localisation** : Douala, Cameroun

---

**Développé avec ❤️ par NJIOTCHO JUNIOR** 