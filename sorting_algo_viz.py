import pygame

import random
pygame.init()
color=255,255,255
new_color=255,100,0
bg_color=255,0,255
black=0,0,0
green = (0, 255, 0)
blue = (0, 0, 128)
screen=pygame.display.set_mode((800,600))

running=True
font = pygame.font.Font('freesansbold.ttf', 20)

pygame.display.set_caption("Sorting Algorithm Visualization")
text = font.render('space - Reset | i-insertionSort| b-Bubble sort | m=merge sort|q-quick sort', True, green, blue)
text_rect=text.get_rect()
text_rect.center=(400,40)
screen.blit(text,text_rect)
pygame.display.update()

def generate_list(n,min_value,max_value):
      lst=[]

      for i in range(n):
              lst.append(random.randint(min_value,max_value))
       
      return lst

def search(list, platform):
    for i in range(len(list)):
        if list[i] == platform:
            return True
    return False

def draw_list(lst,marked):
      x=50
      y=0
      pygame.draw.rect(screen,bg_color,(50,y,800,600))
      
      for i in range(len(lst)):
            num=lst[i]
            if search(marked,i):
              pygame.draw.rect(screen,new_color,(x,600-num,10,num))
            else :     
                 pygame.draw.rect(screen,color,(x,600-num,10,num))
            x=x+12
      pygame.display.update()

def bubble_sort(lst):
      marked=[]
      for i in range(len(lst)-1):
             marked.append(i)         
             for j in range(i+1,len(lst)):
                  if lst[j]<lst[i]:
                        lst[i],lst[j]=lst[j],lst[i]
                  marked.append(j)
                  draw_list(lst,marked)
                  marked.remove(j)
                  clock.tick(50)
                    
def insertion_sort(lst):
  
  marked=[]
  for i in range(1,len(lst)):
        key=lst[i]
        j=i-1
        marked.append(i)   
        while j>=0 and lst[j]>key :
              lst[j+1]=lst[j]
              j=j-1
              marked.append(j)
              draw_list(lst,marked)
              clock.tick(30)
              marked.remove(j)

        lst[j+1]=key

def merge_sort(lst,start,end):
      
  if start<end:
      mid=(start+end)//2
      merge_sort(lst,start,mid)
      merge_sort(lst,mid+1,end)
      marked=[]
      for iti2 in range(start,end+1):
            marked.append(iti2)

        

      clock.tick(10)

      i=start
      j=mid+1
      k=0
      new_arr=[]
      

      while i<=mid and j<=end:
            
            if lst[i]>lst[j]:
                  new_arr.append(lst[j])
                  j=j+1
            else :
                  new_arr.append(lst[i])
                  i=i+1
            
      while i<=mid:
            new_arr.append(lst[i])
            i=i+1
          
      while j<=end:
            new_arr.append(lst[j])
            j=j+1
      k=0
      for iti in range(start,end+1):
            lst[iti]=new_arr[k]
            k+=1
      
      draw_list(lst,marked)
      clock.tick(5)

def partition(lst,start,end):

      pivot=lst[end]
      i=start-1
      marked=[]
      marked.append(end)
      for j in range(start,end):
            if lst[j]<=pivot:
                  i=i+1
                  lst[i],lst[j]=lst[j],lst[i]
            draw_list(lst,marked)
            clock.tick(30)
      lst[i+1],lst[end]=lst[end],lst[i+1]
      return i+1

def quick_sort(lst,start,end):
      if start<end:
            marked=[]
            pi=partition(lst,start,end)
            quick_sort(lst,start,pi-1)
            quick_sort(lst,pi+1,end)
            for i in range (start,end):
                  marked.append(i)
            draw_list(lst,marked)
            clock.tick(10)
           
clock=pygame.time.Clock()
screen.fill((255,0,255))

while running:
  clock.tick(60)
  empty=[]
  screen.blit(text,text_rect)
  pygame.display.update()

  for event in pygame.event.get():
    if event.type==pygame.QUIT:
      running=False
    if event.type != pygame.KEYDOWN:
          continue
    if event.key==pygame.K_SPACE:
          n=random.randint(0,60)
          lst=generate_list(n,0,500)
          draw_list(lst,empty)          
    elif event.key==pygame.K_i:
          insertion_sort(lst)
    elif event.key==pygame.K_b:
          bubble_sort(lst)
    elif event.key==pygame.K_m:
          merge_sort(lst,0,len(lst)-1)
    elif event.key==pygame.K_q:
              quick_sort(lst,0,len(lst)-1)
    

      
  pygame.display.update()
