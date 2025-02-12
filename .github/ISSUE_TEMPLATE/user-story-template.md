---
name: User Story template
about: Create User Story for a Feature
title: USER_STORY
labels: user story
assignees: Dhanrajshyam

---

**Description:**  
As a [User Type], I want to [Action] so that [Goal].  
**Acceptance Criteria:**  
- [Criterion 1]  
- [Criterion 2]

## ✅ Story - Code Checklist

- [ ] All related tasks are completed and merged into this branch.
- [ ] The implemented feature satisfies the acceptance criteria of the user story.
- [ ] Code structure follows modular and reusable principles.
- [ ] No business logic is tightly coupled to the UI layer.
- [ ] API endpoints (if applicable) adhere to RESTful principles.
- [ ] Database models and migrations are correctly implemented.
- [ ] All data inputs are validated before processing.
- [ ] Security concerns (authentication, authorization, data protection) are addressed.
- [ ] Error handling and logging mechanisms are in place.
- [ ] All dependencies are documented (package.json, requirements.txt, etc.).
- [ ] The feature is backward-compatible and does not break existing functionality.
- [ ] Code changes do not introduce significant performance regressions.
- [ ] Tests cover core functionality (unit tests, integration tests, API tests).
- [ ] API documentation (Swagger/OpenAPI/Postman/Insomnia Collection) is updated (if applicable).
- [ ] Code is peer-reviewed before merging.

## 🔥 Story - Best Practices

1. **Ensure Cohesion:** All related tasks should merge into the story branch before merging to a feature.
2. **Follow DRY Principle:** Eliminate duplicate code by reusing existing components.
3. **Separation of Concerns:** Keep UI, business logic, and database operations separate.
4. **Adopt API Standards:** Use RESTful best practices or GraphQL where applicable.
5. **Optimize Performance:** Avoid unnecessary database queries and optimize API response times.
6. **Ensure Security Best Practices:** Prevent common vulnerabilities (SQL Injection, XSS, CSRF).
7. **Handle Edge Cases Gracefully:** Anticipate incorrect inputs, server failures, and network issues.
8. **Maintain Code Readability:** Use meaningful variable names, comments, and structured formatting.
9. **Keep Commits Logical:** Structure commits around meaningful, incremental changes.
10. **Run Automated Tests:** Validate changes using automated test suites before merging.