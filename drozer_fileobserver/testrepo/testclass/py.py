from drozer.modules import common, Module
from drozer.modules.common import loader



class Classloading(Module, loader.ClassLoader, common.FileSystem):
	name = "File Observer"
	description = ""
	examples = ""
	author = [""]
	date = ""
	license = ""
	path = ["b4sic", "fileobserver"]

	def add_arguments(self, parser):
		parser.add_argument("path", default=None, help="Enter path to be observed. Must be world-accessible.")
	
	def observeFolder(self, foldername):
		self.stdout.write("Observing folder %s\n" % foldername)
		clt = self.new(self.classloadtest, foldername)
		self.observerlist.append(clt)
		
		for somefile in self.listFiles(foldername):
			if self.isDirectory(foldername + "/" + somefile[:-1]) == True:
				self.observeFolder(foldername + "/" + somefile[:-1])
	
	
	def execute(self, arguments):
		targetfolder = arguments.path

		# Class load the new class - this will be automatically compiled
		self.classloadtest = self.loadClass("../MyFileObserver.apk", "MyFileObserver",relative_to=__file__)


		self.observerlist = []

		self.observeFolder(targetfolder)

		for clt in self.observerlist:
			clt.startWatching()

		while True:
			for clt in self.observerlist:
				curres = clt.getLog()
				if str(curres) != "":
					self.stdout.write(str(curres))
	
				clt.clearLog()

