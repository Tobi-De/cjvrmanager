from django.test import TestCase
from django.contrib.auth.models import User
from cjvr.models import (Task, AggressionType, Victim,
                         Plaintiff, Testimony, Report)
from django.utils import timezone


class AggressionTypeModelTest(TestCase):

    def setUp(self):
        self.aggression_type = AggressionType.objects.create(
            name="viol", description="Un viol")

    def test_Aggression_creation(self):
        self.assertTrue(isinstance(self.aggression_type, AggressionType))
        self.assertEqual(self.aggression_type.__str__(), "viol")


class VictimModelTest(TestCase):

    def setUp(self):
        viol = AggressionType.objects.create(
            name="viol", description="Un viol")
        self.victim = Victim.objects.create(
            first_name="Doe", last_name="John", age=12, sex="Male", religion="Inconnu", address="Inconnu", status="Death")
        self.victim.aggressions.set([viol])

    def test_victim_creation(self):
        self.assertTrue(isinstance(self.victim, Victim))
        self.assertEqual(self.victim.__str__(), "Doe John")


class PlaintiffModelTest(TestCase):

    def setUp(self):
        self.plaintiff = Plaintiff.objects.create(
            first_name="Doe", last_name="John", age=12, sex="Male", religion="Inconnu", address="Inconnu", contact="+22901020304")

    def test_plaintiff_creation(self):
        self.assertTrue(isinstance(self.plaintiff, Plaintiff))
        self.assertEqual(self.plaintiff.__str__(), "Doe John")


class TestimonyModelTest(TestCase):

    def setUp(self):
        viol = AggressionType.objects.create(
            name="viol", description="Un viol")
        self.victim = Victim.objects.create(
            first_name="Doe", last_name="John", age=12, sex="Male", religion="Inconnu", address="Inconnu", status="Death")
        self.victim.aggressions.set([viol])
        self.plaintiff = Plaintiff.objects.create(first_name="Doe", last_name="John", age=12,
                                                  sex="Male", religion="Inconnu", address="Inconnu", contact="+22901020304")

        self.testimony = Testimony.objects.create(
            plaintiff=self.plaintiff, victim=self.victim, description="une violent scene")

    def test_testimony_creation(self):
        self.assertTrue(isinstance(self.testimony, Testimony))
        self.assertEqual(self.testimony.__str__(),
                         f"Deposition No{self.testimony.id}")
        self.assertEqual(self.testimony.victim, self.victim)
        self.assertEqual(self.testimony.plaintiff, self.plaintiff)


class ReportModelTest(TestCase):

    def setUp(self):
        pass

    def test_report_creation(self):
        pass


class TaskModelTest(TestCase):

    def setUp(self):
        self.user = User.objects.create_user("Test", password="testuser1234")
        self.task = Task.objects.create(user=self.user, name="task1", description="Executer tache1",
                                        start_date=timezone.now(), end_date=timezone.now() + timezone.timedelta(days=1))

    def test_task_creation(self):
        self.assertTrue(isinstance(self.task, Task))
        self.assertEqual(self.task.__str__(), "task1")
