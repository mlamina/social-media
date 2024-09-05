# AI-Assisted Social Media Posts

This project uses [PR Pilot](https://www.pr-pilot.ai) to help create and manage social media content across various platforms.

## Project Structure

All content is organized in the following structure:

- `posts/README.md` - A table of contents for all posts
- `posts/<post-slug>/draft.md` - Source content for the social media post
- `posts/<post-slug>/<platform>/post.md` - Generated post for the platform
- `posts/<post-slug>/<platform>/meta.md` - Generated meta data for the post (e.g., tags, channels)

### Instructions

In [prompts/platform-instructions](prompts/platform-instructions), you will find instructions for generating posts 
on each platform. Adjust them as needed.

### How it Works

Generating a new post is easy

### 1. Create a new Draft

Create a new draft in seconds, by answering a few questions:

```shell
➜  social-media git:(main) pilot run draft

> What are you writing about: An AI-assisted Github template for rapid prototyping
> Who is this post for: Indie devs
> What is the key message: PR Pilot makes it super easy to quickly build and evaluate ideas
> What is the call to action: Use the template to build, ship and evaluate your own prototype
> Any additional notes: Template link: https://github.com/PR-Pilot-AI/rapid-prototyper
▸ List directory posts                                                                                                                                                                                                             
✎ Write content to posts/2-ai-assisted-github-template/draft.md                                                                                                                                                                   
✔ Draft new post: Rapid Prototyping with PR Pilot                                                                                                                                                                                  
● Push branch create-a-social-media                                                                                                                                                                                                
✔ Create PR #4 for branch create-a-social-media                                                                                                                                                                                    
                                                                                                                                                                                              
                                                                                        Draft Created                                                                                         
                                                                                                                                                                                              
  I have drafted the new post with the following content:                                                                                                                                     
                                                                                                                                                                                              
                                                                                                                                                                                              
   # Rapid Prototyping with PR Pilot                                                                                                                                                          
   An AI-assisted Github template for rapid prototyping                                                                                                                                       
                                                                                                                                                                                              
   ## Outline                                                                                                                                                                                 
   - Introduction to PR Pilot                                                                                                                                                                 
   - Benefits of using the template                                                                                                                                                           
   - How to get started                                                                                                                                                                       
   - Success stories from indie devs                                                                                                                                                          
   - Call to action: Use the template to build, ship and evaluate your own prototype                                                                                                          
                                                                                                                                                                                              
   ## Links / Resources                                                                                                                                                                       
   - [PR Pilot Rapid Prototyper Template](https://github.com/PR-Pilot-AI/rapid-prototyper)                                                                                                    
                                                                                                                                                                                              
                                                                                                                                                                                              
                                                                                 Suggestions for Improvement                                                                                  
                                                                                                                                                                                              
   1 Catchy Title: Ensure the title is engaging and relevant to your target audience. The current title is "Rapid Prototyping with PR Pilot," which is clear but could be more enticing.      
   2 Detailed Outline: Expand the bullet points in the outline to provide more detail. This will help in structuring the post better.                                                         
   3 Visuals: Consider adding visuals or examples to make the post more engaging. Screenshots or diagrams can help illustrate the benefits and usage of the template.                         
   4 Testimonials: Including quotes or testimonials from indie developers who have successfully used the template can add credibility and encourage others to try it.                         
   5 SEO Optimization: Use keywords that your target audience is likely to search for. This will help in making the post more discoverable.                                                   
                                                                                                                                                                                              
  Feel free to review and make any additional changes as needed!                                                                                                                              
                                                                                                                                                                                              
↻ Pull latest changes from create-a-social-media 
```

Use this as a starting point and add more detailed information about the post

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
≡ Read files: posts/1-story-behind-pr-pilot/draft.md                                                                                                                                                                              
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