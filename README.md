# 📢 AI-Assisted Social Media Posts

This project uses [PR Pilot](https://www.pr-pilot.ai) to help create and manage social media content across various platforms.

## 🗂️ Project Structure

All content is organized in the following structure:

- `posts/README.md` - A table of contents for all posts
- `posts/<post-slug>/draft.md` - Source content for the social media post
- `posts/<post-slug>/<platform>/post.md` - Generated post for the platform
- `posts/<post-slug>/<platform>/meta.md` - Generated meta data for the post (e.g., tags, channels)

In [prompts/platform-instructions](prompts/platform-instructions), you will find instructions for generating posts 
on each platform. Adjust them as needed.

## ⚙️ How it Works

Generating a new post is easy

### 1️⃣ Create a new Draft

Create a new draft in seconds, by answering a few questions:

```shell
➜  social-media git:(main) pilot run draft 
    
> What are you writing about: An AI-assisted Github template for rapid prototyping
> Who is this post for: Indie Devs
> What is the key message: PR Pilot makes it super easy to quickly build and evaluate ideas
> What is the call to action: Use the template to build, ship and evaluate your own prototype
> Any additional notes: Template link: https://github.com/PR-Pilot-AI/rapid-prototyper
▸ List directory posts                                                                                                                                                                                                             
✎ Write content to posts/2-ai-assisted-github-template/draft.md                                                                                                                                                                    
✔ Draft initial outline for AI-assisted Github template post                                                                                                                                                                       
● Push branch create-a-social-media-2                                                                                                                                                                                              
✔ Create PR #6 for branch create-a-social-media-2                                                                                                                                                                                  
                                                                                                                                                   
  Here are some suggestions to help you fill out the initial draft:                                                                                
                                                                                                                                                   
   1 Introduction                                                                                                                                  
      • Add a meme about the struggles of manual prototyping to highlight the ease PR Pilot brings.                                                
      • Provide a brief history of PR Pilot to support the message of innovation.                                                                  
   2 Key Features                                                                                                                                  
      • Include a screenshot of the Github template in action to visually support the features.                                                    
      • Add a testimonial from an indie dev who has used the template to emphasize its effectiveness.                                              
   3 Benefits                                                                                                                                      
      • Provide a detailed comparison between traditional prototyping methods and using PR Pilot to support the message of saving time and         
        effort.                                                                                                                                    
      • Include a case study or example project that was successfully built using the template.                                                    
   4 How to Get Started                                                                                                                            
      • Add a video tutorial link to help users understand the setup process.                                                                      
      • Provide a checklist of prerequisites needed before starting with the template.                                                             
   5 Links / Resources                                                                                                                             
      • Include a link to the PR Pilot documentation to help the reader understand the tool better.                                                
      • Add a link to a community forum or Discord channel where users can ask questions and share their experiences.                              
                                                                                                                                                   
  These suggestions should help you create a comprehensive and engaging post.                                                                      
                                                                                                                                                   
↻ Pull latest changes from create-a-social-media-2   
```

Use this as a starting point and add more detailed information about the post

### 2️⃣ Generate posts for different platforms
Once you have a decent draft, PR Pilot will use your content to generate posts for the platforms you choose.

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

### 3️⃣ Review and Edit
Review the generated posts and make any necessary edits, then publish them on the respective platforms.

## 🤝 Contributing

We welcome contributions! Please feel free to submit issues, fork the repository, and send pull requests.

## 📜 License

This project is licensed under the MIT License.