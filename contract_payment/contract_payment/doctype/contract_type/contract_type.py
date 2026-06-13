# Copyright (c) 2021, Ibrahim Morghim and contributors
# For license information, please see license.txt

from erpnext.setup.doctype.item_group import item_group
import frappe
from frappe.model.document import Document
from frappe import _
class ContractType(Document):

	@frappe.whitelist()
	def create_item(self):
		"""
		this method for create item
		"""
	
		item = frappe.get_doc({
					'doctype': 'Item',
					'item_name': self.name1,
					'item_code': self.name1,
					'item_group': self.get_contract_item_group(),
					'is_purchase_item': True,
					'is_sales_item': True,
					'is_stock_item': False,
					'include_item_in_manufacturing': False
				})
		item.item_defaults = []
		item.insert(ignore_permissions=True)

		self.db_set("item", item.name)
		frappe.msgprint(_('item created successfuly'))


	def get_contract_item_group(self):
		"""
		Get contract item group.
		"""
		item_groups = frappe.get_value(
			"Item Group",
			filters={"is_contract_group": 1},
			pluck="name"
		)
		if not item_groups:
			frappe.throw(
				_("Please create an Item Group with 'Is Contract Group' checked.")
			)
		
		return item_groups