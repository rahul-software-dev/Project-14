# Project-14
Subscription Lifecycle Automation Engine

subscription_engine/
│
├── app/                          # Main application package
│   ├── __init__.py
│   ├── config.py                 # Environment and configuration variables
│   ├── models/                   # SQLAlchemy ORM models
│   │   ├── __init__.py
│   │   └── user.py
│   │   └── subscription.py
│   │   └── event_log.py
│   │
│   ├── tasks/                    # Celery background tasks
│   │   ├── __init__.py
│   │   ├── scheduler.py          # Task scheduler setup
│   │   ├── transitions.py        # Trial to paid transitions
│   │   ├── alerts.py             # Email/SMS renewal and expiry alerts
│   │   └── churn_analysis.py     # Churn prediction and analysis
│   │
│   ├── services/                 # Business logic
│   │   ├── __init__.py
│   │   ├── billing.py
│   │   ├── notification.py
│   │   └── churn_predictor.py
│   │
│   ├── api/                      # Optional REST API (e.g., Flask/FastAPI)
│   │   ├── __init__.py
│   │   └── routes.py
│   │
│   ├── db/                       # DB session and migration
│   │   ├── __init__.py
│   │   ├── session.py            # SQLAlchemy session
│   │   └── migrate.sh            # Alembic/Flyway migration script
│   │
│   └── utils/                    # Helper functions
│       ├── __init__.py
│       └── time_utils.py
│       └── logger.py
│
├── celery_worker.py             # Entry point for Celery worker
├── beat_scheduler.py            # Celery Beat for periodic tasks
├── requirements.txt             # Python dependencies
├── .env                         # Environment variables
├── Dockerfile                   # Dockerfile for containerization
├── docker-compose.yml           # Compose file to orchestrate services
├── README.md
└── tests/                       # Unit & integration tests
    ├── __init__.py
    ├── test_tasks.py
    ├── test_churn_predictor.py
    └── test_transitions.py


    # Subscription Lifecycle Automation Engine

An automation engine that manages trial-to-paid transitions, alerts, and churn prediction for SaaS products.

## Features
- Automatic trial-to-paid upgrades
- Email/SMS alerts before renewal/expiry
- Churn prediction engine
- Celery + Redis for task scheduling
- REST API with Flask
- PostgreSQL via SQLAlchemy ORM

## Setup

```bash
docker-compose up --build