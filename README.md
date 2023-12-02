# CodeInCStructor.ai

	An AI-driven Cod-Ing Instructor Platform for Inquisitive CS Students and Faculty

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

The "CodeInCStructor.ai" platform has two broader use cases. The first one uses a fine-tuned LLM that creates unique exercises and produces sample solutions for the professor. The second use case is to interactively mentor the student as they attempt (in Python) to complete the AI-generated exercise. This feedback will be generated in natural language and will be a continuous comprehensive response cycle. The correct answers will then be saved along with their natural language explanation, for the student to review later on. The LLM will be based on the gpt-3.5-turbo-0613 model.​

Targeting first-year CS students, this platform encourages active learning, helps tackle syntax and logical errors, while equiping students for technical interviews and getting their first COOP opportunities. Our ultimate goal is to enhance coding engagement and provide valuable feedback, promoting students' coding proficiency, regardless of their experience level. We want the students to work on unique exercises and in a continuous feedback-driven learning approach with unique challenges to enable critical thinking.​


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

### Task List

1. **Read Papers:**
   - Identify relevant research papers.
   - Summarize key findings and methodologies.
   - Note any existing solutions or frameworks.

2. **Alternative Solutions:**
   - Investigate alternative approaches to the problem.
   - Compare pros and cons of different solutions.
   - Consider novel or hybrid approaches.

3. **Collect Sample I/P – O/P Prompts:**
   - Define a set of input-output prompt pairs for testing.
   - Ensure diversity and coverage of potential use cases.
   - Include edge cases and corner scenarios.

4. **Research the API:**
   - Explore the documentation of the selected API.
   - Understand its capabilities and limitations.
   - Identify any prerequisites or dependencies.

5. **Create Sample Questions:**
   - Generate a set of questions based on the collected prompts.
   - Ensure a variety of question types (e.g., open-ended, multiple-choice).
   - Consider potential user queries.

6. **Get Feedback:**
   - Share the sample questions with a small group for feedback.
   - Gather insights on clarity, relevance, and difficulty.
   - Iterate on questions based on feedback.

7. **Summarize the Response:**
   - Develop a system to summarize API responses.
   - Handle different response formats (text, JSON, etc.).
   - Consider how to handle errors or ambiguous responses.

8. **Set up Jupyter Notebook Interface:**
   - Install necessary libraries and dependencies.
   - Configure the Jupyter Notebook environment.
   - Ensure seamless integration with the chosen API.

9. **Prompt Engineer the API:**
   - Fine-tune input prompts for optimal performance.
   - Experiment with variations to enhance response quality.
   - Document any patterns or guidelines for prompt engineering.

10. **Sample Questions and Answers for Testing:**
    - Pair sample questions with expected API responses.
    - Develop a testing protocol for systematic evaluation.
    - Consider scenarios for regression testing.

11. **Prepare the Server to Host Notebook:**
    - Set up a server environment to host the Jupyter Notebook.
    - Configure security settings and access controls.
    - Ensure compatibility with external dependencies.

12. **Create a Prototype UI:**
    - Design a simple user interface for interacting with the system.
    - Integrate input and output components.
    - Consider user experience and accessibility.

13. **Presentation:**
    - Prepare a presentation summarizing the project.
    - Include key findings, challenges, and solutions.
    - Demonstrate the prototype and discuss future enhancements.
    - Allow time for questions and feedback.


### Timeline

This project follows a structured timeline with tasks organized by months. Each task represents a significant step in the development process. 

### October 2023

- **1. Read Papers**
- **2. Alternative Solutions**
- **3. Collect Sample I/P – O/P Prompts**

    - **6. Get Feedback**
    - **7. Summarize the Response**

### November 2023

- **4. Research the API**
- **5. Create Sample Questions**

    - **6. Get Feedback**
    - **7. Summarize the Response**

### December 2023

- **8. Set up Jupyter Notebook Interface**

    - **9. Prompt Engineer the API**

### January 2024

- **10. Sample Questions and Answers for Testing**

    - **11. Prepare the Server to Host Notebook**

### February 2024

- **12. Create a Prototype UI**

    - **13. Presentation**

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

Professional: This project directly influences the professional growth of its creators and the learning experience for students. By developing an effective coding education platform, the creators enhance their programming and AI skills, solidifying their reputation in education technology and AI communities. Specialized knowledge in both programming and AI is crucial for refining the generative AI model, ensuring accurate and beneficial suggestions for students.

Ethical: The project seeks to positively motivate students in their coding journey while addressing ethical considerations. Caution is advised to prevent over-reliance on AI feedback, which could hinder critical thinking. Efforts are made to create an inclusive and unbiased learning environment, prioritizing ethical use of AI suggestions to enhance, not impede, the learning experience.

Legal: Legal aspects, especially regarding intellectual property and data privacy, are carefully considered. Adherence to copyright and fair use laws is essential, particularly when incorporating content from third-party sources. Compliance with data privacy laws is a priority, especially in handling personally identifiable information, to avoid potential legal challenges.

Security: Security measures are paramount, particularly in safeguarding user data and AI functionalities. Encryption and secure storage are implemented for user data, and regular security audits mitigate potential threats like data breaches or malicious code injections. Privacy concerns are addressed by empowering users to control their data sharing preferences, ensuring data is used appropriately.

Social: The project's impact extends to society by providing a valuable educational tool for students in computer science. Personalized support and motivation can enhance the quality of education, potentially increasing student retention in coding-related fields. Making the project accessible to non-profit organizations can further support underserved communities, contributing to public service and enriching lives. The potential to publish research based on testing and surveys underscores a commitment to sharing valuable insights with the broader educational community.

## PPT Slideshow (includes ABET Concerns)

**Video Presentation:** https://www.youtube.com/watch?v=RXlRPnMqUa0


**Slides:** https://mailuc-my.sharepoint.com/:p:/g/personal/pradhask_mail_uc_edu/Efgkoc-HJo1KryDhuV2Lg1gB4Xdi_xeH4qFJ5IR7dFzi9Q?e=0J38sY


---

## Self-Assessment Essays

[**Saumick Pradhan**](https://github.com/SaumickPradhan/CodeInCStructor.ai/blob/main/docs/Saumick-Pradhan-Individual-Capstone-Assessment.md)

[**Roshni Khatri**](https://github.com/SaumickPradhan/CodeInCStructor.ai/blob/main/docs/Roshni-Khatri-Individual-Capstone-Assessment.md)

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
**References**
- Association for Computing Machinery. (2021). User-Centered Design of Augmented Reality Environments for Creativity in Education. ACM Transactions on Computer-Human Interaction (TOCHI), 28(2), Article 8. https://dl.acm.org/doi/abs/10.1145/3501385.3543957

---

**Meeting Notes**
- Link: https://mailuc-my.sharepoint.com/:w:/r/personal/khatrirr_mail_uc_edu/Documents/Meeting%20Notes.docx?d=w0fe1f223d51b466d9529812b4e63455e&csf=1&web=1&e=GsTpuU

---

**Weekly Time Commitment during August to November 2023**

| Sr. No. | Task                            | Saumick | Roshni | Comments |
| ------- | ------------------------------- | ------- | ------ | -------- |
|   1)      | Brainstroming and Research                  | 1 Hr    | 1 Hr   |          |
|   2)      | Testing API and prompt engineering         | 1 Hr    | 0.5 Hr   |          |
|   3)      | Learning Prompt engineering and Notebook Deployment | 0.5 Hr    | 1 Hr   |          |
|   4)      | Assignment Preperation               | 1 Hr    | 1 Hr   |          |
|   5)      | Advisor Meeting         | 0.5 Hr    | 0.5 Hr   |          |




---
