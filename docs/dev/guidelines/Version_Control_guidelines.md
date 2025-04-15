
# Version Control Strategy

## 📌 Overview
This document defines the version control practices for the **Little Lemon** project. It provides guidelines for branching, merging, commit messages, and repository management to ensure a structured and efficient workflow.

---

# Branching Strategy for Epics, Features, User Stories, and Tasks in GitHub

To maintain a clean, organized, and scalable workflow, follow this branching strategy based on best practices in software development.

---
# Branching Hierarchy (Best Practice)
Instead of creating a branch for every Epic, Feature, User Story, and Task, follow a structured approach:

## 1️⃣ Epic Branch (epic/epic-name)
- Create a branch for each Epic from develop.
- Epics represent large deliverables, so multiple features will be implemented within them.
- Naming convention:
``` bash
epic/user-authentication
epic/reservation-system
```

- Example:
``` sh

git checkout -b epic/user-authentication develop
git push -u origin epic/user-authentication
``` 

## 2️⃣ Feature Branches (feature/feature-name)
- Each feature under an epic should have a separate branch.
- The feature branch is created from the Epic branch and merged back once completed.
- Naming convention:

``` 
feature/login-system
feature/signup-system
``` 
- Example:
``` 
git checkout -b feature/login-system epic/user-authentication
git push -u origin feature/login-system
``` 

## 3️⃣ User Story Branch (story/story-name)
- For each user story, create a branch from the feature branch.
- This ensures isolated development for each small unit of functionality.
- Naming convention:
```
story/login-api-validation
story/signup-email-verification
```
- Example:
```
git checkout -b story/login-api-validation feature/login-system
git push -u origin story/login-api-validation
```

##4️⃣ Task Branch (task/task-name)
- If a user story requires multiple tasks, create a branch from the story branch.
- This is used when a story is complex and multiple developers are working on different aspects.
- Naming convention:
```
task/create-login-endpoint
task/add-password-hashing
```

- Example:
```
git checkout -b task/create-login-endpoint story/login-api-validation
git push -u origin task/create-login-endpoint
```

## 🚀 Best Practices & Why This Approach is Ideal
- ✅ Modular Development → Each change is isolated, making debugging easier.
- ✅ Parallel Development → Multiple developers can work on different tasks simultaneously.
- ✅ Easier Code Review → PRs are smaller and focused, reducing merge conflicts.
- ✅ Clear Version Control → You can track progress at each level (Epic → Feature → Story → Task).
- ✅ Rollback Friendly → If a feature breaks, you can revert only that feature instead of affecting the entire project.

### Best Practices for Branch Management
| **Branch Type**	| **Merge Target**	| **Delete After Merge?**	| **Reason**	|
| ----- | ------------- | ---------- | ------------ |
| Feature Branch	| develop	| ✅ Yes	| Feature branches are short-lived and should be removed after merging to keep the repo clean.| 
| Bugfix Branch	| develop / test	| ✅ Yes	| Bugfix branches should be removed after merging unless you expect further fixes.| 
| Hotfix Branch	| main	| ✅ Yes	| Hotfix branches address urgent issues and should be deleted after merging.| 
| Release Branch	| main & develop	| ✅ Yes	| Release branches are temporary and should be deleted after merging.| 
| Test Branch	| develop / main	| ❌ No	| The test branch should not be deleted as it's used for testing before production deployment.| 
| Develop Branch	| main	| ❌ No	| The develop branch should persist as it's the main development branch.| 
| Main Branch	| -	| ❌ No	| The main branch is the production-ready branch and should never be deleted.| 

## 📌 Workflow Summary
| **Level**	| **Branch Naming Convention** | **Created From**	| **Purpose** |
| ----- | ------------- | ---------- | ------------ |
| Epic	| `epic/epic-name`	| `develop`	| Major business functionality (e.g., User Authentication) |
| Feature	| `feature/feature-name`	| `epic/epic-name`	| Implements a specific feature (e.g., Login System) |
| Story	| `story/story-name`	| `feature/feature-name`	| Implements a user story (e.g., API validation for login) |
| Task	| `task/task-name`	| `story/story-name`	| Smallest unit of work (e.g., Add hashing for passwords) |

# 🛠 Merging Strategy
- Task → Story
```
git checkout story/login-api-validation
git merge task/create-login-endpoint
git push origin story/login-api-validation
```
- Story → Feature
```
git checkout feature/login-system
git merge story/login-api-validation
git push origin feature/login-system
```
- Feature → Epic
```
git checkout epic/user-authentication
git merge feature/login-system
git push origin epic/user-authentication
```
- Epic → Develop
```
git checkout develop
git merge epic/user-authentication
git push origin develop
```

## 🚀 When to Delete a Branch?
- Delete Task Branch after merging into Story
- Delete Story Branch after merging into Feature
- Delete Feature Branch after merging into Epic
- Keep Epics for reference until the release is completed
```
git branch -d task/create-login-endpoint
git push origin --delete task/create-login-endpoint
```

## 🎯 Final Thoughts
This structured Git workflow ensures:
- ✅ Scalability (Easier team collaboration)
- ✅ Efficiency (Faster development & testing)
- ✅ Quality (Easier debugging & code reviews)

🚀 Now you're set up for professional-level project management! Let me know if you need further clarifications! 🎯

---

# Merging develop → test and test → main: Best Practices

Since you have three base branches (main, develop, test), follow a structured approach to merging to ensure stability, quality assurance, and seamless deployment.

## 1️⃣ When to Merge develop → test?
- 📌 Purpose: To test newly developed features before merging into main.
- 📌 Best Time: After completing feature development and conducting initial testing in develop.
- 📌 Best Practice: Use Pull Requests (PRs) to merge and enforce code reviews.

### Steps to Merge develop → test
- 1️⃣ Ensure develop is up to date

```
git checkout develop
git pull origin develop
```

- 2️⃣ Switch to test branch

```
git checkout test
```

- 3️⃣ Merge develop into test

```
git merge develop
```

- 4️⃣ Push changes to remote

```
git push origin test
```

- 5️⃣ Run tests (unit tests, integration tests, functional tests)

```
python manage.py test
```

- 6️⃣ Deploy to a staging server for user acceptance testing (UAT)

- Deploy the test branch to a staging environment.
- Conduct manual and automated tests.
- Fix any bugs found.

## 2️⃣ When to Merge test → main?

- 📌 Purpose: To deploy stable, tested features into production.
- 📌 Best Time: After successfully testing all changes in test and completing User Acceptance Testing (UAT).
- 📌 Best Practice: Only merge tested and bug-free code into main.

### Steps to Merge test → main
- 1️⃣ Ensure test is up to date

```
git checkout test
git pull origin test
```

- 2️⃣ Switch to main branch

```
git checkout main
```

- 3️⃣ Merge test into main

```
git merge test
```

- 4️⃣ Push changes to remote

```
git push origin main
```

- 5️⃣ Deploy the main branch to production

- Deploy the latest main branch version to the live environment.
- Run post-deployment checks.
- Monitor for errors and rollback if necessary.

## 3️⃣ What If You Need to Roll Back?
- If something goes wrong after merging test → main, you can roll back using:

### Option 1: Reset to the Previous Commit (Safe)
```
git checkout main
git reset --hard <last-stable-commit-hash>
git push --force origin main
```
- 🔴 Warning: This removes the latest changes permanently.

### Option 2: Revert the Last Merge (Safer)
```
git checkout main
git revert -m 1 <merge-commit-hash>
git push origin main
```
- ✅ This creates a new commit that reverses the changes.

## 🎯 Final Workflow Summary

| **Step**	| **Action**	| **Purpose** |
| ----- | ------------- | ---------- |
| 1	| Merge develop → test	| Move features to staging for QA| 
| 2	| Test & Fix Bugs in test	| Ensure stability| 
| 3	| Merge test → main	| Deploy tested features to production| 
| 4	| Deploy main	| Make features live for users| 
| 5	| Monitor & Rollback if needed	| Ensure stability| 
- 🚀 Now you have a structured release cycle for your Django project! Let me know if you need any modifications. 🎯

---

## 📝 Commit Message Guidelines

### **✅ Best Practices**
- Write meaningful and concise messages.
- Use the present tense (e.g., "Add login validation").
- Prefix commits with the type of change.

### **✅ Format**
```
[type]: [short description]

[Optional detailed description]
```

### **✅ Examples**
- `feature: Add user authentication system`
- `fix: Resolve login API validation issue`
- `docs: Update README with setup instructions`

### **🚀 Allowed Types**
| Type | Purpose |
|------|---------|
| `feature` | Add, update or delete code or new feature. |
| `fix` | Fixes a bug or issue. |
| `docs` | Documentation changes only. |
| `test` | Adding or updating tests. |
| `refactor` | Code changes that do not add new features or fix bugs. |
| `chore` | Maintenance or minor updates. |

---

## 🎯 Tagging Releases
We use semantic versioning (`vX.Y.Z`) for tagging releases.
- **Major release**: `v1.0.0`
- **Minor update**: `v1.1.0`
- **Patch fix**: `v1.1.1`

To create a tag:
```sh
git tag -a v1.0.0 -m "Release version 1.0.0"
git push origin v1.0.0
```

---

## 🚀 Pull Request Workflow
1. **Create a new branch** following the naming convention.
2. **Push changes** and open a pull request (PR) to the target branch.
3. **Code review** is conducted by team members.
4. **Approval & Merge**:
   - Use **squash and merge** for small, related commits.
   - Use **merge commits** for feature branches.

---

## 🔀 Rebasing vs Merging
- **Use rebase** (`git rebase develop`) to keep a clean commit history.
- **Use merge** (`git merge develop`) when integrating a feature into a shared branch.

---

## 🔥 Handling Merge Conflicts
Resolve conflicts using:
```sh
git merge develop
# Manually fix conflicts
```
Use **`git rebase --continue`** if rebasing.

---

## 🚀 CI/CD Integration
- Automated tests run on GitHub Actions before merging into `develop`.
- Releases are automatically deployed from `main`.

---

## 🔥 Backup & Rollback Strategies
- If an issue occurs after merging `test → main`, rollback using:
  ```sh
  git checkout main
  git revert -m 1 <merge-commit-hash>
  git push origin main
  ```
- If needed, reset the branch:
  ```sh
  git reset --hard <previous-stable-commit>
  git push --force origin main
  ```

---

## 🚀 Summary
✅ **Organized branching structure** 
✅ **Clear commit message guidelines**  
✅ **Structured merging workflow**  
✅ **Versioning with tags**  
✅ **CI/CD automation**  
✅ **Rollback strategy in case of issues**  

This version control strategy ensures a scalable, efficient, and structured workflow for our project. 🎯

