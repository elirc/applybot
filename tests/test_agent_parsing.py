from applypilot.apply.agents.parsing import parse_agent_result


def test_parse_result_line_applied() -> None:
    parsed = parse_agent_result("RESULT: APPLIED - submitted")
    assert parsed.status == "APPLIED"
    assert parsed.submitted is True


def test_parse_result_line_failed_colon() -> None:
    parsed = parse_agent_result("RESULT:FAILED:not_eligible_location")
    assert parsed.status == "FAILED"
    assert "not_eligible_location" in parsed.reason


def test_parse_json_output() -> None:
    parsed = parse_agent_result('{"result":"DRY_RUN","reason":"preview","submitted":false}')
    assert parsed.status == "DRY_RUN"
    assert parsed.submitted is False


def test_parse_unknown_defaults_to_needs_review() -> None:
    parsed = parse_agent_result("No final result emitted")
    assert parsed.status == "NEEDS_REVIEW"
