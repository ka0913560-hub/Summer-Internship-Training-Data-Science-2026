# ☁️ Day-12: Introduction to Cloud Computing & AWS S3

## 🎯 Objective

Learn the fundamentals of Cloud Computing, AWS (Amazon Web Services), AWS Account Structure, IAM, Amazon S3, Buckets, Bucket Versioning, ACLs, and perform hands-on practicals.

---

# 🌍 What is Cloud Computing?

Cloud Computing is the delivery of computing services such as storage, servers, databases, networking, and software over the Internet instead of using your own computer or local server.

Instead of buying expensive hardware, users can rent resources whenever needed.

### Traditional Computing

- Data stored on local computer
- Limited storage
- High maintenance cost
- Hardware failures possible

### Cloud Computing

- Data stored on cloud servers
- Accessible from anywhere
- Highly scalable
- Secure
- Cost effective
- Pay only for what you use

---

# ☁️ Popular Cloud Providers

- Amazon Web Services (AWS)
- Microsoft Azure
- Google Cloud Platform (GCP)
- Oracle Cloud
- IBM Cloud

AWS is currently the most popular cloud platform.

---

# ✅ Advantages of Cloud Computing

- Easy to access from anywhere
- High availability
- Better security
- Automatic backup
- Unlimited scalability
- Low maintenance
- Pay-As-You-Go pricing

---

# 📚 What is AWS?

AWS (Amazon Web Services) is Amazon's Cloud Computing platform that provides more than 200 cloud services.

Some AWS services include:

- Amazon S3
- Amazon EC2
- Amazon RDS
- AWS Lambda
- IAM
- CloudWatch

---

# 👤 AWS Account Structure

```

AWS Account
│
└── Root User
│
├── IAM Users
├── IAM Groups
├── IAM Roles
└── Policies

```

---

# 👑 Root User

The Root User is created when a new AWS account is created.

It has complete control over the AWS account.

### Root User can

- Create AWS Services
- Delete Resources
- Manage Billing
- Create IAM Users
- Close AWS Account

### Best Practice

Use the Root User only when necessary.

For daily work, always use IAM Users.

---

# 🔐 IAM (Identity and Access Management)

IAM helps manage users and permissions securely inside AWS.

Using IAM we can create:

- Users
- Groups
- Roles
- Policies

Example:

```

Company
│
Admin
│
├── Developer
├── Tester
└── HR

```

Each user gets only the permissions required for their job.

---

# 📦 What is Amazon S3?

Amazon S3 (Simple Storage Service) is AWS's Object Storage Service.

It is used to store:

- Images
- Videos
- Documents
- PDFs
- Backups
- Machine Learning Datasets
- Application Files

---

# 📂 What is a Bucket?

A Bucket is a container that stores files (objects) in Amazon S3.

Example:

```

Bucket
│
├── image.png
├── report.pdf
├── backup.zip
└── data.csv

```

---

# 📏 Bucket Limits

### Maximum Object Size

- 5 TB per object

### Bucket Storage

- Virtually Unlimited

### Number of Buckets

- Up to 10,000 buckets per AWS account (default quota)

---

# 🌎 AWS Regions

AWS has data centers across different regions.

Examples:

- Mumbai
- Singapore
- London
- Virginia
- Tokyo

Choosing the nearest region reduces latency.

---

# 📤 Creating an S3 Bucket

Steps followed in practical:

1. Login to AWS Console
2. Open Amazon S3
3. Click Create Bucket
4. Enter Bucket Name
5. Select Region
6. Configure Bucket Settings
7. Create Bucket
8. Upload Files

---

# 🔒 Block Public Access

By default, AWS blocks public access to protect bucket data.

If disabled:

- Bucket may become publicly accessible.
- Anyone with permission can access files.

---

# 🔑 ACL (Access Control List)

ACL is an older permission system in S3.

### ACL Enabled

- Object-level permissions can be managed.
- Used by some legacy applications.

### ACL Disabled (Recommended)

- Permissions are managed using IAM Policies and Bucket Policies.
- More secure.
- Easier to manage.

---

# 🔄 Bucket Versioning

Bucket Versioning stores multiple versions of the same object.

Whenever a file is uploaded again with the same name, AWS keeps the old version and creates a new version.

Example:

```

Resume.pdf

↓

Version 1

↓

Upload Again

↓

Version 2

↓

Upload Again

↓

Version 3

```

Benefits:

- Recover deleted files
- Restore previous versions
- Prevent accidental overwrite
- Maintain file history

---

# 🔐 Bucket Permissions

Permissions can be managed using:

- IAM Policies
- Bucket Policies
- ACL (Legacy)

AWS recommends using IAM Policies and Bucket Policies.

---

# 💻 Practical Performed

- Created AWS Free Tier Account
- Learned Root User
- Learned IAM Concepts
- Opened AWS Console
- Opened Amazon S3
- Created S3 Bucket
- Selected AWS Region
- Understood Block Public Access
- Learned ACL Enable and Disable
- Uploaded Files
- Enabled Bucket Versioning
- Uploaded Multiple Versions of Same File
- Viewed Version History
- Explored Bucket Properties
- Explored Bucket Permissions

---

# 🌍 Real Life Uses of Amazon S3

- Website Image Storage
- Mobile Application Files
- Company Backups
- Data Lakes
- Machine Learning Datasets
- Video Streaming
- Cloud Storage
- Disaster Recovery

---

# 📖 Key Terms Learned

- Cloud Computing
- AWS
- Root User
- IAM
- IAM User
- IAM Group
- IAM Role
- Amazon S3
- Bucket
- Object
- Region
- ACL
- Bucket Policy
- IAM Policy
- Versioning
- Block Public Access

---

# 📌 Key Takeaways

- Cloud Computing provides computing resources over the Internet.
- AWS is the world's leading cloud platform.
- Root User has full access and should be used carefully.
- IAM provides secure user and permission management.
- Amazon S3 is an Object Storage Service.
- Buckets are used to store objects.
- ACL is a legacy permission system.
- Bucket Versioning protects files from accidental deletion or overwrite.
- AWS recommends using IAM Policies instead of ACLs.
- S3 is highly scalable, secure, and durable.

---

# 🚀 Outcome

Successfully learned the fundamentals of Cloud Computing, AWS, Root User, IAM, Amazon S3, Bucket creation, ACLs, Bucket Versioning, and performed hands-on practicals to understand cloud storage concepts and their real-world applications.
