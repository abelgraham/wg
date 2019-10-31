import os
import json
import datetime
import mistune
from shutil import copyfile
from jinja2 import Template

BASE_DIR = os.getcwd()
CONTENT_DIR = os.path.join(BASE_DIR, 'content')
OUTPUT_DIR = os.path.join(BASE_DIR, 'docs')
STYLES_DIR = os.path.join(BASE_DIR, 'styles')
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
CONFIG = json.load(open(os.path.join(BASE_DIR, 'config.json')))

atts = {}
atts['year'] = datetime.datetime.now().year

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
    for att in CONFIG:
        atts[att] = CONFIG[att]
        
    for file in files:
        with open(os.path.join(CONTENT_DIR, file)) as f:
            atts['content'] = mistune.markdown(f.read())

        new_filename = os.path.splitext(file)[0] + '.html'
        
        open(os.path.join(OUTPUT_DIR, new_filename), 'w').write(TEMPLATE.render(atts))
        
def main():
    if not os.path.exists(OUTPUT_DIR):
        os.mkdir(OUTPUT_DIR)
        
    for entry in os.scandir(STYLES_DIR):
        if all([
                not entry.name.startswith('.'),
                entry.name.endswith('.css'),
                entry.is_file()
        ]):
            copyfile(os.path.join(STYLES_DIR, entry.name), os.path.join(OUTPUT_DIR, entry.name))
    
        
    generate_html(get_content())

import datetime
if __name__ == '__main__':
    main()

