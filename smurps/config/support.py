from __future__ import unicode_literals
from frappe import _

def get_data():
	return [		
		{
			"label": _("Users"),
			"icon": "icon-group",
			"items": [
				{
					"type": "doctype",
					"name": "User Group",
					"description": _("Assignment and Notification Groups")
				}
			]
		},
	]
