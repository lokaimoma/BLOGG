from src.domain_logic.user_domain import UserDomain


def map_UserDomain_to_UserBaseModel(userDomain: UserDomain) -> dict:
    return {
        "username": userDomain.username,
        "email": userDomain.email
    }
