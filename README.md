# Art Abloom

Art Abloom is an art blogging website built using Django and Python. It allows users to sign in, create, edit, and delete blogs, as well as post blogs with images. Admin users have access to additional functionalities for managing the blog content.

## Features

- **User Authentication**: Sign up, sign in, and sign out functionality.
- **Blog Management**: Create, edit, delete, and view blogs.
- **Image Upload**: Add images to your blog posts.
- **Admin Access**: Enhanced functionalities for managing blogs.

## Table of Contents

- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## Technologies Used

- Django
- Python
- HTML/CSS
- Bootstrap (optional for styling)
- SQLite (default database)

## Installation

### Prerequisites

- Python 3.x installed on your system
- pip (Python package installer)

### Steps

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/Art-Abloom.git
    ```
2. Navigate to the project directory:
    ```bash
    cd Art-Abloom
    ```
3. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
5. Apply migrations to set up the database:
    ```bash
    python manage.py migrate
    ```
6. Create a superuser for admin access:
    ```bash
    python manage.py createsuperuser
    ```
7. Start the development server:
    ```bash
    python manage.py runserver
    ```

## Usage

1. Open your web browser and go to `http://127.0.0.1:8000/`.
2. Sign up for a new account or log in with an existing account.
3. Create, edit, and delete blogs as per your requirements.
4. Admin users can log in at `http://127.0.0.1:8000/admin/` to manage blog content.

## Contributing

Contributions to the project are welcome. Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

For any questions or support, please contact [your email].

---

By following this README, users should be able to understand the purpose of the project, the methods used, and how to replicate the study


