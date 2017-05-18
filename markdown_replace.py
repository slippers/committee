import markdown
from markdown.extensions import Extension
from markdown.preprocessors import Preprocessor

"""
needed to update the links in a mardown file post conversion to html.
perferable to do this while the file is already loaded via markdown.

this simple task could be mastered in other ways.
the alternative was to reload the file and search replace.

the best source for how to do this was the markdown source
it has many existing extentions that employ the preprocessor directive.

https://github.com/waylan/Python-Markdown

the biggest issues doing this was
* realizing that the extention needed its own module file
* understanding the various classes that needed extending
* passing configuration


# the name of the module is used in markdown extention parameter
import markdown_replace


markdown.markdownFromFile(
    input=input_file.md
    output=output_file.html
    extensions=['markdown_replace(search=.md, replace=.html)']
)


"""


class ReplaceExtension(Extension):
    def __init__(self, *args, **kwargs):
        self.config = {
            'search':['','search'],
            'replace':['', 'replace']
        }
        super(ReplaceExtension, self).__init__(*args, **kwargs)

    def extendMarkdown(self, md, md_globals):
        md.registerExtension(self)
        preprocessor = ReplacePreprocessor(self)
        preprocessor.config = self.getConfigs()
        md.preprocessors.add("replace",
                             preprocessor,
                             ">normalize_whitespace")


class ReplacePreprocessor(Preprocessor):

    def run(self, lines):
        search = self.config['search']
        replace =  self.config['replace']
        return [line.replace(search, replace) for line in lines]


def makeExtension(*args, **kwargs):
    return ReplaceExtension(*args, **kwargs)
