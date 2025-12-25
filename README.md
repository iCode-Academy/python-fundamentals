# Python Fundamentals Course

Welcome to the Python Fundamentals course! This repository contains exercises that will be automatically graded when you push your solutions.

## How It Works

1. Each module folder (m01, m02, etc.) contains exercise folders (e01, e02, etc.)
2. Each exercise has:
   - `main.py` - Your solution file with instructions
   - `tests/` - Test files that verify your solution
3. When you push changes, GitHub Actions automatically runs tests
4. Results are sent to the LMS

## Getting Started

1. Clone this repository:
   ```bash
   git clone <your-repo-url>
   cd <repo-name>
   ```

2. Start with Module 1, Exercise 1:
   ```bash
   cd m01-variables/e01-hello-world
   ```

3. Read the instructions in `main.py`

4. Write your solution

5. Test locally (optional):
   ```bash
   pip install pytest
   cd m01-variables/e01-hello-world
   pytest tests/ -v
   ```

6. Commit and push:
   ```bash
   git add .
   git commit -m "Complete e01-hello-world"
   git push
   ```

7. Check GitHub Actions for results

## Course Structure

```
m01-variables/
  e01-hello-world/    # Basic function creation
  e02-data-types/     # Working with numbers, strings, booleans

m02-control-flow/
  e01-conditions/     # if/elif/else statements
  e02-loops/          # for and while loops
```

## Tips

- Read the docstring in each `main.py` carefully
- Run tests locally before pushing to verify your solution
- Each function has example inputs/outputs - use them!
- Don't modify test files

## Need Help?

Check the LMS for course materials and ask questions in the discussion forum.
