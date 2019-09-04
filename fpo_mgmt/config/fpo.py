from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("FPO Management"),
      "icon": "octicon octicon-repo",
			"items": [
				{
					"type": "doctype",
					"name": "Cost of Cultivation",
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "FPO Board of Director",
					"onboard": 1,
				},
				{
					"type": "doctype",
					"name": "Harvest Data",
					"onboard": 1,
				},
        
        {
					"type": "doctype",
					"name": "Production",
					"onboard": 1,
				},
        
        {
					"type": "doctype",
					"name": "Production Details",
					"onboard": 1,
				},
        
        {
					"type": "doctype",
					"name": "FPO CEO",
					"onboard": 1,
				},
        
        {
					"type": "doctype",
					"name": "FPO External Investments",
					"onboard": 1,
				},
        
        {
					"type": "doctype",
					"name": "FPO External Loan",
					"onboard": 1,
				},
        
        {
					"type": "doctype",
					"name": "FPO Meeting",
					"onboard": 1,
				},
        
        {
					"type": "doctype",
					"name": "FPO Member",
					"onboard": 1,
				},
        
        {
					"type": "doctype",
					"name": "FPO Training",
					"onboard": 1,
				},
        
        {
					"type": "doctype",
					"name": "FPO Member Crop",
					"onboard": 1,
				},
        
        {
					"type": "doctype",
					"name": "FPO Member Land",
					"onboard": 1,
				},
        
        {
					"type": "doctype",
					"name": "FPO Registration Details",
					"onboard": 1,
				}

			]