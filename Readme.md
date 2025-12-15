# Portfolio Website - The Ninth Cloud

A modern, responsive portfolio website built with Flask and Docker.

## 🚀 Quick Start

### Local Development

1. **Clone and setup:**
```bash
git clone <your-repo>
cd portfolio-website
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

2. **Run the app:**
```bash
python app.py
```

3. **Visit:** http://localhost:5000

### Docker Deployment

**Option 1: Docker Compose (Recommended)**
```bash
docker-compose up -d
```

**Option 2: Docker Commands**
```bash
# Build
docker build -t portfolio-website .

# Run
docker run -d -p 5000:5000 --name portfolio portfolio-website

# Stop
docker stop portfolio

# Remove
docker rm portfolio
```

## 📁 Project Structure