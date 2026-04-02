# OlaPay Wallet

A Django-based mobile wallet backend system that enables users to securely manage funds, perform transactions, and interact with digital payment services.

---

## Overview

OlaPay Wallet is a fintech backend application designed to power mobile and web wallet solutions. It provides core features such as user authentication, wallet management, fund transfers, and transaction tracking. This project serves as a foundation for building scalable digital payment platforms, with integrated payment support via Paystack.

---

## Features

* User registration and authentication
* Wallet creation and balance management
* Wallet funding via Paystack
* Peer-to-peer (P2P) transfers
* Transaction history and tracking
* Debit and credit operations
* Admin monitoring (optional)

---

## Tech Stack

* Backend: Django, Django REST Framework
* Database: mySQL
* Authentication: Token-based (JWT or DRF Tokens)
* API: RESTful services
* Payments: Paystack integration

---

## Project Structure

```id="jmhgdk"
OlaPay-Wallet/
│── wallet/            
│── users/             
│── transactions/      
│── core/              
│── manage.py
│── requirements.txt
```

---

## Installation & Setup

1. Clone the repository

```id="7i86hs"
git clone https://github.com/Adamsonoladipupo/OlaPay-Wallet.git
cd OlaPay-Wallet
```

2. Create a virtual environment

```id="pxwat9"
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

3. Install dependencies

```id="km3b3h"
pip install -r requirements.txt
```

4. Run migrations

```id="2xdwpb"
python manage.py migrate
```

5. Start the server

```id="7px4my"
python manage.py runserver
```

---

## API Endpoints (Sample)

* POST `/api/register/` → Create user
* POST `/api/login/` → Authenticate user
* GET `/api/wallet/` → View wallet balance
* POST `/api/transfer/` → Send money
* GET `/api/transactions/` → View transaction history
* POST `/api/fund-wallet/` → Fund wallet via Paystack

---

## Security Considerations

* Validate all transactions
* Prevent double spending
* Use HTTPS in production
* Secure Paystack webhook endpoints
* Protect sensitive data

---

## Future Improvements

* Airtime & bill payment features
* Multi-currency support
* Notifications (SMS/Email)
* Fraud detection systems
* KYC verification

---

## Contributing

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

---

## License

MIT License

---

## Author

Adamson Oladipupo
https://github.com/Adamsonoladipupo

---


This project is ideal for learning fintech backend architecture, building MVPs, and showcasing backend engineering skills.
