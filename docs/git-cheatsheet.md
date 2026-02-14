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


New Interview questions : 

# 🚀 Git & GitHub Interview Cheat Sheet  

## 1. Git vs GitHub
- Git → Distributed version control system (local).
- GitHub → Cloud-based hosting platform for Git repositories (collaboration).

---

## 2. git fetch vs git pull
- fetch → Downloads changes (no merge).
- pull → fetch + merge (updates local branch).

---

## 3. Undoing a Commit
- git reset --soft <commit> → Keeps changes staged.
- git reset --hard <commit> → Deletes commit + changes.
- git revert <commit> → Safe undo → creates new commit.

---

## 4. Merge vs Rebase
- Merge → Combines branches, preserves history (extra commit).
- Rebase → Moves commits on top of another branch → clean history.

---

## 5. Detached HEAD
- HEAD points to commit instead of branch.
- Changes may be lost unless saved with a new branch.

---

## 6. Merge Conflicts
- Happens when two devs edit the same line differently.
- Fix manually → edit file → git add → git commit.

---

## 7. .gitignore
- File to ignore unwanted/untracked files.
- Examples:  


---

## 8. Fork vs Clone vs Branch
- Fork → Copy of repo in your GitHub account.
- Clone → Local copy of a repo.
- Branch → Parallel line of development.

---

## 9. Tags in Git
- Mark specific commits (releases).
- Lightweight tag → pointer only.
- Annotated tag → with metadata.  
- Example:  


---

## 10. GitHub Actions
- GitHub’s CI/CD automation tool.
- Defined in .github/workflows/*.yml.
- Triggers: push, pull_request, schedule, workflow_dispatch.

---

## 11. What happens in git push origin main?
1. Compresses local commits.
2. Sends to remote (origin).
3. Updates remote main branch.
4. If rejected → need git pull to sync first.

---

