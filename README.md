# Personal AI Coach
An personal LLM-powered coach which can run locally and improves itself over time.

[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)


## Table of Contents

- [About](#about)
    - [Example Usage](#example-usage)
- [Setup](#setup)
    - [Talking to the personal AI coach](#talking-to-the-personal-ai-coach)
    - [Updating the personal AI coach's context](#updating-the-personal-ai-coachs-context)
- [Contributing](#contributing)


## About
A combination of prompts and scripts for a personal AI coach which:
- You can load with the life context you want
- Knows you better after every conversation (via text files you can look at)
- Can run privately using locally-hosted models
- Has different 'modes' of coaching - and is easily extendible to add your own coaching styles and methods

#### Full context on why I built this and how it works [here](https://chrislovejoy.me/personal-ai-coach).


![AI-Performance-Coach-Diagram](https://github.com/user-attachments/assets/da9c5b73-274f-4c8d-b029-dbcae2552be3)


### Example Usage
https://github.com/user-attachments/assets/04ec1ccb-421d-46c9-aa75-a5ecbc2b0eb3


## Setup

### Talking to the personal AI coach
The easiest set up is to use [Obsidian.md](https://obsidian.md/) and the BMO plug-in. 

The steps required are shown here:

https://www.loom.com/share/77084c5106304dd88630e09c28342bfe


### Updating the personal AI coach's context
To update the coach context, you need to run the python script within the `scripts` directory.

For this, you need to:
i. install dependencies
ii. add required API keys
iii. run the life context update script


#### (i) Install dependencies
For example, you can install dependencies using the `venv` virtual environment manager as follows:

```sh
python -m venv venv
```

```sh
source venv/bin/activate
```

```sh
pip install -r requirements.txt
```


#### (ii) Add required API keys
Add your ANTHROPIC_API_KEY key to .env, as per .env.example



#### (iii) Run the Life Context update scripts

```sh
python scripts/update_life_context.py
```

This will update the [Life Context prompt](./Life%20Context%20Prompts/Personal%20AI%20Coach%20with%20Life%20Context.md) and save previous prompts in [archive](./Life%20Context%20Prompts/archive/).

You can also optionally set up a cron job to automate this process.

See this video for a full walk-through:

https://www.loom.com/share/f500cdd1119b4b5eb5be83635c1f5f01


## Contributing
All contributions welcome. If you'd like to contribute, please submit a PR.

In particular, the project could be improved by:
- adding more prompts for different coaching modes
- alternative ways to set this up (outside of Obsidian + BMO plug-in)
- alternative ways to provide context to the coach
