from ast import NodeTransformer, copy_location, Call, Str, Attribute


class EncodeStrings(NodeTransformer):
    def visit_Str(self, node):
        return copy_location(
            Call(
                func=Attribute(attr='decode',
                               value=Str(s=node.s.encode('rot13'))),
                args=[Str(s='rot13')],
                keywords=(),
                starargs=None,
                kwargs=None
            ),
            node
        )
