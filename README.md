# 🎓 Student Data Management Web App

## 📌 Project Overview
This is a **serverless web application** designed to store, manage, and retrieve student data efficiently.  
The application is hosted on **AWS** and utilizes various AWS services for backend operations.

## 🛠️ Tech Stack
- **Frontend**: HTML, CSS, JavaScript  
- **Backend**: AWS Lambda (Python)  
- **Database**: AWS DynamoDB  
- **Storage**: AWS S3  
- **API Management**: AWS API Gateway  
- **Hosting**: AWS S3 (Static Website Hosting)  

## 🚀 Features
✔️ Add new student records (**Name, ID, Department, Email, etc.**)  
✔️ Retrieve student details based on **Student ID**  
✔️ Update student information  
✔️ Delete student records  
✔️ **Serverless architecture** for cost efficiency  
✔️ **Secure API communication** using AWS API Gateway  

---

## 🛠️ AWS Architecture
```plaintext
[Frontend (HTML, CSS, JS)] ---> [API Gateway] ---> [AWS Lambda (Python)] ---> [DynamoDB]
S3: Hosts the frontend static files.
API Gateway: Manages API requests.
AWS Lambda: Backend logic for CRUD operations.
DynamoDB: Stores student records.

🖥️ Setup & Deployment

🔹 Prerequisites
AWS Account
Python (for AWS Lambda functions)
AWS CLI installed and configured
Node.js (if using additional tools like AWS SDK)

🔹 Steps to Deploy

1️⃣ Clone the repository:

2️⃣ Upload frontend files to AWS S3:
Navigate to AWS S3 → Create a new bucket → Enable static website hosting.
Upload index.html, styles.css, and script.js.
Copy the S3 URL to access your frontend.

3️⃣ Create DynamoDB Table:
Go to AWS DynamoDB → Create a table named Students.
Set StudentID as the Primary Key.

4️⃣ Deploy AWS Lambda functions:
Set the correct IAM role for DynamoDB access.
Want to create seperate Lambda function for each API methods

5️⃣ Set up API Gateway:
Create a new API in API Gateway.
Define methods (GET, POST, PUT, DELETE) and link them to the respective Lambda functions.
Enable CORS for frontend interaction.

6️⃣ Test the application:
Open the S3 URL in your browser.
Perform CRUD operations on student data

⚠️ Troubleshooting
Issue	Solution
CORS Errors?	Ensure CORS is enabled in API Gateway.
Permission Issues?	Check IAM roles for Lambda & DynamoDB.
S3 Website Not Loading?	Enable public access for S3 files.
