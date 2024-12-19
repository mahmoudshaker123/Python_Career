

from celery import shared_task
import requests
from bs4 import BeautifulSoup
from .models import Job

@shared_task
def fetch_jobs_from_indeed():
    url = "https://eg.indeed.com/jobs?q=python&l="
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    job_posts = soup.find_all('div', class_='job_seen_beacon')
    
    for post in job_posts:
        title = post.find('h2').text.strip()
        company = post.find('span', class_='companyName').text.strip()
        location = post.find('div', class_='companyLocation').text.strip()
        posted_at = post.find('span', class_='date').text.strip()
        link = post.find('a')['href']
        
        Job.objects.create(
            title=title,
            company=company,
            location=location,
            posted_at=posted_at,
            link=f"https://eg.indeed.com{link}",
        )

    return "Jobs fetched from Indeed successfully!"
