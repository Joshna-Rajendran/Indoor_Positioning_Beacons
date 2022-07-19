'''importing necessary modules'''
import cv2
import numpy as np 
'''defining a structure for node'''
class Node:
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        self.g = 0
        self.h = 0
        self.f = 0
    def __eq__(self, other):
        return self.position == other.position
''' fxn to resize image without losing aspect ratio'''
def resizeAndPad(img, size, padColor=0):
    h, w = img.shape[:2]
    sh, sw = size
    '''shrink or expand'''
    if h > sh or w > sw: 
        interp = cv2.INTER_AREA
    else: 
        interp = cv2.INTER_CUBIC
    aspect = w/h  
    '''scaling and pad sizing'''
    if aspect > 1: # horizontal image
        new_w = sw
        new_h = np.round(new_w/aspect).astype(int)
        pad_vert = (sh-new_h)/2
        pad_top, pad_bot = np.floor(pad_vert).astype(int), np.ceil(pad_vert).astype(int)
        pad_left, pad_right = 0, 0
    elif aspect < 1: # vertical image
        new_h = sh
        new_w = np.round(new_h*aspect).astype(int)
        pad_horz = (sw-new_w)/2
        pad_left, pad_right = np.floor(pad_horz).astype(int), np.ceil(pad_horz).astype(int)
        pad_top, pad_bot = 0, 0
    else: # square image
        new_h, new_w = sh, sw
        pad_left, pad_right, pad_top, pad_bot = 0, 0, 0, 0
    if len(img.shape)== 3 and not isinstance(padColor, (list, tuple, np.ndarray)): # color image but only one color provided
        padColor = [padColor]*3
    '''scale and pad'''
    scaled_img = cv2.resize(img, (new_w, new_h), interpolation=interp)
    scaled_img = cv2.copyMakeBorder(scaled_img, pad_top, pad_bot, pad_left, pad_right, borderType=cv2.BORDER_CONSTANT, value=padColor)
    return scaled_img
'''reversing the entire list to get path'''
def return_path(current_node):
    path =[]
    current = current_node
    while current is not None:
        path.append(current.position)
        current = current.parent
    path = path[::-1]
    return path
'''fxn to calculate movable neighbours, cost'''
def search(maze, cost, start, end):
    start_node = Node(None, tuple(start))
    start_node.g = start_node.h = start_node.f = 0
    end_node = Node(None, tuple(end))
    end_node.g = end_node.h = end_node.f = 0
    yet_to_visit_list = []  
    visited_list = [] 
    yet_to_visit_list.append(start_node)
    move  =  [[-1, 0 ], [ 0, -1], [ 1, 0 ],[ 0, 1 ]]
    no_rows,no_columns= np.shape(maze)
    while len(yet_to_visit_list) > 0:
        current_node = yet_to_visit_list[0]
        current_index = 0
        for index, item in enumerate(yet_to_visit_list):
            if item.f < current_node.f:
                current_node = item
                current_index = index
        yet_to_visit_list.pop(current_index)
        visited_list.append(current_node)
        if current_node == end_node:
            return return_path(current_node)
        children = []
        for new_position in move: 
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])
            if (node_position[0] > (no_rows - 1) or node_position[0] < 0 or node_position[1] > (no_columns -1) or node_position[1] < 0):
                continue
            if maze[node_position[0]][node_position[1]] != 0:
                continue
            new_node = Node(current_node, node_position)
            children.append(new_node)
        for child in children:
            if len([visited_child for visited_child in visited_list if visited_child == child]) > 0:
                continue
            child.g = current_node.g + cost
            child.h = (((child.position[0] - end_node.position[0]) ** 2) + ((child.position[1] - end_node.position[1]) ** 2)) 
            child.f = child.g + child.h
            if len([i for i in yet_to_visit_list if child == i and child.g > i.g]) > 0:
                continue
            yet_to_visit_list.append(child)

if __name__=="__main__":
    start=[241,457]
    end=[57,464]
    #start=[548,454]
    #end=[300,250]
    #3start=[748,378]
    #end=[386,445]
    #433 rows,1274columns  sooo1274,433]
    cost = 1
    copy_img = cv2.imread(r"C:\Users\SUSMITHA\AppData\Local\Programs\Python\Python39\square.jpg",1)
    gray_img = cv2.cvtColor(copy_img,cv2.COLOR_RGB2GRAY)
    gray_img = cv2.GaussianBlur(gray_img, (3,3), 0)
    ret,thresh1 = cv2.threshold(gray_img,210,255,cv2.THRESH_BINARY_INV)
    height=thresh1.shape[1]
    width=thresh1.shape[0]
    
    '''finding value of pixel at each coordinate'''
    maze=[]
    for y in range(width):
        n=[]
        for x in range(height):
            n.append(int(thresh1[y,x]/255))
        maze.append(n)
    ma=[[maze[j][i] for j in range(len(maze))] for i in range(len(maze[0]))]
    print(maze[start[0]][start[1]],maze[end[0]][end[1]])
    path=[]
    path=search(ma,cost,start,end)
    if((maze[start[0]][start[1]]==1) or (maze[end[0]][end[1]]==1)):
        cv2.circle(copy_img, tuple(start), 5,(0,0,255),-1)
        cv2.circle(copy_img, tuple(end), 5,(0,0,255),-1)
        print("No possible path")
    elif not path:
        cv2.circle(copy_img, tuple(start), 5,(0,0,255),-1)
        cv2.circle(copy_img, tuple(end), 5,(0,0,255),-1)
        print("No possible path")
    else:
        pa=[[path[j][i] for j in range(len(path))] for i in range(len(path[0]))]
        pa.pop()
        cv2.circle(copy_img, tuple(start), 5,(0,0,255),-1)
        cv2.circle(copy_img, tuple(end), 5,(0,0,255),-1)
        for i in range(len(path)-1):
            cv2.line(copy_img,path[i],path[i+1],(255,0,0),3)
        cv2.imshow("result",copy_img)
        cv2.imwrite("result.jpg",copy_img)
        cv2.waitKey(0)
        #c_img=resizeAndPad(copy_img,(1090,3170),0)
        #img = cv2.imread(r"C:\Users\SUSMITHA\AppData\Local\Programs\Python\Python39\final.jpg",1)
        #img[787:1877,175:3345]=c_img
        #cv2.imwrite("fiehih.jpg",img)
