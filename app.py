from flask import Flask, send_from_directory, jsonify, request
from datetime import datetime
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__, static_folder='static')

# Configuration
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-key-please-change-in-production')

# Services data
SERVICES = [
    {
        'icon': '♿',
        'title': 'Mobility Support',
        'description': 'Comprehensive mobility assistance including wheelchair services, transportation, and accessibility solutions'
    },
    {
        'icon': '👁️',
        'title': 'Visual Assistance',
        'description': 'Support for visual impairments with screen readers, braille services, and navigation assistance'
    },
    {
        'icon': '👂',
        'title': 'Hearing Support',
        'description': 'Sign language interpretation, hearing aids assistance, and communication support services'
    },
    {
        'icon': '🧠',
        'title': 'Cognitive Support',
        'description': 'Specialized care for cognitive disabilities with tailored learning and daily living support'
    },
    {
        'icon': '🏥',
        'title': 'Medical Care',
        'description': 'Professional medical support, therapy sessions, and health monitoring services'
    },
    {
        'icon': '👥',
        'title': 'Community Integration',
        'description': 'Social programs, employment support, and community engagement activities'
    }
]

# Pricing plans
PRICING_PLANS = [
    {
        'name': 'Basic Care',
        'price': '$299',
        'period': 'per month',
        'features': [
            'Weekly check-ins',
            'Basic mobility support',
            'Emergency response',
            'Community access',
            'Phone support'
        ]
    },
    {
        'name': 'Standard Care',
        'price': '$599',
        'period': 'per month',
        'popular': True,
        'features': [
            'Daily support visits',
            'All Basic features',
            'Therapy sessions (2x/week)',
            'Transportation assistance',
            'Medical coordination',
            '24/7 emergency support'
        ]
    },
    {
        'name': 'Premium Care',
        'price': '$999',
        'period': 'per month',
        'features': [
            '24/7 dedicated care',
            'All Standard features',
            'Daily therapy sessions',
            'Personal care assistant',
            'Specialized medical care',
            'Family support program',
            'Custom care plans'
        ]
    }
]

@app.route('/')
def home():
    return send_from_directory('static', 'index.html')

@app.route('/about-us')
def about():
    return send_from_directory('static', 'about.html')

@app.route('/pricing')
def pricing():
    return send_from_directory('static', 'pricing.html')

@app.route('/contact-us')
def contact():
    return send_from_directory('static', 'contact.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)

@app.route('/api/services')
def get_services():
    return jsonify(SERVICES)

@app.route('/api/pricing')
def get_pricing():
    return jsonify(PRICING_PLANS)

@app.route('/api/contact', methods=['POST'])
def submit_contact():
    data = request.json
    # In production, send email or save to database
    print(f"Contact form submission: {data}")
    return jsonify({'success': True, 'message': 'Thank you for reaching out! We will contact you within 24 hours.'})

@app.route('/health')
def health():
    return jsonify({
        'status': 'healthy', 
        'timestamp': datetime.now().isoformat()
    })

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)