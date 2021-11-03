import os
import uuid


class FileUtils:
    @staticmethod
    def avatar_upload_to(instance, filename: str) -> str:
        ext = filename.split('.')[-1]
        return os.path.join(instance.user.email, 'avatars', f'{uuid.uuid1()}.{ext}')
