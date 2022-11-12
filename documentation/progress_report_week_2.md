## Progress report week 2

### What I have done this week?
  - Started the software and created main classes
  - Creating UI
  - Setting up tests
  - Tried to get CodeCov up and running
  - Tried to get software into production at Fly.io with Tietokantasovellus instructions.

### How the software has progressed 
  - I have started main classes
  - Tried to get UI and other parts of software functioning with each other
  - Testing software with one proposition symbol (p), simple disjunctive clause (p∨s) and empty ""

### Problems
  - CodeCov setting up failed -> CodeCov doesn't find my repository.
  - Getting software into production failed -> fly launch failed.

### Questions
  - Any ideas about how to get the repo to CodeCov. (Or is there a way to avoid CodeCov? In ohjelmistotekniikka course we used "poetry run invoke coverage-report" for generating coverage reports)
  - Difficulties running tests and software with same directory structure. Now app.py and routes.py are out of src directory. Is this ok, or should these files be under src directory?

### Next week
  - Trying to get CodeCov working and software running at Fly.io
  - Manage to run software with more complex disjunctive and conjunctive clauses

### Hours used
  -  10
