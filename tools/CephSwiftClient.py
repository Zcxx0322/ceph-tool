from tools.CephSwiftConfig import CephSwiftConfig


class CephSwiftClient:
    def __init__(self, config: CephSwiftConfig):
        self.config = config
