# PilatesMembershipAdvisor

## Overview
PilatesMembershipAdvisor is a web application designed to help users find their ideal Pilates membership options based on their anticipated class attendance. This interactive platform allows users to input the number of classes they plan to attend each month and receive tailored recommendations on the most cost-effective membership packages.

## Table of Contents
- [Overview](#overview)
- [Languages & Frameworks Used](#languages--frameworks-used)
- [Purpose](#purpose)
- [Features](#features)
- [Code Structure](#code-structure)
- [Installation](#installation)
- [Requirements](#requirements)
- [Inspiration](#inspiration)
- [Contributing](#contributing)
- [Contact](#contact)

## Languages & Frameworks Used
- **HTML**: Structure of the web pages.
- **CSS**: Styling and layout of the website.
- **JavaScript**: Interactivity and dynamic content.
- **FastAPI**: A modern web framework for building APIs with Python.
- **Jinja2**: A templating engine for rendering HTML pages dynamically.
- **Uvicorn**: An ASGI server for running FastAPI applications.

## Purpose
The purpose of this application is to:
- Provide users with an easy way to determine the best Pilates membership options based on their expected attendance.
- Offer an engaging and interactive user experience with a clean, modern design.

![IMG_9162](https://github.com/user-attachments/assets/27c04cde-f3cf-4769-a113-0066a4ce6de6)

## Features
- **Membership Recommendation System**: Users input the number of classes they plan to attend, and the app calculates the best membership options.
- **Cost Comparison**: The app provides a comparison between single-class pricing and membership options.

## Code Structure
- **static**: Contains CSS, images, videos, and other static files.
- **templates**: Holds the Jinja2 HTML templates for rendering pages.
- **main.py**: The main FastAPI application file that handles routing and logic.
- **style.css**: Styles for the application.

## Installation
1. Clone the repository:
   ```bash
   gh repo clone mariarodr1136/PilatesMembershipAdvisor
- Alternatively, if you prefer to use HTTPS:
   ```bash
   git clone https://github.com/mariarodr1136/PilatesMembershipAdvisor.git
2. Navigate into the project directory:
    ```bash
    cd PilatesMembershipAdvisor
3. Install the required dependencies:
    ```bash
    pip install fastapi uvicorn
4. Start the local server:
    ```bash
    uvicorn main:app --reload
5. Open the application in your browser:
    ```bash
    http://127.0.0.1:8000/

## Requirements
- A modern web browser: Chrome, Firefox, Safari, etc., for the best user experience.
- Python: Ensure you have Python installed on your machine.
- FastAPI and Uvicorn: Required libraries to run the application.

## Inspiration
This application was inspired by the need for a user-friendly tool that simplifies the decision-making process for Pilates enthusiasts looking to choose the right membership package.

## Contributing
Feel free to submit issues or pull requests for improvements or bug fixes. You can also open issues to discuss potential changes or enhancements. All contributions are welcome to enhance the app’s features or functionality!

To contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b feat/your-feature-name
- Alternatively, for bug fixes:
   ```bash
   git checkout -b fix/your-bug-fix-name
3. Make your changes and run all tests before committing the changes and make sure all tests are passed.
4. After all tests are passed, commit your changes with descriptive messages:
   ```bash
   git commit -m 'add your commit message'
5. Push your changes to your forked repository:
   ```bash
   git push origin feat/your-feature-name.
6. Submit a pull request to the main repository, explaining your changes and providing any necessary details.

## Contact
If you have any questions or feedback, feel free to reach out at [mrodr.contact@gmail.com](mailto:mrodr.contact@gmail.com).

