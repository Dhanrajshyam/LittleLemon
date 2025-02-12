---
name: Feature template
about: Create Feature for an Epic
title: FEATURE
labels: feature
assignees: Dhanrajshyam

---

**Description:**  
[Describe the feature and its functionality]  
**User Stories:**  
- [Story 1]  
- [Story 2]

## ✅ Feature - Code Checklist

- [ ] All related user stories are completed and merged into this branch.
- [ ] The feature is implemented according to design specifications.
- [ ] Business logic is encapsulated within services or reusable modules.
- [ ] API endpoints (if applicable) adhere to RESTful or GraphQL best practices.
- [ ] Database changes (models, migrations) are reviewed for performance and consistency.
- [ ] The feature integrates well with existing functionalities.
- [ ] Configurations (.env, settings, API keys) are properly managed and documented.
- [ ] Unit, integration, and system tests cover the feature’s core functionalities.
- [ ] Logging and monitoring are implemented for debugging and analytics.
- [ ] Performance optimizations (caching, lazy loading, pagination) are considered.
- [ ] Feature toggles (if applicable) are implemented for gradual rollout.
- [ ] API documentation is updated (Swagger, Postman, internal wiki).
- [ ] CI/CD pipeline successfully builds and tests the feature branch.
- [ ] The feature branch is ready for merging into the epic branch after approval.

## 🔥 Feature - Best Practices

1. **Ensure All Stories Are Merged:** A feature branch should only be merged once all dependent stories are complete.
2. **Follow Microservices & Modular Design:** Code should be loosely coupled and reusable across the application.
3. **Design for Scalability:** Optimize database queries, minimize API calls, and use caching when necessary.
4. **Maintain Backward Compatibility:** Avoid breaking changes that affect existing users or systems.
5. **Enhance Security:** Implement encryption, authentication, and authorization checks.
6. **Use Efficient Data Structures & Algorithms:** Optimize for performance and memory usage.
7. **Automate Testing:** Ensure the feature is covered by unit, integration, and regression tests.
8. **Follow Semantic Versioning:** Clearly define version updates if the feature affects public APIs.
9. **Write Meaningful Commit Messages:** Provide clear explanations of what each commit does.
10. **Prepare for Deployment:** Ensure rollback strategies are in place before releasing the feature.