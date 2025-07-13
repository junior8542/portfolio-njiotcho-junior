from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_mail import Mail, Message
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'votre_cle_secrete_ici'  # Changez ceci en production

# Configuration CORS pour permettre les requêtes depuis le frontend React
CORS(app, origins=['http://localhost:3000', 'http://127.0.0.1:3000'])

# Configuration
app.config['UPLOAD_FOLDER'] = 'static/uploads'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max file size

# Configuration Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'juniornjiotcho@gmail.com'  # Remplacez par votre email
app.config['MAIL_PASSWORD'] = 'juniorlion8542' # Mot de passe d'application Gmail

mail = Mail(app)

# Données du portfolio (à personnaliser)
portfolio_data = {
    'name': 'NJIOTCHO JUNIOR',
    'title': 'Développeur Web Full-Stack & Spécialiste IA',
    'tagline': 'Développeur web passionné avec plus de 2 ans d\'expérience dans la création d\'applications web modernes et performantes. De même, je fais mes preuves dans l\'intelligence artificielle. Spécialisé en Python, JavaScript et React.',
    'email': 'juniornjiotcho@gmail.com',
    'phone': '+237 680 640 264',
    'location': 'Douala, Cameroun',
    'about': {
        'description': "Développeur Full-Stack, Data Analyst, Expert en IA & Électronicien.\n\nPassionné par les technologies, je conçois des solutions intelligentes qui unissent développement logiciel, analyse des données et systèmes embarqués. J'interviens sur toute la chaîne, de la création d'applications web/mobile (React, Node.js, Django, Flask) à l'implémentation d'algorithmes d'IA (Machine Learning, Deep Learning) pour valoriser les données. Parallèlement, j'intègre capteurs et microcontrôleurs (Arduino, Raspberry Pi) pour développer des systèmes IoT performants. Curieux, rigoureux et orienté innovation, je transforme les idées complexes en produits fonctionnels, fiables et centrés sur l'utilisateur.",
        'skills': [
            'Python', 'Flask', 'Django', 'JavaScript', 'React', 'Vue.js',
            'HTML5', 'CSS3', 'Sass', 'Git', 'Docker', 'AWS', 'PostgreSQL', 'MongoDB'
        ],
        'experience': [
            {
                'title': 'Développeur Full-Stack Senior',
                'company': 'Soft-Express',
                'period': '2020 - Présent',
                'description': 'Développement d\'applications web complexes avec Python et React'
            },
            {
                'title': 'Développeur Backend',
                'company': 'Enset_Douala',
                'period': '2024 - 2025',
                'description': 'API REST avec Flask et bases de données PostgreSQL'
            }
        ],
        'education': [
            {
                'degree': 'Licence en Informatique fondamentale',
                'school': " Faculte des Sciences Université De Douala",
                'year': '2022'
            },
            {
                'degree': 'DIPET1',
                'school': "École Normale d'Enseignement Technique",
                'year': '2026'
            },
            {
                'degree': 'Licence Technologique (Automatisme)',
                'school': "École Normale d'Enseignement Technique / Université De Douala",
                'year': '2026'
            },
            {
                'degree': 'Baccalauréat C ',
                'school': "Lycée Bilingue de Balengou ",
                'year': '2018'
            },
            {
                'degree': 'Probatoire C ',
                'school': "Lycée Bilingue de Balengou ",
                'year': '2017'
            },
            {
                'degree': 'BEPC ',
                'school': "Lycée Bilingue de Balengou ",
                'year': '2014'
            },
            
            
        ]
    },
    'projects': [
        {
            'id': 1,
            'title': 'Plateforme de gestion des elections presidentielles au  Cameroun',
            'description': 'Une application web Flask pour la gestion des élections présidentielles au Cameroun..',
            'technologies': ['Python', 'Flask', 'PostgreSQL', 'Stripe', 'Bootstrap','Vercel'],
            'image': 'project1.jpg',
            'github': 'https://github.com/junior8542/project1',
            'demo': 'https://demo-project1.com',
            'featured': True
        },
        {
            'id': 2,
            'title': 'Robot Suiveur',
            'description': 'Implementation d\'un robot suiveur de ligne et application de contrôle.',
            'technologies': ['Arduino','Proteus'],
            'image': 'project2.jpg',
            'github': 'https://github.com/junior8542/project2',
            'demo': 'https://demo-project2.com',
            'featured': True
        },
        {
            'id': 3,
            'title': 'Design Avec photoshop',
            'description': 'logo de ma plateforme de troc nommé : PmExchange réalisé avec photoshop et illustrator.',
            'technologies': ['Photoshop','Illustrator'],
            'image': 'project3.jpg',
            'github': 'https://github.com/junior8542/project3',
            'demo': 'https://demo-project3.com',
            'featured': False
        },
        {
            'id': 4,
            'title': 'PmExchange - Plateforme d\'échange de biens et services',
            'description': 'Plateforme web innovante permettant l\'échange de biens et services entre utilisateurs. Système de notation, messagerie intégrée, géolocalisation et paiements sécurisés.',
            'technologies': ['React', 'Node.js', 'MongoDB', 'Express.js', 'Socket.io', 'Stripe', 'Google Maps API'],
            'image': 'project4.jpg',
            'github': 'https://github.com/junior8542/pmexchange',
            'demo': 'https://pmexchange-demo.com',
            'featured': True
        },
        {
            'id': 5,
            'title': 'Serveur de messagerie ZIMBRA - Déploiement et configuration',
            'description': 'Déploiement complet d\'un serveur de messagerie d\'entreprise avec ZIMBRA. Configuration des services email, calendrier, contacts et collaboration. Mise en place de la sécurité et sauvegarde automatisée.',
            'technologies': ['ZIMBRA', 'Linux', 'Docker', 'PostgreSQL', 'Nginx', 'SSL/TLS', 'Bash Scripting'],
            'image': 'project5.jpg',
            'github': 'https://github.com/junior8542/zimbra-server',
            'demo': 'https://mail.company-demo.com',
            'featured': True
        }
    ],
    'social': {
        'github': 'https://github.com/junior8542',
        'linkedin': 'https://linkedin.com/in/junior-njiotcho-58581228b',
        'twitter': 'https://twitter.com/njiotcho_junior',
        'instagram': 'https://instagram.com/njiotcho_junior',
        'facebook': 'https://facebook.com/njiotcho.junior',
        'youtube': 'https://youtube.com/@juniornjiotcho9716',
        'discord': 'https://discord.gg/njiotcho',
        'telegram': 'https://t.me/njiotcho_junior'
    }
}

# Routes API

@app.route('/api/health')
def health_check():
    """Endpoint de santé de l'API"""
    return jsonify({
        'status': 'healthy',
        'message': 'API Portfolio fonctionnelle',
        'timestamp': datetime.now().isoformat()
    })

@app.route('/api/profile')
def get_profile():
    """Récupérer les informations du profil"""
    return jsonify({
        'name': portfolio_data['name'],
        'title': portfolio_data['title'],
        'tagline': portfolio_data['tagline'],
        'email': portfolio_data['email'],
        'phone': portfolio_data['phone'],
        'location': portfolio_data['location'],
        'social': portfolio_data['social']
    })

@app.route('/api/about')
def get_about():
    """Récupérer les informations à propos"""
    return jsonify(portfolio_data['about'])

@app.route('/api/projects')
def get_projects():
    """Récupérer tous les projets"""
    return jsonify({
        'projects': portfolio_data['projects']
    })

@app.route('/api/projects/<int:project_id>')
def get_project(project_id):
    """Récupérer un projet spécifique par ID"""
    project = next((p for p in portfolio_data['projects'] if p['id'] == project_id), None)
    if project:
        return jsonify(project)
    return jsonify({'error': 'Projet non trouvé'}), 404

@app.route('/api/projects/featured')
def get_featured_projects():
    """Récupérer seulement les projets mis en avant"""
    featured_projects = [p for p in portfolio_data['projects'] if p['featured']]
    return jsonify({
        'projects': featured_projects
    })

@app.route('/api/contact', methods=['POST'])
def send_contact():
    """Envoyer un message de contact"""
    try:
        data = request.get_json()
        
        # Validation des données
        required_fields = ['name', 'email', 'subject', 'message']
        for field in required_fields:
            if not data.get(field):
                return jsonify({'error': f'Le champ {field} est requis'}), 400
        
        name = data['name']
        email = data['email']
        subject = data['subject']
        message = data['message']
        
        # Construction du message email
        msg = Message(
            subject=f"Contact Portfolio: {subject}",
            sender=app.config['MAIL_USERNAME'],
            recipients=[app.config['MAIL_USERNAME']],  # Vous recevez le mail
            body=f"De: {name} <{email}>\n\n{message}"
        )
        
        mail.send(msg)
        
        return jsonify({
            'success': True,
            'message': 'Message envoyé avec succès ! Je vous répondrai bientôt.'
        })
        
    except Exception as e:
        return jsonify({
            'error': 'Erreur lors de l\'envoi du message. Veuillez réessayer plus tard.',
            'details': str(e)
        }), 500

@app.route('/api/skills')
def get_skills():
    """Récupérer la liste des compétences"""
    return jsonify({
        'skills': portfolio_data['about']['skills']
    })

@app.route('/api/experience')
def get_experience():
    """Récupérer l'expérience professionnelle"""
    return jsonify({
        'experience': portfolio_data['about']['experience']
    })

@app.route('/api/education')
def get_education():
    """Récupérer la formation"""
    return jsonify({
        'education': portfolio_data['about']['education']
    })

# Gestion des erreurs
@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Endpoint non trouvé'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Erreur interne du serveur'}), 500

@app.errorhandler(405)
def method_not_allowed(error):
    return jsonify({'error': 'Méthode non autorisée'}), 405

if __name__ == '__main__':
    # Créer le dossier uploads s'il n'existe pas
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    
    print("🚀 API Portfolio démarrée sur http://localhost:5000")
    print("📚 Documentation des endpoints:")
    print("   GET  /api/health - Vérification de santé")
    print("   GET  /api/profile - Informations du profil")
    print("   GET  /api/about - Informations à propos")
    print("   GET  /api/projects - Tous les projets")
    print("   GET  /api/projects/<id> - Projet spécifique")
    print("   GET  /api/projects/featured - Projets mis en avant")
    print("   POST /api/contact - Envoyer un message")
    print("   GET  /api/skills - Compétences")
    print("   GET  /api/experience - Expérience professionnelle")
    print("   GET  /api/education - Formation")
    
    # Configuration pour le déploiement
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV') == 'development'
    
    app.run(debug=debug, host='0.0.0.0', port=port) 