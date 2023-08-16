from pathlib import Path

from happy_python import HappyLog, HappyConfigParser

from tools.CephSwiftConfig import CephSwiftConfig

conf_dir = Path(__file__).parent.parent / 'conf'
log_conf_file = conf_dir / 'log.ini'
app_conf_file = conf_dir / 'swift.ini'

hlog = HappyLog.get_instance(str(log_conf_file))

app_config = CephSwiftConfig()
HappyConfigParser.load(str(app_conf_file), app_config)
