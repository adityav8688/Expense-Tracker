# 💸 Expense Tracker API

A RESTful backend API for personal expense management, built with **FastAPI** and **PostgreSQL**. It supports user authentication, wallet management, expense categorization, and full transaction CRUD operations.

---

## 🚀 Tech Stack

| Layer | Technology |
|---|---|
| Framework | FastAPI |
| ORM | SQLAlchemy (async) |
| Database | PostgreSQL (`psycopg2-binary`) |
| Migrations | Alembic |
| Auth | JWT via `python-jose` + `passlib` + `bcrypt` |
| Server | Uvicorn |
| Validation | Pydantic v2 |
| Config | `python-dotenv` |

---

## 📁 Project Structure

```
backend/
├── app/
│   ├── main.py                  # FastAPI app entry point
│   ├── core/
│   │   ├── config.py            # Environment settings (BaseSettings)
│   │   ├── database.py          # Async SQLAlchemy engine & session
│   │   └── security.py          # JWT token creation & role checking
│   ├── models/
│   │   ├── users_model.py       # User ORM model
│   │   ├── wallets_model.py     # Wallet ORM model
│   │   ├── categories_model.py  # Category ORM model
│   │   └── transactions_model.py# Transaction ORM model (income/expense)
│   ├── schemas/
│   │   ├── user_schema.py
│   │   ├── wallet_schema.py
│   │   ├── category_schema.py
│   │   └── transaction_schema.py
│   ├── routers/
│   │   ├── user_router.py
│   │   ├── wallet_router.py
│   │   ├── category_router.py
│   │   └── transaction_router.py
│   ├── services/
│   │   ├── user_services.py
│   │   ├── wallet_services.py
│   │   ├── category_services.py
│   │   └── transaction_services.py
│   └── utils/
│       └── hashing.py           # Password hashing helpers
├── pyproject.toml
└── requirements.txt
```

---

## ⚙️ Getting Started

### Prerequisites

- Python 3.10+
- PostgreSQL running locally or in the cloud

### 1. Clone the Repository

```bash
git clone https://github.com/adityav8688/Expense-Tracker.git
cd Expense-Tracker/backend
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate      # macOS/Linux
venv\Scripts\activate         # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the `backend/` directory:

```env
DATABASE_URL=postgresql+asyncpg://your_user:your_password@localhost:5432/expense_tracker
SECRET_KEY=your_secret_key_here
ALGORITHM=HS256
```

### 5. Run Database Migrations

```bash
alembic upgrade head
```

### 6. Start the Server

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`.

---

## 📖 API Documentation

Interactive docs are available at:

- **Swagger UI:** `http://localhost:8000/docs`
- **ReDoc:** `http://localhost:8000/redoc`

---

## 🔑 API Endpoints

### Users
| Method | Endpoint | Description |
|---|---|---|
| POST | `/user/register` | Register a new user |
| POST | `/user/login` | Authenticate and receive JWT token |

### Wallets
| Method | Endpoint | Description |
|---|---|---|
| GET | `/wallet/` | List all wallets for the current user |
| POST | `/wallet/` | Create a new wallet |
| PATCH | `/wallet/{id}` | Update a wallet |
| DELETE | `/wallet/{id}` | Delete a wallet |

### Categories
| Method | Endpoint | Description |
|---|---|---|
| GET | `/category/` | List all categories |
| POST | `/category/` | Create a new category |
| PATCH | `/category/{id}` | Update a category |
| DELETE | `/category/{id}` | Delete a category |

### Transactions
| Method | Endpoint | Description |
|---|---|---|
| GET | `/transaction/` | List all transactions for the current user |
| POST | `/transaction/` | Create a new transaction (income or expense) |
| PATCH | `/transaction/{id}` | Update a transaction |
| DELETE | `/transaction/{id}` | Delete a transaction |

> All wallet, category, and transaction endpoints require a valid **Bearer token** in the `Authorization` header.

---

## 🗄️ Data Models

### Transaction Types
Transactions support two types:
- `income`
- `expense`

### Transaction Fields
| Field | Type | Description |
|---|---|---|
| `id` | int | Primary key |
| `user_id` | int (FK) | Owning user |
| `category_id` | int (FK) | Category reference |
| `wallet_id` | int (FK) | Wallet reference |
| `type` | enum | `income` or `expense` |
| `amount` | float | Transaction amount |
| `title` | string | Short title |
| `description` | string | Optional notes |
| `transaction_date` | datetime | When the transaction occurred |
| `created_at` | datetime | Auto-set on creation (UTC) |

---

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Commit your changes: `git commit -m "Add your feature"`
4. Push to the branch: `git push origin feature/your-feature`
5. Open a Pull Request

---

## 📄 License

This project is open source. See the repository for details.
