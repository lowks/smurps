# -*- coding: utf-8 -*-
from __future__ import unicode_literals

app_name = "smurps"
app_title = "SMURPS"
app_publisher = "Strella Consulting Sdn Bhd"
app_description = "SMURPS"
app_icon = "octicon octicon-person"
app_color = "#2C82C9"
app_email = "smurps@strellagroup.com"
app_version = "0.0.1"
app_license = "MIT"

# Strella - Add Custom Fields
fixtures = ["Custom Field"]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/smurps/css/smurps.css"
# app_include_js = "/assets/smurps/js/smurps.js"

# include js, css files in header of web template
# web_include_css = "/assets/smurps/css/smurps.css"
# web_include_js = "/assets/smurps/js/smurps.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "smurps.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "smurps.install.before_install"
# after_install = "smurps.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "smurps.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"smurps.tasks.all"
# 	],
# 	"daily": [
# 		"smurps.tasks.daily"
# 	],
# 	"hourly": [
# 		"smurps.tasks.hourly"
# 	],
# 	"weekly": [
# 		"smurps.tasks.weekly"
# 	]
# 	"monthly": [
# 		"smurps.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "smurps.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "smurps.event.get_events"
# }

