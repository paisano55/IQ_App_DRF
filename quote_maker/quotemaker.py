class QuoteMaker:
    def get_request(self,req):
        self.price = req['price']
        self.usage = req['usage']
        self.ssd_cap = req['ssd_cap']
        self.nvme = req['nvme']
        self.hdd_cap = req['hdd_cap']
        self.inter_gpu = req['inter_gpu']
    def make_quote(self):

        return 0