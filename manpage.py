# -*- coding: utf-8 -*-

from distutils.core import Command

class install(Command):
    
    description = "install man pages"
    
    user_options = []
    
    def initialize_options(self):
        pass
    
    def finalize_options(self):
        pass
    
    def run(self):
        if not self.dry_run:
            pass
