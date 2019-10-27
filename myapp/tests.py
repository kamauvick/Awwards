from django.test import TestCase

from .models import Project, Profile, Rate, User

new_user = User(username='vick')

test_project = Project(
    title='Hello world',
    details='a hello world app',
    link='https://github.com/hello.git',
    user=new_user, image='/media/hello.jpg',
    user_project_id='1',
    design='7',
    usability='8',
    creativity='9',
    content='8',
    vote_submissions='87'
)


class TestProject(TestCase):
    def setUp(self) -> None:
        self.new_project = Project(
            title='Hello world',
            details='a hello world app',
            link='https://github.com/hello.git',
            user=new_user,
            image='/media/hello.jpg',
            user_project_id='1',
            design='7',
            usability='8',
            creativity='9',
            content='8',
            vote_submissions='87'

        )

    def testInstance(self):
        self.assertTrue(isinstance(self.new_project, Project))

    def testSaveProject(self):
        before = Project.objects.all()
        self.new_project.save()
        after = Project.objects.all()

        self.assertTrue(before < after)

    def testDeleteProject(self):
        before = Project.objects.all()
        self.new_project.delete()
        after = Project.objects.all()

        self.assertTrue(before > after)

    def tearDown(self) -> None:
        self.new_project.delete()


class TestProfile(TestCase):
    def setUp(self) -> None:
        self.new_profile = Profile(
            profile_picture='media/profile.jpg',
            prof_user=new_user,
            bio='this is a test default bio',
            contact_info='testcontact@mail.com',
            profile_Id=1,
            all_projects=test_project,
        )

    def testInstance(self):
        self.assertTrue(isinstance(self.new_profile, Profile))

    def testSaveProfile(self):
        before = Profile.objects.all()
        self.new_profile.save()
        after = Profile.objects.all()

        self.assertTrue(before < after)

    def testEditProfile(self):
        before = Profile.objects.all()
        self.new_profile.save()
        after = Profile.objects.all()

        self.assertTrue(before != after)

    def testDeleteProfile(self):
        before = Profile.objects.all()
        self.new_profile.save()
        after = Profile.objects.all()

        self.assertTrue(before > after)

    def tearDown(self) -> None:
        self.new_profile.delete()

