def get_auth_token():
    """
    Returns an authentication token for API testing.
    In a real system, this would call an auth service
    or retrieve a token securely.
    """
    return "dummy-access-token"


def get_test_user(role="admin", tenant="company1"):
    """
    Returns test user credentials based on role and tenant.
    """
    return {
        "email": f"{role}@{tenant}.com",
        "password": "password123"
    }
