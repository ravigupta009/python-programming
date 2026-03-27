# x = np.linspace(0, 10, 100)
# fig, ax = plt.subplots(figsize=(8, 6)),layout='constrained'
# ax.plot(x,np.exp(x), label='Exponential', color='blue')
# ax.set_xlabel('x')
# ax.


# import tkinter as tk

# root = tk.Tk()
# # root.title("Data Visualization")
# root.mainloop()


from tkinter import*
root = Tk()
Frame = Frame(root)
Frame.pack()
button = Button(Frame, text="ABC")
button.pack()
root.mainloop()
