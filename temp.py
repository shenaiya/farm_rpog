import tkinter
root=tkinter.Tk()
but=[0,1,2]
nadpis=["0","1","2"]
def pod(event):
    print(nadpis[xx])
for xx in but:
    but[xx]=tkinter.Button(root,text=nadpis[xx],width=10)
    but[xx].bind("<Button-1>",pod)
    but[xx].pack()
root.mainloop()