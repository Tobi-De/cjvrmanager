from django.test import TestCase
from cjvr.forms import TaskCreationForm
from datetime import timedelta, date


class TestimonyCreationFormTest(TestCase):
    pass


class PlaintiffCreationFormTest(TestCase):
    pass


class VictimCreationFormTest(TestCase):
    pass


class ReportCreationFormTest(TestCase):
    pass


class TaskCreationFormTest(TestCase):

    def setUp(self):
        self.data = {
            "name": "tache",
            "description": "tache a faire"
        }

    def test_valid_start_date(self):
        self.data["start_date"] = date.today()
        self.data["end_date"] = date.today() + timedelta(days=1)

        form = TaskCreationForm(data=self.data)
        self.assertTrue(form.is_valid())

        self.data["start_date"] = date.today() - timedelta(days=1)
        form = TaskCreationForm(data=self.data)
        self.assertFalse(form.is_valid())

    def test_valid_end_date(self):
        self.data["start_date"] = date.today()
        self.data["end_date"] = date.today() + timedelta(days=1)
        form = TaskCreationForm(data=self.data)
        self.assertTrue(form.is_valid())

        self.data["end_date"] = date.today() - timedelta(days=1)
        form = TaskCreationForm(data=self.data)
        self.assertFalse(form.is_valid())
