# 🎭 Playwright for MLOps: Automated E2E & UI Testing

This repository demonstrates how to integrate **Playwright** into an **MLOps pipeline** to test web-based ML applications (Streamlit, Gradio, React dashboards) before and after model deployment.

## 🚀 Quickstart

### 1. Prerequisites & Setup
```bash
# Clone repository

git clone https://github.com/mpluwu/playwright-demo
cd playwright-demo


# Install dependencies and Playwright browsers

pip install -r requirements.txt
npm init playwright@latest
env_setup (can edit)


#Running the Example Test

npx playwright test

#HTML Test Reports

npx playwright show-report

#Running the Example Test in UI Mode

npx playwright test --ui

#The python test (using streamlit to turn the code into a web)

streamlit run app.py

#Run the testing script

pytest test_app.py 

```
Referenced by:
[https://playwright.dev/docs/intro]
[https://www.youtube.com/watch?v=dn_Z11y7Fuo]
[https://github.com/pavanoltraining/Playwright_Opencart_AI_v1]
