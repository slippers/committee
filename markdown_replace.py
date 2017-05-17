import pdb
import markdown
from markdown.extensions import Extension
from markdown.preprocessors import Preprocessor


# https://ana-balica.github.io/2013/07/16/custom-python-markdown-extension/
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


