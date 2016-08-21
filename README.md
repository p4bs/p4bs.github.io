# Takeovertheword.com (p4bs.github.io)

This website was built using [Jekyll](https://jekyllrb.com) and [GitHub Pages](https://pages.github.com/).
Jekyll is a static site generator that creates static websites ready to be served by any modern web server.

Instructions:
  - To preview the content generated while developing you can use Jekyll's own web server.
    You can run it by using the command `jekyll serve`
  - Build the site by running the command `jekyll build`
  - When you build the website, the generated files are found in the folder `_site`
    - The current version of on `takeovertheword.com` is therefore found under `_site`

For more information on Jekyll see these articles:
  - Installation: https://jekyllrb.com/docs/installation/
  - Basic usage: http://jekyllrb.com/docs/usage/
  - Deployment methods: http://jekyllrb.com/docs/deployment-methods/
  
### CNAME domain
The `CNAME` file is used by Github when using a CNAME domain with your Github Page.
Thus the file is only necessary when hosting this page on Github.
Please check with your web server setup for how to setup CNAME domains.

### Facebook Sharing
Since Facebook's OpenGraph tags are meta tags in the header of a page I created a "dummy" site for each 
word with the correct meta data. When sharing a word through the web site you are actually sharing 
one of these dummy sites. These pages can be found under the folder `word_pages`. 

### Copy
All copy can be found in the main HTML file `_layouts/default.html`. The folder `text/` was used for development purposes, it can be ignored.
