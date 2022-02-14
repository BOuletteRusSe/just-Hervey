
from tkinter import *
from autoit import win_move


async def Banane(ctx):
    
    await ctx.reply('Vous avez ouvert une popup de banane sur le pc du créateur du bot pour 10 secondes lol.\nhttps://i.ibb.co/L9y6vJF/banana.png')
     
    window = Tk() 
    window.overrideredirect(True)
    window.wm_attributes("-topmost", True)
    window.wm_attributes('-transparentcolor', 'white')
    window.title('main banana')
    posx = 0
    posy = 0
    window.geometry("700x700")
    
    canvas = Canvas(window, highlightthickness=0, width=700, height=700, bg='white')
    canvas.pack()
    
    image = PhotoImage(file=r'assets\images\banana.png')
    canvas.create_image(350, 350, image=image)

    for i in range(1000):
        
        try: window.update()
        except: break
        
        try: win_move('main banana', posx, posy)
        except: continue
        
        posx += 1
        posy += 1
        
    window.destroy()
            