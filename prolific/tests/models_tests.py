import unittest

from prolific.exceptions import ParticipantBlockedError
from prolific.models import Submission, Study


class TestSubmission(unittest.TestCase):

    def test_start(self):
        study = Study.objects.create(name="test", total_places=10, user_id=1)
        self.assertIsNotNone(Submission.start(study_id=study.id, user_id=2).id)

    def test_fail_second_start(self):
        study = Study.objects.create(name="test", total_places=10, user_id=1)
        self.assertIsNotNone(Submission.start(study_id=study.id, user_id=1).id)

        with self.assertRaises(ParticipantBlockedError):
            Submission.start(study_id=study.id, user_id=1)
