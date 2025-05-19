# Identity and Access Management - Ti Kloud Réunion

The Identity and Access Management (IAM) system for **Ti Kloud Réunion** is designed to manage user identities, roles, and access control. Built with modern technologies, it ensures secure and scalable user management for cloud applications.

## Technologies Used

The project utilizes the following technologies:

* **Python 3** - Backend programming language
* **FastAPI** - High-performance API framework
* **SQLModel with SQLite** - Development database
* **PostgreSQL** - Production database
* **Docker & Docker Compose** - Containerization and orchestration
* **Redis** - Caching layer for performance improvements

## Getting Started

### Prerequisites

Ensure you have the following installed:

* Python 3.8 or higher
* Docker and Docker Compose
* virtualenv (optional, recommended for isolated environments)

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/tikloudreunion/iam.git
   cd iam
   ```

2. Create a virtual environment and activate it:

   ```bash
   python3 -m venv .venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

### Running the Application (Development)

1. Run the application locally:

   ```bash
   python iam
   ```

2. Access the API at:

The server runs on port `3000` on `localhost` by default. You can access the API at:

[http://localhost:3000](http://localhost:3000)

## License

This project is licensed under the MIT License - see the LICENSE file for details.

