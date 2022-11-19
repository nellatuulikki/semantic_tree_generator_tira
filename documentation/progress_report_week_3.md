## Progress report week 3

### What I have done this week?
  - Improved main classes
  - Created better parser which can now parse nested paranthesis clauses and split the proposition by main connective (either conjunction or disjunction)
  - Testing
  - Improved code quality with pylint
  - Created simple function for printing binary tree list
  - Didn't have time to get software running at Fly.io

### How the software has progressed 
  - The software is now working with little bit more complex conjunction and disjunction proposition clauses (Tested with (a∧b)v(b∧c) and av(b∧c) )
  - It has now better parsing algorithm
  - Started thinking about how the result will be presented

### Problems
  - No new major problems, pretty clear plan what to do next
  - Getting software into production failed -> fly launch failed.

### Questions
  - Any ideas about how to get the repo to CodeCov. (Or is there a way to avoid CodeCov? In ohjelmistotekniikka course we used "poetry run invoke coverage-report" for generating coverage reports)

### Next week
  - Manage to run software with even more complex disjunctive and conjunctive clauses
  - Add features for proposition that have 
  - Start writing docstrings for more complex functions
  - Improve binary tree result in UI
  - Fixing conjunction to work with 

### Hours used
  -  7-8 hours
