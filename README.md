# Python Career

## 📌 Project Overview
Python Career is a job portal designed to help Python professionals find relevant job opportunities. The platform allows users to browse job listings, view job details, and search for specific roles without requiring authentication.

## 🚀 Technologies Used
- **Python**
- **Django**
- **PostgreSQL**
- **Docker**
- **Git**
- **Celery & Redis** (for asynchronous tasks)
- **BeautifulSoup** (for web scraping)

## 🎯 Features
### 1️⃣ User-Free Interaction
- The platform is designed without user authentication, ensuring seamless access for job seekers and recruiters.

### 2️⃣ Job Listings
- Displays job postings with structured details, including:
  - Job title
  - Company name
  - Location
  - Publication date

### 3️⃣ Search Functionality
- Users can search for jobs based on:
  - Keywords
  - Filters for refining job searches

### 4️⃣ Data Scraping
- Integrated **BeautifulSoup** to scrape real-time job postings and populate the platform with up-to-date listings.

### 5️⃣ Asynchronous Tasks
- Implemented **Celery** and **Redis** to handle background tasks such as:
  - Job scraping
  - Updating job feeds automatically

### 6️⃣ Database Management
- Utilized **PostgreSQL** for efficient data storage and retrieval.

### 7️⃣ Containerization
- Used **Docker** for streamlined development and deployment processes.

## 📂 Project Structure
```
Python_Career/
├── jobportal/  # Main project directory
│   ├── jobportal/  # Django project settings
│   ├── jobs/  # Job listings app
│   │   ├── migrations/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── forms.py
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── tasks.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   ├── views.py
├── static/  # Static files (CSS, JS, Images)
├── templates/  # HTML templates
├── manage.py  # Django management script
├── requirements.txt  # Project dependencies
```

## ⚙️ How to Run the Project
### 1️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 2️⃣ Apply Migrations and Set Up the Database
```bash
python manage.py migrate
```

### 3️⃣ Run the Development Server
```bash
python manage.py runserver
```
Then, open your browser and go to `http://127.0.0.1:8000/`

### 4️⃣ Running the Celery Worker
```bash
celery -A jobportal worker --loglevel=info
```

### 5️⃣ Running Redis (if using Docker)
```bash
docker run -d -p 6379:6379 redis
```

## 📬 Contribution
If you would like to contribute, please fork the repository and submit a pull request with your improvements.

## 📜 License
This project is open-source and available under the **MIT License**.

