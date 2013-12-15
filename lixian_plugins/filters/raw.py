
from lixian_plugins.api import name_filter

@name_filter(protocol='raw')
def filter_by_raw_text(keyword, name):
	return keyword.lower() in name.lower()

