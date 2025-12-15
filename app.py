from flask import Flask, send_from_directory, jsonify, request,make_response
from datetime import datetime
import os

app = Flask(__name__, static_folder='static')

# Sample data for projects
PROJECTS = [
    {
        'id': 1,
        'title': 'E-Commerce Platform',
        'category': 'web',
        'description': 'A full-stack e-commerce solution with payment integration',
        'image': 'https://images.unsplash.com/photo-1557821552-17105176677c?w=800',
        'tags': ['Python', 'Flask', 'PostgreSQL', 'Stripe']
    },
    {
        'id': 2,
        'title': 'AI Chat Application',
        'category': 'ai',
        'description': 'Real-time chat application powered by machine learning',
        'image': 'https://images.unsplash.com/photo-1677442136019-21780ecad995?w=800',
        'tags': ['Python', 'TensorFlow', 'WebSocket', 'React']
    },
    {
        'id': 3,
        'title': 'Mobile Fitness Tracker',
        'category': 'mobile',
        'description': 'Cross-platform mobile app for health and fitness tracking',
        'image': 'https://images.unsplash.com/photo-1461896836934-ffe607ba8211?w=800',
        'tags': ['React Native', 'Node.js', 'MongoDB']
    },
    {
        'id': 4,
        'title': 'Data Visualization Dashboard',
        'category': 'data',
        'description': 'Interactive dashboard for business analytics and insights',
        'image': 'https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=800',
        'tags': ['Python', 'Plotly', 'Pandas', 'FastAPI']
    },
    {
        'id': 5,
        'title': 'Cloud Infrastructure Manager',
        'category': 'devops',
        'description': 'Tool for managing and monitoring cloud resources',
        'image': 'https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=800',
        'tags': ['Python', 'AWS', 'Docker', 'Kubernetes']
    },
    {
        'id': 6,
        'title': 'Blockchain Wallet',
        'category': 'blockchain',
        'description': 'Secure cryptocurrency wallet with multi-chain support',
        'image': 'https://images.unsplash.com/photo-1639762681485-074b7f938ba0?w=800',
        'tags': ['Solidity', 'Web3.js', 'Ethereum']
    }
]

SERVICES = [
    {
        'icon': '💻',
        'title': 'Web Development',
        'description': 'Custom web applications built with modern frameworks and best practices'
    },
    {
        'icon': '📱',
        'title': 'Mobile Development',
        'description': 'Native and cross-platform mobile apps for iOS and Android'
    },
    {
        'icon': '🤖',
        'title': 'AI & Machine Learning',
        'description': 'Intelligent solutions powered by cutting-edge AI technology'
    },
    {
        'icon': '☁️',
        'title': 'Cloud Solutions',
        'description': 'Scalable cloud infrastructure and deployment strategies'
    },
    {
        'icon': '🎨',
        'title': 'UI/UX Design',
        'description': 'Beautiful, intuitive interfaces that users love'
    },
    {
        'icon': '🔒',
        'title': 'Security & DevOps',
        'description': 'Secure, automated deployment pipelines and monitoring'
    }
]

@app.route("/", methods=['GET','POST'])
def index():

        with open("./static/index.html","r", encoding="utf-8") as file:
            file = file.read()
            
            response = make_response(file)
   
            return response

@app.route("/script.js")
def func():
    with open("./static/script.js","r") as file:
        file = file.read()
        response = make_response(file)
        response.headers['Content-Type'] = 'text/javascript; charset=utf-8'
        response.headers['X-Content-Type-Options'] = 'nosniff'
        return response
@app.route("/style.css")
def style():
    with open("./static/style.css","r") as file:
        file = file.read()
        response = make_response(file)
        response.headers['Content-Type'] = 'text/css; charset=utf-8'
        response.headers['X-Content-Type-Options'] = 'nosniff'
        return response
@app.route("/favicon.ico")
def fav():
    with open("./static/style.css","r") as file:
        file = file.read()
        response = make_response(file)
        response.headers['Content-Type'] = 'text/css; charset=utf-8'
        response.headers['X-Content-Type-Options'] = 'nosniff'
        return response

@app.route('/api/projects')
def get_projects():
    category = request.args.get('category', 'all')
    if category == 'all':
        return jsonify(PROJECTS)
    filtered = [p for p in PROJECTS if p['category'] == category]
    return jsonify(filtered)

@app.route('/api/services')
def get_services():
    return jsonify(SERVICES)

@app.route('/api/contact', methods=['POST'])
def contact():
    data = request.json
    # In production, you would send email or save to database
    print(f"Contact form submission: {data}")
    return jsonify({'success': True, 'message': 'Thank you for your message!'})

@app.route('/health')
def health():
    return jsonify({'status': 'healthy', 'timestamp': datetime.now().isoformat()})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=False)