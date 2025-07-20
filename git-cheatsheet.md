# 🧠 Git Cheat Sheet for Interview & Daily Use

## 🔧 Initial Setup

```bash
git config --global user.name "Eesho"
git config --global user.email "avincarvalho7@gmail.com"
```

Use your GitHub name and email ID.

---

## 📁 Initialize Local Repo

```bash
git init
```

Creates a new Git repository in your project folder.

---

## 🌐 Connect to GitHub

```bash
git remote add origin https://github.com/AvinCarvalho/Project-.git
```

Adds a remote GitHub repo to your local repo.

### 🔍 Check if remote is connected

```bash
git remote -v
```

Shows URLs for `fetch` and `push`.

---

## 📦 Staging and Committing

```bash
git add .        # Stage all changes
git commit -m "Your message"
```

Stage and save your changes with a message.

---

## 🚀 Push Code to GitHub

```bash
git push origin main   # or master
```

Uploads your commits to GitHub.

---

## 🔄 Pull Changes from GitHub

```bash
git pull origin main
```

Gets the latest code from GitHub.

---

## 👀 Status and Logs

```bash
git status     # Check current status
git log        # See commit history
```

---

## 🧠 Common Git Interview Questions

* What is Git? What is GitHub?
* Difference between `git add`, `commit`, and `push`?
* What is the difference between `pull` and `fetch`?
* What is a merge conflict? How to resolve it?
* How do you revert a commit?
* How do you clone a repo?

---

✅ **Pro Tip:** Practice in real projects (like your login page) to retain commands!

You’re doing awesome bro! 💪
