from src.domain_logic.user_domain import UserDomain


def map_user_domain_to_user_base_model(user_domain: UserDomain) -> dict:
    return {
        "username": user_domain.username,
        "email": user_domain.email
    }
