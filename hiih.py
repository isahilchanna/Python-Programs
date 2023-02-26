def configPasswordEntry(self):
        """Gui Password Entry Configuration"""
        self.startButton.config(text=_("Open Sessions"), state=tkinter.NORMAL)
        self.chooseNsfButton.config(text=_("Select Directory of SOURCE nsf files"),
                                    state=tkinter.DISABLED)
        self.chooseDestButton.config(text=_("Select Directory of DESTINATION files"),
                                     state=tkinter.DISABLED)
        self.entryPassword.config(state=tkinter.NORMAL)
        self.formatTypeEML.config(state=tkinter.DISABLED)
        self.formatTypeMBOX.config(state=tkinter.DISABLED)
        self.formatTypePST.config(state=tkinter.DISABLED)
        self.optionsButton.config(state=tkinter.DISABLED)
configPasswordEntry(self)
