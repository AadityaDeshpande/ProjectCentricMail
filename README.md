# ProjectCentricMail
New Way of accessing your gmail account

# Dependencies 
dependencies are given in env_setup.sh

```
make your way to the current directory
chmod +x env_setup.sh
./env_setup.sh
```
this will install dependencies required 
provided python3 and pip3 should be installed alreadly

# Run Project
```
make your way to the current directory
chmod +x run.sh
./run.sh
```

this will execute the project

# Scrrenshots
## Login page
![Landing Page](https://github.com/AadityaDeshpande/ProjectCentricMail/blob/master/Documentation/Screenshots/Log%20in.png)

## Signup page
![Landing Page](https://github.com/AadityaDeshpande/ProjectCentricMail/blob/master/Documentation/Screenshots/Signup.png)

## Home page
![Landing Page](https://github.com/AadityaDeshpande/ProjectCentricMail/blob/master/Documentation/Screenshots/Home.png)

## Project searching page
![Landing Page](https://github.com/AadityaDeshpande/ProjectCentricMail/blob/master/Documentation/Screenshots/project.png)

## Spam page
![Landing Page](https://github.com/AadityaDeshpande/ProjectCentricMail/blob/master/Documentation/Screenshots/spam.png)

## Formal-informal page
![Landing Page](https://github.com/AadityaDeshpande/ProjectCentricMail/blob/master/Documentation/Screenshots/formal.png)

## about page
![Landing Page](https://github.com/AadityaDeshpande/ProjectCentricMail/blob/master/Documentation/Screenshots/about.png)

## About the project

About

“To realize the value of one second, ask the person who just missed a bus or train.”

This project, the Project Centric Mailbox (PCM) is based on a simple observation. In business, it is not easy to end up in his mailbox. Following this, the student engineers found a solution to improve the mailbox, with great attention to the visualization part.

In this project if someone works on five projects, they will have five clusters. In a concrete use case, a person arrives on the PCM. It allows the access to its mails, and these are imported on a database SQLite, encrypted and secured. Once connected, the person arrives on a home page, where they can see the different clusters, and go to the page that interests them. The mails of the various projects are no longer mixed, which facilitates the visibility of these. The second big change is using pattern matching for identification of spamming mails.

The third big feature is classification of mails on the basis of whether it is formal or informal. It helps the individual to identify the mails which belongs to its business ,projects ,etc .For this supervise machine learning is used .

google API are used to fetch mails from gmail, for this authentication from user is required.

# Notes
https://mail.google.com/mail?authuser=me@gmail.com#all/m_id

## College Report

college report is here[Report_PCM_final.pdf](Documentation/Report_PCM_final.pdf)
