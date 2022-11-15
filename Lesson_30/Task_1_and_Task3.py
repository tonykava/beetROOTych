import operator
from typing import Generic, TypeVar, List

from oop_tree import BinaryTree

T = TypeVar("T")


class Stack(Generic[T]):
    def __init__(self) -> None:
        self._container: List[T] = []

    @property
    def empty(self) -> bool:
        return not self._container  # not is true for empty container

    def push(self, item: T) -> None:
        self._container.append(item)

    def pop(self) -> T:
        return self._container.pop()  # LIFO

    def __repr__(self) -> str:
        return repr(self._container)


def build_parse_tree(math_exp: str) -> BinaryTree:
    tokens_list = []
    for i in math_exp:
        if i.isdigit() and tokens_list[-1].isdigit():
            tokens_list[-1] += i
        else:
            tokens_list.append(i)
    print(tokens_list)
    stack = Stack()
    tree: BinaryTree = BinaryTree('')
    stack.push(tree)
    current_tree = tree

    for i in tokens_list:
        if i == '(':
            current_tree.insert_left('')
            stack.push(current_tree)
            current_tree = current_tree.get_left_child()

        elif i in ['+', '-', '*', '/']:
            current_tree.set_root_val(i)
            current_tree.insert_right('')
            stack.push(current_tree)
            current_tree = current_tree.get_right_child()

        elif i == ')':
            current_tree = stack.pop()

        elif i not in ['+', '-', '*', '/', ')']:
            try:
                current_tree.set_root_val(int(i))
                parent = stack.pop()
                current_tree = parent

            except ValueError:
                raise ValueError("token '{}' is not a valid integer".format(i))

    return tree


def evaluate(parse_tree):
    operates = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}

    left_c = parse_tree.get_left_child()
    right_c = parse_tree.get_right_child()

    if left_c and right_c:
        fn = operates[parse_tree.get_root_val()]
        return fn(evaluate(left_c), evaluate(right_c))
    else:
        return parse_tree.get_root_val()

def print_exp(tree: BinaryTree) -> str:
    s_val = ""
    if tree.left_child:
        s_val = '(' + print_exp(tree.get_left_child())
        s_val += str(tree.get_root_val())
        s_val += print_exp(tree.get_right_child()) + ')'
    else:
        s_val += str(tree.get_root_val())
    return s_val



if __name__ == "__main__":
    pt: BinaryTree = build_parse_tree("((10+5)*3)")
    print(evaluate(pt))
    print()
    pt.pre_order()
    print()
    pt.post_order()
    print()
    pt.in_order()
    print("__")
    print(print_exp(pt))






