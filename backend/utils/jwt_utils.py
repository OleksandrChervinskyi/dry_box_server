from datetime import timedelta

from rest_framework_simplejwt.token_blacklist.models import OutstandingToken
from rest_framework_simplejwt.tokens import AccessToken, BlacklistMixin

from backend.exeptions.jwt_exeption import JwtException


class _AccessToken(BlacklistMixin, AccessToken):
    token_type = 'action'
    lifetime = timedelta(minutes=30)


class JwtUtils:
    @staticmethod
    def create_activated_token(user):
        return _AccessToken.for_user(user)

    @staticmethod
    def validate_token(token):
        try:
            access_token = _AccessToken(token)
            if not OutstandingToken.objects.filter(token=token).exists():
                raise JwtException
            access_token.check_blacklist()
            access_token.blacklist()
        except Exception:
            raise JwtException
