from tkinter import*
import cv2
import numpy as np
#books available dict in library
books_available = {
    "Federal supplement 800 series":(645,318),
    "Federal supplement 100 series":(620,134),
    "FR 200 series":(602,370),
    "FR 600 series":(579,24),
    "SALES TAX CASES vol - 80s":(559,520),
    "DIRECT TAXES REPORTER YEAR -2000s":(539,402),
    "Income Tax case law  2000 s series":(516,430),
    "ALL INDIA REPORTER - allahabad AP":(496,113),
    "AIR BOMBAY CALCULTTA":(470,200),
    "AMERICAN LAW REPORTS - ANNOTATED 100 SERIES":(452,200),
    "ALR 2D LATER CASE SERVICE 40-100 SERIES":(423,495),
    "THE DIGEST 20-30 SERIES":(400,303),
    "HARVARD LAW REVIEW VOL 50S":(374,222),
    "LAW REPORTS OF  THE COMMON WEALTH - 1988 -YEAR":(400,303),
    "LABOR CASES 90 SERIES":(333,321),
    "AM JUR PROOF OF FACTS 3D 20 SERIES":(302,400),
    "EXCISE LAW TIMES 2002 YEAR":(288,50),
    "COMPANY CASES  VOL 180 SERIES":(260,57),
    "TAX CASES VOL 50 SERIES":(248,319),
    "CURRENT TAX REPORTER VOL 170 SERIES":(218,301),
    "ALL INDIA REPORTER 1981":(24,532),
    "ALL INDIA REPORTER 2008 VOL 95 – BOMBAY SECTION":(45,514),
    "SCALE VOL 1 – 1998":(66,369),
    "MADRAS LAW JOURNAL VOL 1 1991":(85,254),
    "CRIMES VOL 4 1998,G.RAMASWAMY":(103,204),
    "CONSUMER PROTECTION REPORTER VOL 1 2013":(128,364),
    "SERVICES LAW REPORTER VOL 65 1990(2)":(145,532),
    "CURRENT CENTRAL LEGISTLATION VOL 38 2012":(167,473),
    "SALES TAX CASES VOL 31 1973":(184,425),
    "VAT SERVICES AND TAX CASES VOL 44 2011":(207,192),  
  
   
}

class Node:
    def __init__(self, parent=None, position=None):
        self.parent = parent
        self.position = position
        self.g = 0
        self.h = 0
        self.f = 0
    def __eq__(self, other):
        return self.position == other.position
    
def return_path(current_node):
    path =[]
    current = current_node
    while current is not None:
        path.append(current.position)
        current = current.parent
    path = path[::-1]
    return path

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
            #print(child.position[0],child.position[1])
root = Tk()
root.geometry('500x500')#creating a window for ui
root.title("BOOKS")
#adding labels to ui
label_0 = Label(root, text="SEARCH BOOKS",width=20,font=("bold", 20))
label_0.place(x=90,y=53)
label_1 = Label(root, text="ENTER BOOK NAME",width=20,font=("bold", 10))
label_1.place(x=80,y=130)
label_2 = Label(root, text="BOOK STATUS: ",width=20,font=("bold", 10))
label_2.place(x=80,y=250)
#dropdown menu display
def show():
    label.config( text = "map is being generated..."+str(books_available[clicked.get()] ))
 

if __name__=="__main__":
       clicked = StringVar()
       clicked.set( "PLEASE SELECT A BOOK FROM THE LIST" )#default
       lb = OptionMenu( root , clicked , *books_available )#adding books dict to list
       lb.place(x=240,y=130)
       Button(root, text='SUBMIT',width=20,bg='brown',fg='white',command=show).place(x=180,y=200)
       label = Label( root , text = " " )#label to display result
       label.place(x=100,y=270)
       root.mainloop()
         #b2
    #end=[505,549]
    #start=[431,272]
    #start=[100,490]
    #start=[600,560]
    #start=[169,410]
    #------------
       #start=[645,318]#-1st
    #start=[620,134]-2nd
    #start=[423,495]- 6R
    #start=[400,303]#- 6L
    #start=[374,222]#- 7R
    #start=[400,303]#- 7L
    #start=[333,321]#- 8R
    #start=[302,400]#- 8L
    #start=[288,50]#- 9R
    #start=[260,57]#- 9L
       start=[184,425]#- 10R
    #start=[218,301]#- 10L
    #___________
    
       end=[502,570]
    #end=[320,568]
    #end=[155,567]
    #__________
       cost=1
       img = cv2.imread(r"C:\Users\merli\OneDrive\Desktop\mini project\final.jpg",1)
       cropped_img=img[789:1867,153:3340]
       copy_img=cv2.resize(cropped_img,(700,700))
       cv2.imwrite("sq.jpg",copy_img)
       gray_img = cv2.cvtColor(copy_img,cv2.COLOR_RGB2GRAY)
       gray_img = cv2.GaussianBlur(gray_img, (3,3), 0)
       ret,thresh1 = cv2.threshold(gray_img,230,255,cv2.THRESH_BINARY_INV)
       height=thresh1.shape[1]
       width=thresh1.shape[0]
       maze=[]
       for y in range(width):
           n=[]
           for x in range(height):
               n.append(int(thresh1[y,x]/255))
           maze.append(n)
       ma=[[maze[j][i] for j in range(len(maze))] for i in range(len(maze[0]))]
       path=[]
       path=search(ma,cost,start,end)
       if((copy_img[tuple(start)][0]==1 or copy_img[tuple(start)][1]==1 or copy_img[tuple(start)][2]==1 )or (copy_img[tuple(end)][0]==1 or copy_img[tuple(end)][1]==1 or copy_img[tuple(end)][2]==1)):
           print("No possible path")
       elif not path:
           cv2.circle(copy_img, tuple(start), 5,(0,0,255),-1)
           cv2.circle(copy_img, tuple(end), 5,(0,0,255),-1)
           cv2.imshow("result",copy_img)
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
            
