def assert_status_in(response, allowed_status_codes: tuple[int, ...]):
    assert response.status_code in allowed_status_codes, (
        f"Unexpected status code: {response.status_code}\n"
        f"Response body: {response.text}"
    )


def assert_has_keys(data: dict, keys: list[str]):
    missing = [k for k in keys if k not in data]
    assert not missing, f"Missing keys: {missing}. Found keys: {list(data.keys())}"