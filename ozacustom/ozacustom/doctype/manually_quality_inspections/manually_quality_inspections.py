# Copyright (c) 2024, sanpra and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class ManuallyQualityInspections(Document):
	@frappe.whitelist()
	def gettemp(self):
		rw_temp = frappe.get_doc("Quality Inspection Template", self.quality_inspection_template)	
		for j in rw_temp.get("custom_quality_inspection_item"):
			self.append("quality_inspection_item", {
				"min_outer_dia": j.min_outer_dia,
				"max_outer_dia": j.max_outer_dia,
				"ovality_max": j.ovality_max,
				"o_d_by_pi_tape": j.o_d_by_pi_tape,
				"out_of_seq_max": j.out_of_seq_max,
				"wall_thik_min": j.wall_thik_min,
				"wall_thik_max": j.wall_thik_max,
				"pipe_length": j.pipe_length,
			})
   
	@frappe.whitelist()
	def gett(self):
		rw_temp = frappe.get_doc("Longitudinal Reversion Template", self.longitudinal_reversion)	
		for j in rw_temp.get("longitudinal_reversion_item"):
			self.append("longitudinal_reversion_test", {
				"test_period": j.test_period,
				"initial_lenght": j.initial_lenght,
				"final_length": j.final_length,
				"reversion": j.reversion,
			})
   
	@frappe.whitelist()
	def mdn(self):
		rw_temp = frappe.get_doc("Internal Pressure test Template", self.internal_pressure_template)	
		for j in rw_temp.get("items"):
			self.append("internal_pressure_test", {
				"test": j.test,
				"no_of_sample": j.no_of_sample,
				"test_temp": j.test_temp,
				"induced_stress": j.induced_stress,
				"test_period": j.test_period,
				"calculate_test_pressure": j.calculate_test_pressure,
				"result": j.result,
			})
   
	@frappe.whitelist()
	def mocks(self):
		rw_temp = frappe.get_doc("Quality Other Test Template", self.quality_other_test_template)	
		for j in rw_temp.get("quality_other"):
			self.append("quality_other_test", {
				"carbon_black_content83": j.carbon_black_content83,
				"carbon_black_dispersion83": j.carbon_black_dispersion83,
				"melt_flow_index84": j.melt_flow_index84,
				"oxidation_induction_time85": j.oxidation_induction_time85,
				"density_test87": j.density_test87,
				"results": j.results,
				"elongation_at_break89": j.elongation_at_break89,
			})