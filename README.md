# USDA_Project (Unified Scientific Discovery Accelerator)
Designed a system to analyze and suggest disease-related research papers using graph databases. Utilized Neo4j to model relationships between variuos entities such as diseases,research papers,USDA datasets.

🔬 A Django + Neo4j-based web app that helps users search for diseases or medicines and discover related scientific research, treatments, and authorship details.

## 🌐 Tech Stack

- 🐍 Django (Backend)
- 🧠 Neo4j (Graph Database)
- 💅 HTML/CSS (Frontend)
- 🔍 Cypher Query Language

## ⚙️ Features

- Search by **Disease** or **Medicine**
- Get related:
  - Paper title
  - Author & affiliation
  - Medicine used
  - Overview & paper link
- Clean UI with Django templates and custom CSS

## 🗃️ Setup Instructions

```bash
# Clone the repo
git clone https://github.com/your-username/usda-project.git
cd usda-project

# Set up virtual environment
python -m venv myenv
myenv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run Django server
python manage.py runserver

## 📸 Screenshots

### 🏠 Landing Page
![Home Page](assets/Home_page.png)

### 📄 Result Page
![Result Page](assets/Result_page.png)
