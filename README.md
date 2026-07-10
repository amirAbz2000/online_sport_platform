README.md for SportX Project

Overview

SportX is a professional, production-ready online fitness coaching and sports management platform. It facilitates seamless interaction between coaches and clients, manages subscription plans, automates workout program creation, generates secure program PDFs, and offers dynamic user assessment tools.

Built with a modern Python/Django backend and a dynamic, lightweight frontend (HTMX + Alpine.js + Tailwind CSS), this project follows software engineering best practices, including the Service Layer Pattern, Strategy Pattern for payments, and asynchronous background tasks.



🚀 Key Features

🔑 User Management & Role-Based Access





Custom User Model: Inherited from AbstractUser with support for three roles: Admin, Coach, and Client.



Physical Profiles: Detailed tracking for clients, including height, weight, and fitness goals.



Granular Permissions: Utilization of Django Groups & Permissions along with Custom Mixins (e.g., CoachRequiredMixin).

💳 Subscriptions & Payments





Membership Management: Dynamic management of pricing, validity, and feature sets.



Decoupled Architecture: Payment gateways (ZarinPal, IDPay, etc.) implemented via the Strategy Pattern.



Automation: Subscription auto-activation via Django Signals upon successful payment.

📋 Dynamic Assessment Forms





Customizable Forms: Coaches and Admins can build dynamic forms.



Data Handling: Schemas are stored as JSON, supporting various input types such as short text, long text, and medical history.

🏋️ Exercise Bank & Program Builder





Exercise Library: Comprehensive management system with video tutorials, muscle groups, and difficulty levels.



Program Assignment: Direct assignment of workout programs with specific sets, reps, rest intervals, and custom notes.



Security: Utilization of Signed URLs for media files to ensure that videos and PDFs are only accessible to authorized users.

📄 Asynchronous PDF Generation





Document Engine: HTML-to-PDF generation using WeasyPrint.



Performance: Background tasks handled by Celery and Redis to maintain server responsiveness.

✉️ Support Ticket System





Communication: A structured system for direct interaction between clients and coaches.



Real-time Interaction: Features powered by HTMX Polling for seamless message updates.

📝 SEO-Friendly Blog & Tools





Content Management: Educational resources utilizing PostgreSQL Full-Text Search.



Calculators: Client-side fitness tools (BMI, Daily Calorie Intake) built with Alpine.js for zero database overhead.



🛠️ Tech Stack:

        Backend: Django 5.x, Python
        Database: PostgreSQL (Production), SQLite (Development)
        Task Queue: Celery + Redis
        Frontend: Django Templates, HTMX, Alpine.js, Tailwind CSS
        PDF Engine: WeasyPrint
        Storage: django-storages + S3-Compatible Cloud Storage
        Payment Gateway: Strategy Pattern Implementation



📂 Project Structure

sports_platform/
├── manage.py
├── requirements.txt
├── .env.example
├── config/             # Django configuration and settings
├── apps/               # Modular applications:
│   ├── accounts/       # Authentication and roles
│   ├── plans/          # Subscription logic
│   ├── payments/       # Payment gateway strategies
│   ├── assessments/    # Dynamic forms
│   ├── exercises/      # Exercise database
│   ├── programs/       # Workout generation
│   ├── tickets/        # Messaging
│   ├── blog/           # SEO and Search
│   ├── tools/          # Interactive calculators
│   └── core/           # Base models and helpers
├── templates/          # Frontend templates
└── static/             # CSS/JS assets




⚙️ Installation & Setup

1. Clone the Repository:git clone https://github.com/yourusername/sportex.git

2. Environment Variables: Create a .env file from .env.example and populate your credentials.

3. Dependencies: Install using pip install -r requirements.txt.

4. Migrations: Run python manage.py migrate.

5. Admin: Create an account via python manage.py createsuperuser.

6. Task Queue: Start the Celery worker: celery -A config worker --loglevel=info.

7. Server: Run the application with python manage.py runserver.



🔒 Security Measures:

Protected Media: Files are served via temporary, time-limited S3 Signed URLs, preventing unauthorized access to sensitive training materials.

Environment Isolation: Sensitive configurations are strictly managed through environment variables to protect project integrity.



🗺️ Development Roadmap:

    Phase 1: Core Infrastructure & Auth.
    Phase 2: Subscriptions & Payment Strategies.
    Phase 3: Assessment Forms & Exercise DB.
    Phase 4: Program Builder & PDF Generation.
    Phase 5: Support Ticket System.
    Phase 6: Blog Engine & Fitness Tools.