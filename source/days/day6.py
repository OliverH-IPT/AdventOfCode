#part 1 / part 2 mixed

class OrbitTree:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.hasParent = False

    def __eq__(self, other): 
        return self.name == other.name

    def __str__(self):
        return "Orbiter, name = " + self.name + ", has Parent = " + str(self.hasParent)

    def setParent(self, parent):
        self.hasParent = True
        self.parent = parent

    def findDepthTraversal(self, depth):
        res = depth
        for child in self.children:
            res += child.findDepthTraversal(depth + 1)
    
        return res

    def findOrbiterTraversal(self, name):
        # check node
        if self.name == name:
            return True, self

        # recursion into children
        for child in self.children:
            found, orbiter = child.findOrbiterTraversal(name)
            if found is True:
                # cancel when found
                return found, orbiter
        
        # didn't find it in children
        return False, None

    def getPathToRoot(self):
        res = []
        cur = self
        while cur.hasParent == True:
            cur = cur.parent
            res.append(cur)
        
        res.reverse()
        return res

def createOrbitTreeItem(name, parent):
    treeItem = OrbitTree(name)
    treeItem.setParent(parent)
    parent.children.append(treeItem)
    return treeItem

def findDirectOrbiters(current, orbitPairs):
    indices = []
    for index, orbitPair in reversed(list(enumerate(orbitPairs))):
        if orbitPair[0] == current:
            # add them from last to first to enable deletion after tree item creation
            indices.append(index)

    return indices

def setupOrbitTreeInt(orbitPairs, currentRoot):
    children = []
    # Find direct orbiters
    directOrbiterIndices = findDirectOrbiters(currentRoot.name, orbitPairs)

    # create tree items, add to children and remove entries from orbitPairs
    for oi in directOrbiterIndices:
        children.append(createOrbitTreeItem(orbitPairs.pop(oi)[1], currentRoot))

    # recursion
    for child in children:
        setupOrbitTreeInt(orbitPairs, child)


def setupOrbitTree(orbitPairs):
    root = OrbitTree("COM")
    setupOrbitTreeInt(orbitPairs, root)
    return root

def getLastCommonOrbit(myOrbits, santasOrbits):
    minLen = min([len(myOrbits), len(santasOrbits)])
    
    last = None
    for i in range(0, minLen):
        cur = myOrbits[i]
        if cur != santasOrbits[i]:
            return last, i

        last = cur
    
    return last

def getMinimumOrbitalTransfers(root):

    FoundMe, me = root.findOrbiterTraversal("YOU")
    if FoundMe is False:
        print("Did not find me :(")
    
    myOrbits = me.getPathToRoot()

    FoundSanta, santa = root.findOrbiterTraversal("SAN")
    if FoundSanta is False:
        print("Did not find Santa :(")
    
    santasOrbits = santa.getPathToRoot()

    lco, index = getLastCommonOrbit(myOrbits, santasOrbits)
     
    meToLco = len(myOrbits)-index
    santaToLco = len(santasOrbits)-index
    return meToLco + santaToLco

