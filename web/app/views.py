from flask import redirect
from sqlalchemy.exc import IntegrityError

from app.app import db
from app.models import ShortLink, ShortLinkSchema
from app.utils import generate_short_link


shortlink_schema = ShortLinkSchema()


def long_to_short(body):
    long_url = body["long_url"]
    link_obj = ShortLink(long_url=long_url)

    link_exists = True
    while link_exists:
        short_url = generate_short_link()
        link_exists = ShortLink.query.filter_by(short_url=short_url).first()

    link_obj.short_url = short_url

    try:
        db.session.add(link_obj)
    except IntegrityError as ex:
        db.session.rollback()
        return {"error": f"Sqlalchemy Error {repr(ex)}"}
    else:
        db.session.commit()
    link_obj_data = shortlink_schema.dump(link_obj)

    return {"short_url": link_obj_data["short_url"]}, 200


def stats(short_postfix):
    link_obj = ShortLink.query.filter_by(short_url=short_postfix).first()
    if link_obj:
        link_obj_data = shortlink_schema.dump(link_obj)
        return {"count": link_obj_data["hits_count"]}, 200
    else:
        return {"error": f"Short link {short_postfix} not found"}, 404


def go_postfix(short_postfix):
    link_obj = ShortLink.query.filter_by(short_url=short_postfix).first()
    if link_obj:
        link_obj.hits_count += 1
        # response = requests.go
        db.session.commit()
        # return (
        #     {"long_url": link_obj.long_url}, 200
        # )

        return redirect(f"http://{link_obj.long_url}", code=302)

    else:
        return {"error": f"Short link {short_postfix} not found"}, 404
