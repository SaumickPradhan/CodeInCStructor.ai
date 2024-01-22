# TEST PLAN

# Description of Overall Test Plan
The overall test plan for CodeInCStructor.ai employs a multi-level testing strategy to ensure the robustness and effectiveness of the platform. The testing includes unit testing, integration testing, and system testing. <br>

Unit tests focus on individual components, ensuring they perform as expected. Integration tests examine the interaction between subsystems, ensuring seamless collaboration. System tests evaluate the entire platform's functionality, covering end-to-end scenarios. <br>

Additionally, both blackbox and whitebox testing methodologies are applied to validate external and internal behaviors. Functional testing ensures that features meet user requirements, while performance testing assesses the system's responsiveness under different workloads. The testing plan is designed to verify that CodeInCStructor.ai meets the project's goals and satisfies user stories.


# Test Case Descriptions
List a series of 10-25 tests for validating your project outcomes. For each test case provide the following:
1.  test case identifier (a number or unique name)
2.  purpose of test
3.  description of test
4.  inputs used for test
5.  expected outputs/results
6.  normal/abnormal/boundary case indication
7.  blackbox/whitebox test indication
8.  functional/performance test indication
9.  unit/integration test indication

Note that some of these categories may be inappropriate for your project and may be omitted if you can justify doing so. For items 6-9, only one term should apply.


## Test Case 1

Purpose: Verify platform interaction for a first-year college student.

Description: The test involves a student interacting with the platform, seeking code recommendations.

Inputs: Student input in the form of code-related queries.

Expected Outputs: Platform provides efficient code recommendations and tips for coding efficiency.

Normal/Abnormal/Boundary Case: Normal case.

Blackbox/Whitebox: Blackbox.

Functional/Performance: Functional.

Unit/Integration: Unit.

## Test Case 2

Purpose: Validate assignment submission feedback.

Description: A student submits a response to a coding assignment, and the platform provides feedback.

Inputs: Student's coding assignment response.

Expected Outputs: Platform gives relevant feedback and tips based on the student's response.

Normal/Abnormal/Boundary Case: Normal case.

Blackbox/Whitebox: Blackbox.

Functional/Performance: Functional.

Unit/Integration: Unit.

## Test Case 3

Purpose: Confirm assignment creation for a computer science professor.

Description: The professor publishes a coding assignment, and the platform assists in creating unique exercises.

Inputs: Coding assignment details provided by the professor.

Expected Outputs: Platform generates innovative exercises and produces sample solutions.

Normal/Abnormal/Boundary Case: Normal case.

Blackbox/Whitebox: Blackbox.

Functional/Performance: Functional.

Unit/Integration: Integration.

## Test Case 4

Purpose: Assess feedback analysis for a computer science professor.

Description: The professor receives feedback on student attempts to enable personalized feedback.

Inputs: Feedback on student attempts.

Expected Outputs: Comprehensive feedback aiding active learning by students.

Normal/Abnormal/Boundary Case: Normal case.

Blackbox/Whitebox: Blackbox.

Functional/Performance: Functional.

Unit/Integration: Integration.

## Test Case 5

Purpose: To ensure that the application launches successfully without errors and that the user interface components are initialized properly.

Description: This test verifies the initial state of the application by checking if the launch process is error-free and if the UI components are correctly initialized.

Inputs: Launch the application by executing the Jupyter Notebook containing the generative AI for assisted learning. Observe the user interface as it loads.

Expected Outputs: The application launches without any errors. The user interface is displayed with the expected components (e.g., buttons, menus, input fields). No unexpected pop-ups, error messages, or crashes occur during the launch.

Normal/Abnormal/Boundary Case: Boundary Case.

Blackbox/Whitebox: Blackbox.

Functional/Performance: Functional.

Unit/Integration: Unit.

## Test Case 6

Purpose: To ensure that the user interface performs proper input validation and displays accurate error messages for invalid inputs.

Description:  
   - Open the application and navigate to the input section.
   - Attempt to submit the form with various types of invalid inputs to trigger validation checks.
   - Verify that the system responds appropriately to each invalid input scenario.

Inputs: 
   - (Professors): Enter a list of relevant topics to generate the question.
   - (Students): Enter answers for feedback.
   - Enter nothing for the prompt.

Expected Outputs: 
   - For an empty required field, the system should display an error message stating that the field is mandatory.

Normal/Abnormal/Boundary Case: Abnormal.

Blackbox/Whitebox: Blackbox.

Functional/Performance: Functional.

Unit/Integration: Unit.

## Test Case 7

Purpose: To ensure the accuracy of personalized suggestions provided by the model in the learning platform.

Description:  Evaluate the platform's ability to tailor suggestions based on the user's skill level and coding experience.

Inputs: Code snippets representing different difficulty levels.

Expected Outputs: The platform should provide personalized suggestions that align with the user's skill level.

Normal/Abnormal/Boundary Case: Normal case.

Blackbox/Whitebox: Blackbox.

Functional/Performance: Functional.

Unit/Integration: Integration.

## Test Case 8

Purpose: To verify that the platform effectively helps users prepare for technical interviews.

Description: Simulate a scenario where a user is preparing for a technical interview using the platform. Test the system's ability to provide relevant resources, guidance, and suggested solutions for common interview questions.

Inputs: Input a set of common technical interview questions into the platform.

Expected Outputs: The platform should provide personalized guidance and suggestions for solving the input technical interview questions.

Normal/Abnormal/Boundary Case: Normal case.

Blackbox/Whitebox: Blackbox.

Functional/Performance: Functional.

Unit/Integration: Integration.

## Test Case 9

Purpose: To validate the accuracy of personalized suggestions provided by the model.

Description: This test focuses on assessing how well the system's model can personalize feedback and suggestions based on the user's coding experience.

Inputs: Input a code snippet from a user with varying skill levels (e.g., beginner, intermediate, advanced).

Expected Outputs: The expected output is feedback and suggestions that are tailored to the specific skill level of the user. For example, a beginner might receive more fundamental guidance, while an advanced user should receive more nuanced suggestions.

Normal/Abnormal/Boundary Case: Normal case.

Blackbox/Whitebox: Blackbox.

Functional/Performance: Performance.

Unit/Integration: Unit.

## Test Case 10

Purpose: To validate the data collection process for the research paper.

Description: Simulate the data collection process to ensure that the system gathers relevant information for the research paper on user outcomes.

Inputs: Simulated user interactions with the platform.

Expected Outputs: Collected data includes user feedback, usage patterns, and responses to surveys.

Normal/Abnormal/Boundary Case: Normal case.

Blackbox/Whitebox: Blackbox.

Functional/Performance: Functional.

Unit/Integration: Unit.

# Test Case Matrix: summarizes the test case coverage (items 1, 6-9 in a tabular format)

# Part III. Test Case Matrix

| Test Case | Normal/Abnormal/Boundary | Blackbox/Whitebox | Functional/Performance  | Unit/Integration  |
|-----------|--------------------------|-------------------|-------------------------|-------------------|
| 1         | Normal                   | Blackbox          | Functional              | Unit              |
| 2         | Normal                   | Blackbox          | Functional              | Unit              |
| 3         | Normal                   | Blackbox          | Functional              | Integration       |
| 4         | Normal                   | Blackbox          | Functional              | Integration       |
| 5         | Boundary                 | Blackbox          | Functional              | Unit              |
| 6         | Abnormal                 | Blackbox          | Functional              | Unit              |
| 7         | Normal                   | Blackbox          | Functional              | Integration       |
| 8         | Normal                   | Blackbox          | Performance             | Unit              |
| 9         | Normal                   | Blackbox          | Performance             | Unit              |
| 10        | Normal                   | Blackbox          | Functional              | Unit              |



