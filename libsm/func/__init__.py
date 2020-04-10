import xml.etree.ElementTree as ET
import os.path
from ..val import Val


class XML:
    def __init__(self, filename):
        tree = ET.parse(filename)
        self.__workspace = os.path.dirname(filename)
        self.__root = tree.getroot()

    def __call__(self, **kwargs):
        assert self.__root.tag == 'libsm'
        assert self.__root.attrib['type'] == 'equation'

        try:
            root = self.__root[0]
            assert root.tag == 'Not'
            root = root[0]
            assert root.tag == 'Equal'
            var, root = root[0], root[1]
            assert var.tag == 'var'
            assert var.attrib['name'] == 'S'
        except:
            raise 'feature not implemented'

        return self.eval(root, **kwargs)

    def eval(self, node, *args, **kwargs):
        values = [self.eval(child, **kwargs) for child in node]

        if node.tag == 'var':
            index = node.attrib['index']
            return args[index]

        if node.tag == 'sym':
            name = node.attrib['name']
            return kwargs[name]

        if node.tag == 'mod':
            path = node.attrib['path']
            index = node.attrib['index']

            if os.path.isabs(path) == False:
                path = os.path.join(self.__workspace, path)

            tree = ET.parse(path)
            root = tree.getroot()

            assert root.tag == 'libsm'
            assert root.attrib['type'] == 'module'

            node = root[index]

            return self.eval(node, *values, **kwargs)

        f = getattr(Val, node.tag)
        return f(*values)
