import xml.etree.ElementTree as ET
import os.path
from ..val import Val


class XML:
    def __init__(self, filename, nosolve=None):
        tree = ET.parse(filename)
        self.__workspace = os.path.dirname(filename)
        self.__root = tree.getroot()
        self.__nosolve = nosolve

    def __call__(self, **kwargs):
        assert self.__root.tag == 'libsm'
        assert self.__root.attrib['type'] == 'equation'

        root = self.__root[0]

        if self.__nosolve:
            assert root.tag == 'Not'
            root = root[0]
            assert root.tag == 'Equal'
            var, root = root[0], root[1]
            assert var.tag == 'sym'

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

        val = Val

        if 'package' in node.attrib:
            val = __import__(node.attrib['package'])
            for v in node.attrib['package'].split('.')[1:]:
                val = getattr(val, v)
            val = val.Type

        f = getattr(val, node.tag)
        return f(*values)
