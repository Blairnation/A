# Advocate Information Web Application

The Advocate Information Web Application is a web platform that allows users to explore information about various developer advocates. It combines the power of Django Rest Framework (DRF) as the backend and React as the frontend to create a seamless and interactive user experience.

## Key Features

- **Advocate Data:** The app collects data about developer advocates, including their username, profile picture, bio, and other relevant information. This data is retrieved from multiple sources, including web scraping and the Twitter API.

- **Search Functionality:** Users can search for specific advocates using a search bar. The application communicates with the backend to fetch advocate information that matches the search query.

- **Advocate Details:** Clicking on an advocate's profile provides detailed information, including their profile picture, username, bio, and the company they work for.

- **Responsive Design:** The application offers a responsive design, making it accessible from various devices, including desktops, tablets, and mobile phones.

- **API Integration:** DRF serves as the backend API for the application. It is responsible for retrieving advocate data from various sources and delivering it to the frontend.

## Tech Stack

- **Backend:** Django, Django Rest Framework (DRF), Web Scraping, Twitter API
- **Frontend:** React, Axios for API requests
- **Database:** (Not mentioned in the provided code, but you'll likely use a database for storing advocate data)
- **Styling:** CSS (your provided CSS styles)
- **Deployment:** The application can be hosted on platforms like Heroku or AWS for public access.

## Getting Started

To set up and run the Advocate Information Web Application on your local machine, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/Blairnation/Advocates-Backend-API-with-DRF.git
