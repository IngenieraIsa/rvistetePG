# Circular Fashion App

## Overview
The Circular Fashion App is a social network platform designed to promote circular fashion by allowing users to buy, sell, or rent clothing items. This application aims to create a sustainable fashion community where users can easily exchange clothing items, reducing waste and promoting eco-friendly practices.

## Features
- User registration and authentication
- Profile management for users
- Listing of clothing items for sale or rent
- Search and filter options for items
- Messaging system for users to communicate
- Admin panel for managing users and items

## Technologies Used
- Django: A high-level Python web framework for building web applications.
- Django REST Framework: A powerful toolkit for building Web APIs.
- PostgreSQL: A robust database system for storing user and item data.
- HTML/CSS/JavaScript: For front-end development.

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
6. Set up the database:
   ```
   python manage.py migrate
   ```
7. Create a superuser for the admin panel:
   ```
   python manage.py createsuperuser
   ```
8. Run the development server:
   ```
   python manage.py runserver
   ```

## Usage
- Access the application at `http://127.0.0.1:8000/`.
- Use the admin panel at `http://127.0.0.1:8000/admin/` to manage users and items.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for details.