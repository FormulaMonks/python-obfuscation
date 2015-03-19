from ast import NodeTransformer


class Scrambler(NodeTransformer):
    HEADER = '# scrambled'

    def __init__(self, scramble=True):
        self.do_scramble = scramble

    def visit(self, node):
        node_out = super(Scrambler, self).visit(node)
        if hasattr(node_out, 'body') and isinstance(node_out.body, list):
            if self.do_scramble:
                node_out.body = self.scramble(node_out.body)
            else:
                node_out.body = self.unscramble(node_out.body)
        return node_out

    def scramble(self, items):
        return self._step2(self._step1(items[:]))

    def unscramble(self, items):
        return self._step1(self._step2(items[:]))

    def _step1(self, items):
        i = 0
        length = len(items)
        while (i + 1) < length:
            items[i], items[i + 1] = items[i + 1], items[i]
            i += 2
        return items

    def _step2(self, items):
        length = len(items)
        if length % 2 == 0:
            items[:length / 2], items[length / 2:] = \
                items[length / 2:], items[:length / 2]
        else:
            items[:(length - 1) / 2], items[(length + 1) / 2:] = \
                items[(length + 1) / 2:], items[:(length - 1) / 2]
        return items
