# Social Media Content Pipeline

This project uses [PR Pilot](https://www.pr-pilot.ai) to implement a social media content pipeline. From an initial draft, a DEV.to article is generated, which contains the main post. Secondary posts are generated for other platforms and linked back to the original post.

```mermaid
graph TD;
    A[Draft] -->|Generate| B[DEV.to Blog Post];
    B -->|Review| C[Reviewed Post];
    C -->|Publish| D[Published Post];
    D -->|Distribute| E[Secondary Posts];
    E -->|Link Back| B;
```


## Pipeline Stages

The pipeline has five stages:
1. **Draft** - Drafts are stored as Markdown files in the `drafts` directory.
2. **Generate** - From the draft, a DEV.to blog post is generated.
3. **Review** - The generated post is reviewed and edited before being published.
4. **Publish** - The post is published on the DEV Community platform.
5. **Distribute** - Secondary posts for other platforms are generated, linked to the original post, and published.

## Project Structure

All content is organized in the following structure:
- `drafts/` - Contains all draft content
- `posts/` - Contains all generated posts
- `dist/` - Contains all distributed posts
- `prompts/` - Contains prompts for generating posts

## How to Use

Use the pilot commands in this directory to run the pipeline stages.

```shell
➜  social-media git:(create-a-draft-for-a) ✗ pilot run
Usage: pilot run [OPTIONS] COMMAND [ARGS]...

  🚀 Run a saved command.

  Create new commands by using the --save-command flag when running a task.

Options:
  --help  Show this message and exit.

Commands:
  draft          Answer a few questions and create a new draft
  generate-post  Generate a post for a specific platform
```

### 1 - Draft
PR Pilot will [ask you a series of questions](./prompts/draft-post.md.jinja2) to draft a new social media post. The draft will be saved in the [drafts/](./drafts) directory.

Run: `pilot run draft`

![Draft](./generate_draft.gif)

### 2 - Generate

Based on your draft, PR Pilot will generate a DEV.to blog post. The post will be saved in the [posts/](./posts) directory.