# Learning Platform Backend - README

## Overview
This project is the backend for a **Learning Platform** designed to connect learners with professionals through a subscription-based model. It provides APIs for user management, subscription handling, and a modular chat system for course-based communication. The backend is built using **Python**, **FastAPI**, and **MySQL**, with a focus on scalability, performance, and ease of development.

---

## Technology Choices

### Why Python?
Python was chosen as the primary programming language for the following reasons:
- **Simplicity and Readability**: Python’s clean syntax allows for rapid development and easy maintenance, which is crucial for a project with tight deadlines. It ensures the code is readable and understandable for the jury and future developers.
- **Rich Ecosystem**: Python has a vast ecosystem of libraries, such as `passlib` for password hashing, `SQLAlchemy` for ORM, and `pydantic` for data validation, which accelerated development.
- **Comparison with Alternatives**: Compared to Node.js (JavaScript), Python offers better readability and fewer asynchronous complexities for this project. While Java could offer better performance for enterprise-scale applications, Python’s development speed and simplicity were prioritized for this prototype.

### Why FastAPI?
FastAPI was selected as the web framework for the following reasons:
- **Performance**: FastAPI is one of the fastest Python frameworks, built on Starlette and leveraging asynchronous programming with `asyncio`. This ensures high performance for handling API requests, which is critical for a platform with potential high user traffic.
- **Automatic Documentation**: FastAPI provides built-in Swagger UI and ReDoc for API documentation, which was invaluable for testing and presenting the API to the jury. This reduced the need for manual documentation efforts.
- **Type Hints and Validation**: FastAPI uses Python type hints and integrates with `pydantic` for automatic request validation, reducing bugs and ensuring data integrity.
- **Comparison with Alternatives**: Compared to Flask, FastAPI offers better performance and native async support. Django, while robust, is heavier and more suited for monolithic applications, whereas FastAPI’s lightweight nature aligns better with a microservices-ready API.

### Why MySQL?
MySQL was chosen as the database for the following reasons:
- **Relational Structure**: The platform requires a relational database to manage relationships between users, subscriptions, professionals, plans, and chat channels. MySQL’s relational model ensures data consistency and supports complex queries efficiently.
- **Performance and Scalability**: MySQL is optimized for read-heavy workloads, which aligns with the platform’s need to frequently retrieve user data, plans, and chat messages. It also scales well with proper indexing and optimization.
- **Comparison with Alternatives**: PostgreSQL was considered, but MySQL was chosen for its simplicity and slightly better performance in read-heavy scenarios. NoSQL databases like MongoDB were not suitable due to the relational nature of the data (e.g., foreign keys between users, subscriptions, and chat channels).

---

## System Architecture

### Core Components
1. **User Management**:
   - Users are stored in the `users` table with fields like `username`, `email`, `password_hash`, and `account_type` (enum: `free`, `premium`).
   - Passwords are hashed using `passlib` with the bcrypt algorithm for security.
   - Endpoints: `POST /users/` (create user), `POST /login` (authenticate user).

2. **Subscription System**:
   - Users can subscribe to professional plans using `POST /users/{user_id}/subscribe/{plan_id}`.
   - Subscriptions are stored in the `subscriptions` table, linking `user_id` and `plan_id`.
   - Professional plans are stored in the `professional_plans` table, created by professionals (stored in the `professionals` table).

3. **Chat System**:
   - A modular chat system allows communication between learners and professionals.
   - When a user subscribes to a plan, a `ChatChannel` is created (stored in `chat_channels` table) with `channel_type="course"`, linking to the `plan_id`.
   - Messages are stored in the `chat_messages` table, associated with a `channel_id`.
   - Endpoints:
     - `GET /chat/users/{user_id}/channels`: Retrieve all channels for a user.
     - `GET /chat/channels/{channel_id}`: Retrieve messages in a channel.

### Database Schema
The database (`learning_platform`) contains the following key tables:
- `users`: Stores user information (user_id, username, email, password_hash, account_type).
- `professionals`: Stores professional user details (professional_id, user_id, is_verified).
- `professional_plans`: Stores plans created by professionals (plan_id, professional_id, name, price).
- `subscriptions`: Links users to plans (subscription_id, user_id, plan_id, payment_method).
- `chat_channels`: Stores chat channels (channel_id, channel_type, related_id, professional_id).
- `chat_messages`: Stores messages within channels (message_id, channel_id, sender_id, content).
- `pro_content`: Stores professional content for courses (content_id, professional_id, full_content).

### Why This Chat System Design?
- **Modularity**: The chat system is designed to be modular, allowing for easy extension to support different `channel_type`s (e.g., `course`, `direct_message`) in the future.
- **Scalability**: Storing messages in a separate `chat_messages` table allows for efficient retrieval and pagination, which is critical for scaling to many users and messages.
- **Comparison with Alternatives**: A WebSocket-based real-time chat (e.g., using `FastAPI-WebSocket`) was considered but avoided due to the complexity and resource demands. The current REST-based chat system is simpler for a prototype and meets the basic needs of course-based communication.

---

## How It Works

### Setup and Running the Backend
1. **Prerequisites**:
   - Python 3.12
   - MySQL server
   - Install dependencies: `pip install -r requirements.txt`

2. **Environment Variables**:
   - Create a `.env` file with:
     ```
     DB_URL=mysql+pymysql://root:your_password@localhost/learning_platform
     SECRET_KEY=your_secret_key
     ```

3. **Database Setup**:
   - Create the database: `CREATE DATABASE learning_platform;`
   - The tables are created automatically via SQLAlchemy models when the app starts.

4. **Run the Server**:
   - Start the FastAPI server: `python3 -m uvicorn main:app --reload`
   - Access the API at `http://localhost:8000/docs` for Swagger UI.

### Example Workflow
1. **Create a User**:
   - `POST /users/` with:
     ```json
     {
       "username": "testlearner2",
       "email": "testlearner2@example.com",
       "password": "testpassword123",
       "account_type": "free"
     }
     ```
   - Password is hashed and stored in the `users` table.

2. **Login**:
   - `POST /login` with:
     ```json
     {
       "username": "testlearner2",
       "password": "testpassword123"
     }
     ```
   - The backend verifies the password using `passlib`.

3. **Subscribe to a Plan**:
   - `POST /users/4/subscribe/1` with:
     ```json
     {
       "payment_method": "credit_card",
       "transaction_id": "txn_123456"
     }
     ```
   - Creates a subscription and a chat channel for the course.

4. **Access Chat**:
   - `GET /chat/users/4/channels`: Lists all channels for `user_id=4`.
   - `GET /chat/channels/1`: Retrieves messages in `channel_id=1`.

---

## Conclusion
The backend leverages Python, FastAPI, and MySQL to provide a robust, scalable, and easy-to-use API for the Learning Platform. The tech stack was chosen for its balance of development speed, performance, and scalability, making it an ideal choice for this prototype. The modular chat system ensures flexibility for future enhancements, such as real-time messaging or additional channel types.

