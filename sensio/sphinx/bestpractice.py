from docutils import nodes
from docutils.parsers.rst import directives, Directive
from docutils.parsers.rst.directives.admonitions import BaseAdmonition

from sphinx import addnodes
from sphinx.locale import _

class bestpractice(nodes.admonition):
    pass

class BestPractice(BaseAdmonition):
    required_arguments = 0
    node_class = bestpractice

    def run(self):
        ret = super(BestPractice, self).run(self)
        if self.arguments:
            argnodes, msgs = self.state.inline_text(self.arguments[0],
                                                    self.lineno)
            para = nodes.paragraph()
            para += argnodes
            para += msgs
            ret[0].insert(1, para)

        return ret

def visit_bestpractice_node(self, node):
    self.body.append(self.starttag(node, 'div', CLASS=('admonition best-practice')))
    self.set_first_last(node)

def depart_bestpractice_node(self, node):
    self.body.append('</div>\n')

def setup(app):
    app.add_node(bestpractice, html=(visit_bestpractice_node, depart_bestpractice_node))
    app.add_directive('best-practice', BestPractice)
