**SauceDemo QA Automation Suite (Selenium + Pytest)
UI Automation • API Testing • Python • Professional QA Portfolio Project**

**⭐ Overview**

This project is a complete QA automation suite combining:

UI automation using Selenium WebDriver

API testing using Python requests

Test planning + test cases + bug reporting

Professional pytest structure

xfail handling for flaky UI elements

The system under test is the public SauceDemo web application, which is commonly used for QA interview tasks and automation practice.

This suite demonstrates real-world QA automation skills suitable for entry-level QA, automation trainee, or junior SDET roles.

**🧰 Tech Stack**
Area	Tools
Language	Python 3.12
Automation Framework	Pytest
UI Testing	Selenium WebDriver
Browser	Chrome (webdriver-manager)
API Testing	requests
Virtual Environment	venv
Editor	VS Code

**📁 Project Structure**
qa_automation_project/
│
├── manual/
│   ├── test_plan.md
│   ├── test_cases.md
│   └── bug_reports.md
│
├── tests/
│   ├── api/
│   │   └── test_users_api.py
│   ├── ui/
│   │   └── test_ui_login.py
│   └── test_ui_inventory_cart.py
│
├── utils/
│   └── conftest.py   # Browser fixture + Selenium setup
│
├── requirements.txt
└── README.md

**🖥️ UI Test Coverage (Selenium)**
Test Case	Description	Status
TC_UI_001	Login with valid credentials	✅ PASS
TC_UI_002	Login with invalid password	✅ PASS
TC_UI_003	Login with locked-out user	✅ PASS
TC_UI_004	Sort items by “Price: Low → High”	✅ PASS
TC_UI_005	Add item to cart → badge = 1	✅ PASS
TC_UI_006	Remove item from cart → badge disappears	⚠️ XFAIL (timing-dependent)
TC_UI_007	Logout returns to login page	⚠️ XFAIL (menu animation delay)

The two xfail tests are intentionally kept as stretch tests to demonstrate handling of asynchronous UI timing issues in headless mode.

**🌐 API Test Coverage**
Test Case	Endpoint	Expected Behavior	Status
TC_API_001	/api/users?page=2	Returns 200 + user list	🟢 PASS

**▶️ How to Run the Tests**
**1. Activate virtual environment**
venv\Scripts\activate

**2. Install dependencies**
pip install -r requirements.txt

**3. Run all tests**
pytest -v

**4. Run only UI tests**
pytest -v tests/ui

**5. Run only API tests**
pytest -v tests/api

**⚠️ Handling Flaky Tests (Professional Practice)**

Two tests are marked as:

@pytest.mark.xfail


because:

SauceDemo uses animated side menus

Dynamic elements sometimes load late

Headless browsers are more timing-sensitive

Instead of deleting or hiding them, they are documented and kept for realism — recruiters appreciate this transparency.

**📸 Example Pytest Output**
7 passed, 1 xfailed, 1 xpassed in 110.58s


This output is expected and reflects a mature suite with documented flakiness.

**🚀 Future Enhancements**

Convert to Page Object Model (POM)

Add screenshots on failure

Integrate GitHub Actions CI

Add coverage reports

Add more API endpoints + negative cases

Parallel execution with pytest-xdist
