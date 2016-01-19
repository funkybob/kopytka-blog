# Kopytka Blog

A simple blog addition for use with Kopytka CMS

## Installation

1. `pip install kopytka_blog`
2. Add to INSTALLED_APPS as 'kopytka_blog'
3. ```url(r'^blog/', include('kopytka_blog.urls', namespace='blog')),```
4. Migrate
5. Write templates `blog/post_list.html` and `blog/post_detail.html`

In the list view's context is `most_common`, a list of two-tuples of (tag, count) of the most common tags for the current filtered posts.

In the detail view's context is `most_like`, the 6 most similar (by number of matching tags) posts.

The number of `most_list` is controlled by the `most_like` property of the PostList view.
