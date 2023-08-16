from happy_python import HappyConfigBase


class CephSwiftConfig(HappyConfigBase):
    def __init__(self):
        super().__init__()

        self.section = 'main'
        self.swift = ''
        self.base_url = ''
        self.uid = ''
        self.secret_key = ''

    def __str__(self) -> str:
        return "%s -A %s -U %s -K '%s' " % (self.swift,
                                            self.base_url,
                                            self.uid,
                                            self.secret_key)
