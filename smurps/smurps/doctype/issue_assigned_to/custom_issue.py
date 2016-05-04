import frappe
from frappe import msgprint
from frappe.exceptions import DoesNotExistError

def create_todo(owner, issue):
    count_in_db = frappe.db.count("ToDo",
                                  filters={'reference_name': issue,
                                           'reference_type': 'Issue',
                                           'description': issue,
                                           'owner': owner})
    if not count_in_db:
        todo = frappe.get_doc({"doctype":"ToDo",
                               "owner": owner,
                               "description": issue,
                               "reference_type": "Issue",
                               "reference_name": issue})
        todo.insert()
        return True
    elif count_in_db:
        todo = frappe.get_doc("ToDo", {"owner": owner,
                                       "description": issue,
                                       "reference_type": "Issue",
                                       "reference_name": issue})
        todo.update({"owner": owner,
                      "description": issue,
                      "reference_type": "Issue",
                      "reference_name": issue})

        return False

def get_group_names(name):
    try:
        return frappe.get_list("User Group",
                               fields = ['group_name'],
                               filters = {'group_name': name})
    except DoesNotExist:
        return None

def get_group_members(group_name):
    try:
        return frappe.get_list("User Group Member",
                               fields = ["user"],
                               filters= {'parent': group_name})
    except DoesNotExist:
        return None

@frappe.whitelist()
def get_custom_issue(issue):
    issue_from_db = frappe.get_doc("Issue", issue)
    assignees = frappe.get_list("Issue Assigned To",
				filters = {"parent": issue},
				fields=["user_or_group",
                        "user", "user_group"])
    if not issue_from_db.notify_via_email:
    	msgprint("From Py")
	for assignee in assignees:
            if assignee['user_or_group'] == 'User':
                create_todo(assignee["user"], issue)
                msgprint("Finished Creating TODOs for User")
            elif assignee['user_or_group'] == 'Group':
                group_names = get_group_names(assignee["user_group"])
                all_members = []
                for group_name in group_names:
                    if get_group_members(group_name['group_name']):
                        for member in get_group_members(group_name['group_name']):
                            all_members.append(member['user'])
                for member in set(all_members):
                    create_todo(member, issue)
                msgprint("Finished Creating TODOs for Group")
