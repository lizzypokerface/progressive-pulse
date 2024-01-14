# progressive-pulse
Progressive Pulse: News for the People  
A Weekly Digest of Socialist News and Insights

# Pre-requisites
Before you start, make sure you have the following installed on your system:
- Ruby (version 3.1.4)
- RubyGems (Ruby's package manager)
- GCC (GNU Compiler Collection)
- Make (build automation tool)

These tools are essential for setting up and running a Jekyll site.

# Setting Up for Local Development
Follow these steps to set up your local environment for developing the Jekyll static site:

1. **Install Bundler:**
   Navigate to the project root directory in your terminal and run:
   ```bash
   gem install bundler
   ```
   Bundler manages Ruby gem dependencies, making it easier to handle Jekyll's requirements.

2. **Install Dependencies:**
   Install the required gems specified in your Gemfile:
   ```bash
   bundle install
   ```
   This command installs all the necessary dependencies for your Jekyll site.

3. **Build the Site:**
   Compile your site's source code into static files:
   ```bash
   jekyll build
   ```
   This step generates the static site files in the `_site` directory.

4. **Serve the Site Locally:**
   Start a local server to view your Jekyll site:
   ```bash
   bundle exec jekyll serve
   ```
   This allows you to view your site in a web browser at `http://localhost:4000`.

### Accessing the Site Locally
Once you've successfully run the above commands, you can access your Jekyll site by navigating to `http://localhost:4000` in your web browser. This local server will reflect any changes you make to the site as you develop.

# Development Guidelines

The primary focus of development is the addition of new posts. To contribute, follow these steps to add new entries to the `_posts` folder:

### Creating a New Post

1. **Create a New Branch:**
   - Create a branch for your new post using the format: `feat/<new-post-title>`.
   - Example: `git checkout -b feat/my-awesome-post`.

2. **Navigate to the _posts Directory:**
   - In your local repository, navigate to the `_posts` directory.

3. **Create a New Markdown File:**
   - File name format: `YYYY-MM-DD-NAME-OF-POST.markdown`.
   - Replace `YYYY-MM-DD` with the date of your post and `NAME-OF-POST` with the title of your post.
   - Example: `2024-01-01-my-awesome-post.markdown`.

4. **Add YAML Frontmatter:**
   - At the top of the file, include the following frontmatter:
     ```yaml
     layout: post
     title: "Your Post Title"
     date: YYYY-MM-DD HH:MM:SS +/-TTTT
     categories: category1 category2
     ```
   - Replace placeholders with your post's details.

5. **Add Content:**
   - Follow the provided template to add your content after the YAML frontmatter.
   - Remove any categories for which there are no articles.
   - Feel free to add new categories as needed.
   - Create timestamps with the following shell command: `$ date +'%Y-%m-%d %H:%M:%S %z'`
   - Below is an example content template:

     ```markdown
     ---
     layout: post
     title:  "✊ Progressive News | 01 Jan 2023"
     date:   2024-01-01 03:58:56 +0800
     categories: weekly news
     ---

     ### International
     - [Article](https://website.com/)

     ### China
     - [Article](https://website.com/)

     ### East Asia
     - [Article](https://website.com/)

     ...additional categories...

     ### Other
     - [Article](https://website.com/)
     ```

6. **Commit Your Changes:**
   - Use the commit message template: `feat: YYYY-MM-DD-NAME-OF-POST added`.
   - Example: `git commit -m "feat: 2024-01-01-my-awesome-post added"`.

7. **Create a Pull Request:**
   - Push your branch to GitHub and create a pull request for your proposed changes.
   - Example: `git push origin feat/my-awesome-post`.

8. **Pull Request Review:**
   - Your pull request will be reviewed and, if approved, merged into the main branch.

## Best Practices for Contributors
- Ensure your post is relevant and adheres to the blog's theme.
- Double-check for spelling and grammatical errors.
- Make sure all links are working and relevant to the content.

By following these guidelines, you can contribute effectively to the 'Progressive Pulse' blog and help maintain a high standard of content.


# Troubleshooting
1. [Resolving Ruby Installation Error '__rvm_make -j12' on ARM64 Macs)](https://github.com/rvm/rvm/issues/5379)
