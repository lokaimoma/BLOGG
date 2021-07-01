import json
from src.domain_logic.blog_domain import BlogDomain
from src.util.convertors.datetime_to_string import convert_datetime_to_string as datetime_convertor


def blog_domain_json(blog_domain: BlogDomain) -> str:
    return json.dumps(blog_domain.to_dict(), default=datetime_convertor)
