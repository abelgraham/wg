import os
import json
import mistune
from shutil import copyfile
from jinja2 import Template

BASE_DIR = os.getcwd()
CONTENT_DIR = os.path.join(BASE_DIR, 'content')
OUTPUT_DIR = os.path.join(BASE_DIR, 'docs')
STYLES_DIR = os.path.join(BASE_DIR, 'styles')
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
CONFIG = json.load(open(os.path.join(BASE_DIR, 'config.json')))

with(open(os.path.join(TEMPLATE_DIR, 'layout.j2'))) as t:
    TEMPLATE = Template(t.read())

def get_content():
    for entry in os.scandir(CONTENT_DIR):
        if all([
            not entry.name.startswith('.'),
            entry.name.endswith('.md'),
            entry.is_file()
        ]):
            yield entry.name

def generate_html(files):
    for file in files:
        with open(os.path.join(CONTENT_DIR, file)) as f:
            content = mistune.markdown(f.read())
            
        new_filename = os.path.splitext(file)[0] + '.html'
        open(os.path.join(OUTPUT_DIR, new_filename), 'w').write(TEMPLATE.render(content=content, title=title, description=description, author=author, style=style, year=datetime.datetime.now().year))
        
def main():
    for att in CONFIG:
        globals()[att] = CONFIG[att]
    
    if not os.path.exists(OUTPUT_DIR):
        os.mkdir(OUTPUT_DIR)
        
    copyfile(os.path.join(STYLES_DIR, '%s.css' % (style)), os.path.join(OUTPUT_DIR, '%s.css' % (style)))
    copyfile(os.path.join(STYLES_DIR, 'spectre.min.css'), os.path.join(OUTPUT_DIR, 'spectre.min.css')) 
        
    generate_html(get_content())

import datetime
if __name__ == '__main__':
    main()

