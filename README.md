# **Project Setup Guide**

This document provides instructions to set up and run project.

---


### **Clone the Repository**

```bash
git clone https://github.com/kienht-nobisoft/lnine-django-lab2.git
```

---

### **Set Up a Virtual Environment**

```bash
python3 -m venv env
source env/bin/activate
```

---

### **Install Dependencies**

Install the required Python packages from the requirements.txt file:
```bash
pip install -r requirements.txt
```

---

### **Run Database Migrations**

```bash
python manage.py migrate
```

---

### **Create Initial Data**
Note: pwd: abcd1234

```bash
python manage.py loaddata users/fixtures/sample.json 
```

---

### **Run the Development Server**

```bash
python manage.py runserver
```
