# Personal AI Coach
An LLM-powered coach which can run locally and improves itself over time.

[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat-square)](https://github.com/RichardLitt/standard-readme)


<!-- TODO: add gif / loom showing use -->


## Table of Contents

- [About](#about)
- [Setup](#setup)
- [How To Contribute](#how-to-contribute)


## About
A combination of prompts and scripts for a personal AI coach which:
- You can load with the life context you want
- Knows you better after every conversation (via text files you can look at)
- Can run privately using locally-hosted models
- Has different 'modes' of coaching - and is easily extendible to add your own coaching styles and methods


[TODO: add map diagram here]


Full context on how I built this as a side project [here](https://chrislovejoy.me/personal-ai-coach.)


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
iii. (optional) set up a cron job to automatically update your coach 


### (i) Install dependencies
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


### (ii) Add required API keys
Add your ANTHROPIC_API_KEY key to .env, as per .env.example



### (iii) (optional) set up a cron job to automatically update your coach 

TODO



## How To Contribute


would love contributions to:
- prompts around coaching - different coaching modes 
- alternative ways to implement this (outside Obsidian + BMO plug-in)
- ways to give the model more context



TODO: add details




<!-- TODO: consider adding the relevant Obsidian vault setup/config files -->
