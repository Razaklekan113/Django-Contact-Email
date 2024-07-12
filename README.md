# Django Contact Form

Simple Django project for sending emails via a contact form.

## Setup

1. Clone the repository.
2. Install dependencies (`pip install -r requirements.txt`).
3. Configure environment variables in `.env`.
4. Run migrations (`python manage.py migrate`).
5. Start the server (`python manage.py runserver`).

## Usage

- Fill out the form with recipient's email, subject, and message.
- Click "Send" to send the email.
- Feedback messages will confirm success or display errors.

## Deployment

- Set `DEBUG=False` for production.
- Securely manage email credentials and sensitive data.
