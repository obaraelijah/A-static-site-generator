import os
import markdown2
from jinja2 import Environment, FileSystemLoader

def generate_site(input_folder, output_folder):
    """
    Creating the Jinja2 environment
    """
    env = Environment(loader=FileSystemLoader('templates'))
    """
    Getting list of all files in the input folder
    """
    files = os.listdir(input_folder)
    
    """Iterating through the list of files
    """
    for file in files:
        if file.endswidth('.md'):
            name = os.path.splitext(file)[0] 
            
    """converting the md to HTML 
    """
    html = markdown2.markdown_path(input_folder + '/' + file)

    """Choosing templates to use
    """
    if name == "index":
        template = env.get_template('home.html')
    elif name == "about":
        template = env.get_template('about.html')
    else:
        template = env.get_template('article.html')
    """REndering templates with thei respective titles
    """
    output = template.render(title = name, content = html)
    
    """writing outcome to the output folder
    """
    with open(output_folder + '/' + name + '.html', 'w') as f:
        f.write(output)
        
