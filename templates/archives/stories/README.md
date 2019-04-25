### Making a story

To create a story, you must create 3 data sources...

```
templates/archives/stories/STORY_SLUG.jinja2
templates/archives/stories/STORY_SLUG-teaser.jinja2
static/img/stories/STORY_SLUG-teaser.png
```

... and add an entry to the list ```STORIES``` in ```apps.archives.views```.
