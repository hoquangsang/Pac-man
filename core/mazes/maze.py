# from config import *

# class Maze(object):
#     def __init__(self, mazepath):
#         self.homeoffset = (0, 0)
#         self.ghostNodeDeny = {UP:(), DOWN:(), LEFT:(), RIGHT:()}
#         self.portalPairs = {0:((0, 17), (27, 17))}
#         self.homeoffset = (11.5, 14)
#         self.homenodeconnectLeft = (12, 14)
#         self.homenodeconnectRight = (15, 14)
#         self.pacmanStart = (15, 26)
#         self.fruitStart = (9, 20)
#         self.ghostNodeDeny = {UP:((12, 14), (15, 14), (12, 26), (15, 26)), LEFT:(self.addOffset(2, 3),),
#                               RIGHT:(self.addOffset(2, 3),)}
        
        
#     def setPortalPairs(self, nodes):
#         for pair in list(self.portalPairs.values()):
#             nodes.setPortalPair(*pair)

#     def connectHomeNodes(self, nodes):
#         key = nodes.createHomeNodes(*self.homeoffset)
#         nodes.connectHomeNodes(key, self.homenodeconnectLeft, LEFT)
#         nodes.connectHomeNodes(key, self.homenodeconnectRight, RIGHT)

#     def addOffset(self, x, y):
#         return x+self.homeoffset[0], y+self.homeoffset[1]

#     def denyGhostsAccess(self, ghosts, nodes):
#         nodes.denyAccessList(*(self.addOffset(2, 3) + (LEFT, ghosts)))
#         nodes.denyAccessList(*(self.addOffset(2, 3) + (RIGHT, ghosts)))

#         for direction in list(self.ghostNodeDeny.keys()):
#             for values in self.ghostNodeDeny[direction]:
#                 nodes.denyAccessList(*(values + (direction, ghosts)))