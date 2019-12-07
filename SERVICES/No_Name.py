class check:
    def __init__(self,args):
        self.args = args

    def clear(self,text=False):
        return self.args.replace('@','').replace('None','').replace('http','').format(text) if text else self.args.replace('@','').replace('None','').replace('http','')
