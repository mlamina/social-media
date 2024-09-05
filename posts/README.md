# Social Media Posts

Welcome to the Social Media Posts repository! This project uses PR Pilot to help create and manage social media content across various platforms.

## Project Structure

All content is organized in the following structure:

- `posts/README.md` - A table of contents for all posts
- `posts/<post-slug>/source.md` - Source content for the social media post
- `posts/<post-slug>/<platform>/post.md` - Generated post for the platform
- `posts/<post-slug>/<platform>/meta.md` - Generated meta data for the post (e.g., tags, channels)

### Post Structure
The structure of each post is as follows:

```markdown
# Meta

<platform-specific meta info like tags, channels, etc>

# Post

<generated post content>
```

### Platforms
Use the following identifiers for platforms:

- `x` - X
- `linkedin` - LinkedIn
- `facebook` - Facebook
- `devto` - DEV Community
- `reddit` - Reddit
- `tumblr` - Tumblr
- `discord` - Discord

## How to Use

1. **Source Content**: Add your source content in a markdown file located at `posts/<post-slug>/source.md`.
2. **Generate Posts**: Use PR Pilot to generate social media posts for the desired platforms.
3. **Review and Edit**: Review the generated posts and make any necessary edits.
4. **Publish**: Use the generated meta data to publish your posts on the respective platforms.

## Contributing

We welcome contributions! Please feel free to submit issues, fork the repository, and send pull requests.

## License

This project is licensed under the MIT License.