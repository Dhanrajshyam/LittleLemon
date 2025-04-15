
## As part of issue
- [ ] user story
- [ ] task
- [ ] feature
- [ ] epic
- [ ] bug

**On successful completion of this PR, the following issue(s) will be closed:**
close #(issue number)

## Updated
- [ ] Code
    - [ ] add
    - [ ] delete
    - [ ] modify
        - [ ] refactor
        - [ ] optimize
    - [ ] test
    - [ ] fix(Bug)
        - [ ] hotfix
- [ ] Documentation
    - [ ] Designs
    - [ ] Templates
    - [ ] Project Documents(README, LICENCE, CODE OF CONDUCT, etc.)
    - [ ] Project Guidelines(Version control practices, coding standards, etc.)
    - [ ] Images
    - [ ] Others
- [ ] Configuration
    - [ ] GitHub Actions
    - [ ] Settings(.env, .gitignore, .pytest.ini, django settings, etc.)
    - [ ] Dependencies(requirements.txt, package.json, etc.)
    - [ ] Others

## Verified/Tested
- [ ] Code
    - [ ] Lint
    - [ ] Test
    - [ ] Coverage
    - [ ] Security
    - [ ] Performance
    - [ ] Others
- [ ] Documentation
- [ ] Configurations

## Merged branch
- [ ] task -> story
- [ ] story -> feature
- [ ] feature -> epic
- [ ] epic -> develop
- [ ] develop -> test
- [ ] test -> main
- [ ] hotfix -> main (Urgent Bug Fixes in production)

## Deleted branch
- [ ] task
- [ ] story
- [ ] feature
- [ ] epic (After Release only)

## Code Checklist
- [ ] I have performed a self-review of my code
- [ ] My code follows the style guidelines of this project
- [ ] I have commented my code where necessary
- [ ] I have made corresponding changes to the documentation
- [ ] My changes generate no new warnings
- [ ] All existing tests pass
- [ ] I have added tests that prove my fix is effective
- [ ] I have ensured my code is backward-compatible
- [ ] I have run all database migrations (if applicable)
- [ ] I have tested API responses (if applicable)

## Screenshots (if applicable)
Add screenshots to help explain changes if applicable.

## Additional Information
Provide any other relevant information here.

## 🚀 When to Delete a Branch?
- Delete Task Branch after merging into Story
- Delete Story Branch after merging into Feature
- Delete Feature Branch after merging into Epic
- Keep Epics for reference until the release is completed

## What If You Need to Roll Back?
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

