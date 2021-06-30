from src.domain_logic.user_domain import UserDomain


def map_UserDomain_to_UserBaseModel(userDomain: UserDomain):
    return {
        "username": userDomain.username,
        "email": userDomain.email
    }
