class FileSearchController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def browse_directory(self):
        directory = filedialog.askdirectory()
        if directory:
            self.view.set_directory(directory)

    def start_search(self):
        directory = self.view.get_directory()
        pattern = self.view.get_pattern()
        if not directory or not pattern:
            self.view.show_warning("Please provide both directory and search pattern.")
            return
        
        results = self.model.search_files_and_folders(directory, pattern)
        self.view.show_results(results)
