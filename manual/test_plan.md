# Test Plan – QA Automation Project

## 1. Introduction
This test plan outlines the approach, resources, scope, and strategy for testing the QA Automation Project.  
The application under test includes a UI login flow (SauceDemo) and REST API endpoints (ReqRes API).  
The objective is to validate correct functionality through manual testing and automated Python-based tests.

---

## 2. Scope

### In Scope
- UI testing of SauceDemo login functionality  
- API testing of public ReqRes endpoints  
- Manual test case creation  
- Bug reporting  
- UI automation using Selenium  
- API automation using Python requests + pytest  

### Out of Scope
- Performance testing  
- Load testing  
- Mobile testing  
- Security testing  
- Database validation  

---

## 3. Test Types
- Functional Testing  
- Negative Testing  
- Regression Testing  
- API Automation Testing  
- UI Automation Testing  

---

## 4. Test Environment
- **OS:** Windows 10  
- **Browser:** Google Chrome  
- **Language:** Python 3.x  
- **Framework:** pytest  
- **Tools & Libraries:**  
  - Selenium WebDriver  
  - Webdriver Manager  
  - Requests library  
  - Visual Studio Code  
  - Git / GitHub  

---

## 5. Test Data

### UI Valid Login Credentials
- Username: `standard_user`  
- Password: `secret_sauce`

### UI Invalid Login Credentials
- Username: `standard_user`  
- Password: `wrong_password`

### API Test Data
- GET endpoint: `https://reqres.in/api/users?page=2`  
- Invalid GET endpoint: `https://reqres.in/api/unknown/999`  
- POST body:
```json
{
  "name": "morpheus",
  "job": "leader"
}
6. Risks
API may change or become unavailable

Browser/WebDriver incompatibility

Network instability may affect response times

Third-party test website (SauceDemo) may experience downtime

7. Deliverables
Test Plan

Test Cases (UI + API)

Bug Reports

Automated API Tests (pytest + requests)

Automated UI Tests (pytest + Selenium)

Project README

GitHub repository with full documentation

8. Entry & Exit Criteria
Entry Criteria
Test environment is ready

Required tools installed (Python, pytest, Selenium, Requests)

Test cases authored

Basic framework structure created

Exit Criteria
All test cases executed

All high/medium severity bugs logged

Automation scripts completed for API and UI flows

No critical or blocker issues open

README updated

9. References
https://www.saucedemo.com/

https://reqres.in/

Project GitHub repository README