# Contribution Guide

Thank you for your interest in contributing to the Django Admin Dashboard project! This document contains essential information on how you can contribute to this project.

---

## How to Contribute

1. **Fork the Repository**
   
   Start by forking this repository to your GitHub account.

2. **Clone the Repository**
   
   ```bash
   git clone https://github.com/yourusername/django-admin-dashboard.git
   cd django-admin-dashboard
   ```

3. **Create a New Branch**
   
   ```bash
   git checkout -b feature/feature-name
   ```
   or
   ```bash
   git checkout -b fix/bug-name
   ```

4. **Make Changes**
   
   Make the necessary changes and ensure your code follows the project's coding guidelines.

5. **Commit the Changes**
   
   ```bash
   git commit -m "Description of the changes made"
   ```

6. **Push to the Branch**
   
   ```bash
   git push origin feature/feature-name
   ```

7. **Create a Pull Request**
   
   Go to the GitHub page of your forked repository and click on "New Pull Request".

---

## Code Guidelines

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) for Python code style
- Use 4 spaces for indentation (not tabs)
- Use descriptive names for functions, variables, and classes
- Add clear comments for complex code logic
- Separate business logic from the view code

---

## Pull Request Process

1. **Code Review**
   
   Every pull request will be reviewed by the project maintainer. They might provide feedback or request changes.

2. **CI/CD Checks**
   
   Pull requests must pass all configured CI/CD checks.

3. **Merging**
   
   Once reviewed and approved, your pull request will be merged into the main branch.

---

## Types of Contributions

### New Features

If you want to add a new feature:

1. Discuss the feature with the maintainers first by creating an issue
2. Provide a detailed description of the proposed feature
3. Explain why this feature is useful for the project

### Bug Fixes

To fix a bug:

1. Check if the bug has already been reported in the issues section
2. If not, create a new issue with steps to reproduce the bug
3. Describe the expected behavior vs. the actual behavior

### Documentation

Documentation contributions are highly appreciated:

1. Fix typos or inaccurate information
2. Add examples or clearer explanations
3. Improve the overall clarity and completeness of the documentation

---

## Development Setup

1. **Prepare Environment**
   
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate  # Windows
   pip install -r requirements.txt
   ```

2. **Setup Database**
   
   ```bash
   python manage.py migrate
   ```

3. **Run the Server**
   
   ```bash
   python manage.py runserver
   ```

---

## Testing

- Write unit tests for every new feature or bug fix
- Run tests before making a pull request:
  ```bash
  python manage.py test
  ```

---

## Bug Reports

If you find a bug, please create an issue with the following information:

- A clear and concise description of the bug
- Steps to reproduce the bug
- Expected behavior
- Screenshots (if possible)
- Environment details (OS, browser, Python version, Django version)

---

## Contact

If you have any questions that are not covered in this document, feel free to reach out:

- Maintainer Name: ikbaltaqyudin@gmail.com

---

Thank you for contributing to the Django Admin Dashboard!