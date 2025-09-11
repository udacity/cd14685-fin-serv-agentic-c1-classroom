# Purpose of This Repo

This repo is meant to be used to keep things organized during content development and act as the source of truth for all projects and exercises related to this course.

## Folder Structure

### Lesson Folder

This repo contains a folder for each `lesson` and one `project` folder.

Example
```
lesson-1-hello
lesson-2-world
lesson-3-foo
lesson-4-bar
project
```

Each `lesson` folder is named using the naming convention of `lesson-#-name-of-lesson`.

Example
```
lesson-1-hello
```

Four lesson folders have been provided as a template; However, you may need to add more or possibly use less than four depending on what is needed.

If you require an additional lesson folder, you can make a copy of the folder and paste it into the root directory.

### Exercises Folder

Each `lesson` folder contains an `exercises` folder. This `exercises` folder should contain all files and instructions necessary for the exercises along with the solution. The solutions for these exercises will be shared with students. See the `README` in the `exercises` folder for information about folder structure.

### Project Folder

The `project` folder should contain all files and instructions necessary for setup. If possible, a set of instructions should be provided for both Udacity workspaces and a way to work locally (for both MacOS and Windows OS). At a minimum, one set of instructions should be provided. A `README` template has been provided in the project folder. This template layout should be used to write your README.

## Vocareum OpenAI Client Configuration

All exercise files in this repository use the Vocareum-specific OpenAI client configuration to ensure they run correctly in the Udacity classroom environment.

### Required Configuration

Exercise notebooks use the following OpenAI client setup:

```python
# Setup OpenAI client for Vocareum environment
client = OpenAI(
    base_url="https://openai.vocareum.com/v1",
    api_key=os.getenv("OPENAI_API_KEY")
)
```

### Key Requirements
- All exercise notebooks include the `base_url="https://openai.vocareum.com/v1"` parameter
- API keys are loaded from environment variables using `os.getenv("OPENAI_API_KEY")`
- The API key should start with `voc-` for Vocareum environments
- Proper error handling is included for missing API keys

### Helper Function for Projects

For project work, you can use the helper function provided in the project starter code:
```python
from src import create_vocareum_openai_client

# Create client with proper Vocareum configuration
client = create_vocareum_openai_client()
```
