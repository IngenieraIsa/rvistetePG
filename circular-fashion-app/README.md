# Circular Fashion App

## Overview
Circular Fashion App is a Django-based web application designed to promote circular fashion practices through a social networking platform. Users can share, exchange, and discuss sustainable fashion choices, fostering a community focused on eco-friendly clothing.

## Features
- User authentication and profiles
- Ability to post and share fashion items
- Commenting and liking system for posts
- Search functionality for items and users
- Responsive design for mobile and desktop

## Installation
1. Clone the repository:
   ```
   git clone https://github.com/yourusername/circular-fashion-app.git
   ```
2. Navigate to the project directory:
   ```
   cd circular-fashion-app
   ```
3. Create a virtual environment:
   ```
   python -m venv venv
   ```
4. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```
5. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage
1. Run database migrations:
   ```
   python manage.py migrate
   ```
2. Create a superuser to access the admin panel:
   ```
   python manage.py createsuperuser
   ```
3. Start the development server:
   ```
   python manage.py runserver
   ```
4. Access the application at `http://127.0.0.1:8000/`.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or features.

## License
This project is licensed under the MIT License. See the LICENSE file for details.