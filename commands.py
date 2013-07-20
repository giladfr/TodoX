import sublime, sublime_plugin

class ExampleCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.insert(edit, 0, "Hello, World!")


class ToggleDoneCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		for region in self.view.sel():
			if region.empty(): 
				# empty region only, means that no selection was marked
				line = self.view.full_line(region)
				line_str = self.view.substr(line).strip("\n")
				if line_str.startswith("x"): # already marked as done
					self.view.erase(edit, sublime.Region(line.begin(),line.begin() + 2 ))
				else:
					# remove line
					self.view.erase(edit,line)
					# add at the end with "x"
					self.view.insert(edit, self.view.size(),"\nx " + line_str)









