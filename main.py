import pygame 
import sys
import time

pygame.init()
screen=pygame.display.set_mode((1000,400))
pygame.display.set_caption("Linear Search visualizer")

WHITE=(255,255,255)
BLACK=(0,0,0)
GREEN=(0,255,0)
RED=(255,0,0)
BLUE=(0,0,255)
GRAY=(200,200,200)

font=pygame.font.Font(None,36)
input_font=pygame.font.Font(None,50)

def get_user_input(prompt):
    input_text = ""
    while True:
        screen.fill(WHITE)
        prompt_text = input_font.render(prompt, True, BLACK)
        screen.blit(prompt_text, (10, 10))
        user_text = input_font.render(input_text, True, BLACK)
        screen.blit(user_text, (20, 100))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return input_text
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

def draw_array(array, current=-1, target=-1, message=""):
    screen.fill(WHITE)
    block_width = 800 // len(array)
    for i, value in enumerate(array):
        x = i * block_width + 20
        y = 400 // 2 - 50

        color = GREEN if i == target else (RED if i == current else BLUE)
        pygame.draw.rect(screen, color, (x, y, block_width - 20, 50))

        text = font.render(str(value), True, BLACK)
        text_rect = text.get_rect(center=(x + (block_width - 20) // 2, y + 25))
        screen.blit(text, text_rect)

        if i == current:
            pygame.draw.polygon(screen, GRAY, [
                (x + (block_width - 20) // 2 - 10, y - 10),
                (x + (block_width - 20) // 2 + 10, y - 10),
                (x + (block_width - 20) // 2, y - 30)
            ])

    if message:
        msg_text = font.render(message, True, BLACK)
        screen.blit(msg_text, (800 // 2 - msg_text.get_width() // 2, 400 - 100))
    pygame.display.flip()

def draw_array1(array, low=-1, mid=-1, high=-1, message=""):
    screen.fill(WHITE)
    block_width = 800 // len(array)
    for i, value in enumerate(array):
        x = i * block_width + 20
        y = 400 // 2 - 50

        # Highlight low, mid, and high
        if i == mid:
            color = GREEN
        elif i == low:
            color = RED
        elif i == high:
            color = BLUE
        else:
            color = GRAY
        pygame.draw.rect(screen, color, (x, y, block_width - 20, 50))

        # Draw the value
        text = font.render(str(value), True, BLACK)
        text_rect = text.get_rect(center=(x + (block_width - 20) // 2, y + 25))
        screen.blit(text, text_rect)

    # Display the message
    if message:
        msg_text = font.render(message, True, BLACK)
        screen.blit(msg_text, (800 // 2 - msg_text.get_width() // 2, 400 - 100))
    pygame.display.flip()

def linear_search(arr,target):
    for i in range(len(arr)):
        draw_array(arr,current=i,message=f"checking index {i}")
        time.sleep(2)
        if arr[i]==target:
            draw_array(arr,current=i,target=i,message=f"Found at index {i}")
            return i
    draw_array(arr,message="element not found")
    return -1      

def binary_search(arr,target):
    l=0
    h=len(arr)-1

    while(l<=h):
        m=(l+h)//2
        draw_array1(array=arr,low=l,mid=m,high=h,message=f"checking at index {m}")
        time.sleep(1)
        if arr[m]==target:
            draw_array1(array=arr,low=l,mid=m,high=h,message=f"Found at index {m}")
            return m
        elif arr[m]<target:
            l=m+1
        else:
            h=m-1
    draw_array(f"Elememnt not found")
    return -1


def main():
    search_type = get_user_input("Enter 'L' for Linear Search, 'B' for Binary Search:")
    if search_type.lower()=='l':
        arr=get_user_input("Enter the array with values seprated by comma:")
        arr=list(map(int,arr.split(',')))
        target=get_user_input("Enter the target element:")
        try:
           target=int(target)
        except ValueError:
            return
        
        linear_search(arr,target)
    
    if search_type.lower()=='b':
        arr=get_user_input("Enter the array element in the sorted manner(sepreated by comma):")
        arr=list(map(int,arr.split(',')))
        target=get_user_input("Enter the target element:")
        try:
           target=int(target)
        except ValueError:
            return
        binary_search(arr,target)

    pygame.time.wait(3000)
    pygame.quit

if __name__=="__main__":
    main()