from nose2.tools import params

from test import GithubBoardTestCase

from github_board import STEP, template_to_tape


class TestTemplateToTape(GithubBoardTestCase):
    @params(
        ([[1]], 0, [0]),
        ([[1, 1]], 0, [0, 7 * STEP]),
        ([[1, 0, 1]], 0, [0, 2 * 7 * STEP]),
        ([[0, 1]], 0, [7 * STEP]),
        ([[1], [1]], 0, [0, STEP]),
        ([[1], [0], [1]], 0, [0, 2 * STEP]),
        ([[0], [1]], 0, [STEP]),
        ([[1, 0], [0, 1]], 0, [0, 7 * STEP + STEP]),
        ([[0, 0], [0, 0]], 0, []),
        ([[0, 1], [1]], 42, [42 + 7 * STEP, 42 + STEP]),
        ([[3]], 0, [0, 0, 0]),
        ([[1, 2, 3]], 0, [0, 7 * STEP, 7 * STEP, 7 * 2 * STEP, 7 * 2 * STEP, 7 * 2 * STEP]),
        ([[1], [2], [3]], 0, [0, STEP, STEP, 2 * STEP, 2 * STEP, 2 * STEP]),
    )
    def test(self, template, origin, expected_result):
        self.assertListEqual(expected_result, template_to_tape(template, origin))
