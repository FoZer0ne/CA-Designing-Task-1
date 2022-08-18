# Introduction to Git and GitHub

1. Install [Git](https://git-scm.com/downloads/).
2. Join [GitHub](https://github.com/join/).
3. Go to your repositories page.

![image](https://user-images.githubusercontent.com/110683229/185362494-c139fd3b-44fb-472e-a99f-00c533487f51.png)

4. Create repository with name **"CA-Designing-Task-1"**.

![image](https://user-images.githubusercontent.com/110683229/185362517-a491306c-8e25-4759-8136-9d3ff990246c.png)

5. Create a folder on your machine and open Git Bash there.

![image](https://user-images.githubusercontent.com/110683229/185366002-5820e5d2-7d7b-498a-9457-b84bab79b8a9.png)

6. Enter commands (don't forget to replace *[ім'я]* with your GitHub username:
```
git config --global user.name "[ім'я]"
git config --global user.email "[поштова скринька]"
git clone https://github.com/zymbaliuk/CA-Designing-Task-1.git
git init
git remote rename origin upstream
git remote add origin https://github.com/[ім'я]/CA-Designing-Task-1.git
git commit -m "initial commit"
git push origin master
```

7. Copy your repository URL and paste it to chat with teacher.
