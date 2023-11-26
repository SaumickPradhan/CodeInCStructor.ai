# CodeInCStructor.ai

	An AI driven Cod-Ing Instructor Platform for Inquisitive CS Students and Faculty

### Table of Contents

1. [Team Names and Project Abstract](#team-names-and-project-abstract)
2. [Project Description](#project-description)
3. [User Stories and Design Diagrams](#user-stories-and-design-diagrams)
    - [User Stories](#user-stories)
    - [Design Diagrams](#design-diagrams)
      - [Design D0](#design-D0)
      - [Design D1](#design-D1)
      - [Design D2](#design-D2)
      - [Design D3](#design-D3)
      - [Description of the Diagrams](#description-of-the-diagrams)
4. [Project Tasks and Timeline](#project-tasks-and-timeline)
    - [Task List](#task-list)
    - [Timeline](#timeline)
    - [Effort Matrix](#effort-matrix)
5. [ABET Concerns Essay](#abet-concerns-essay)
6. [PPT Slideshow (includes ABET Concerns)](#ppt-slideshow-includes-abet-concerns)
7. [Self-Assessment Essays](#self-assessment-essays)
8. [Professional Biographies](#professional-biographies)
9. [Budget](#budget)
10. [Appendix](#appendix)

---

## Team Names and Project Abstract

**Team Members:**
- Saumick Pradhan (pradhask@mail.uc.edu)​
- Roshni Khatri (khatrirr@mail.uc.edu)​
- Advisor:
	- Dr. William III Hawkins (hawkinwh@ucmail.uc.edu)​
 	- Dr. Raj Bhatnagar (bhatnark@ucmail.uc.edu)​


**Project Abstract** <br><br>
CodeInCStructor.ai aims to develop a dynamic platform tailored for first-year Computer Science students and those in related programming fields. The central focus is to foster motivation, positive support, and encouragement throughout their coding journey. Leveraging Generative AI, the platform seeks to engage students with insightful feedback to overcome coding challenges, whether they are beginners or experienced programmers. The platform also enables professors to come up with innovative and unique exercises for the students to enable critical thinking. These exercises will supplement the material from the professor and help students interact with customized problems.​

---

## Goal Statement​

Making coding engaging by providing good feedback so that beginner Students can push through the inevitable tough parts that come with writing code, irrespective of experience. Working on unique assignments will help students actively think towards the solution rather than resorting to online help resources. Referring back to the old assignments helps students recollect the old concepts in an easy-to-read natural language form.

## Project Description

The "CodeInCStructor.ai” platform has two broader use cases. The first one uses a fine tuned LLM that creates unique exercises and produces sample solutions for the professor. The second is using the student’s attempt in Python to the exercise and providing feedback based on the sample solution. This feedback will be generated in Natural language and will be a continuous comprehensive response cycle. The correct answers will then be saved along with their natural language explanation, for the student to review later on. The LLM will be based on the gpt-3.5-turbo-0613 model.​

Targeting first-year CS students, this platform encourages active learning, helps tackle syntax and logical errors, while equips students for technical interviews and getting their first COOP opportunities. Our ultimate goal is to enhance coding engagement and provide valuable feedback, promoting students' coding proficiency, regardless of their experience level. We want the students to work on unique exercises and in a continuous feedback-driven learning approach with unique challenges to enable critical thinking.​


---

## User Stories and Design Diagrams

### User Stories
<img width="42" alt="image" src="https://github.com/SaumickPradhan/CodeInCStructor.ai/assets/85262444/d0784726-3aae-486e-9e85-1d77f0887a41">

**User Profile 1:** I am a First year College student, starting my Computer Science (or similar) degree. I have little to no prior experience in programming and I have just started to learn the basics.​

**User Story 1:** Given my background, I face a lot of syntax and logical errors while coding during my assignments. I sometimes do not know the correct or most effective way to approach the solution. Hence, I want to have an interactive platform which can help me learn coding in an efficient manner and help answer my questions during the assignment, so that I can have strong fundamentals.​


<img width="67" alt="image" src="https://github.com/SaumickPradhan/CodeInCStructor.ai/assets/85262444/75e25788-b13c-4965-8030-7fd692d36595">

**User Profile 2:** I am a Computer Science professor teaching an Intro computer Science class with 50 + students.​

**User Story 2:** It is difficult to provide personalized feedback to every student based on their attempts to the exercises to enable active learning by trying. It is also challenging to come up with unique exercises for each class/ student as most questions have solutions online. ​



### Design Diagrams


#### Design D0:

In this highest-level view, we have the Input from the user. It passes through the “Coding Platform” which is the machine. And then the output is the efficient Code recommendation generated from the “Coding Platform”. The “Machine” is depicted in a cloud.

<img width="709" alt="image" src="https://github.com/SaumickPradhan/UG-senior-design/assets/85262444/c2f9e0fd-b44e-4e5e-94c6-63e247a39b6a">

#### Design D1:

In this diagram, we go one layer deep. We understand that the Professor publishes the coding Assignment for the Student. The student can access it via a notebook or a Discord bot. The student submits their response to the question on the platform. The platform outputs tips for coding efficiency with appropriate comments. We understand here that the platform is intrinsic to the assignment given by the professor.

<img width="738" alt="image" src="https://github.com/SaumickPradhan/UG-senior-design/assets/85262444/95fbfe28-8a58-444e-8513-d491f1ff1227">


#### Design D2

Our final design shows the complete working of the subsystems of the platform. The professor publishes the assignment and every student accesses it through their university login ID. The student interacts with the assignment and then submits a response. The response is then passed through an Open API generative API. The API is pre-trained on a model which is imported. The model gives the output to the student. The student reviews the comments and implements the code recommendations. The subsystems of the platform are in square boxes.

<img width="611" alt="image" src="https://github.com/SaumickPradhan/UG-senior-design/assets/85262444/13d847c1-1113-48c4-9b0b-b7a0c8052c59">


#### Design D3

We decided to add additional components to the project. The Teacher will provide exercises and study materials for the students using the platform. The AI platform will produce solutions to the exercises. The students will access these and  will manually get solutions to the exercise and get an attempt. The platform will check the attempt and provide feedback to the student. 

![image](https://github.com/SaumickPradhan/UG-senior-design/assets/85262444/d490c4fd-0c2f-41ff-9c7d-ca6721ebed72)
---

## Project Tasks and Timeline

*Assignment #5-6*

### Task List
!!!!!!!!!!!!!FOR ROSHINI!!!!!!!!!!!!!!!
PLEASE USE SOME TASKS FROM THE EFFORT MATRIX GIVEN BELOW IN THE TASK LIST, I HAVE ADDED NEW TASKS THERE.

PLEASE WRITE MORE DETAILED TASKS AND TIMELINE. ALSO WE SHOULD SERIOUSLY THINK ABOUT MAKING A REALISTIC TIMELINE THAT WE CAN ACTUALLY FOLLOW
!!!!!!!!!!!!!!!!
1. Define project scope
2. Conduct market research
3. Develop user personas
4. ...

### Timeline

| Task            | Start Date | End Date   |
| --------------- | ---------- | ---------- |
| Define scope    | 2023-01-01 | 2023-01-15 |
| Market research | 2023-01-16 | 2023-02-01 |
| ...

### Effort Matrix

| Sr. No. | Task                            | Saumick | Roshni | Comments |
| ------- | ------------------------------- | ------- | ------ | -------- |
|   1)      | Read papers                  | 100%    | 100%   |          |
|   2)      | Alternative Solutions          | 100%    | 100%   |          |
|   3)      | Collect sample I/P – O/P prompts | 100%    | 100%   |          |
|   4)      | Research the API               | 100%    | 100%   |          |
|   5)      | Create sample questions         | 100%    | 100%   |          |
|   6)      | Get feedback                   | 100%    | 100%   |          |
|   7)      | Summarize the response         | 100%    | 100%   |          |
|   8)      | Set up Jupyter Notebook Interface           |     | 100%   |          |
|   9)      | Prompt Engineer the API                    | 100%    |    |          |
|   10)      | Sample Questions and answers for testing              | 100%    |    |          |
|   11)      | Prepare the server to host notebook           | 100%    | 100%   |          |
|   12)      | Create a prototype UI           | 100%    | 100%   |          |
|   13)      | Presentation                    | 100%    | 100%   |          |
---

## ABET Concerns Essay

*Assignment #7*

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed vestibulum quam id mauris tincidunt, ac consequat arcu rhoncus. Nulla facilisi. Proin lacinia tortor nec magna viverra, ac lacinia mauris dictum.

---

## PPT Slideshow (includes ABET Concerns)

**Video Presentation:** https://www.youtube.com/watch?v=RXlRPnMqUa0


**Slides:** https://mailuc-my.sharepoint.com/:p:/g/personal/pradhask_mail_uc_edu/Efgkoc-HJo1KryDhuV2Lg1gB4Xdi_xeH4qFJ5IR7dFzi9Q?e=0J38sY


---

## Self-Assessment Essays

[**Saumick Pradhan**](https://github.com/SaumickPradhan/CodeInCStructor.ai/blob/main/docs/Saumick-Pradhan-Individual-Capstone-Assessment.md)

---

## Professional Biographies

[**Saumick Pradhan**](https://github.com/SaumickPradhan/CodeInCStructor.ai/blob/main/docs/Saumick-Pradhan-Professional-Biography.md)


[**Roshni Khatri**](https://github.com/SaumickPradhan/CodeInCStructor.ai/blob/main/docs/Roshni-Khatri-Professional-Biography.md)

---

## Budget

Expenses to date: $10

*Statement:*
We have incurred expenses for purchase of OpenAI API key. This is the base rate while purchasing the API for the first time. We will be billed as per our use duing the testing phase. Following is the pricing information from OpenAI.

https://openai.com/pricing

---

## Appendix

*References, citations, links to code repositories, and meeting notes.*

**Weekly Time Commitment during August to November 2023**

| Sr. No. | Task                            | Saumick | Roshni | Comments |
| ------- | ------------------------------- | ------- | ------ | -------- |
|   1)      | Brainstroming and Research                  | 1 Hr    | 1 Hr   |          |
|   2)      | Testing API and prompt engineering         | 1 Hr    | 0.5 Hr   |          |
|   3)      | Learning Prompt engineering and Notebook Deployment | 0.5 Hr    | 1 Hr   |          |
|   4)      | Assignment Preperation               | 1 Hr    | 1 Hr   |          |
|   5)      | Advisor Meeting         | 0.5 Hr    | 0.5 Hr   |          |




---
