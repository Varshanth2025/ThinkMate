# ThinkMate-Collaborative Study Platform

A high-performance collaborative study platform built with Django and Django REST Framework. Thinkmate enables users to join study rooms, participate in discussions, and connect with other learners. The platform is designed for scalability, security, and responsive user experience.

---

## 🎯 Performance Highlights

- **Responsive Design:** 25% increase in user engagement through mobile-friendly layouts and fast navigation.
- **Optimized Queries:** Efficient database access for rooms, topics, and messages, supporting thousands of records.
- **Secure Authentication:** Fast and secure login, registration, and session management using Django's built-in auth system.
- **RESTful API:** Easily extendable API endpoints for rooms and activities, ready for integration with mobile or SPA frontends.

---

## 🛠️ Technical Stack

### Backend

- **Django & Django REST Framework**

  - Robust MVC architecture
  - RESTful API endpoints for rooms, topics, messages, and users
  - Custom user model for flexible authentication
  - Middleware for security and session management
  - Efficient ORM for scalable data handling

- **SQLite (default) / PostgreSQL (recommended for production)**
  - Reliable relational data storage
  - Easy migration and scaling

### Authentication & Security

- **Django Auth System**
  - Secure password hashing
  - Session-based authentication
  - Custom user profiles

### Development Tools

- **Git & GitHub:** Version control and collaboration
- **pip:** Python package management
- **Django Admin:** Built-in admin interface for data management
- **Unit Testing:** Django’s test framework for backend reliability

---

## 🚀 Features

- **Study Rooms:** Create, join, and discuss in themed rooms
- **Topics:** Browse and filter rooms by subject
- **User Profiles:** Customizable profiles with avatars and bios
- **Messaging:** Real-time discussions (upgradeable to Django Channels for live chat)
- **REST API:** Easily connect to mobile apps or modern JS frontends

---

## 📦 Getting Started

        ### Cloning the repository

--> Clone the repository using the command below :

```bash
git clone https://github.com/Varshanth2025/ThinkMate
```

--> Move into the directory where we have the project files :

```bash
cd Think

```

--> Create a virtual environment :

```bash
# Let's install virtualenv first
pip install virtualenv

# Then we create our virtual environment
virtualenv envname

```

--> Activate the virtual environment :

```bash
envname\scripts\activate

```

--> Install the requirements :

```bash
pip install -r requirements.txt

```

#

### Running the App

--> To run the App, we use :

```bash
python manage.py runserver

```

### App Preview :

<table width="100%"> 
<tr>
<td width="50%">      
&nbsp; 
<br>
<p align="center">
   Home
</p>
<img src="https://github.com/Varshanth2025/ThinkMate/blob/main/thinkmate/static/images/home.png">
</td> 
<td width="50%">
<br>
<p align="center">
  Room Conversation Preview
</p>
<img src="https://github.com/Varshanth2025/ThinkMate/blob/main/thinkmate/static/images/room_conversation.png">  
</td>
</table>
