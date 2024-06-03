if __name__ == "__main__":
    root = tk.Tk()
    model = FileSearchModel()
    view = FileSearchView(root, None)  # will set the controller
    controller = FileSearchController(model, view)
    view.controller = controller  # Set the controller for the view
    root.mainloop()
