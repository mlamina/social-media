# How I ended up building my own AI Dev Assistant from scratch

### Remember the first time you saw an LLM write code?

![Whoa](https://media1.tenor.com/m/wS9gJkWOuecAAAAC/coroca-keanu-reeves.gif)


### Yeah, me too 😲

When I learned **I could use this technology to build things**, I got pulled into an endless stream of ideas and side projects - The kind of excitement I hadn’t felt in years. I started experimenting with small scripts and had tasted blood. **I wanted more**.

## TLDR;
This is the story of how I built [PR Pilot](https://www.pr-pilot.ai), a virtual agent designed to assist development teams in their daily work by interacting with code repositories, wikis, chat platforms, and ticketing systems.

{% embed https://youtu.be/9ddxwwGtmfk %}

## **The Gap**
The LLM-based tools at the time (mid 2023?) were powerful, but not tailored to my workflow. Sure, ChatGPT could answer questions, and GitHub CoPilot could generate code. But **I needed something that was more integrated**, something that understood not just my code but also my tools and daily routines. Something I could control from the CLI and with config files. **Something that speaks my language**. 🖥️

## **The Turning Point**
In my day job, I am the technical lead for a team with 8 engineers and my little side project started to change how I viewed our workflows at the company. **I saw inefficiencies everywhere** — especially in large teams. Big orgs (we are but one of many teams) are **a maze of systems and isolated knowledge pools** that we all have to navigate to get our jobs done.

![This is fine](https://media1.tenor.com/m/MYZgsN2TDJAAAAAC/this-is.gif)

We have source control in one place, ticketing systems in another, CI/CD pipelines elsewhere, and internal knowledge **scattered across multiple platforms**. On top of that, **each team member has unique needs**. QA engineers, DevOps, junior devs, senior devs — everyone has their own way of working and different environments.


## **Shaping PR Pilot for Real-World Teams**
To be useful for the average team in my organization, **the ideal assistant would have to navigate these complexities seamlessly**. It couldn’t just generate code or assist with a single task — it had to connect the dots across different roles and workflows. It needed to act as **a bridge between siloed information and team-specific processes**.

![Math Meme](https://media1.tenor.com/m/hh6n7Ou_OnUAAAAC/math-hangover.gif)

This realization shaped PR Pilot into what it is today: **a tool for developers, QA engineers, DevOps, and everyone in between**. It’s designed to integrate with your specific workflows and help you get work done faster.

## Showcase: Agent-Driven Bug Reporting & Analysis

Let's look at a simple scenario from may daily work:
* We **collect** errors / stack traces in [Sentry](https://sentry.io)
* To get them fixed, bug **report** tickets need to be created
* The tickets need to have a specific **format**
* The QA team wants to be **notified on Slack**

### The Problem

This would involve **me juggling 3 different systems**, switching between apps and browser tabs, etc... Lots of context switching, remembering, copy/pasting information.

### The Solution
With the **[CLI](https://docs.pr-pilot.ai/user_guide.html#the-basics)**, I can run this scenario in a few minutes without leaving my terminal:

![Screen capture of terminal](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/1790riipanze9wsbjzol.png)

🤩 How amazing is that! Here is a breakdown:

#### Integrations
You can see that the agent interacted with Sentry, Github and Slack intuitively. PR Pilot [makes it super easy](https://docs.pr-pilot.ai/integrations.html) to connect the services and tools you use every day.

#### Knowledge
This part almost seems like magic:
![Knowledge retrieval](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/rg6nrqpk5srt1gug6hqz.png)
However, it knows where to look because:
1. I've [connected](https://docs.pr-pilot.ai/integrations.html#sentry) my Sentry account to PR Pilot
2. I [taught it](https://github.com/PR-Pilot-AI/pr-pilot/blob/b0eafe8b2e198b40216ce31062be682488dc98aa/.pilot-hints.md?plain=1#L7) which project that particular Github repo belongs to

It's as simple as dropping a Markdown file into your project and the agent will use that knowledge to run your tasks ([Learn More](https://docs.pr-pilot.ai/user_guide.html#give-hints-for-consistent-high-quality-results)).
#### Skills
You may have noticed the "Bug report skill":
![Invoking a skill](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/f3fkc9sk03xt9fs9e1bl.png)
PR Pilot also **makes it easy to codify repetitive workflows** by dropping a [YAML file](https://github.com/PR-Pilot-AI/pr-pilot/blob/b0eafe8b2e198b40216ce31062be682488dc98aa/.pilot-skills.yaml#L16) into your project. These skills are automatically picked up and used by the agent, so when I say `Report this as a bug`, it will automatically:
1. Read the relevant code
2. Create a new Github issue and write a report according to [my preferences for structure and formatting](https://github.com/PR-Pilot-AI/pr-pilot/blob/b0eafe8b2e198b40216ce31062be682488dc98aa/.pilot-skills.yaml#L26)
3. Post a message with a link to the issue into `#qa-team` on Slack

#### Knowledge + Skills + Integrations = Magic
Put it all together and what you get is an assistant that:

* Has **intuitive**, developer-friendly interfaces
* Is controlled **with config files** in my repositories
* Can autonomously navigate the services I use
* **Has domain knowledge** of my project(s) and organization(s)
* Can automate some of my daily work **efficiently and with confidence**

Most importantly, it is an assistant that I can trust to produce **predictable results and behavior**.

## **Why I Built PR Pilot**

![Hacker Meme](https://media1.tenor.com/m/54mjjpuowCgAAAAC/ninjala-jane.gif)

PR Pilot is now an AI-powered assistant that integrates with GitHub, ticketing systems, and chat platforms to **streamline workflows** and **reduce context switching**. My mission? To help developers **stay in the flow** by providing the right assistance at the right time with minimal friction. 🚀

### Learn More
Of course there's a lot more to discover:
* Check out our [demo repository](https://github.com/PR-Pilot-AI/demo?tab=readme-ov-file) with more show cases
* There's also a [REST API](https://docs.pr-pilot.ai/user_guide.html#using-the-rest-api) and a [Python SDK](https://docs.pr-pilot.ai/user_guide.html#python-sdk)
* You can build powerful, [dynamic prompts with Jinja templates](https://github.com/PR-Pilot-AI/pr-pilot-cli/tree/main/prompts)
* We have a comprehensive [User Guide](https://docs.pr-pilot.ai/user_guide.html)

### [Automate your own project!](https://www.pr-pilot.ai)

It’s been a wild ride from hacking together scripts to launching a full-fledged product. If you’ve ever felt bogged down by **manual tasks** or that **context switching** is killing your productivity, I’d love to hear your thoughts or ideas. Maybe PR Pilot can help make your dev life smoother too. 👇


