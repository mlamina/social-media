# AI-Assisted Social Media Posts

This project uses [PR Pilot](https://www.pr-pilot.ai) to help create and manage social media content across various platforms.

## Project Structure

All content is organized in the following structure:

- `posts/README.md` - A table of contents for all posts
- `posts/<post-slug>/source.md` - Source content for the social media post
- `posts/<post-slug>/<platform>/post.md` - Generated post for the platform
- `posts/<post-slug>/<platform>/meta.md` - Generated meta data for the post (e.g., tags, channels)

### Instructions

In [prompts/platform-instructions](prompts/platform-instructions), you will find instructions for generating posts 
on each platform. Adjust them as needed.

### How it Works

Generating a new post is easy

### 1. Provide your content

Either use `pilot run draft-post` to create a new draft or provide the content 
directly in `posts/<post-slug>/source.md`.

### 2. Generate posts
PR Pilot will use your content to generate posts for the platforms you choose.

Run `pilot run generate-post` and select the post and platform you want to generate a post for:
```shell
➜  social-media git:(create-social-media) pilot run generate-post

✔ Running shell command: ls posts
[?] Select post: 
 > 1-story-behind-pr-pilot
   README.md

[?] Select platform: 
 > x
   linkedin
   facebook
   devto
   reddit
   tumblr
   discord

✔ Running shell command: cat prompts/platform-instructions/x.md
○ Check out PR branch create-social-media                                                                                                                                                                                          
≡ Read files: posts/1-story-behind-pr-pilot/source.md                                                                                                                                                                              
└─┐ Invoking skill: Write a social media post                                                                                                                                                                                      
  ✎ Write content to posts/1-story-behind-pr-pilot/x/post.md                                                                                                                                                                       
  ✔ Add X platform post for 'The Story Behind PR Pilot'                                                                                                                                                                            
  ✎ Write content to posts/1-story-behind-pr-pilot/x/meta.md                                                                                                                                                                       
  ! Connection was interrupted, reconnecting...                                                                                                                                                                                    
  ≡ Read files: posts/README.md                                                                                                                                                                                                    
┌─┘ Skill finished                                                                                                                                                                                                                 
✎ Write content to posts/1-story-behind-pr-pilot/x/post.md                                                                                                                                                                         
✔ Created post for X platform in posts/1-story-behind-pr-pilot/x/post.md                                                                                                                                                           
● Push branch create-social-media                                                                                                                                                                                                  
                                                                      
  Created post in posts/1-story-behind-pr-pilot/x/post.md for x.      
                                                                      
↻ Pull latest changes from create-social-media           
```

### 3. Review and Edit
Review the generated posts and make any necessary edits, then publish them on the respective platforms.

## Contributing

We welcome contributions! Please feel free to submit issues, fork the repository, and send pull requests.

## License

This project is licensed under the MIT License.