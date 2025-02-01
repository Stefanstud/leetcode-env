import http.client
from time import sleep
import leetcode
import leetcode.auth

class LeetCodeClient:
    """
    A client for submitting solutions to LeetCode 
    and retrieving their results. Example response: 
    {
        "status_code": 10,
        "lang": "python3",
        "run_success": true,
        "status_runtime": "0 ms",
        "memory": 19132000,
        "display_runtime": "0",
        "question_id": "1",
        "elapsed_time": 63,
        "compare_result": "111111111111111111111111111111111111111111111111111111111111111",
        "code_output": "",
        "std_output": "",
        "last_testcase": "",
        "expected_output": "",
        "task_finish_time": 1736276152703,
        "task_name": "judger.judgetask.Judge",
        "finished": true,
        "total_correct": 63,
        "total_testcases": 63,
        "runtime_percentile": 100,
        "status_memory": "19.1 MB",
        "memory_percentile": 9.140700000000024,
        "pretty_lang": "Python3",
        "submission_id": "1501060176",
        "status_msg": "Accepted",
        "state": "SUCCESS"
    }
    """

    def __init__(self, session_cookie: str, csrf_token: str, debug: bool = False):
        """
        :param session_cookie: Value of your LEETCODE_SESSION cookie.
        :param csrf_token:     Value of your csrftoken cookie.
        :param debug:          If True, enables debug logging.
        """
        self._api_instance = self._init_api(session_cookie, csrf_token, debug)

    @staticmethod
    def _init_api(session_cookie: str, csrf_token: str, debug: bool) -> leetcode.DefaultApi:
        configuration = leetcode.Configuration()
        configuration.api_key["x-csrftoken"] = csrf_token
        configuration.api_key["csrftoken"] = csrf_token
        configuration.api_key["LEETCODE_SESSION"] = session_cookie
        configuration.api_key["Referer"] = "https://leetcode.com"
        configuration.debug = debug

        return leetcode.DefaultApi(leetcode.ApiClient(configuration))

    def submit_solution(self, code: str, problem_slug: str, question_id: str, lang: str = "python3") -> dict:
        """
        Submits the given code to LeetCode and waits for the final result.

        :param code:         The solution code to submit (string).
        :param problem_slug: The URL-friendly name of the problem, e.g., "two-sum".
        :param question_id:  The numeric ID of the problem, e.g., "1" for two-sum.
        :param lang:         The programming language, e.g. "python3".
        :return:             A dict with submission results.
        """
        submission_info = self._submit_code(code, lang, problem_slug, question_id)
        result = self._poll_submission(submission_info.submission_id)
        return result

    def _submit_code(self, code: str, lang: str, problem_slug: str, question_id: str) -> leetcode.SubmissionId:
        """
        Sends the solution to LeetCode. Returns a submission ID object.
        """
        submission = leetcode.Submission(
            judge_type="large",
            typed_code=code,
            question_id=question_id,
            test_mode=False,
            lang=lang
        )
        return self._api_instance.problems_problem_submit_post(problem=problem_slug, body=submission)

    def _poll_submission(self, submission_id: str, sleep_time: float = 5.0) -> dict:
        """
        Polls LeetCode until the submission is no longer pending/started, 
        then returns the final result.
        """
        attempt_count = 0

        while True:
            sleep(sleep_time)
            try:
                submission_result = self._api_instance.submissions_detail_id_check_get(id=submission_id)
                state = submission_result.get("state", "")
                if state not in ("PENDING", "STARTED"):
                    # Submission finished
                    return submission_result

            except (leetcode.rest.ApiException, http.client.RemoteDisconnected) as e:
                # exponential backoff for rate limiting
                attempt_count += 1
                sleep_duration = min((attempt_count + 1) ** 2, 4 * 60)
                if isinstance(e, leetcode.rest.ApiException) and e.status == 429:
                    sleep(sleep_duration)
                else:
                    raise e