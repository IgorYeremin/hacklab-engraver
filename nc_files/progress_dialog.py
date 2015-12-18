import gtk, threading

class ProgressDialog():
  def run(self):
    self.dlg = gtk.Dialog("Gmask Streamer")
    self.pbar = gtk.ProgressBar()
    self.dlg.vbox.pack_start(self.pbar)
    self.pbar.show()
    self.dlg.run()
  
  def update(self,fraction):
    self.pbar.set_fraction(fraction)


