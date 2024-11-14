# Tolbot
## Introduction
This is a simple program for creating Test Object List (TOL) documentation directly from up to 3 gerrit commits.

Program is written in Python and it follows modern design principles ex. dependency injection so it's completely modular and anyone is free to add their own modules such as a different server or a different export document type (ex. Excel). Or you can even change your filter for how test descriptions will be differentiated from the rest of the code.

It is meant for new projects with new tests in the codebase. If it is used for project which alternate legacy test codebase it will not work properly.

### How it works
Tolbot uses following steps for operating
- Connects to Gerrit through REST API for fetching `git diff`
- It filters through code additions and stores only test descriptions (test name, verifications and triggers) and ignores any other changes
- This test data alongside team name, project name and some statistics are then exported to a MS Word file

I will be refering to [**test descriptions**]  as commented lines of code which are describing the tests

Before using Tolbot make sure you have a commit which follows these rules for test descriptions:
- Test description data line starts with `%%!` exact characters (`%` character is used for commenting in programming language Erlang)
- Test descriptions start and end with minimally 20 `-` characters (`-------------------`)
  
  **IMPORTANT**: Any added code which consists `%%!-------------------` will result in undefined behaviour. This is because this string of chars indicate beginning and the end of a test description.
  Ex. `%%-------------------` is ok and will not create bugs if it doesn't represent beginning or the end of a test description.
  
- First line of test description is a test name ex. `%%! tc_custom_test`
- The rest of the test description is sectioned with the following keywords: `PREREQUISITES`, `UPDATE PRECONDITIONS`, `PURPOSE`, `TRIGGER`, `VERIFICATION`
### Example of a correctly written test description
```
%%!-------------------------------------------------------------------------------------------------
%%! tc_example_test_case
%%!
%%! PURPOSE:         - Lorem ipsum dolor sit amet, consectetur adipiscing elit.
%%!                    Aenean est lorem, laoreet non rutrum at, pretium at nisi. Aliquam
%%!                    maximus tellus id consequat
%%!
%%! PREREQUISITES:   - In eros augue
%%!                  - porttitor eu viverra vel, ullamcorper sed metus
%%!                    Integer malesuada
%%!                  - Morbi eget nunc tortor
%%!
%%! TRIGGER 1:       - Nullam eu sapien sagittis,
%%!
%%! VERIFICATION 1a: - Vestibulum cursus mi: 
%%!                    -Nunc ligula nisl, suscipit vel sollicitudin at, accumsan rutrum mi. 1
%%!                    -Nunc ligula nisl, suscipit vel sollicitudin at, accumsan rutrum mi. 2
%%!                    -Nunc ligula nisl, suscipit vel sollicitudin at, accumsan rutrum mi. 3
%%!                    -Nunc ligula nisl, suscipit vel sollicitudin at, accumsan rutrum mi. 4
%%!
%%! VERIFICATION 1b: - Donec luctus interdum orci:
%%!                    -Nulla semper tincidunt risus.
%%!                    -Maecenas molestie mi sapien, ut vehicula tortor iaculis et.
%%!                     Curabitur at facilisis nisi. Nullam sit amet sollicitudin mauris.
%%!
%%! VERIFICATION 2:  - Sed fringilla odio et accumsan lobortis:
%%!                    -A) Maecenas malesuada
%%!                    -B) Maecenas malesuada
%%!                    -c) Maecenas malesuada
%%!-------------------------------------------------------------------------------------------------
```
## How to use
1. Configure the servers which will be used in the `servers_config.json` ex. _https://gerrit-review.googlesource.com/_
2. Start Tolbot.exe
3. Log in with your credentials.
4. Fill necessary informations such as team name, project name, Change ID and Revision ID (patchset hash value) for up to 3 branches/repo-s
5. Press export when ready, TOL is saved with name "<project_name>_TOL.docx"
## Example of a generated TOL MS Word file
![Example 1](https://github.com/user-attachments/assets/13591d1d-ca88-443a-a855-4f731afe0042)
![Example 2](https://github.com/user-attachments/assets/53a9e989-af21-4b38-99a3-dc7f0841d015)


