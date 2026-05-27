from collections import deque

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class MapTree:
    def __init__(self):
        self.map = {}

    def addtree(self, name, koren):
        self.map.setdefault(name, koren)
        print("Добавлено\n")

    def getTree(self, name):
        return self.map.get(name, None)
    
    def printNames(self):
        for key in self.map.keys():
            print(f"{key} ")

def preorder(root, result=None):
    if result is None:
        result = []
    if root:
        result.append(root.value)
        preorder(root.left, result)        
        preorder(root.right, result)

    return result

def inorder(root, result=None):
    if result is None:
        result = []
    if root:
        inorder(root.left, result)
        result.append(root.value)     
        inorder(root.right, result)

    return result

def postorder(root, result = None):
    if result is None:
        result = []
    if root:
        postorder(root.left, result)     
        postorder(root.right, result)
        result.append(root.value)
    return result

def check_symmetry(node=None):
    if node == None:
        return True
    return is_mirror(node.left, node.right)

def is_mirror(nodeleft, noderight):
    if nodeleft is None and noderight is None:
        return True
    elif nodeleft is None or noderight is None:
        return False
    
    return (nodeleft == noderight and is_mirror(nodeleft.left, noderight.right) and is_mirror(nodeleft.right, noderight.left))

def level_to_order(root):
    result = []
    if root is None:
        return result
    queue = deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result


if __name__ == "__main__":
    trees = MapTree()
    nametree = None
    A = True
    while A == True:
        print("Выберите, что хотите сделать с деревьями и их узлами")
        print(f"0. Выбрать текущее дерево (Сейчас выбрано дерево: {nametree})")
        print("1. Создать дерево")
        print("2. Добавить узел в существующее дерево")
        print("3. Проверить симметрию дерева")
        print("4. Вывести все названия деревьев")
        print("5. Провести прямой обход дерева и вывести его")
        print("6. Провести симметричный обход дерева и вывести его")
        print("7. Провести обратный обход дерева и вывести его")
        print("8. Сделать обход в ширину и вывести его")
        print("Все остальные значения - закончить работу с программой")
        vubor = input("")
        match vubor:
            case "0":
                print("Введите название дерева, с которым хотите работать")
                nametree = input("")
                if nametree not in trees.map.keys():
                    print("Такого дерева нет. Попробуйте еще раз")
                    nametree = None
                else:
                    print(f"Выбрано {nametree}")
            case "1":
                print("Введите название нового дерева")
                nametree = input("")
                print("Введите значение его корня")
                value = int(input(""))
                node = TreeNode(value)
                trees.addtree(nametree, node)

            case "2":
                if not nametree:
                    print("Введите название дерева")
                    nametree = input("")
                curr = trees.getTree(nametree)
                while curr != None:
                    print(f"Сейчас вы находитесь в узле со значением {curr.value}")
                    B = True
                    while B:
                        print("Введите в какое поддерево хотите добавить узел (l или r)")
                        v2 = input("")
                        assert curr != None
                        match v2:
                            case "l":
                                
                                if not curr.left:
                                    print("Мы дошли до свободного узла. Введите его значение")
                                    value = int(input(""))
                                    node = TreeNode(value)
                                    curr.left = node
                                    curr = None
                                else:
                                    curr = curr.left
                                B = False
                            case "r":
                                if not curr.right:
                                    print("Мы дошли до свободного узла. Введите его значение")
                                    value = int(input(""))
                                    node = TreeNode(value)
                                    curr.right = node
                                    curr = None
                                
                                else:
                                    curr = curr.right
                                B = False
                            case _:
                                print("Введите одно из двух значений. ОДНО ИЗ ДВУХ. Я многого не прошу")
                print("Добавлено")
                
                
            case "3":
                if not nametree:
                    print("Введите название дерева")
                    nametree = input("")
                koren = trees.getTree(nametree)
                print(check_symmetry(koren))

            case "4":
                trees.printNames()
            
            case "5":
                if not nametree:
                    print("Введите название дерева")
                    nametree = input("")
                koren = trees.getTree(nametree)
                print(preorder(koren))
            
            case "6":
                if not nametree:
                    print("Введите название дерева")
                    nametree = input("")
                koren = trees.getTree(nametree)
                print(inorder(koren))
            
            case "7":
                if not nametree:
                    print("Введите название дерева")
                    nametree = input("")
                koren = trees.getTree(nametree)
                print(postorder(koren))
            
            case "8":
                if not nametree:
                    print("Введите название дерева")
                    nametree = input("")
                koren = trees.getTree(nametree)
                print(level_to_order(koren))

            case _:
                print("Покедова")
                A = False
                
