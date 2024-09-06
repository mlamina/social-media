# Mastering PR Descriptions: Make Your PRs Stand Out

## TL;DR
Learn how to generate beautiful and comprehensive PR descriptions effortlessly with PR Pilot in minutes.

## Introduction

Are you too lazy to write **comprehensive and beautiful PR descriptions**? 😅 You're not alone! Good PR descriptions are crucial for effective collaboration and project management. But they can be time-consuming and tedious to write. Enter **[PR Pilot](https://www.pr-pilot.ai)** – your new best friend for creating consistent, clear, and beautiful PR descriptions effortlessly.

## Benefits of Using Generative AI for PR Descriptions

**Consistency**: Ensures that all your PR descriptions follow a consistent format by storing the instructions as part of your code.

**Time-saving**: No more spending hours crafting the perfect PR description. PR Pilot does it for you in seconds!

**Customizable**: Use our customizable [prompt template](https://github.com/PR-Pilot-AI/core/blob/main/prompts/generate-pr-description.md.jinja2) to tailor PR descriptions to your project's specific needs.

## What it will look like

Here is a [real-life example](https://github.com/PR-Pilot-AI/pr-pilot/pull/210):

![Image description](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/tvdwrdj98u0q8avofwdq.png)

## How it Works
It's dead simple. All you do is run `pilot run pr-description` and:
1. The agent asks you for the PR number
2. It will read the PR description, comments, commits and code changes
3. It will generate a new PR description based on your preferences

{% collapsible summary %}
### Prompt Template
```markdown
I've made some changes and opened a new PR: #{{ env('PR_NUMBER') }}.

I need a PR title and a description that summarizes these changes in short, concise bullet points.
The PR description will also be used as merge commit message, so it should be clear and informative.

Use the following guidelines:

## PR Title
- Start with a verb in the imperative mood (e.g., "Add", "Fix", "Update").
- Put an emoji at the beginning that reflects the nature of the changes

## PR Body

- At the very top, provide short paragraph summarizing the changes and their impact.
- Below, list the changes made in bullet points.
- Use bold text instead of sections/sub-sections to separate the bullet points into topics
- There should be no more than 3-4 topics
- Use the present tense and the active voice.
- Be specific - Include names, paths, identifiers, names, versions, etc
- Where possible, make file names/paths clickable using Markdown links. Use this format for the URL: `https://github.com/<github_project>/blob/<pr_branch>/<file_path>`


# Your task
Edit PR #{{ env('PR_NUMBER') }} title and description to reflect the changes made in this PR.
Respond only with a link to the PR.
```
{% endcollapsible %}

## How to Get Started

Getting started with PR Pilot is a breeze! Follow these simple steps:

1. **Install the CLI** via Homebrew

```bash
brew tap pr-pilot-ai/homebrew-tap
brew install pr-pilot-cli
```

2. **Grab the prompt**: Download the [prompt template](https://github.com/PR-Pilot-AI/core/blob/main/prompts/generate-pr-description.md.jinja2) from our core repo
   {% embed https://asciinema.org/a/675042 %}
3. **Customize the template**: Adjust the downloaded prompt template to suit your project's needs.
4. **Run the prompt**: Generate a PR description with a single command: `pilot run pr-description`.
   {% embed https://asciinema.org/a/675043 %}

## Links / Resources

- [PR Pilot User Guide](https://docs.pr-pilot.ai/user_guide.html)
- [PR Pilot Demo Repo](https://github.com/PR-Pilot-AI/demo)

## Call-to-Action

Ready to transform your PR descriptions? 🚀 Give PR Pilot a try today and experience the difference! Share your experiences and tips in the comments below. Let's make PR descriptions beautiful together! 💬✨
