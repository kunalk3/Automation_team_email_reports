<div align="right">
<img src="https://user-images.githubusercontent.com/41562231/141720820-090897f9-f564-45e2-9265-15c1269db795.png" height="120" width="900">
</div>

# __Daily email report delivarables__ (python email automation with scheduler)
__Usecase -__ User wants to pull data from client source (Web, email, servers, shared locations, etc) on daily basis and need to ETL process, information retrivals and generate report. This report is of any type (Ex. Html file, Excel file, etc) and for further client activities, we need to notify by mail to team members/ HODs on daily basis as per the reqiorements. 

![1](https://user-images.githubusercontent.com/41562231/179714764-f2d6517b-414d-4880-88f6-316e3e81d994.JPG)

_- Google has announced that it’s disabling the Less Secure Apps feature on some Google accounts from May 30th, 2022. If you’re using Gmail SMTP details with our Other SMTP mailer, you may have difficulty sending emails when this feature is disabled._ __What next??__


<div align="center">
  <a href="https://github.com/kunalk3/P1_tmlc_n2o_streamlit_v2/issues"><img src="https://img.shields.io/github/issues/kunalk3/workiing_with_text_data_scraping" alt="Issues Badge"></a>
  <a href="https://github.com/kunalk3/P1_tmlc_n2o_streamlit_v2/graphs/contributors"><img src="https://img.shields.io/github/contributors/kunalk3/workiing_with_text_data_scraping?color=872EC4" alt="GitHub contributors"></a>
  <a href="https://www.python.org/downloads/release/python-390/"><img src="https://img.shields.io/static/v1?label=python&message=v3.9&color=faff00" alt="Python 3.9"</a>
  <a href="https://github.com/kunalk3/P1_tmlc_n2o_streamlit_v2/blob/main/LICENSE"><img src="https://img.shields.io/github/license/kunalk3/workiing_with_text_data_scraping?color=019CE0" alt="License Badge"/></a>
  <a href="https://github.com/kunalk3/P1_tmlc_n2o_streamlit_v2g"><img src="https://img.shields.io/badge/lang-eng-ff1100"></img></a>
  <a href="https://github.com/kunalk3/P1_tmlc_n2o_streamlit_v2"><img src="https://img.shields.io/github/last-commit/kunalk3/workiing_with_text_data_scraping?color=309a02" alt="GitHub last commit">
</div>
  
<div align="center">   
  
  [![Windows](https://img.shields.io/badge/WindowsOS-000000?style=flat-square&logo=windows&logoColor=white)](https://www.microsoft.com/en-in/)
  [![Visual Studio Code](https://img.shields.io/badge/VSCode-0078d7.svg?style=flat-square&logo=visual-studio-code&logoColor=white)](https://code.visualstudio.com/)
  [![Jupyter](https://img.shields.io/badge/Jupyter-F37626.svg?style=flat-square&logo=Jupyter&logoColor=white)](https://jupyter.org/)
  [![Pycharm](https://img.shields.io/badge/Pycharm-41c907.svg?style=flat-square&logo=Pycharm&logoColor=white)](https://www.jetbrains.com/pycharm/)
  [![Colab](https://img.shields.io/badge/Colab-F9AB00.svg?style=flat-square&logo=googlecolab&logoColor=white)](https://colab.research.google.com/?utm_source=scs-index/)
  [![Spyder](https://img.shields.io/badge/Spyder-838485.svg?style=flat-square&logo=spyder%20ide&logoColor=white)](https://www.spyder-ide.org/)
  [![Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg?style=flat-square&logo=spyder%20ide&logoColor=white)](https://share.streamlit.io/)
</div>
  
<div align="center">
  
  [![LinkedIn Badge](https://img.shields.io/badge/LinkedIn-Profile-informational?style=flat&logo=linkedin&logoColor=white&color=0078d7)](https://www.linkedin.com/in/kunalkolhe3/)
  [![Github Badge](https://img.shields.io/badge/Github-Profile-informational?style=flat&logo=github&logoColor=white&color=black)](https://github.com/kunalk3/)
  [![Gmail Badge](https://img.shields.io/badge/Gmail-Profile-informational?style=flat&logo=Gmail&logoColor=white&color=e44e4e)](mailto:kunalkolhe333@gmail.com)
  [![Facebook Badge](https://img.shields.io/badge/Facebook-Profile-informational?style=flat&logo=facebook&logoColor=white&color=0078d7)](https://www.facebook.com/kunal.kolhe.98/)
  [![Instagram Badge](https://img.shields.io/badge/Instagram-Profile-informational?style=flat&logo=Instagram&logoColor=white&color=c90076)](https://www.instagram.com/kkunalkkolhe/)
</div>
  
---
  
## :ice_cube: Overview:
- With growing awareness of security, it’s highly recommended to have 2-Step Verification set up in your Google account, if not already. However, with 2-Step Verification enabled, you’ll realise that:
  - Less secure app access” option is no longer visible in Google
  - Programmatic login with your Google password only satisfies one of the 2-Step Verification

Essentially, you are blocked from accessing your Google Account programmatically now. So, __how do we proceed from here now?__

---

## :bulb: Demo

https://user-images.githubusercontent.com/41562231/179727952-5dbf4e25-c451-4b92-b186-a78241441c0f.mp4

---

## :wrench: Installation
__Structure__

__A)__ Generating App Passwords from Google

__B)__ Programming: Setup script and send email in Python

__C)__ Adding script in Task Scheduler for automation 

---

__A) Generating App Passwords from Google:__ First, I recommend setting up a new Google account as a development environment for this tutorial instead of direct implementation in your desired (production/personal) Google Gmail account.
- i. Set up a Google account. Skip this if you are using an existing Gmail account, and skip to point 4 if the account has 2-Step Verification enabled.
- ii) Once logged on to your Google account, navigate to _Manage your Google Account -> Security -> Privacy Setting_

![2](https://user-images.githubusercontent.com/41562231/179715730-6d07c88e-5b33-4282-969f-cb452d472e5e.JPG)

- iii) Setup 2-Step Verification by following the on-screen instructions. Once you have 2-Step Verification enabled, the _App Passwords_ option should be visible.
- iv) Under App Passwords, select _Other (Custom name)_ from the _Select app_ dropdown list. 

![3](https://user-images.githubusercontent.com/41562231/179715837-30c5cad2-7bb9-418f-b7bc-58fc931a0f1b.JPG)

- v) Give it a name for your own identification. Click on _GENERATE_ and a 16-character code _(in the format of xxxx-xxxx-xxxx-xxxx)_ should be generated. This code is important for programatically access.

![4](https://user-images.githubusercontent.com/41562231/179715885-13c5e230-f627-4129-a87d-53b34b0d4e88.JPG)

__B) Programming: Setup script and send email in Python:__ We will be using the built-in module for sending emails via SMTP. SMTP is the protocol used for sending emails and routing emails between mail servers.

- Create __virtual environment__ `python -m venv VIRTUAL_ENV_NAME` and activate it `.\VIRTUAL_ENV_NAME\Scripts\activate`.
- Install necessary library for this project from the file `requirements.txt` or manually install by `pip`.
  ```
  pip install -r requirements.txt
  ```
  To create project library requirements, use below command,
  ```
  pip freeze > requirements.txt
  ```
- Store your own 16-character code _(xxxx-xxxx-xxxx-xxxx)_ generated from Google in credentials JSON file into _pass_ key without '-'. Also mentioned email person details _To, CC, BCC_ as per below.

  ```json
  {
    "from": "XYZ@gmail.com",
    "pass": "xxxxxxxxxxxxxxxx",
    "to": "ABC@gmail.com",
    "cc": ["ABC1@gmail.com", "ABC2@gmail.com"],
    "bcc": ["ABC3@gmail.com", "ABC4@gmail.com"]
  }
  ```
- Configure input and output path with data as per requirements in code file.
  ```python
  SOURCE_NODE = './sourceNode/'            # Input directory / data
  DESTINATION_NODE = './destinationNode/'  # Output directory / data

  # Email body
  text1 = 
  '''
  Hi Team,
  Good Morning, Please find below report.
  '''

  # Email configuration setup
  context = ssl.create_default_context()
  server = smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context)
  server.login(sender_id, sender_pass)
  ```
- Run app.py python file locally in machine. Once all set, check mails, windows notification and then we will move to automate the process by Schedulling job.
  ``` 
  python run app.py
  ```
  Once all set, check mails, windows notification and then we will move to automate the process by Scheduling job.

__C) Adding script in Task Scheduler for automation:__ Here I have created video for this process automation on daily basis for a references (System: Windows 10).
- Create task from Task Scheduler (Add name, description, machine settings)
- Configure trigger settings on daily/ weekly/ specific day with time and repeatition for job.
- Provide script path, script name and python path for python application.
  
  C:\Users\...\Scripts\python.exe  -> python cmd enabled
  
  C:\Users\...\Scripts\pythonw.exe -> python cmd disabled

https://user-images.githubusercontent.com/41562231/179728006-7d5ecb89-3a71-478c-923b-5123824a7374.mp4

---  
  
## :bookmark: Directory Structure 
```bash
    .                                       # Root directory
    ├── sourceNode                          # Data source directory
    │   └──us-500.csv                       # Data file - input
    ├── destinationNode                     # Data destination directory
    │   └──output.html                      # Data file - output
    ├── app.py                              # Script file
    ├── credentials.json                    # Email credentials
    ├── requirements.txt                    # Project requirements library with versions
    ├── README.md                           # Project README file
    └── LICENSE                             # Project License file
```

---
  
### :iphone: Connect with me
`You say freak, I say unique. Don't wait for an opportunity, create it.`
  
__Let’s connect, share the ideas and feel free to ping me...__
  
<div align="center"> 
  <p align="left">
    <a href="https://linkedin.com/in/kunalkolhe3" target="blank"><img align="center" src="https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/linkedin.svg" alt="kunalkolhe3" height="30" width="40"/></a>
    <a href="https://github.com/kunalk3/" target="blank"><img align="center" src="https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/github.svg" alt="kunalkolhe3" height="30" width="40"/></a>
    <a href="https://fb.com/kunal.kolhe.98" target="blank"><img align="center" src="https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/facebook.svg" alt="kunal.kolhe.98" height="30" width="40"/></a>
    <a href="mailto:kunalkolhe333@gmail.com" target="blank"><img align="center" src="https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/gmail.svg" alt="kunalkolhe333" height="30" width="40"/></a>
    <a href="https://instagram.com/kkunalkkolhe" target="blank"><img align="center" src="https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/instagram.svg" alt="kkunalkkolhe" height="30" width="40"/></a>
    <a href="https://www.hackerrank.com/kunalkolhe333" target="blank"><img align="center" src="https://cdn.jsdelivr.net/npm/simple-icons@3.0.1/icons/hackerrank.svg" alt="kunalkolhe333" height="30" width="40"/></a>
  </p>
</div>
  
<div align="left">
<img src="https://user-images.githubusercontent.com/41562231/141720940-53eb9b25-777d-4057-9c2d-8e22d2677c7c.png" height="120" width="900">
</div>
