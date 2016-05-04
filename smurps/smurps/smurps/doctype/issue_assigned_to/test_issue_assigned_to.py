import ipdb; ipdb.set_trace()
import frappe
from unittest import TestCase
from mock import Mock, patch, call
from frappe.exceptions import DoesNotExistError

from smurps.smurps.doctype.issue_assigned_to.issue_assigned_to import (create_todo,
                                                                       get_group_names,
                                                                       get_group_members)


class TestCustomIssue(TestCase):

    @patch('smurps.smurps.doctype.issue_assigned_to.issue_assigned_to.frappe.db.count')
    @patch('smurps.smurps.doctype.issue_assigned_to.issue_assigned_to.frappe.get_doc')
    def test_create_todo_for_existing_issue(self, mock_get_doc, mock_count):

        """Test create_todo function for existing record"""

        def count_side_effect(*args, **kwargs):
            if kwargs['filters'] == {'description': 'mock_description',
                                     'reference_type': 'Issue',
                                     'reference_name': 'mock_description',
                                     'owner': "Administrator"}:
                return 10
            else:
                return 0

        mock_count.side_effect = count_side_effect
        result = create_todo("Administrator", 'mock_description')
        self.assertEqual(mock_get_doc.return_value.update.call_args,
                         call({'owner': 'Administrator',
                               'reference_name': 'mock_description',
                               'reference_type': 'Issue',
                               'description': 'mock_description'}))
        self.assertFalse(result)

    @patch('smurps.smurps.doctype.issue_assigned_to.issue_assigned_to.frappe.db.count')
    @patch('smurps.smurps.doctype.issue_assigned_to.issue_assigned_to.frappe.get_doc')
    def test_create_todo_for_non_existing_issue(self, mock_get_doc,
                                                mock_count):

        """Test create_todo function for non existing record"""

        mock_count.return_value = 0
        result = create_todo("Administrator", "nonexistingrecord")
        self.assertTrue(mock_get_doc.return_value.insert.called)
        self.assertEqual(mock_get_doc.call_args,
                         call({'owner': 'Administrator', 'doctype': 'ToDo',
                               'reference_name': 'nonexistingrecord',
                               'reference_type': 'Issue',
                               'description': 'nonexistingrecord'}))
        self.assertTrue(result)

    @patch('smurps.smurps.doctype.issue_assigned_to.issue_assigned_to.frappe.get_list')
    def test_get_group_names_exists(self, mock_get_list):

        """Get a  group name that exists"""

        mock_get_list.return_value = [{'group_name': 'Strella'}]
        data = get_group_names("Strellaxx")
        self.assertEqual(data[0]['group_name'], 'Strella')

    @patch('smurps.smurps.doctype.issue_assigned_to.issue_assigned_to.frappe.get_list')
    def test_get_group_names_non_exists(self, mock_get_list):

        """Get a group name that does not exists"""

        mock_get_list.return_value = None
        data = get_group_names("StrellaXX")
        self.assertFalse(data)

    @patch('smurps.smurps.doctype.issue_assigned_to.issue_assigned_to.frappe.get_list')
    def test_get_group_members_non_exists(self, mock_get_list):

        """Get a group members for group that don't exist"""

        mock_get_list.return_value = None
        data = get_group_members("Strellaxx")
        self.assertFalse(data)

    @patch('smurps.smurps.doctype.issue_assigned_to.issue_assigned_to.frappe.get_list')
    def test_get_group_members_exists(self, mock_get_list):

        """Get a group members for group that exists"""

        mock_get_list.return_value = [{'user': u'mock@mockuser.com'}, ]
        data = get_group_members("Strella")
        self.assertEqual(data, [{'user': u'mock@mockuser.com'}, ])
